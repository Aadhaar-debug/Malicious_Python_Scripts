import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

# Set up email parameters
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@gmail.com"

# Set up the message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Email with attachment"

# Add the file or image attachment
filename = "file.txt" # replace with your file name
with open(filename, 'rb') as attachment:
    # If the attachment is an image, use MIMEImage
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image = MIMEImage(attachment.read())
        msg.attach(image)
    # Otherwise, use MIMEBase
    else:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename={filename}')
        msg.attach(part)

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
