"""
Anti-Auto-Run Function 4: Detect Spyware Persistence
Scans Startup folder for spyware shortcuts and autorun mechanisms
"""

import os

def detect_spyware_persistence():
    """
    Scan Startup folder for spyware persistence shortcuts
    Returns: List of suspicious shortcut paths
    """
    print("\n[Anti-Spyware] Function 4: Detecting spyware persistence mechanisms...")
    
    suspicious_shortcuts = []
    
    try:
        startup_folder = os.path.join(os.getenv('APPDATA'), 
                                     r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        if not os.path.exists(startup_folder):
            print("[Anti-Spyware]   Startup folder not found")
            return []
        
        # Spyware shortcut keywords
        spyware_keywords = [
            'SecurityScanner', 'SystemSecurity', 'SecurityService',
            'WindowsUpdate', 'SystemService', 'SecurityUpdate'
        ]
        
        # Scan for shortcuts
        for item in os.listdir(startup_folder):
            if item.endswith('.lnk') or item.endswith('.bat') or item.endswith('.exe'):
                shortcut_path = os.path.join(startup_folder, item)
                
                # Check for spyware keywords
                if any(keyword in item for keyword in spyware_keywords):
                    suspicious_shortcuts.append(shortcut_path)
                    print(f"[Anti-Spyware]   ⚠ Found spyware persistence: {item}")
        
        if not suspicious_shortcuts:
            print("[Anti-Spyware]   ✓ No spyware persistence in startup folder")
        else:
            print(f"[Anti-Spyware]   ⚠ Total persistence entries found: {len(suspicious_shortcuts)}")
        
        return suspicious_shortcuts
    except Exception as e:
        print(f"[Anti-Spyware] Error scanning Startup folder: {e}")
        return []
