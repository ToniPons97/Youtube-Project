import os
from dotenv import load_dotenv
import ssl, smtplib
import getpass

load_dotenv()

sender_email = os.getenv("SENDER")
receiver_email = os.getenv("RECEIVER")
message = "Python is fucking awsome22222222222222!!!!!!!!!!!!!!!!!!!"
port = 465  
password = getpass.getpass("Password: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

