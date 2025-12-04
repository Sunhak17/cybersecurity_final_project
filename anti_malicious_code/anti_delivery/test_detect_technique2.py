"""
ANTI-DELIVERY TECHNIQUE 2: Detect Fake Software Update
Detects spyware delivered via drive-by download (fake Windows update)

This demonstrates detection of:
- Fake Windows update processes
- Suspicious update-related folders
- Hidden update installer executables
"""

import sys
import os
import psutil

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import functions directly
import function1_detect_spyware
import function2_scan_spyware_files

detect_spyware_processes = function1_detect_spyware.detect_spyware_processes
scan_spyware_files = function2_scan_spyware_files.scan_spyware_files

def detect_technique2():
    """Detect spyware from Technique 2 (Fake Windows Update)"""
    
    print("="*70)
    print("ANTI-DELIVERY TECHNIQUE 2: Detect Fake Software Update")
    print("="*70)
    print("\nThis detects spyware delivered via drive-by download:")
    print("- Fake 'Windows Update' processes")
    print("- WindowsUpdateService folders")
    print("- Hidden update-related executables")
    print("="*70 + "\n")
    
    # Function 1: Detect processes
    print("[Detection Phase 1] Scanning for fake update processes...")
    processes = detect_spyware_processes()
    
    technique2_procs = [p for p in processes if 'Technique 2' in p.get('technique', '')]
    
    if technique2_procs:
        print(f"\n⚠️ THREAT DETECTED: {len(technique2_procs)} fake update process(es)")
        for proc in technique2_procs:
            print(f"   - {proc['name']} (PID: {proc['pid']})")
    else:
        print("\n✓ No fake update processes detected")
    
    # Function 2: Scan files
    print("\n[Detection Phase 2] Scanning for fake update files...")
    files = scan_spyware_files()
    
    technique2_folders = [f for f in files['folders'] if 'Technique 2' in f.get('technique', '')]
    
    if technique2_folders:
        print(f"\n⚠️ THREAT DETECTED: {len(technique2_folders)} fake update folder(s)")
        for folder in technique2_folders:
            print(f"   - {folder['name']} at {folder['path']}")
        print(f"\n   Contains: {len(files['executables'])} executables, {len(files['data_files'])} data files")
    else:
        print("\n✓ No fake update folders detected")
    
    # Summary
    print("\n" + "="*70)
    print("DETECTION SUMMARY - Technique 2")
    print("="*70)
    
    total_threats = len(technique2_procs) + len(technique2_folders)
    
    if total_threats > 0:
        print(f"⚠️ STATUS: INFECTED - {total_threats} threat(s) from fake update")
        print("\nRecommended Actions:")
        print("1. Terminate suspicious update processes")
        print("2. Quarantine update-related folders")
        print("3. Scan for additional payloads")
    else:
        print("✓ STATUS: CLEAN - No fake update detected")
    
    print("="*70 + "\n")
    
    return {
        'processes': technique2_procs,
        'folders': technique2_folders,
        'files': files
    }

if __name__ == "__main__":
    detect_technique2()
