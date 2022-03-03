import pandas as pd
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

SenderAddress ="aritrabasu71@gmail.com"
password = "runabasu71"

e = pd.read_excel("emails.xlsx",engine='openpyxl')
emails = e['Emails'].values
names = e['Names'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)



index = 0


for email in emails:
    msg = MIMEMultipart()
    msg['From'] = "aritrabasu71@gmail.com"
    msg['Subject'] = "Certificate of appreciation for Innovision 2021 presented to you by CSE , RCCIIT "
    msg['To'] = email

    body  = '''
<html>
<body>
<b> Dear '''+names[index]+''', <br>
<br>
Warm Greetings from the Innovision team! </b>
<br>
<p>We are grateful for actively organizing this event and making this a great success . We have attached your appreciation certificate with this mail. <br> 
Please do provide us with your valuable feedback on your experience using the attached Google form, or you can reply to this email . </p>
<br>
<br>
<b> Feedback Link : https://forms.gle/uPX42nTdWpaEQZNK7 </b>
<br>
<br>
<br>
<strong> Regards, <br>
<font color="#e5012e"> 
<i>Team Innovision 2021 <br>
Presented by CSE , RCCIIT <br>
</i></font></strong> '''
    

    msg.attach(MIMEText(body, 'html'))

    folders = ["organizers"]

    for folder in folders:
        filename = names[index]+".png"
        filepath ="./"+folder+"/"+filename
        file = Path(filepath)
        if file.is_file():
            with open(filepath, 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data, name=filename)
            msg.attach(image)


    
    server.sendmail(SenderAddress, email, msg.as_string())
    print("email sent to "+names[index])
    index = index+1
    
server.quit()










