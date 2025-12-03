"""
Anti-Spreading Function 8: Scan Network Shares
Scans accessible network shares for malware
"""

import os

def scan_network_shares():
    """
    Scan accessible network shares for malware
    Returns: List of found threat paths
    """
    print("[Defender] Function 8: Scanning network shares...")
    
    found_threats = []
    
    try:
        # SIMULATION: In a real scenario, this would scan actual network shares
        # For safety, we only simulate the scan
        simulated_shares = [
            r"\\DESKTOP-PC1\SharedDocs",
            r"\\LAPTOP-USER2\Public",
            r"\\FILESERVER\Downloads"
        ]
        
        print(f"[Defender]   Scanning {len(simulated_shares)} network locations (simulated)...")
        
        # Simulate finding threats
        suspicious_files = [
            "PayrollReport_2025.exe",
            "CompanyPhotos.exe"
        ]
        
        for share in simulated_shares:
            for filename in suspicious_files:
                threat_path = os.path.join(share, filename)
                found_threats.append(threat_path)
                print(f"[Defender]   Found suspicious file: {threat_path} (simulated)")
        
        if not found_threats:
            print("[Defender]   No threats found on network shares")
        
        return found_threats
    except Exception as e:
        print(f"[Defender] Error scanning shares: {e}")
        return []
