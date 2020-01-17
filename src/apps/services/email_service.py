import smtplib
import ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "brian.lobo@moorea.io"
receiver_email = "brian.d.lobo@gmail.com"
password = '$leafnoise%'

message = "MUERTO...!!!!"

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
