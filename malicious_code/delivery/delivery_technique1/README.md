# Delivery Technique 1: Phishing Direct Download

## Purpose
Simulates a phishing attack where a victim is tricked into downloading and executing a malicious file via a fake email or website.

## Workflow
1. Attacker sends a phishing email with a download link.
2. Victim clicks the link and downloads the spyware installer.
3. Spyware is installed and begins execution.

## Key Files & Functions
- `auto_send_phishing_direct_download.py`: Automates sending phishing emails.
- `function2_install_spyware.py`: Handles spyware installation.
- `function3_hide_spyware.py`: Hides spyware after installation.

## Usage
Run `setup_delivery.py` to start the phishing delivery simulation. Use `START_SERVERS.bat` to launch supporting servers.

## Defense
See anti-malicious/anti_delivery for detection and blocking methods.