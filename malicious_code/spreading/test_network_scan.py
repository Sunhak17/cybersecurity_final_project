"""
Test Network Scanning - Diagnostic tool to find computers on local network
"""

import socket
import subprocess
import re
import sys

def test_network_discovery():
    """Test all network discovery methods"""
    print("=" * 60)
    print("NETWORK DISCOVERY DIAGNOSTIC TEST")
    print("=" * 60)
    
    # Get local info
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\n[LOCAL INFO]")
    print(f"  Hostname: {hostname}")
    print(f"  IP Address: {local_ip}")
    
    discovered_computers = []
    
    # Test 1: net view
    print(f"\n[TEST 1: NET VIEW]")
    try:
        result = subprocess.run(['net', 'view'], capture_output=True, text=True, timeout=30)
        print(f"  Return code: {result.returncode}")
        if result.returncode == 0:
            print(f"  Output:\n{result.stdout}")
            for line in result.stdout.split('\n'):
                match = re.search(r'\\\\([\w\-]+)', line)
                if match:
                    computer_name = match.group(1)
                    discovered_computers.append(computer_name)
                    print(f"  ✓ Found: {computer_name}")
        else:
            print(f"  Error: {result.stderr}")
    except Exception as e:
        print(f"  Exception: {e}")
    
    # Test 2: ARP cache
    print(f"\n[TEST 2: ARP CACHE]")
    try:
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=10)
        print(f"  Return code: {result.returncode}")
        if result.returncode == 0:
            arp_count = 0
            for line in result.stdout.split('\n'):
                match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\-]+)\s+(\w+)', line)
                if match:
                    ip, mac, type_ = match.groups()
                    if type_.lower() == 'dynamic' and ip != local_ip:
                        arp_count += 1
                        print(f"  IP: {ip} | MAC: {mac} | Type: {type_}")
                        # Try to resolve hostname
                        try:
                            host = socket.gethostbyaddr(ip)[0]
                            print(f"    └─ Hostname: {host}")
                            if host not in discovered_computers:
                                discovered_computers.append(host)
                        except:
                            print(f"    └─ Cannot resolve hostname")
            print(f"  Total dynamic entries: {arp_count}")
        else:
            print(f"  Error: {result.stderr}")
    except Exception as e:
        print(f"  Exception: {e}")
    
    # Test 3: Ping sweep of local subnet
    print(f"\n[TEST 3: PING SWEEP]")
    subnet_parts = local_ip.split('.')
    if len(subnet_parts) == 4:
        subnet = '.'.join(subnet_parts[:3])
        print(f"  Scanning subnet: {subnet}.0/24 (first 10 IPs)")
        alive_hosts = []
        for i in range(1, 11):
            target_ip = f"{subnet}.{i}"
            if target_ip != local_ip:
                try:
                    result = subprocess.run(['ping', '-n', '1', '-w', '500', target_ip],
                                          capture_output=True, text=True, timeout=2)
                    if 'Reply from' in result.stdout or result.returncode == 0:
                        alive_hosts.append(target_ip)
                        print(f"  ✓ {target_ip} is alive")
                        # Try hostname
                        try:
                            host = socket.gethostbyaddr(target_ip)[0]
                            print(f"    └─ Hostname: {host}")
                        except:
                            print(f"    └─ No hostname")
                except:
                    pass
        print(f"  Total alive hosts: {len(alive_hosts)}")
    
    # Test 4: Check for shared folders on discovered computers
    print(f"\n[TEST 4: SHARE ENUMERATION]")
    print(f"  Testing {len(discovered_computers)} discovered computers...")
    accessible_shares = []
    
    for computer in discovered_computers[:5]:  # Test first 5
        print(f"\n  Computer: {computer}")
        try:
            result = subprocess.run(['net', 'view', f'\\\\{computer}'], 
                                  capture_output=True, text=True, timeout=15)
            if result.returncode == 0:
                print(f"    Shares found:")
                for line in result.stdout.split('\n'):
                    if 'Disk' in line:
                        parts = line.split()
                        if parts:
                            share_name = parts[0]
                            share_path = f"\\\\{computer}\\{share_name}"
                            print(f"      - {share_path}")
                            accessible_shares.append(share_path)
            else:
                print(f"    No shares or access denied")
                print(f"    Error: {result.stderr[:100]}")
        except Exception as e:
            print(f"    Exception: {e}")
    
    # Summary
    print(f"\n" + "=" * 60)
    print(f"SUMMARY")
    print(f"=" * 60)
    print(f"  Discovered computers: {len(discovered_computers)}")
    for comp in discovered_computers:
        print(f"    - {comp}")
    print(f"  Accessible shares: {len(accessible_shares)}")
    for share in accessible_shares:
        print(f"    - {share}")
    
    if not discovered_computers:
        print(f"\n⚠ No computers found on network!")
        print(f"  Possible reasons:")
        print(f"    - Firewall blocking network discovery")
        print(f"    - Network discovery disabled in Windows")
        print(f"    - On isolated network or not connected")
        print(f"    - Other computers have SMB/NetBIOS disabled")

if __name__ == "__main__":
    test_network_discovery()
