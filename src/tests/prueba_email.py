# import smtplib
# import ssl

# port = 465
# smtp_server = "smtp.gmail.com"
# sender_email = "brian.lobo@moorea.io"
# receiver_email = "brian.d.lobo@gmail.com"
# password = '$leafnoise%'

# message = "MUERTO...!!!!"

# with smtplib.SMTP_SSL(smtp_server, port) as server:
#     server.ehlo()
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)



import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "brian.lobo@moorea.io"
receiver_email = "brian.d.lobo@gmail.com"
password = '$leafnoise%'

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails
# msg["Cc"] = "serenity@example.com,inara@example.com" # PROBAR

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "app.py"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
