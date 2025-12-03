"""
Anti-Auto-Run Function 6: Remove Persistence Mechanisms
Removes startup shortcuts and registry keys
"""

import os
import winreg

def remove_persistence_mechanisms(shortcuts, registry_entries):
    """
    Remove all persistence mechanisms
    Args:
        shortcuts: List of suspicious shortcut paths
        registry_entries: List of suspicious registry entry dictionaries
    Returns: Number of items removed
    """
    print("[Defender] Function 6: Removing persistence mechanisms...")
    
    removed_count = 0
    
    try:
        # Remove startup shortcuts
        for shortcut in shortcuts:
            try:
                os.remove(shortcut)
                print(f"[Defender]   Removed shortcut: {shortcut}")
                removed_count += 1
            except Exception as e:
                print(f"[Defender]   Error removing shortcut: {e}")
        
        # Remove registry entries
        for entry in registry_entries:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, entry['key'], 0, winreg.KEY_SET_VALUE)
                winreg.DeleteValue(key, entry['name'])
                winreg.CloseKey(key)
                print(f"[Defender]   Removed registry entry: {entry['name']}")
                removed_count += 1
            except Exception as e:
                print(f"[Defender]   Error removing registry entry: {e}")
        
        print(f"[Defender]   Total persistence mechanisms removed: {removed_count}")
        return removed_count
    except Exception as e:
        print(f"[Defender] Error removing persistence: {e}")
        return 0
