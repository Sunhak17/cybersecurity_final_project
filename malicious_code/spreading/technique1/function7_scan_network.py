"""
Spreading Function 7: Scan Network for Spreading
Scans network for accessible shared folders to spread spyware
"""

import socket
import subprocess

def scan_network_targets():
    """
    Scan network for accessible shared folders to spread spyware
    Returns: List of accessible share paths
    """
    print("[Spyware] Function 7: Scanning network for spreading targets...")
    
    accessible_shares = []
    
    try:
        # Get local machine info
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"[Spyware]   - Local machine: {hostname} ({local_ip})")
        
        # SIMULATION: In real scenario, would scan network using nmap or similar
        # For safety, we simulate finding network shares
        simulated_shares = [
            r"\\DESKTOP-PC1\SharedDocs",
            r"\\LAPTOP-USER2\Public",
            r"\\FILESERVER\Downloads",
            r"\\WORKSTATION-03\Users\Public"
        ]
        
        print(f"[Spyware] Discovered {len(simulated_shares)} potential spread targets (simulated)")
        for share in simulated_shares:
            print(f"[Spyware]   Target: {share}")
            accessible_shares.append(share)
        
        return accessible_shares
    except Exception as e:
        print(f"[Spyware] Error scanning network: {e}")
        return []
