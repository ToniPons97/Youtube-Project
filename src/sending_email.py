import os
from dotenv import load_dotenv
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

load_dotenv()

fromaddr = os.getenv("SENDER")
toaddr = os.getenv("RECEIVER")
password = os.getenv("PASSWORD")
def send_email_with_file():
    msg = MIMEMultipart()     
    msg['From'] = fromaddr 
    msg['To'] = toaddr     
    msg['Subject'] = "CSV GENERATED WITH YOUTUBE DATA EXTRACTOR!!!"    
    body = "Python is AWSOME"
    
    msg.attach(MIMEText(body, 'plain')) 
    
    filename = "youtube.csv"
    attachment = open("../output/youtube.csv", "rb") 
    
    p = MIMEBase('application', 'octet-stream')     
    
    p.set_payload((attachment).read()) 

    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    msg.attach(p) 
    
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    s.starttls() 
    
    s.login(fromaddr, password) 

    text = msg.as_string() 
    
    s.sendmail(fromaddr, toaddr, text) 
    
    s.quit()

