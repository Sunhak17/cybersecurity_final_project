# ANTI-DELIVERY DETECTION - Testing Guide

This folder contains detection mechanisms for **both delivery techniques**.

---

## 🛡️ Detection Functions

### **Function 1: detect_spyware_processes()**
**Purpose:** Detect spyware processes from both delivery methods

**Detects:**
- **Technique 1:** Fake security scanner processes (SecurityScanner, AntivirusScanner)
- **Technique 2:** Fake update processes (WindowsUpdate, UpdateInstaller, KB5034203)

**Location:** `function1_detect_spyware.py`

---

### **Function 2: scan_spyware_files()**
**Purpose:** Scan file system for spyware installations

**Detects:**
- **Technique 1:** SystemSecurityService, SecurityScanner folders
- **Technique 2:** WindowsUpdateService, SecurityUpdate folders
- Executables, data files, logs in suspicious locations

**Location:** `function2_scan_spyware_files.py`

---

## 🧪 Testing Detection

### **Test Against Technique 1 (Fake Security Scanner)**

```powershell
# First, run the attack
cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\malicious_code\delivery\technique1"
python main.py

# Then detect it
cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\anti_malicious_code\anti_delivery"
python test_detect_technique1.py
```

**Expected Detection:**
- ⚠️ Fake security scanner folders
- ⚠️ SystemSecurityService directory
- ⚠️ Hidden executables and data files

---

### **Test Against Technique 2 (Fake Software Update)**

```powershell
# First, run the attack
cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\malicious_code\delivery\technique2"
python main.py

# Then detect it
cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\anti_malicious_code\anti_delivery"
python test_detect_technique2.py
```

**Expected Detection:**
- ⚠️ Fake update installer folders
- ⚠️ WindowsUpdateService directory (if created)
- ⚠️ Update-related executables

---

### **Comprehensive Detection (Both Techniques)**

```powershell
cd "c:\Users\TUF\Documents\Year3\Term 1\Cybersecurity\Project\anti_malicious_code"
python defender_scanner.py
```

**Click "START SCAN"** - will detect threats from both techniques in Phase 1.

---

## 📊 Detection Comparison

| Feature | Technique 1 Detection | Technique 2 Detection |
|---------|----------------------|----------------------|
| **Process Keywords** | security, scanner, antivirus | update, installer, KB5034 |
| **Folder Indicators** | SystemSecurityService | WindowsUpdateService |
| **Behavior Patterns** | Fake scanning activity | Fake update progress |
| **File Signatures** | SecurityScanner.exe | UpdateInstaller.exe |

---

## 🎓 For Demonstration

**Show parallel attack & defense:**

### **Scenario 1: Social Engineering Attack**
1. Run `delivery/technique1/main.py` (fake scanner)
2. Run `anti_delivery/test_detect_technique1.py`
3. Show detection of fake security software

### **Scenario 2: Drive-by Download**
1. Run `delivery/technique2/main.py` (fake update)
2. Run `anti_delivery/test_detect_technique2.py`
3. Show detection of fake update installer

### **Scenario 3: Full System Scan**
1. Run both attack techniques
2. Run `defender_scanner.py`
3. Show comprehensive detection of all threats

---

## ⚠️ Detection Indicators

### **Technique 1 Indicators:**
- ✓ Process names containing: security, scanner, antivirus
- ✓ Folders: SystemSecurityService, SecurityScanner
- ✓ Files: SecurityScanner.exe, system_scan.log

### **Technique 2 Indicators:**
- ✓ Process names containing: update, installer, patch
- ✓ Folders: WindowsUpdateService, SecurityUpdate
- ✓ Files: UpdateInstaller.exe, KB*.exe

---

## 🔗 Related Files

**Detection Functions:**
- `function1_detect_spyware.py` - Process detection
- `function2_scan_spyware_files.py` - File system scanning
- `function3_quarantine_spyware.py` - Threat removal

**Test Scripts:**
- `test_detect_technique1.py` - Test vs social engineering
- `test_detect_technique2.py` - Test vs drive-by download

**Main Application:**
- `defender_scanner.py` - Full GUI scanner (detects both)

---

## 💡 Key Points for Lecturer

1. **Each delivery technique has unique signatures**
   - Technique 1: Security-themed names
   - Technique 2: Update-themed names

2. **Detection uses multiple methods**
   - Process monitoring (runtime detection)
   - File system scanning (installation detection)

3. **Both techniques are detected by same functions**
   - Demonstrates comprehensive defense
   - Single scanner detects multiple attack vectors

4. **Real-world applicability**
   - Social engineering requires user awareness
   - Drive-by downloads require system hardening
