================================================================================
DELIVERY TECHNIQUE 1: MALICIOUS WEBSITE - COMPLETE GUIDE
================================================================================

WHAT IS THIS TECHNIQUE?
========================

In this technique, the victim visits a website that has been created or modified 
by the attacker. The webpage automatically triggers a hidden download in the 
background. If the victim opens the downloaded file, the spyware installs.

This method works because the download looks like a normal file (WindowsUpdate.exe), 
and the victim does not realize it contains harmful content.


HOW TO USE:
===========

STEP 1: START WEB SERVER
-------------------------

cd C:\Users\TUF\Documents\Cyber\cybersecurity_final_project-master\malicious_code\delivery\delivery_technique1
py -m http.server 8000

(Keep this running)


STEP 2: START ATTACKER SERVER
------------------------------

cd C:\Users\TUF\Documents\Cyber\cybersecurity_final_project-master\malicious_code
py attacker_server.py

(Keep this running)


STEP 3: SHARE MALICIOUS WEBSITE LINK
-------------------------------------

Get your IP address:
ipconfig

Your malicious website link:
http://192.168.5.128:8000/malicious-website.html

Send this link to victim via:
• WhatsApp/Telegram message
• Social media DM
• Email
• SMS text
• Or just tell them the URL


STEP 4: VICTIM VISITS WEBSITE
------------------------------

When victim clicks the link:
1. Website opens (looks like official Microsoft page)
2. Shows "Preparing security update..." with loading spinner
3. After 2 seconds → AUTOMATIC DOWNLOAD starts!
4. WindowsUpdate.exe downloads to victim's Downloads folder
5. Victim sees "Download Started!" message


STEP 5: VICTIM OPENS FILE
--------------------------

Victim checks Downloads folder:
1. Sees WindowsUpdate.exe file
2. Double-clicks to open it
3. Spyware GUI appears (fake security scanner)
4. Spyware installs and runs all 9 functions
5. INFECTED! ✅


STEP 6: ATTACKER RECEIVES DATA
-------------------------------

Watch your attacker_server.py terminal:
• Victim data appears
• System information collected
• Files scanned
• Data exfiltrated
• SUCCESS! ✅


ATTACK SCENARIOS:
=================

Scenario 1: Social Media Message
---------------------------------
Attacker: "Hey! Check out this important Windows update:
          http://192.168.5.128:8000/malicious-website.html"

Victim: *clicks link*
Victim: *website opens, looks official*
Victim: *download starts automatically*
Victim: "Oh, Windows update downloaded. Let me install it..."
Victim: *runs file* → INFECTED!


Scenario 2: WhatsApp/Telegram
------------------------------
Message: "🔴 URGENT: Critical Windows security patch released!
         
         Download here: http://192.168.5.128:8000/malicious-website.html
         
         Your system is vulnerable until updated!"

Victim: *clicks link out of urgency*
Victim: *automatic download* → INFECTED!


Scenario 3: QR Code on Poster
------------------------------
Poster: "Free System Security Scan - Scan QR Code"

Victim: *scans QR with phone*
Victim: *opens link on computer*
Victim: *automatic download* → INFECTED!


WHY THIS TECHNIQUE IS EFFECTIVE:
=================================

✅ No email account needed (no trace)
✅ Automatic download (victim doesn't explicitly click)
✅ Looks like legitimate Microsoft update
✅ File name "WindowsUpdate.exe" seems safe
✅ Professional website design builds trust
✅ Loading spinner creates sense of legitimacy
✅ Clear instructions guide victim to run file


DEMO FOR PRESENTATION:
======================

Setup:
------
• Start web server (port 8000)
• Start attacker server (port 5000)
• Prepare victim computer

Show:
-----
1. "Attacker creates malicious Microsoft website"
   → Show malicious-website.html code

2. "Attacker shares link with victim"
   → Show link: http://192.168.5.128:8000/malicious-website.html

3. "Victim visits the website"
   → Open link in browser
   → Show professional Microsoft page

4. "Website automatically downloads spyware"
   → Show loading spinner
   → Show "Download Started!" message
   → Show WindowsUpdate.exe in Downloads folder

5. "Victim runs the downloaded file"
   → Double-click WindowsUpdate.exe
   → Show spyware GUI appearing

6. "Victim gets infected!"
   → Show fake security scan running
   → Show attacker server receiving data

7. "Attacker successfully stole victim data"
   → Show received_victim_data folder
   → Show victim information collected


TALKING POINTS:
===============

"This demonstrates drive-by download attack:
• Victim only needs to visit a website
• Download happens automatically in background
• File appears legitimate (WindowsUpdate.exe)
• Victim voluntarily runs the file
• No suspicious emails or obvious red flags
• Very difficult to detect until too late

This is why:
• Web filtering is important
• Download scanning is critical
• User awareness training is essential
• Only download from official sources"


IMPORTANT REMINDERS:
====================

⚠️ EDUCATIONAL USE ONLY
⚠️ Test only on systems you own
⚠️ Do NOT attack real victims
⚠️ Unauthorized access is ILLEGAL

================================================================================
