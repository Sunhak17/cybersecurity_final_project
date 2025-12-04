"""
Anti-Spreading Function 7: Monitor Data Exfiltration
Monitors for spyware data exfiltration attempts
"""

import os
import json

def monitor_exfiltration():
    """
    Monitor for spyware data exfiltration signs
    Returns: Dictionary with exfiltration indicators
    """
    print("\n[Anti-Spyware] Function 7: Monitoring for data exfiltration...")
    
    exfiltration_indicators = {
        'log_files_found': [],
        'captured_data_found': [],
        'total_indicators': 0
    }
    
    try:
        appdata = os.getenv('APPDATA')
        
        # Check for spyware data folders
        spyware_folders = [
            os.path.join(appdata, 'SystemSecurityService'),
            os.path.join(appdata, 'WindowsUpdateService')
        ]
        
        for folder in spyware_folders:
            if os.path.exists(folder):
                # Check for logs folder
                logs_folder = os.path.join(folder, 'logs')
                if os.path.exists(logs_folder):
                    for file in os.listdir(logs_folder):
                        file_path = os.path.join(logs_folder, file)
                        exfiltration_indicators['log_files_found'].append(file_path)
                        print(f"[Anti-Spyware]   ⚠ Exfiltration log found: {file}")
                
                # Check for captured data
                data_folder = os.path.join(folder, 'captured_data')
                if os.path.exists(data_folder):
                    for file in os.listdir(data_folder):
                        file_path = os.path.join(data_folder, file)
                        exfiltration_indicators['captured_data_found'].append(file_path)
                        print(f"[Anti-Spyware]   ⚠ Captured data found: {file}")
        
        exfiltration_indicators['total_indicators'] = (
            len(exfiltration_indicators['log_files_found']) +
            len(exfiltration_indicators['captured_data_found'])
        )
        
        if exfiltration_indicators['total_indicators'] == 0:
            print("[Anti-Spyware]   ✓ No exfiltration activity detected")
        else:
            print(f"[Anti-Spyware]   ⚠ Found {exfiltration_indicators['total_indicators']} exfiltration indicators")
        
        return exfiltration_indicators
    except Exception as e:
        print(f"[Anti-Spyware] Error monitoring exfiltration: {e}")
        return exfiltration_indicators
