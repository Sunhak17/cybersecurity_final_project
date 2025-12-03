"""
Anti-Spreading Function 7: Monitor Network File Copies
Monitors file copy operations to network shares
"""

def monitor_network_file_copies():
    """
    Monitor file copy operations to network shares
    Returns: True if monitoring is active
    """
    print("\n[Defender] Function 7: Monitoring network file copies...")
    
    try:
        # In a real implementation, this would use file system monitoring
        # For demonstration, we simulate detection
        print("[Defender]   Network monitoring active (simulated)")
        print("[Defender]   Would detect file copies to network shares in real-time")
        
        # Check for common malicious file names on shares
        suspicious_patterns = [
            'PayrollReport*.exe',
            'CompanyPhotos.exe',
            'ImportantDocument.exe',
            'QuickFix.exe'
        ]
        
        print(f"[Defender]   Watching for suspicious files: {', '.join(suspicious_patterns)}")
        return True
    except Exception as e:
        print(f"[Defender] Error monitoring network: {e}")
        return False
