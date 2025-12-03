"""
Auto-Run Function 4: Send Fake Email
Sends email to appear legitimate while triggering persistence
"""

import time
from email.mime.text import MIMEText

def send_fake_email(user_email):
    """
    Send actual email to make program look legitimate
    Args:
        user_email: Email address entered by user
    Returns: True if successful, False otherwise
    """
    print(f"[Malicious] Function 4: Sending email to {user_email}...")
    
    try:
        # Create simple email message
        msg = MIMEText("This is a test email from Email Sender Utility.")
        msg['Subject'] = "Test Email"
        msg['From'] = "emailsender@utility.com"
        msg['To'] = user_email
        
        # NOTE: In a real demo, you would configure an SMTP server
        # For now, we just simulate success
        print(f"[Malicious] Email 'sent' to {user_email} (simulated)")
        
        return True
    except Exception as e:
        print(f"[Malicious] Email sending failed: {e}")
        return False
