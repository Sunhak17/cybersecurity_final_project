"""
Anti-Delivery Function 1: Detect Spyware Processes
Detects spyware processes from both delivery techniques:
- Technique 1: Fake Security Scanner processes
- Technique 2: Fake Update installer processes
"""

import psutil

def detect_spyware_processes():
    """
    Monitor and detect spyware processes from both delivery techniques
    Returns: List of suspicious spyware process dictionaries
    """
    print("\n[Anti-Spyware] Function 1: Detecting spyware processes...")
    
    suspicious_processes = []
    
    # Spyware keywords for BOTH delivery techniques
    technique1_keywords = [
        'securityscanner', 'systemsecurity',
        'fakescanner', 'fakeantivirus'  # Fake security software (removed generic 'scanner', 'defender', 'antivirus' to avoid false positives)
    ]
    
    technique2_keywords = [
        'windowsupdate', 'update', 'installer',
        'kb5034', 'patch'  # Fake Windows update
    ]
    
    general_spyware = [
        'spyware', 'keylog', 'screenshot', 'monitor',
        'emailsender', 'datacollector'
    ]
    
    all_keywords = technique1_keywords + technique2_keywords + general_spyware
    
    # Exclude legitimate Windows system processes to avoid false positives
    system_processes = [
        'mpdefendercoreservice', 'msmpeng', 'nissrv', 'securityhealthservice',
        'trustedinstaller', 'am_delta_patch', 'mpcmdrun', 'windows defender',
        'svchost', 'csrss', 'lsass', 'services', 'smss', 'wininit',
        'explorer', 'dwm', 'conhost', 'taskhostw'
    ]
    
    try:
        for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
            try:
                proc_info = proc.info
                proc_name = proc_info['name'].lower() if proc_info['name'] else ''
                
                # Skip system processes
                if any(sys_proc in proc_name for sys_proc in system_processes):
                    continue
                
                # Check for spyware keywords in process name
                for keyword in all_keywords:
                    if keyword in proc_name:
                        technique = "Technique 1 (Fake Scanner)" if keyword in technique1_keywords else \
                                  "Technique 2 (Fake Update)" if keyword in technique2_keywords else \
                                  "General Spyware"
                        
                        suspicious_processes.append({
                            'pid': proc_info['pid'],
                            'name': proc_info['name'],
                            'exe': proc_info['exe'],
                            'technique': technique
                        })
                        print(f"[Anti-Spyware]   ⚠ Found {technique}: {proc_info['name']} (PID: {proc_info['pid']})")
                        break  # Avoid duplicate entries
                        
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if not suspicious_processes:
            print("[Anti-Spyware]   ✓ No spyware processes detected")
        else:
            print(f"[Anti-Spyware]   ⚠ Total spyware processes found: {len(suspicious_processes)}")
        
        return suspicious_processes
    except Exception as e:
        print(f"[Anti-Spyware] Error monitoring processes: {e}")
        return []
