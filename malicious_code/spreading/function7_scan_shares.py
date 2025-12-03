"""
Spreading Function 7: Scan Network Shares
Scans network for accessible shared folders
"""

def scan_network_shares():
    """
    Scan network for accessible shared folders
    Returns: List of accessible share paths
    """
    print("[Malicious] Function 7: Scanning network shares...")
    
    accessible_shares = []
    
    try:
        # SIMULATION: In a real scenario, this would scan the network
        # For safety, we only list simulated shares
        simulated_shares = [
            r"\\DESKTOP-PC1\SharedDocs",
            r"\\LAPTOP-USER2\Public",
            r"\\FILESERVER\Downloads"
        ]
        
        print(f"[Malicious] Found {len(simulated_shares)} network shares (simulated)")
        for share in simulated_shares:
            print(f"[Malicious]   - {share}")
        
        # In real malware, this would test write access
        # For demo, we return the simulated list
        return simulated_shares
    except Exception as e:
        print(f"[Malicious] Error scanning network: {e}")
        return []
