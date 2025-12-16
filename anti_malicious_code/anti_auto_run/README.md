# Anti-Auto-Run Techniques

## Purpose
Detects and removes malware persistence mechanisms from both the Startup folder and Windows registry.

## Workflow
1. Scans Startup folder and registry for suspicious entries.
2. Identifies and removes malware persistence.

## Key Files & Functions
- `function4_detect_persistence.py`: Detects persistence mechanisms.
- `function5_scan_registry_spyware.py`: Scans registry for spyware.
- `function6_remove_spyware_persistence.py`: Removes detected persistence.

## Usage
Run these scripts to scan and clean persistence mechanisms from the system.

## Related Attacks
See malicious_code/auto_run/technique2 for corresponding attack methods.