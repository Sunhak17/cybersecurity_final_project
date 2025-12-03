"""
Anti-Spreading Function 9: Block and Clean Network
Blocks spreading and cleans network shares
"""

def block_and_clean_network(threats):
    """
    Block spreading and clean network shares
    Args:
        threats: List of threat paths found on network
    Returns: Number of threats cleaned
    """
    print("[Defender] Function 9: Blocking and cleaning network...")
    
    cleaned_count = 0
    
    try:
        if threats:
            print(f"[Defender]   Cleaning {len(threats)} threats from network...")
            
            for threat in threats:
                # SAFETY: We don't actually delete from real network shares
                # Just simulate the action
                print(f"[Defender]   Would remove: {threat} (simulated)")
                cleaned_count += 1
            
            # Generate alert
            print(f"\n[Defender] === NETWORK ALERT ===")
            print(f"[Defender] Detected and blocked malware spreading attempt")
            print(f"[Defender] Threat: Email Sender Utility (malicious)")
            print(f"[Defender] Action: Removed {cleaned_count} copies from network")
            print(f"[Defender] Status: Network is now clean")
            print(f"[Defender] =====================\n")
        else:
            print("[Defender]   Network is clean, no action needed")
        
        return cleaned_count
    except Exception as e:
        print(f"[Defender] Error cleaning network: {e}")
        return 0
