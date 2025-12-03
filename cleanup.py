"""
CLEANUP UTILITY
Removes all artifacts created by the malicious code demo

This script will:
- Remove hidden folders in AppData
- Delete startup shortcuts
- Remove registry keys
- Clean quarantine folder
"""

import os
import winreg
import shutil

def cleanup_all():
    """Remove all malicious artifacts"""
    print("="*60)
    print("CLEANUP UTILITY - Removing all demo artifacts")
    print("="*60)
    
    cleaned_count = 0
    
    # 1. Remove hidden folder
    print("\n[Cleanup] Removing hidden folder...")
    try:
        appdata = os.getenv('APPDATA')
        hidden_folder = os.path.join(appdata, "WindowsUpdateService")
        if os.path.exists(hidden_folder):
            shutil.rmtree(hidden_folder)
            print(f"[Cleanup] Removed: {hidden_folder}")
            cleaned_count += 1
        else:
            print("[Cleanup] Hidden folder not found")
    except Exception as e:
        print(f"[Cleanup] Error removing hidden folder: {e}")
    
    # 2. Remove startup shortcut
    print("\n[Cleanup] Removing startup shortcut...")
    try:
        startup_folder = os.path.join(os.getenv('APPDATA'),
                                     r'Microsoft\Windows\Start Menu\Programs\Startup')
        shortcut_path = os.path.join(startup_folder, "WindowsUpdateService.lnk")
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            print(f"[Cleanup] Removed: {shortcut_path}")
            cleaned_count += 1
        else:
            print("[Cleanup] Startup shortcut not found")
    except Exception as e:
        print(f"[Cleanup] Error removing shortcut: {e}")
    
    # 3. Remove registry key
    print("\n[Cleanup] Removing registry key...")
    try:
        key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        try:
            winreg.DeleteValue(key, 'WindowsUpdateService')
            print(f"[Cleanup] Removed: HKCU\\{key_path}\\WindowsUpdateService")
            cleaned_count += 1
        except FileNotFoundError:
            print("[Cleanup] Registry key not found")
        winreg.CloseKey(key)
    except Exception as e:
        print(f"[Cleanup] Error removing registry key: {e}")
    
    # 4. Clean quarantine folder
    print("\n[Cleanup] Cleaning quarantine folder...")
    try:
        quarantine_folder = os.path.join(os.getenv('TEMP'), 'MalwareQuarantine')
        if os.path.exists(quarantine_folder):
            shutil.rmtree(quarantine_folder)
            print(f"[Cleanup] Removed: {quarantine_folder}")
            cleaned_count += 1
        else:
            print("[Cleanup] Quarantine folder not found")
    except Exception as e:
        print(f"[Cleanup] Error cleaning quarantine: {e}")
    
    print("\n" + "="*60)
    print(f"CLEANUP COMPLETE - Removed {cleaned_count} artifacts")
    print("="*60)

if __name__ == "__main__":
    cleanup_all()
    input("\nPress Enter to exit...")
