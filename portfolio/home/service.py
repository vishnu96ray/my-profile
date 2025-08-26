import smtplib
from email.mime.text import MIMEText
from django.conf import settings


def send_email(to, subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = to

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.send_message(msg)

        print("✅ Email sent successfully!")
        return True

    except Exception as e:
        print("❌ Error sending email:", e)
        return False

# Example usage
# send_email("receiver@example.com", "Test Email", "Hello, this is a test email!")

