# Cybersecurity Project: Malicious Code vs Anti-Malicious Code

## ⚠️ EDUCATIONAL PURPOSE ONLY
This project is for educational demonstration in a controlled lab environment. Do NOT use these techniques maliciously or deploy on production systems.

---

## 📋 Project Overview

This project demonstrates a complete malware attack chain and its corresponding defense mechanisms:

### **Attacker Side: Malicious Email Sender (9 Functions)**
- **Delivery Stage (3 functions):** Shows GUI while creating hidden folders
- **Auto-Run Stage (3 functions):** Adds persistence via startup and registry
- **Spreading Stage (3 functions):** Replicates to network shares

### **Defender Side: Anti-Malicious Scanner (9 Functions)**
- **Anti-Delivery (3 functions):** Detects and quarantines hidden threats
- **Anti-Auto-Run (3 functions):** Removes persistence mechanisms
- **Anti-Spreading (3 functions):** Blocks network spreading

---

## 📁 Project Structure

```
Project/
├── PROPOSAL.md                      # Detailed project proposal
├── malicious_email_sender.py        # Main malicious code (9 functions)
├── defender_scanner.py              # Main anti-malicious code (9 functions)
├── cleanup.py                       # Cleanup utility
└── README.md                        # This file
```

---

## 🚀 How to Use

### **1. Run the Malicious Code (Attacker Demo)**

```powershell
python malicious_email_sender.py
```

**What happens:**
1. A GUI window appears asking for your email
2. Enter any email address and click "Send Test Email"
3. **Behind the scenes:**
   - Hidden folder created in `%APPDATA%\WindowsUpdateService`
   - Executable copied to hidden location
   - Startup shortcut added
   - Registry Run key added
   - Network spreading simulated

**User Experience:**
- User only sees the email GUI
- Sees "Email sent successfully!" message
- Unaware of malicious activities in background

---

### **2. Run the Defender (Detection Demo)**

```powershell
python defender_scanner.py
```

**What happens:**
1. Scans for suspicious processes
2. Detects hidden folders in AppData
3. Quarantines malicious files
4. Removes startup shortcuts
5. Removes registry keys
6. Scans and cleans network shares (simulated)

**Output:**
- Detailed log of all detected threats
- Actions taken to neutralize threats
- Summary of quarantined/removed items

---

### **3. Clean Up All Artifacts**

```powershell
python cleanup.py
```

**What it removes:**
- Hidden folder: `%APPDATA%\WindowsUpdateService`
- Startup shortcut: `WindowsUpdateService.lnk`
- Registry key: `HKCU\...\Run\WindowsUpdateService`
- Quarantine folder: `%TEMP%\MalwareQuarantine`

---

## 🎯 9 Functions Breakdown

### **Malicious Code Functions:**
1. `show_email_gui()` - Display legitimate-looking interface
2. `create_hidden_folder()` - Create hidden AppData folder
3. `copy_to_hidden_location()` - Copy executable to hidden location
4. `send_fake_email()` - Send email while triggering persistence
5. `add_startup_shortcut()` - Add to Startup folder
6. `add_registry_key()` - Add to registry Run key
7. `scan_network_shares()` - Find accessible network shares
8. `replicate_to_shares()` - Copy to network locations
9. `log_and_cleanup()` - Log infection status

### **Defender Functions:**
1. `monitor_running_processes()` - Detect suspicious processes
2. `scan_hidden_folders()` - Find hidden folders in AppData
3. `analyze_and_quarantine()` - Terminate and quarantine threats
4. `scan_startup_folder()` - Detect malicious shortcuts
5. `scan_registry_run_keys()` - Find malicious registry entries
6. `remove_persistence_mechanisms()` - Remove all persistence
7. `monitor_network_file_copies()` - Watch network activity
8. `scan_network_shares()` - Scan shares for malware
9. `block_and_clean_network()` - Remove threats from network

---

## 🔒 Safety Features

- Network spreading is **simulated only** (no actual file copies to network)
- All malicious actions are **logged and reversible**
- Cleanup utility provided to remove all artifacts
- Code is clearly labeled as educational

---

## 📊 Demo Scenario

### **Attack Flow:**
1. Victim receives "Email Sender Utility.exe"
2. Victim runs the program
3. GUI appears asking for email
4. Victim enters email and clicks send
5. Email is sent (looks legitimate)
6. Hidden actions occur in background
7. Program closes normally
8. Malware persists and spreads

### **Defense Flow:**
1. Defender scanner runs
2. Detects GUI program creating hidden folders
3. Identifies persistence mechanisms
4. Quarantines malicious files
5. Removes all persistence
6. Blocks network spreading
7. System is clean and protected

---

## 🛠️ Requirements

- **OS:** Windows 10/11
- **Python:** 3.7+
- **Dependencies:** 
  ```powershell
  pip install psutil
  ```

---

## 📝 Testing Instructions

### **Recommended Testing Order:**
1. Run `malicious_email_sender.py` first
2. Wait for it to complete
3. Run `defender_scanner.py` to detect and remove
4. Run `cleanup.py` to ensure everything is removed

### **Expected Results:**
- Malicious code creates 4 artifacts (folder, exe, shortcut, registry key)
- Defender detects and removes all 4 artifacts
- Cleanup ensures nothing remains

---

## ⚖️ Legal Disclaimer

This code is provided for **educational purposes only** in controlled lab environments. 

**You must NOT:**
- Deploy this code on any system you don't own
- Use it for malicious purposes
- Distribute the malicious code to others
- Test on production systems

**By using this code, you agree:**
- To use it only for educational purposes
- To use it only in isolated lab environments
- To take full responsibility for any misuse
- To comply with all applicable laws

---

## 👥 Project Team

[Add your team members here]

---

## 📄 License

Educational use only. Not for distribution or commercial use.

---

## 🎓 Learning Objectives

This project demonstrates:
1. How malware uses social engineering (fake GUI)
2. Common persistence techniques (startup, registry)
3. Network spreading mechanisms
4. Detection techniques (process monitoring, file scanning)
5. Remediation strategies (quarantine, removal)

---

## 📞 Support

For questions about this educational project, contact your instructor.

**Do NOT use this code for any malicious purposes.**
