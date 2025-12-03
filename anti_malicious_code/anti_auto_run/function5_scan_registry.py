"""
Anti-Auto-Run Function 5: Scan Registry Run Keys
Scans registry Run keys for malicious entries
"""

import winreg

def scan_registry_run_keys():
    """
    Scan registry Run keys for malicious entries
    Returns: List of suspicious registry entry dictionaries
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
