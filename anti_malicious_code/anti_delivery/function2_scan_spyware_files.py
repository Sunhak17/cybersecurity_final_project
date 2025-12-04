"""
Anti-Delivery Function 2: Scan for Spyware Files
Scans AppData for spyware folders and executables from both delivery techniques:
- Technique 1: Fake Security Scanner files
- Technique 2: Fake Update installer files
"""

import os
import json

def scan_spyware_files():
    """
    Scan AppData for spyware folders and captured data (detects both techniques)
    Returns: Dictionary with suspicious folders and files
    """
    print("[Anti-Spyware] Function 2: Scanning for spyware files...")
    
    scan_results = {
        'folders': [],
        'executables': [],
        'data_files': [],
        'total_files': 0
    }
    
    try:
        appdata = os.getenv('APPDATA')
        
        # Spyware folder names from BOTH delivery techniques
        technique1_folders = [
            'SystemSecurityService',  # Created by technique 1
            'SecurityScanner',
            'AntivirusScanner'
        ]
        
        technique2_folders = [
            'WindowsUpdateService',   # Created by technique 2
            'SecurityUpdate',
            'SystemService',
            'KB5034203'
        ]
        
        all_spyware_folders = technique1_folders + technique2_folders
        
        # Scan AppData for spyware folders
        for item in os.listdir(appdata):
            item_path = os.path.join(appdata, item)
            
            if os.path.isdir(item_path) and item in all_spyware_folders:
                technique = "Technique 1 (Fake Scanner)" if item in technique1_folders else \
                           "Technique 2 (Fake Update)"
                
                scan_results['folders'].append({
                    'path': item_path,
                    'name': item,
                    'technique': technique
                })
                print(f"[Anti-Spyware]   ⚠ Found {technique} folder: {item}")
                
                # Scan inside folder for executables and data
                try:
                    for root, dirs, files in os.walk(item_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            scan_results['total_files'] += 1
                            
                            if file.endswith('.exe'):
                                scan_results['executables'].append(file_path)
                                print(f"[Anti-Spyware]      - Spyware executable: {file}")
                            elif file.endswith(('.json', '.log', '.txt')):
                                scan_results['data_files'].append(file_path)
                                print(f"[Anti-Spyware]      - Captured data: {file}")
                except Exception as e:
                    print(f"[Anti-Spyware]      Error scanning folder contents: {e}")
        
        if not scan_results['folders']:
            print("[Anti-Spyware]   ✓ No spyware files detected")
        else:
            print(f"[Anti-Spyware]   ⚠ Summary: {len(scan_results['folders'])} folders, "
                  f"{len(scan_results['executables'])} executables, "
                  f"{len(scan_results['data_files'])} data files")
        
        return scan_results
    except Exception as e:
        print(f"[Anti-Spyware] Error scanning files: {e}")
        return scan_results
