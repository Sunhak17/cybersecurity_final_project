"""
Anti-Auto-Run Function 6: Remove Spyware Persistence
Removes all spyware persistence mechanisms (shortcuts and registry keys)
"""

import os
import winreg

def remove_spyware_persistence(shortcuts, registry_entries):
    """
    Remove all spyware persistence mechanisms
    Args:
        shortcuts: List of spyware shortcut paths
        registry_entries: List of spyware registry entry dictionaries
    Returns: Dictionary with removal statistics
    """
    print("[Anti-Spyware] Function 6: Removing spyware persistence...")
    
    removal_stats = {
        'shortcuts_removed': 0,
        'registry_removed': 0
    }
    
    try:
        # Remove startup shortcuts
        for shortcut in shortcuts:
            try:
                if os.path.exists(shortcut):
                    os.remove(shortcut)
                    print(f"[Anti-Spyware]   ✓ Removed shortcut: {os.path.basename(shortcut)}")
                    removal_stats['shortcuts_removed'] += 1
            except Exception as e:
                print(f"[Anti-Spyware]   ✗ Error removing shortcut: {e}")
        
        # Remove registry entries
        for entry in registry_entries:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, entry['key'], 0, winreg.KEY_SET_VALUE)
                winreg.DeleteValue(key, entry['name'])
                winreg.CloseKey(key)
                print(f"[Anti-Spyware]   ✓ Removed registry entry: {entry['name']}")
                removal_stats['registry_removed'] += 1
            except Exception as e:
                print(f"[Anti-Spyware]   ✗ Error removing registry entry: {e}")
        
        print(f"\n[Anti-Spyware] Persistence Removal Summary:")
        print(f"  - Shortcuts removed: {removal_stats['shortcuts_removed']}")
        print(f"  - Registry entries removed: {removal_stats['registry_removed']}")
        
        return removal_stats
    except Exception as e:
        print(f"[Anti-Spyware] Error removing persistence: {e}")
        return removal_stats
