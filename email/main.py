import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Retrieve email configuration from environment variables
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_username = os.environ.get('SMTP_USERNAME')
smtp_password = os.environ.get('SMTP_PASSWORD')

# Sender and recipient email addresses
sender_email = os.environ.get('SENDER_EMAIL')
recipient_email = os.environ.get('RECIPIENT_EMAIL')

# Create a message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Test Email'

# Email body
body = 'This is a test email sent from Python using Outlook.com SMTP.'
msg.attach(MIMEText(body, 'plain'))

# Initialize the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Use TLS for encryption
server.login(smtp_username, smtp_password)

# Send the email
server.sendmail(sender_email, recipient_email, msg.as_string())

# Quit the SMTP server
server.quit()

print("Email sent successfully!")