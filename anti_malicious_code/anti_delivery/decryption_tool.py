"""
ANTI-MALWARE DECRYPTION TOOL
Decrypts files encrypted by the spyware
Uses the actual encryption key from the ransomware
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk
import json
from cryptography.fernet import Fernet

def load_encryption_key():
    """Load encryption key from spyware data file"""
    try:
        appdata = os.getenv('APPDATA')
        key_file = os.path.join(appdata, 'SystemSecurityService', 'encryption_data.json')
        
        if os.path.exists(key_file):
            with open(key_file, 'r') as f:
                data = json.load(f)
            return data.get('key', None), data.get('encrypted_files', [])
        return None, []
    except Exception as e:
        return None, []

def scan_encrypted_files():
    """Scan Documents folder for encrypted files"""
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
    encrypted_files = []
    
    for root, dirs, files in os.walk(documents_path):
        for filename in files:
            if filename.endswith('.encrypted'):
                file_path = os.path.join(root, filename)
                encrypted_files.append({
                    'path': file_path,
                    'name': filename,
                    'size': os.path.getsize(file_path)
                })
    
    return encrypted_files

def decrypt_file(file_path, encryption_key):
    """Decrypt a single file"""
    try:
        # Convert key to bytes if string
        if isinstance(encryption_key, str):
            encryption_key = encryption_key.encode()
        
        cipher = Fernet(encryption_key)
        
        # Read encrypted file
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt data
        decrypted_data = cipher.decrypt(encrypted_data)
        
        # Write original file back
        original_path = file_path[:-10]  # Remove .encrypted
        with open(original_path, 'wb') as f:
            f.write(decrypted_data)
        
        # Delete encrypted file
        os.remove(file_path)
        
        return True, os.path.basename(original_path)
    except Exception as e:
        return False, str(e)

class DecryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("🔓 File Decryption Tool - Anti-Malware")
        self.root.geometry("700x550")
        self.root.configure(bg='#f0f0f0')
        
        # Header
        header = tk.Frame(root, bg='#0078d4', height=80)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🔓 ANTI-MALWARE DECRYPTION TOOL",
                        font=("Segoe UI", 18, "bold"),
                        bg='#0078d4', fg='white')
        title.pack(pady=25)
        
        # Main content
        content = tk.Frame(root, bg='#f0f0f0')
        content.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Info label
        info_label = tk.Label(content,
                             text="This tool will decrypt files encrypted by the ransomware.\n"
                                  "The decryption key will be loaded automatically from the spyware data.",
                             font=("Segoe UI", 10),
                             bg='#f0f0f0', fg='#333333',
                             justify='left')
        info_label.pack(anchor='w', pady=(0, 15))
        
        # Auto-load key button
        load_btn = tk.Button(content, text="🔑 Auto-Load Decryption Key",
                            font=("Segoe UI", 11, "bold"),
                            bg='#0078d4', fg='white',
                            padx=20, pady=10,
                            command=self.load_key)
        load_btn.pack(pady=10)
        
        # Scan button
        scan_btn = tk.Button(content, text="🔍 Scan for Encrypted Files",
                            font=("Segoe UI", 11, "bold"),
                            bg='#0078d4', fg='white',
                            padx=20, pady=10,
                            command=self.scan_files)
        scan_btn.pack(pady=5)
        
        # Files list
        list_frame = tk.Frame(content, bg='#ffffff', relief='ridge', borderwidth=2)
        list_frame.pack(fill='both', expand=True, pady=10)
        
        list_label = tk.Label(list_frame, text="Encrypted Files Found:",
                             font=("Segoe UI", 10, "bold"),
                             bg='#ffffff', fg='#333333')
        list_label.pack(anchor='w', padx=5, pady=5)
        
        self.files_text = tk.Text(list_frame, height=8,
                                 font=("Consolas", 9),
                                 bg='#ffffff', fg='#000000',
                                 state='disabled')
        self.files_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Key entry
        key_frame = tk.Frame(content, bg='#f0f0f0')
        key_frame.pack(pady=10, fill='x')
        
        key_label = tk.Label(key_frame, text="Decryption Key:",
                            font=("Segoe UI", 10, "bold"),
                            bg='#f0f0f0')
        key_label.pack(anchor='w', padx=5)
        
        self.key_entry = tk.Entry(key_frame, font=("Consolas", 9))
        self.key_entry.pack(fill='x', padx=5, pady=5)
        
        # Decrypt button
        decrypt_btn = tk.Button(content, text="🔓 DECRYPT FILES",
                               font=("Segoe UI", 12, "bold"),
                               bg='#107c10', fg='white',
                               padx=30, pady=12,
                               command=self.decrypt_files)
        decrypt_btn.pack(pady=15)
        
        self.encrypted_files = []
        self.encryption_key = None
        
        # Auto-load key on startup
        self.load_key()
    
    def load_key(self):
        """Load encryption key from spyware data"""
        key, files = load_encryption_key()
        
        if key:
            self.encryption_key = key
            self.key_entry.delete(0, 'end')
            self.key_entry.insert(0, key)
            messagebox.showinfo("Key Loaded", 
                              f"✅ Decryption key loaded successfully!\n\n"
                              f"Key: {key[:20]}...\n\n"
                              "Click 'Scan for Encrypted Files' to find encrypted files.")
        else:
            messagebox.showwarning("Key Not Found",
                                 "⚠️ Could not find encryption key!\n\n"
                                 "The spyware must be run first to encrypt files.\n"
                                 "Or manually enter the key from the spyware output.")
    
    def scan_files(self):
        """Scan for encrypted files"""
        self.files_text.config(state='normal')
        self.files_text.delete(1.0, 'end')
        
        self.encrypted_files = scan_encrypted_files()
        
        if self.encrypted_files:
            self.files_text.insert('end', f"Found {len(self.encrypted_files)} encrypted file(s):\n\n")
            for file_info in self.encrypted_files:
                size_kb = file_info['size'] / 1024
                self.files_text.insert('end', f"• {file_info['name']} ({size_kb:.1f} KB)\n")
        else:
            self.files_text.insert('end', "No encrypted files found.\n")
        
        self.files_text.config(state='disabled')
    
    def decrypt_files(self):
        """Decrypt all files with encryption key"""
        encryption_key = self.key_entry.get()
        
        if not encryption_key:
            messagebox.showerror("Error", "Please load or enter the decryption key!")
            return
        
        if not self.encrypted_files:
            messagebox.showwarning("Warning", "No encrypted files found!\n\nClick 'Scan for Encrypted Files' first.")
            return
        
        # Decrypt files
        success_count = 0
        failed_files = []
        
        for file_info in self.encrypted_files:
            success, result = decrypt_file(file_info['path'], encryption_key)
            if success:
                success_count += 1
            else:
                failed_files.append(file_info['name'])
        
        # Remove ransom note
        ransom_note = os.path.join(os.path.expanduser('~'), 'Documents', 'README_DECRYPT.txt')
        if os.path.exists(ransom_note):
            os.remove(ransom_note)
        
        # Show result
        if success_count == len(self.encrypted_files):
            messagebox.showinfo("Success",
                              f"✅ Successfully decrypted {success_count} file(s)!\n\n"
                              "Your files have been restored.\n"
                              "Ransom note removed.")
            self.scan_files()  # Refresh list
        else:
            messagebox.showwarning("Partial Success",
                                 f"Decrypted: {success_count}\n"
                                 f"Failed: {len(failed_files)}\n\n"
                                 f"Failed files:\n" + "\n".join(failed_files))

if __name__ == "__main__":
    root = tk.Tk()
    app = DecryptionTool(root)
    root.mainloop()
