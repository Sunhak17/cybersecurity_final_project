# Auto-Run Technique 1: Startup Folder Persistence

## Purpose
Ensures malware persists by adding itself to the Windows Startup folder, so it runs on every system boot.

## Workflow
1. Malware copies itself to the Startup folder.
2. On reboot, Windows automatically executes the malware.

## Key Files & Functions
- `function5_persistence_startup.py`: Implements startup folder persistence.
- `main.py`: Orchestrates the persistence process.

## Usage
Run `main.py` to simulate persistence via the Startup folder.

## Defense
See anti_malicious_code/anti_auto_run for detection and removal methods.