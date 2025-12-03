# Project Proposal: Malicious Code vs Anti-Malicious Code

## Overview
This project demonstrates one complete malicious code implementation with 9 functions covering delivery, auto-run, and spreading stages, along with a corresponding anti-malicious defense system with 9 functions to detect and block each stage.

**Attack Scenario:**
The attacker sends an executable file that appears to be a legitimate email utility. When the victim runs it:
1. A GUI appears asking the user to enter their email address
2. The program claims to send an email (legitimate-looking feature)
3. **Hidden malicious actions occur in the background:**
   - Creates a hidden folder and copies itself there
   - Adds itself to startup for persistence
   - Spreads to network shares
4. The user only sees the email interface and doesn't know about the malicious activities

---

## ATTACKER SIDE - Malicious Code (9 Functions Total)

### 1. DELIVERY STAGE (3 Functions)
**Goal:** Execute malicious actions while showing a legitimate-looking UI to the user

**Function 1: `show_email_gui()`**
- Displays a GUI window with title "Email Sender Utility"
- Shows input field for email address
- Shows "Send Email" button
- **Purpose:** Distracts user while malicious code runs in background

**Function 2: `create_hidden_folder()`**
- Creates a hidden folder in AppData\Roaming\WindowsUpdate (runs in background)
- Sets folder attributes to hidden
- Returns the folder path for next functions
- **User doesn't see this happening**

**Function 3: `copy_to_hidden_location()`**
- Copies the executable itself to the hidden folder
- Renames it to look like a system file (e.g., "WindowsUpdateService.exe")
- Returns success status
- **User is focused on the email GUI**

**Flow:** User runs EXE → GUI appears asking for email → Hidden folder created in background → EXE copied to hidden location

---

### 2. AUTO-RUN STAGE (3 Functions)
**Goal:** Ensure the program runs automatically on every system start (while user types email)

**Function 4: `send_fake_email()`**
- When user clicks "Send Email" button, shows "Email sent successfully!" message
- Actually sends the email to make it look legitimate
- **Meanwhile, triggers auto-run functions in background**

**Function 5: `add_startup_shortcut()`**
- Creates shortcut in Startup folder pointing to hidden payload
- Sets shortcut to run minimized/hidden (no window appears on startup)
- Returns shortcut path
- **Happens while "Sending email..." message is displayed**

**Function 6: `add_registry_key()`**
- Adds entry to HKCU\Software\Microsoft\Windows\CurrentVersion\Run
- Points to the hidden payload location in AppData
- Provides backup persistence if startup shortcut is deleted
- **User sees "Email sent!" and closes the program, unaware of persistence**

**Flow:** User enters email and clicks Send → Email actually sent (to look legitimate) → Startup shortcut created → Registry key added → User closes program thinking it's done

---

### 3. SPREADING STAGE (3 Functions)
**Goal:** Silently copy the malicious program to other locations to infect more systems

**Function 7: `scan_network_shares()`**
- Runs in background after user closes the program
- Scans local network for accessible shared folders
- Tests write permissions on each share
- Returns list of writable shares
- **User has no idea this is happening**

**Function 8: `replicate_to_shares()`**
- Copies the malicious "Email Sender Utility.exe" to each accessible share
- Uses tempting names to trick other users (e.g., "PayrollReport.exe", "CompanyPhotos.exe")
- Other users who run it will see the same email GUI and get infected

**Function 9: `log_and_cleanup()`**
- Records which shares were successfully infected
- Saves log to hidden folder
- Closes any visible windows silently
- Program appears to have finished normally

**Flow:** User closes program → Network shares scanned in background → Payload copied to shares with tempting names → Log saved → Process ends cleanly

---

## DEFENDER SIDE - Anti-Malicious Code (9 Functions Total)

### 1. ANTI-DELIVERY STAGE (3 Functions)
**Goal:** Detect programs that create hidden folders while showing fake GUIs

**Function 1: `monitor_running_processes()`**
- Monitors all running programs in real-time
- Detects programs that show GUI windows
- Checks if these programs are also creating hidden folders in AppData
- Flags programs doing "dual behavior" (visible GUI + hidden actions)

**Function 2: `scan_hidden_folders()`**
- Scans AppData\Roaming for newly created hidden folders
- Detects folders with suspicious names (e.g., "WindowsUpdate", "SystemService")
- Checks if executables in these folders match running processes

**Function 3: `analyze_and_quarantine()`**
- Analyzes suspicious executables found in hidden folders
- Checks digital signatures (malicious ones are usually unsigned)
- Moves suspicious files to quarantine
- Terminates the malicious GUI process
- Alerts user: "Blocked suspicious program pretending to be [Email Utility]"

**Detection Flow:** GUI program detected → Hidden folder creation detected → Files analyzed → Malicious process terminated and quarantined

---

### 2. ANTI-AUTO-RUN STAGE (3 Functions)
**Goal:** Detect and remove startup entries created by suspicious programs

