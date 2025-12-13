"""
Enhanced Network Scanner - Finds computers and shares on local network
"""

import socket
import subprocess
import re
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_local_info():
    """Get local machine info"""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return hostname, local_ip

def scan_arp_cache():
    """Scan ARP cache for active IPs"""
    print("[*] Scanning ARP cache...")
    ips = []
    try:
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\-]+)\s+dynamic', line, re.IGNORECASE)
                if match:
                    ip = match.group(1)
                    mac = match.group(2)
                    ips.append((ip, mac))
                    print(f"  Found: {ip} ({mac})")
    except Exception as e:
        print(f"  Error: {e}")
    return ips

def test_smb_connection(ip):
    """Test if IP has SMB/CIFS shares available"""
    try:
        # Try net view with IP
        result = subprocess.run(['net', 'view', f'\\\\{ip}'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            # Parse shares
            shares = []
            for line in result.stdout.split('\n'):
                if 'Disk' in line:
                    parts = line.split()
                    if parts:
                        share_name = parts[0]
                        shares.append(share_name)
            return ip, True, shares
        else:
            return ip, False, []
    except:
        return ip, False, []

def get_hostname_from_ip(ip):
    """Try to get hostname from IP"""
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname.split('.')[0]
    except:
        return None

def scan_network_enhanced():
    """Enhanced network scanner"""
    print("=" * 70)
    print("ENHANCED NETWORK SCANNER")
    print("=" * 70)
    
    # Get local info
    hostname, local_ip = get_local_info()
    print(f"\n[LOCAL MACHINE]")
    print(f"  Hostname: {hostname}")
    print(f"  IP: {local_ip}")
    
    # Scan ARP cache
    print(f"\n[ARP CACHE SCAN]")
    arp_ips = scan_arp_cache()
    
    if not arp_ips:
        print("  No devices found in ARP cache")
        return []
    
    # Test SMB connections in parallel
    print(f"\n[SMB CONNECTION TEST]")
    print(f"  Testing {len(arp_ips)} IPs for SMB shares...")
    
    accessible_shares = []
    computers_found = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(test_smb_connection, ip): ip for ip, mac in arp_ips}
        
        for future in as_completed(futures):
            ip, has_smb, shares = future.result()
            hostname_resolved = get_hostname_from_ip(ip)
            
            if has_smb and shares:
                print(f"  ✓ {ip} ({hostname_resolved or 'unknown'})")
                computers_found.append((ip, hostname_resolved))
                for share in shares:
                    share_path = f"\\\\{ip}\\{share}"
                    print(f"    └─ {share_path}")
                    accessible_shares.append(share_path)
            elif has_smb:
                print(f"  • {ip} ({hostname_resolved or 'unknown'}) - SMB available but no shares")
                computers_found.append((ip, hostname_resolved))
            else:
                print(f"  ✗ {ip} - No SMB or access denied")
    
    # Summary
    print(f"\n" + "=" * 70)
    print(f"SCAN RESULTS")
    print(f"=" * 70)
    print(f"  Total IPs in ARP cache: {len(arp_ips)}")
    print(f"  Computers with SMB: {len(computers_found)}")
    print(f"  Accessible shares: {len(accessible_shares)}")
    
    if computers_found:
        print(f"\n  Discovered Computers:")
        for ip, hostname in computers_found:
            print(f"    - {hostname or 'Unknown'} ({ip})")
    
    if accessible_shares:
        print(f"\n  Accessible Shares:")
        for share in accessible_shares:
            print(f"    - {share}")
    else:
        print(f"\n  ⚠ No accessible shares found")
        print(f"  Possible reasons:")
        print(f"    - File sharing disabled on other computers")
        print(f"    - Password-protected shares (credentials needed)")
        print(f"    - Firewall blocking SMB (port 445)")
        print(f"    - Network discovery disabled")
    
    print(f"\n  To enable file sharing on other computers:")
    print(f"    1. Open 'Network and Sharing Center'")
    print(f"    2. Click 'Change advanced sharing settings'")
    print(f"    3. Enable 'Turn on network discovery'")
    print(f"    4. Enable 'Turn on file and printer sharing'")
    print(f"    5. Share a folder (right-click > Properties > Sharing)")
    
    return accessible_shares

if __name__ == "__main__":
    scan_network_enhanced()
