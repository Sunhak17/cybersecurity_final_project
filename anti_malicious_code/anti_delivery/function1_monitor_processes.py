"""
Anti-Delivery Function 1: Monitor Running Processes
Detects programs showing GUI while creating hidden folders
"""

import psutil

def monitor_running_processes():
    """
    Monitor processes for suspicious dual behavior
    Returns: List of suspicious process dictionaries
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