**Function 4: `scan_startup_folder()`**
- Continuously monitors Startup folder for new shortcuts
- Detects shortcuts pointing to hidden locations (AppData\Roaming)
- Checks if the target files are unsigned or recently created
- Returns list of suspicious startup entries

**Function 5: `scan_registry_run_keys()`**
- Scans registry Run keys (HKCU\...\Run and HKLM\...\Run)
- Identifies entries pointing to suspicious locations (AppData, Temp)
- Cross-references with quarantined files from anti-delivery stage
- Flags entries created by the malicious program

**Function 6: `remove_persistence_mechanisms()`**
- Removes suspicious startup shortcuts
- Deletes malicious registry keys
- Also removes the hidden folder and its contents
- Logs all removed items
- Alerts user: "Removed auto-start entry for suspicious program"

**Detection Flow:** New startup shortcut detected → Registry entry found → Both removed → Hidden files deleted → User alerted

---

### 3. ANTI-SPREADING STAGE (3 Functions)
**Goal:** Detect and block the malicious program from spreading to network shares

**Function 7: `monitor_network_file_copies()`**
- Monitors all file copy operations to network shares
- Detects when programs copy themselves to shares
- Flags copies with suspicious names (e.g., "PayrollReport.exe" that's actually an email utility)
- Returns list of spreading attempts

**Function 8: `scan_network_shares()`**
- Scans all accessible network shares for suspicious executables
- Checks file signatures and compares with quarantined malware
- Detects multiple copies of the same malicious program
- Identifies the malware's spreading pattern

**Function 9: `block_and_clean_network()`**
- Blocks the malicious program from copying to more shares
- Removes already-spread copies from network shares
- Alerts all users on the network
- Generates report: "Stopped spreading of [Email Utility malware] to 5 network locations"

**Detection Flow:** File copy to network detected → Shares scanned → Malicious copies found → Spreading blocked → Network cleaned → Users alerted

---

## Summary Table

| Stage | Attacker Functions | Defender Functions |
|-------|-------------------|-------------------|
| **Delivery** | 1. create_hidden_folder()<br>2. download_payload()<br>3. prepare_persistence() | 1. scan_hidden_folders()<br>2. analyze_suspicious_files()<br>3. quarantine_delivery_artifacts() |
| **Auto-Run** | 4. add_startup_shortcut()<br>5. add_registry_key()<br>6. verify_persistence() | 4. scan_startup_folder()<br>5. scan_registry_run_keys()<br>6. remove_persistence_mechanisms() |
| **Spreading** | 7. scan_network_shares()<br>8. replicate_to_shares()<br>9. log_infection_status() | 7. monitor_network_activity()<br>8. scan_shared_folders()<br>9. block_and_clean_spreading() |

**Total Functions:**
- Attacker: 9 functions (3 delivery + 3 auto-run + 3 spreading)
- Defender: 9 functions (3 anti-delivery + 3 anti-auto-run + 3 anti-spreading)
- Grand Total: 18 functions

---

## How The Attack Chain Works Together

### Complete Attack Flow (9 Functions):
1. **Delivery Stage:**
   - `create_hidden_folder()` → Creates hidden location
   - `download_payload()` → Places malicious file
   - `prepare_persistence()` → Prepares for auto-run

2. **Auto-Run Stage:**
   - `add_startup_shortcut()` → Creates startup entry
   - `add_registry_key()` → Adds registry persistence
   - `verify_persistence()` → Ensures it will run again

3. **Spreading Stage:**
   - `scan_network_shares()` → Finds targets
   - `replicate_to_shares()` → Copies to other systems
   - `log_infection_status()` → Records success

### Complete Defense Flow (9 Functions):
1. **Anti-Delivery Stage:**
   - `scan_hidden_folders()` → Finds hidden locations
   - `analyze_suspicious_files()` → Checks files
   - `quarantine_delivery_artifacts()` → Blocks threats

2. **Anti-Auto-Run Stage:**
   - `scan_startup_folder()` → Checks startup entries
   - `scan_registry_run_keys()` → Checks registry
   - `remove_persistence_mechanisms()` → Removes threats

3. **Anti-Spreading Stage:**
   - `monitor_network_activity()` → Watches network
   - `scan_shared_folders()` → Checks shares
   - `block_and_clean_spreading()` → Stops spreading

---

## Implementation Notes

1. **Safety:** All malicious code will be clearly labeled as educational demos and will include safety comments
2. **Testing:** Each function will be tested independently, then as a complete chain
3. **Documentation:** Each function will include docstrings explaining its purpose
4. **Demo:** Final demo will show attack → detection → mitigation flow

---

## Next Steps

1. Review and approve this proposal
2. Implement the 9 attacker functions
3. Implement the 9 defender functions
4. Add optional UI (Tkinter GUI or colored console)
5. Test the complete attack and defense chain
6. Create final demonstration

---

**Questions to Confirm:**
- Does this structure with 9+9 functions meet your requirements?
- Would you like to add a UI (GUI or colored console)?
- Are you ready to proceed with implementation?
