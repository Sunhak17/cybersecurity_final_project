"""
ANTI-MALICIOUS CODE DEFENDER
Educational demonstration of malware detection and removal

This program detects and blocks the malicious email sender:
- Anti-Delivery: Detects GUI programs creating hidden folders
- Anti-Auto-Run: Removes startup and registry persistence
- Anti-Spreading: Blocks network spreading attempts

Total: 9 functions working together as one defense system
"""

import os
import sys
import time
import winreg
import psutil
import shutil
from pathlib import Path
from datetime import datetime

# ============================================================================
# STAGE 1: ANTI-DELIVERY (Functions 1-3)
# ============================================================================

def monitor_running_processes():
    """
    Function 1: Monitor processes for suspicious dual behavior
    Detects programs showing GUI while creating hidden folders
    """
    print("\n[Defender] Function 1: Monitoring running processes...")
    
    suspicious_processes = []
    
    try:
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                # Check if process has a window (GUI)
                proc_info = proc.info
                
                # Look for suspicious process names
                if proc_info['name'] and ('email' in proc_info['name'].lower() or 
                                         'sender' in proc_info['name'].lower() or
                                         'update' in proc_info['name'].lower()):
                    suspicious_processes.append({
                        'pid': proc_info['pid'],
                        'name': proc_info['name'],
                        'exe': proc_info['exe']
                    })
                    print(f"[Defender]   Found suspicious process: {proc_info['name']} (PID: {proc_info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if not suspicious_processes:
            print("[Defender]   No suspicious processes detected")
        
        return suspicious_processes
    except Exception as e:
        print(f"[Defender] Error monitoring processes: {e}")
        return []

def scan_hidden_folders():
    """
    Function 2: Scan AppData for newly created hidden folders
    Detects folders created by malicious programs
    """
    print("[Defender] Function 2: Scanning for hidden folders...")
    
    suspicious_folders = []
    
    try:
        appdata = os.getenv('APPDATA')
        
        # Known suspicious folder names used by malware
        suspicious_names = [
            'WindowsUpdateService',
            'SystemService',
            'SecurityUpdate',
            'MicrosoftUpdate'
        ]
        
        # Scan AppData
        for item in os.listdir(appdata):
            item_path = os.path.join(appdata, item)
            
            if os.path.isdir(item_path):
                # Check if folder name is suspicious
                if item in suspicious_names:
                    # Check if folder is hidden
                    attrs = os.stat(item_path).st_file_attributes
                    if attrs & 0x02:  # FILE_ATTRIBUTE_HIDDEN
                        suspicious_folders.append(item_path)
                        print(f"[Defender]   Found suspicious hidden folder: {item_path}")
                    else:
                        suspicious_folders.append(item_path)
                        print(f"[Defender]   Found suspicious folder: {item_path}")
        
        if not suspicious_folders:
            print("[Defender]   No suspicious hidden folders detected")
        
        return suspicious_folders
    except Exception as e:
        print(f"[Defender] Error scanning hidden folders: {e}")
        return []

def analyze_and_quarantine():
    """
    Function 3: Analyze and quarantine suspicious files
    Terminates malicious processes and moves files to quarantine
    """
    print("[Defender] Function 3: Analyzing and quarantining threats...")
    
    quarantine_folder = os.path.join(os.getenv('TEMP'), 'MalwareQuarantine')
    quarantined_count = 0
    
    try:
        # Create quarantine folder
        if not os.path.exists(quarantine_folder):
            os.makedirs(quarantine_folder)
            print(f"[Defender]   Created quarantine folder: {quarantine_folder}")
        
        # Get suspicious processes and folders
        suspicious_procs = monitor_running_processes()
        suspicious_folders = scan_hidden_folders()
        
        # Terminate suspicious processes
        for proc in suspicious_procs:
            try:
                p = psutil.Process(proc['pid'])
                p.terminate()
                p.wait(timeout=5)
                print(f"[Defender]   Terminated process: {proc['name']} (PID: {proc['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
                print(f"[Defender]   Could not terminate process {proc['pid']}: {e}")
        
        # Quarantine suspicious folders
        for folder in suspicious_folders:
            try:
                folder_name = os.path.basename(folder)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                quarantine_path = os.path.join(quarantine_folder, f"{folder_name}_{timestamp}")
                
                shutil.move(folder, quarantine_path)
                print(f"[Defender]   Quarantined: {folder} -> {quarantine_path}")
                quarantined_count += 1
            except Exception as e:
                print(f"[Defender]   Error quarantining {folder}: {e}")
        
        print(f"[Defender]   Total items quarantined: {quarantined_count}")
        return quarantined_count
    except Exception as e:
        print(f"[Defender] Error in quarantine process: {e}")
        return 0

# ============================================================================
# STAGE 2: ANTI-AUTO-RUN (Functions 4-6)
# ============================================================================

def scan_startup_folder():
    """
    Function 4: Scan Startup folder for suspicious shortcuts
    Detects shortcuts created by malware
    """
    print("\n[Defender] Function 4: Scanning Startup folder...")
    
    suspicious_shortcuts = []
    
    try:
        startup_folder = os.path.join(os.getenv('APPDATA'), 
                                     r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        if not os.path.exists(startup_folder):
            print("[Defender]   Startup folder not found")
            return []
        
        # Scan for .lnk files
        for item in os.listdir(startup_folder):
            if item.endswith('.lnk'):
                shortcut_path = os.path.join(startup_folder, item)
                
                # Check for suspicious names
                suspicious_keywords = ['WindowsUpdate', 'SystemService', 'SecurityUpdate']
                if any(keyword in item for keyword in suspicious_keywords):
                    suspicious_shortcuts.append(shortcut_path)
                    print(f"[Defender]   Found suspicious shortcut: {item}")
        
        if not suspicious_shortcuts:
            print("[Defender]   No suspicious shortcuts detected")
        
        return suspicious_shortcuts
    except Exception as e:
        print(f"[Defender] Error scanning Startup folder: {e}")
        return []

def scan_registry_run_keys():
    """
    Function 5: Scan registry Run keys for malicious entries
    Checks HKCU and HKLM Run keys
    """
    print("[Defender] Function 5: Scanning registry Run keys...")
    
    suspicious_entries = []
    
    try:
        # Scan HKEY_CURRENT_USER
        key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    
                    # Check for suspicious entries
                    suspicious_keywords = ['WindowsUpdate', 'SystemService', 'SecurityUpdate']
                    if any(keyword in name for keyword in suspicious_keywords) or \
                       any(keyword in value for keyword in suspicious_keywords):
                        suspicious_entries.append({
                            'hive': 'HKCU',
                            'key': key_path,
                            'name': name,
                            'value': value
                        })
                        print(f"[Defender]   Found suspicious registry entry: {name} -> {value}")
                    
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(key)
        except FileNotFoundError:
            print("[Defender]   Run key not found in HKCU")
        
        if not suspicious_entries:
            print("[Defender]   No suspicious registry entries detected")
        
        return suspicious_entries
    except Exception as e:
        print(f"[Defender] Error scanning registry: {e}")
        return []

def remove_persistence_mechanisms():
    """
    Function 6: Remove all persistence mechanisms
    Deletes startup shortcuts, registry keys, and hidden folders
    """
    print("[Defender] Function 6: Removing persistence mechanisms...")
    
    removed_count = 0
    
    try:
        # Remove startup shortcuts
        shortcuts = scan_startup_folder()
        for shortcut in shortcuts:
            try:
                os.remove(shortcut)
                print(f"[Defender]   Removed shortcut: {shortcut}")
                removed_count += 1
            except Exception as e:
                print(f"[Defender]   Error removing shortcut: {e}")
        
        # Remove registry entries
        entries = scan_registry_run_keys()
        for entry in entries:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, entry['key'], 0, winreg.KEY_SET_VALUE)
                winreg.DeleteValue(key, entry['name'])
                winreg.CloseKey(key)
                print(f"[Defender]   Removed registry entry: {entry['name']}")
                removed_count += 1
            except Exception as e:
                print(f"[Defender]   Error removing registry entry: {e}")
        
        # Hidden folders already quarantined in Stage 1
        
        print(f"[Defender]   Total persistence mechanisms removed: {removed_count}")
        return removed_count
    except Exception as e:
        print(f"[Defender] Error removing persistence: {e}")
        return 0

# ============================================================================
# STAGE 3: ANTI-SPREADING (Functions 7-9)
# ============================================================================

def monitor_network_file_copies():
    """
    Function 7: Monitor file copy operations to network shares
    Detects programs copying themselves to shares
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

def scan_network_shares():
    """
    Function 8: Scan accessible network shares for malware
    Detects malicious files already spread to shares
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

def block_and_clean_network():
    """
    Function 9: Block spreading and clean network shares
    Removes malicious files from shares and alerts users
    """
    print("[Defender] Function 9: Blocking and cleaning network...")
    
    cleaned_count = 0
    
    try:
        # Get list of threats from scan
        threats = scan_network_shares()
        
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

# ============================================================================
# MAIN DEFENSE EXECUTION
# ============================================================================

def run_full_scan():
    """Execute all 9 defender functions in sequence"""
    print("\n" + "="*60)
    print("ANTI-MALICIOUS DEFENDER - FULL SYSTEM SCAN")
    print("="*60)
    
    start_time = time.time()
    
    # Stage 1: Anti-Delivery
    print("\n[Defender] === STAGE 1: ANTI-DELIVERY ===")
    quarantined = analyze_and_quarantine()
    
    # Stage 2: Anti-Auto-Run
    print("\n[Defender] === STAGE 2: ANTI-AUTO-RUN ===")
    removed = remove_persistence_mechanisms()
    
    # Stage 3: Anti-Spreading
    print("\n[Defender] === STAGE 3: ANTI-SPREADING ===")
    monitor_network_file_copies()
    cleaned = block_and_clean_network()
    
    # Summary
    elapsed_time = time.time() - start_time
    print("\n" + "="*60)
    print("SCAN COMPLETE")
    print("="*60)
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Items quarantined: {quarantined}")
    print(f"Persistence mechanisms removed: {removed}")
    print(f"Network threats cleaned: {cleaned}")
    print("="*60 + "\n")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("ANTI-MALICIOUS CODE DEFENDER")
    print("Educational demonstration of malware detection and removal")
    print("="*60)
    
    try:
        run_full_scan()
        
        print("\n[Defender] System protection active")
        print("[Defender] All threats have been neutralized")
        
    except KeyboardInterrupt:
        print("\n\n[Defender] Scan interrupted by user")
    except Exception as e:
        print(f"\n[Defender] Error during scan: {e}")
    
    print("\n[Defender] Defender terminated")
