import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import requests
import ast
import smtplib
import json

url = "http://apps.cptm.sp.gov.br:8080/AppMobileService/api/LinhasMetropolitanas"

resp = requests.get(url=url)
data = json.loads(resp.text)
string_body = ''

for d in data:

 string_body += "Linha: " + str(d['LinhaId']) +" " + d['Nome']+  " - " + d['Status'] + " (" +d['Descricao'] + ") " + "; \n "
  
email_user = 'spviva8@gmail.com'
email_password = 'iWeekedBR'
email_send = open(r'C:\Users\PC-Casa\Desktop\Python Email\data\recipients.txt').read()

subject = 'Situacao do Metro SP'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = string_body
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)

server.quit()