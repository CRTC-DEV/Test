import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email settings
smtp_server = smtp.gmail.com
smtp_port = 587
sender_email = os.getenv('MAIL_USER')
receiver_email = os.getenv('RECEIVER_EMAIL')
email_password = os.getenv('MAIL_PASSWORD')

# Email subject and body
subject = "GitHub Issues Export"
body = "Attached is the latest GitHub issues export."

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

# Attach CSV file
filename = '.github/issues.csv'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {filename}")

msg.attach(part)

# Send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, email_password)
server.sendmail(sender_email, receiver_email, msg.as_string())
server.quit()

print(f"Email sent to {receiver_email}")
