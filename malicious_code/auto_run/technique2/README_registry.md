# Auto-Run Technique 2: Registry Persistence

## Purpose
Ensures malware persists by modifying Windows registry keys to auto-start on boot.

## Workflow
1. Malware writes itself to a registry run key.
2. On reboot, Windows executes the malware from the registry entry.

## Key Files & Functions
- `function6_persistence_registry.py`: Implements registry-based persistence.
- `main.py`: Orchestrates the persistence process.

## Usage
Run `main.py` to simulate registry-based persistence.

## Defense
See anti_malicious_code/anti_auto_run for detection and removal methods.