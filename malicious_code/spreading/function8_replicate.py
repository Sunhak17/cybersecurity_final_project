"""
Spreading Function 8: Replicate to Shares
Copies malicious program to network shares with tempting names
"""

import os
import shutil

def replicate_to_shares(shares):
    """
    Copy malicious program to network shares
    Args:
        shares: List of network share paths
    Returns: Number of successful replications
    """
    print("[Malicious] Function 8: Replicating to shares...")
    
    tempting_names = [
        "PayrollReport_2025.exe",
        "CompanyPhotos.exe",
        "ImportantDocument.exe",
        "QuickFix.exe"
    ]
    
    try:
        # Get current executable
        appdata = os.getenv('APPDATA')
        source_exe = os.path.join(appdata, "WindowsUpdateService", "WindowsUpdateService.exe")
        
        spread_count = 0
        for share in shares:
            for filename in tempting_names:
                target_path = os.path.join(share, filename)
                
                # SAFETY: We don't actually copy to real network shares
                # Just simulate the action
                print(f"[Malicious]   Would copy to: {target_path} (simulated)")
                spread_count += 1
        
        print(f"[Malicious] Spreading simulation complete: {spread_count} copies")
        return spread_count
    except Exception as e:
        print(f"[Malicious] Error replicating to shares: {e}")
        return 0
