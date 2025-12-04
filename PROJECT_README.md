# SPYWARE ATTACK & DEFENSE DEMONSTRATION
**Educational Cybersecurity Project**

⚠️ **WARNING: FOR EDUCATIONAL USE ONLY IN VIRTUAL MACHINE ENVIRONMENT**

---

## PROJECT OVERVIEW

This project demonstrates comprehensive spyware attack techniques and their corresponding defense mechanisms. It maintains a strict 3x3 structure: **3 purposes × 3 functions = 9 functions** on both attack and defense sides.

### 📊 Attack Scenario: Professional Spyware
- **Delivery**: Victim receives fake "System Security Scanner" with professional GUI
- **Auto-Run (Data Collection)**: Spyware collects system info, files, installed apps
- **Spreading**: Data exfiltration and network propagation

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
│   │   ├── technique1/
│   │   │   └── function1_spyware_gui.py         # Function 1: Fake security GUI
│   │   └── technique2/
│   │       ├── function2_install_spyware.py     # Function 2: Install to hidden folder
│   │       └── function3_hide_spyware.py        # Function 3: Hide executable
│   │
│   ├── auto_run/                      # PURPOSE 2: AUTO-RUN (DATA COLLECTION)
│   │   ├── technique1/
│   │   │   └── function4_collect_data.py        # Function 4: Collect victim data
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
└── anti_malicious_code/               # DEFENSE SIDE
    ├── defender_scanner.py            # Main defender GUI (comprehensive scanner)
    │
    ├── anti_delivery/                 # PURPOSE 1: ANTI-DELIVERY
    │   ├── function1_detect_spyware.py          # Function 1: Process detection
    │   ├── function2_scan_spyware_files.py      # Function 2: File scanning
    │   └── function3_quarantine_spyware.py      # Function 3: Quarantine threats
    │
    ├── anti_auto_run/                 # PURPOSE 2: ANTI-AUTO-RUN
    │   ├── function4_detect_persistence.py      # Function 4: Startup detection
    │   ├── function5_scan_registry_spyware.py   # Function 5: Registry scanning
    │   └── function6_remove_spyware_persistence.py # Function 6: Remove persistence
    │
    └── anti_spreading/                # PURPOSE 3: ANTI-SPREADING
        ├── function7_monitor_exfiltration.py    # Function 7: Monitor exfiltration
        ├── function8_block_spreading.py         # Function 8: Block spreading
        └── function9_generate_report.py         # Function 9: Security report
```

---

## 🚀 USAGE INSTRUCTIONS

### **PREREQUISITE: VMware Environment**
- ✅ Run ONLY in VMware virtual machine
- ✅ Windows OS with Python 3.x installed
- ✅ Install required library: `pip install psutil`

### **Running the Spyware Attack**

1. Navigate to malicious_code directory:
   ```powershell
   cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\malicious_code"
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
| 1 | `function1_spyware_gui.py` | Delivery | Shows professional fake security scanner GUI |
| 2 | `function2_install_spyware.py` | Delivery | Creates `SystemSecurityService` hidden folder |
| 3 | `function3_hide_spyware.py` | Delivery | Copies to hidden location as `SecurityScanner.exe` |
| 4 | `function4_collect_data.py` | Auto-Run | Collects system info, file lists, installed apps |
| 5 | `function5_persistence_startup.py` | Auto-Run | Adds hidden shortcut to Startup folder |
| 6 | `function6_persistence_registry.py` | Auto-Run | Adds registry Run key: `SystemSecurityScanner` |
| 7 | `function7_scan_network.py` | Spreading | Scans network for accessible shares (simulated) |
| 8 | `function8_spread_spyware.py` | Spreading | Replicates to network with social engineering names |
| 9 | `function9_exfiltrate_report.py` | Spreading | Packages data and simulates email exfiltration |

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
- **Threading**: Background execution for non-blocking operations

### **System Requirements**
- Windows 10/11 (VMware VM)
- Python 3.7 or higher
- psutil library: `pip install psutil`
- Minimum 2GB RAM
- 100MB free disk space

### **Data Collected by Spyware** (Simulated)
- System information (hostname, username, OS version)
- File lists (Documents, Pictures, Desktop folders)
- Installed applications list
- Network configuration
- All saved to JSON format

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
- ✅ **Simulated Actions**: Network spreading and exfiltration are simulated
- ✅ **No Real Harm**: No actual data sent to external servers
- ✅ **VM Environment**: Isolated from host system
- ✅ **Easy Removal**: Defender scanner completely cleans system
- ✅ **Educational Purpose**: Demonstrates concepts, not malicious intent

### **Ethical Considerations**
- 🔒 Run ONLY in controlled lab environment
- 🔒 NEVER deploy on production systems
- 🔒 NEVER use for malicious purposes
- 🔒 VMware snapshot before testing
- 🔒 Respect cybersecurity ethics and laws

---

## 📈 PROJECT COMPLETION STATUS

✅ **100% COMPLETE**

- [x] All 9 spyware functions implemented
- [x] Professional spyware GUI (spyware_main.py)
- [x] All 9 defender functions implemented
- [x] Professional defender GUI (defender_scanner.py)
- [x] Threat detection working
- [x] Quarantine operations working
- [x] Persistence removal working
- [x] Report generation working
- [x] No syntax errors
- [x] VMware-ready

**Ready for 80% submission to lecturer** ✓

---

## 📞 PROJECT INFORMATION

**Course**: Year 3 - Term 1 - Cybersecurity  
**Project Type**: Malicious Code Attack & Defense Demonstration  
**Architecture**: 3 Purposes × 3 Functions = 9 Functions per side  
**Environment**: VMware Windows Virtual Machine  
**Language**: Python 3.x with tkinter GUI  

---

## 🎯 QUICK START GUIDE

### **For Demonstration**

```powershell
# 1. Install psutil
pip install psutil

# 2. Run spyware attack
cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\malicious_code"
python spyware_main.py
# Click "Start Security Scan" and wait for completion

# 3. Run defender scanner
cd "..\anti_malicious_code"
python defender_scanner.py
# Click "START SCAN" to detect threats
# Click "QUARANTINE THREATS" to remove
# Click "REMOVE PERSISTENCE" to clean

# 4. Verify clean system
# Run defender_scanner.py again and scan
# Should show: "✓ System Clean"
```

---

**END OF README**
