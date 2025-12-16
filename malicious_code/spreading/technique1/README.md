# Spreading Technique 1: Network Scanning

## Purpose
Scans the local network to identify other vulnerable machines for potential infection.

## Workflow
1. Malware scans the network for active hosts.
2. Identifies targets based on open ports or vulnerabilities.
3. Prepares to spread or exfiltrate data.

## Key Files & Functions
- `function7_scan_network.py`: Performs network scanning.
- `main.py`: Orchestrates the scanning process.
- `test_scan.py`: Test script for scanning functionality.

## Usage
Run `main.py` to start network scanning. Use `test_scan.py` for testing.

## Defense
See anti_malicious_code/anti_spreading for monitoring and blocking methods.