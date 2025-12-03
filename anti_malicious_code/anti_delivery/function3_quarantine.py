"""
Anti-Delivery Function 3: Analyze and Quarantine
Terminates malicious processes and quarantines files
"""

import os
import shutil
import psutil
from datetime import datetime

def analyze_and_quarantine(suspicious_procs, suspicious_folders):
    """
    Analyze and quarantine suspicious files
    Args:
        suspicious_procs: List of suspicious process dictionaries
        suspicious_folders: List of suspicious folder paths
    Returns: Number of items quarantined
    """
    print("[Defender] Function 3: Analyzing and quarantining threats...")
    
    quarantine_folder = os.path.join(os.getenv('TEMP'), 'MalwareQuarantine')
    quarantined_count = 0
    
    try:
        # Create quarantine folder
        if not os.path.exists(quarantine_folder):
            os.makedirs(quarantine_folder)
            print(f"[Defender]   Created quarantine folder: {quarantine_folder}")
        
        # Terminate suspicious processes
        for proc in suspicious_procs:
            try:
                p = psutil.Process(proc['pid'])
                p.terminate()
                p.wait(timeout=5)
                print(f"[Defender]   Terminated process: {proc['name']} (PID: {proc['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
                print(f"[Defender]   Could not terminate process {proc['pid']}: {e}")
        
        # Quarantine suspicious folders
        for folder in suspicious_folders:
            try:
                folder_name = os.path.basename(folder)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                quarantine_path = os.path.join(quarantine_folder, f"{folder_name}_{timestamp}")
                
                shutil.move(folder, quarantine_path)
                print(f"[Defender]   Quarantined: {folder} -> {quarantine_path}")
                quarantined_count += 1
            except Exception as e:
                print(f"[Defender]   Error quarantining {folder}: {e}")
        
        print(f"[Defender]   Total items quarantined: {quarantined_count}")
        return quarantined_count
    except Exception as e:
        print(f"[Defender] Error in quarantine process: {e}")
        return 0
