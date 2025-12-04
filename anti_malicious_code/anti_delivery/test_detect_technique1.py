"""
ANTI-DELIVERY TECHNIQUE 1: Detect Fake Security Scanner
Detects spyware delivered via social engineering (fake security software)

This demonstrates detection of:
- Fake security scanner processes
- Suspicious security-related folders
- Hidden executables masquerading as security tools
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

def detect_technique1():
    """Detect spyware from Technique 1 (Fake Security Scanner)"""
    
    print("="*70)
    print("ANTI-DELIVERY TECHNIQUE 1: Detect Fake Security Scanner")
    print("="*70)
    print("\nThis detects spyware delivered via social engineering:")
    print("- Fake 'Security Scanner' processes")
    print("- SystemSecurityService folders")
    print("- Hidden security-related executables")
    print("="*70 + "\n")
    
    # Function 1: Detect processes
    print("[Detection Phase 1] Scanning for fake security scanner processes...")
    processes = detect_spyware_processes()
    
    technique1_procs = [p for p in processes if 'Technique 1' in p.get('technique', '')]
    
    if technique1_procs:
        print(f"\n⚠️ THREAT DETECTED: {len(technique1_procs)} fake security scanner process(es)")
        for proc in technique1_procs:
            print(f"   - {proc['name']} (PID: {proc['pid']})")
    else:
        print("\n✓ No fake security scanner processes detected")
    
    # Function 2: Scan files
    print("\n[Detection Phase 2] Scanning for fake security scanner files...")
    files = scan_spyware_files()
    
    technique1_folders = [f for f in files['folders'] if 'Technique 1' in f.get('technique', '')]
    
    if technique1_folders:
        print(f"\n⚠️ THREAT DETECTED: {len(technique1_folders)} fake security folder(s)")
        for folder in technique1_folders:
            print(f"   - {folder['name']} at {folder['path']}")
        print(f"\n   Contains: {len(files['executables'])} executables, {len(files['data_files'])} data files")
    else:
        print("\n✓ No fake security scanner folders detected")
    
    # Summary
    print("\n" + "="*70)
    print("DETECTION SUMMARY - Technique 1")
    print("="*70)
    
    total_threats = len(technique1_procs) + len(technique1_folders)
    
    if total_threats > 0:
        print(f"⚠️ STATUS: INFECTED - {total_threats} threat(s) from fake security scanner")
        print("\nRecommended Actions:")
        print("1. Terminate suspicious processes")
        print("2. Quarantine infected folders")
        print("3. Remove persistence mechanisms")
    else:
        print("✓ STATUS: CLEAN - No fake security scanner detected")
    
    print("="*70 + "\n")
    
    return {
        'processes': technique1_procs,
        'folders': technique1_folders,
        'files': files
    }

if __name__ == "__main__":
    detect_technique1()
