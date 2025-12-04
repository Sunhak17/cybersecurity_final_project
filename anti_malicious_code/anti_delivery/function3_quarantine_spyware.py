"""
Anti-Delivery Function 3: Quarantine Spyware
Terminates spyware processes and quarantines all spyware files
"""

import os
import shutil
import psutil
import json
from datetime import datetime

def quarantine_spyware(spyware_processes, scan_results):
    """
    Terminate spyware processes and quarantine all spyware files
    Args:
        spyware_processes: List of spyware process dictionaries
        scan_results: Dictionary with folders, executables, and data files
    Returns: Dictionary with quarantine statistics
    """
    print("[Anti-Spyware] Function 3: Quarantining spyware...")
    
    quarantine_folder = os.path.join(os.getenv('TEMP'), 'SpywareQuarantine')
    quarantine_stats = {
        'processes_terminated': 0,
        'folders_quarantined': 0,
        'files_quarantined': 0
    }
    
    try:
        # Create quarantine folder
        if not os.path.exists(quarantine_folder):
            os.makedirs(quarantine_folder)
            print(f"[Anti-Spyware]   Created quarantine folder: {quarantine_folder}")
        
        # Terminate spyware processes
        for proc in spyware_processes:
            try:
                p = psutil.Process(proc['pid'])
                proc_name = proc.get('name', 'Unknown')
                
                # Check if it's a system-protected process
                if p.username() and 'SYSTEM' in p.username().upper():
                    print(f"[Anti-Spyware]   ⚠ Skipping system-protected process: {proc_name} (PID: {proc['pid']})")
                    continue
                
                p.terminate()
                p.wait(timeout=5)
                print(f"[Anti-Spyware]   ✓ Terminated spyware: {proc_name} (PID: {proc['pid']})")
                quarantine_stats['processes_terminated'] += 1
            except psutil.AccessDenied:
                print(f"[Anti-Spyware]   ⚠ Access denied (system-protected): {proc.get('name', proc['pid'])}")
            except (psutil.NoSuchProcess, psutil.TimeoutExpired) as e:
                print(f"[Anti-Spyware]   ✗ Could not terminate process {proc['pid']}: {type(e).__name__}")
        
        # Quarantine spyware folders
        for folder in scan_results['folders']:
            try:
                # Handle both dict and string formats
                folder_path = folder['path'] if isinstance(folder, dict) else folder
                folder_name = os.path.basename(folder_path)
                
                # Skip if folder doesn't exist
                if not os.path.exists(folder_path):
                    print(f"[Anti-Spyware]   ⚠ Folder not found: {folder_name}")
                    continue
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                quarantine_path = os.path.join(quarantine_folder, f"{folder_name}_{timestamp}")
                
                shutil.move(folder_path, quarantine_path)
                print(f"[Anti-Spyware]   ✓ Quarantined folder: {folder_name}")
                quarantine_stats['folders_quarantined'] += 1
            except PermissionError:
                print(f"[Anti-Spyware]   ✗ Permission denied: {folder_name} (may be in use)")
            except Exception as e:
                print(f"[Anti-Spyware]   ✗ Error quarantining {folder_name}: {type(e).__name__}")
        
        # Count actual files quarantined
        quarantine_stats['files_quarantined'] = len(scan_results.get('executables', [])) + len(scan_results.get('data_files', []))
        
        # Save quarantine report
        report_file = os.path.join(quarantine_folder, f"quarantine_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(report_file, 'w') as f:
            json.dump(quarantine_stats, f, indent=4)
        
        print(f"\n[Anti-Spyware] Quarantine Summary:")
        print(f"  - Processes terminated: {quarantine_stats['processes_terminated']}")
        print(f"  - Folders quarantined: {quarantine_stats['folders_quarantined']}")
        print(f"  - Files quarantined: {quarantine_stats['files_quarantined']}")
        
        return quarantine_stats
    except Exception as e:
        print(f"[Anti-Spyware] Error in quarantine process: {e}")
        return quarantine_stats
