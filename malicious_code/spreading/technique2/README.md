# Spreading Technique 2: Spyware Spreading & Data Exfiltration

## Purpose
Spreads spyware to other machines and exfiltrates sensitive data from infected hosts.

## Workflow
1. Malware attempts to copy itself to other machines.
2. Exfiltrates collected data to attacker server.

## Key Files & Functions
- `function8_spread_spyware.py`: Handles spreading to other hosts.
- `function9_exfiltrate_report.py`: Exfiltrates data.
- `main.py`: Orchestrates spreading and exfiltration.

## Usage
Run `main.py` to simulate spreading and data exfiltration.

## Defense
See anti_malicious_code/anti_spreading for monitoring and blocking methods.