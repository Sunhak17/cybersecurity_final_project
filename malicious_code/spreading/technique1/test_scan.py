from function7_scan_network import scan_network_targets

print("\n" + "="*70)
print("NETWORK SCANNING TEST - Finding devices on your WiFi")
print("="*70)

targets = scan_network_targets()

print("\n" + "="*70)
print("SCAN RESULTS")
print("="*70)
print(f"Total devices/shares found: {len(targets)}")
if targets:
    for i, target in enumerate(targets, 1):
        print(f"  {i}. {target}")
else:
    print("  No accessible shares found")
print("="*70)
