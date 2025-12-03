"""
Anti-Delivery Function 2: Scan Hidden Folders
Scans AppData for newly created hidden folders
"""

import os

def scan_hidden_folders():
    """
    Scan AppData for newly created hidden folders
    Returns: List of suspicious folder paths
    """
    print("[Defender] Function 2: Scanning for hidden folders...")
    
    suspicious_folders = []
    
    try:
        appdata = os.getenv('APPDATA')
        
        # Known suspicious folder names used by malware
        suspicious_names = [
            'WindowsUpdateService',
            'SystemService',
            'SecurityUpdate',
            'MicrosoftUpdate'
        ]
        
        # Scan AppData
        for item in os.listdir(appdata):
            item_path = os.path.join(appdata, item)
            
            if os.path.isdir(item_path):
                # Check if folder name is suspicious
                if item in suspicious_names:
                    # Check if folder is hidden
                    try:
                        attrs = os.stat(item_path).st_file_attributes
                        if attrs & 0x02:  # FILE_ATTRIBUTE_HIDDEN
                            suspicious_folders.append(item_path)
                            print(f"[Defender]   Found suspicious hidden folder: {item_path}")
                        else:
                            suspicious_folders.append(item_path)
                            print(f"[Defender]   Found suspicious folder: {item_path}")
                    except:
                        suspicious_folders.append(item_path)
                        print(f"[Defender]   Found suspicious folder: {item_path}")
        
        if not suspicious_folders:
            print("[Defender]   No suspicious hidden folders detected")
        
        return suspicious_folders
    except Exception as e:
        print(f"[Defender] Error scanning hidden folders: {e}")
        return []
