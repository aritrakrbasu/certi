import pandas as pd
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

SenderAddress ="aritrabasu71@gmail.com"
password = "aritrabasu71"

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
    msg['Subject'] = "Invitation for Apracchana 2022 presented to you by 3rd years , RCCIIT "
    msg['To'] = email

    body  = '''
<html>
<body>
<b> Dear '''+names[index]+''', <br>
<br>
Warm Greetings from the Apracchana team! </b>
<br>
<p>"The two hardest things to say in life are hello for the first time and goodbye for the last."

It's really upsetting to see you leave but we wish you lots of happiness and success as you begin new chapters in your lives. You have been a great mentor and outstanding friends to us since our freshmen years. Before wishing you Au Revoir, we invite you to join us in  ”Apracchana”, the Farewell Party ’22 on 3rd June 2022, Friday in the Institute Auditorium. </p>
<br>
<br>
<strong>
<font color="#e5012e"> 
<i>Location : College Auditorium <br>
Dress Code : Ethnic <br>
</i></font></strong> '''
    

    msg.attach(MIMEText(body, 'html'))

    folders = ["organizers"]

    for folder in folders:
        filename = "invitation.png"
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










