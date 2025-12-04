"""
Anti-Auto-Run Function 5: Scan Registry for Spyware
Scans registry Run keys for spyware persistence entries
"""

import winreg

def scan_registry_spyware():
    """
    Scan registry Run keys for spyware entries
    Returns: List of spyware registry entry dictionaries
    """
    print("[Anti-Spyware] Function 5: Scanning registry for spyware...")
    
    spyware_entries = []
    
    # Spyware registry entry keywords
    spyware_keywords = [
        'SecurityScanner', 'SystemSecurity', 'SecurityService',
        'WindowsUpdate', 'SystemService', 'SecurityUpdate'
    ]
    
    try:
        # Scan HKEY_CURRENT_USER Run keys
        key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    
                    # Check for spyware keywords
                    if any(keyword in name for keyword in spyware_keywords) or \
                       any(keyword in value for keyword in spyware_keywords):
                        spyware_entries.append({
                            'hive': 'HKCU',
                            'key': key_path,
                            'name': name,
                            'value': value
                        })
                        print(f"[Anti-Spyware]   ⚠ Found spyware registry: {name}")
                    
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(key)
        except FileNotFoundError:
            print("[Anti-Spyware]   Run key not found in HKCU")
        
        if not spyware_entries:
            print("[Anti-Spyware]   ✓ No spyware registry entries detected")
        else:
            print(f"[Anti-Spyware]   ⚠ Total registry entries found: {len(spyware_entries)}")
        
        return spyware_entries
    except Exception as e:
        print(f"[Anti-Spyware] Error scanning registry: {e}")
        return []
