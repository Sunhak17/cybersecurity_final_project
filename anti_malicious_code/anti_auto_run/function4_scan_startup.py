"""
Anti-Auto-Run Function 4: Scan Startup Folder
Scans Startup folder for suspicious shortcuts
"""

import os

def scan_startup_folder():
    """
    Scan Startup folder for suspicious shortcuts
    Returns: List of suspicious shortcut paths
    """
    print("\n[Defender] Function 4: Scanning Startup folder...")
    
    suspicious_shortcuts = []
    
    try:
        startup_folder = os.path.join(os.getenv('APPDATA'), 
                                     r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        if not os.path.exists(startup_folder):
            print("[Defender]   Startup folder not found")
            return []
        
        # Scan for .lnk files
        for item in os.listdir(startup_folder):
            if item.endswith('.lnk') or item.endswith('.bat'):
                shortcut_path = os.path.join(startup_folder, item)
                
                # Check for suspicious names
                suspicious_keywords = ['WindowsUpdate', 'SystemService', 'SecurityUpdate']
                if any(keyword in item for keyword in suspicious_keywords):
                    suspicious_shortcuts.append(shortcut_path)
                    print(f"[Defender]   Found suspicious shortcut: {item}")
        
        if not suspicious_shortcuts:
            print("[Defender]   No suspicious shortcuts detected")
        
        return suspicious_shortcuts
    except Exception as e:
        print(f"[Defender] Error scanning Startup folder: {e}")
        return []
