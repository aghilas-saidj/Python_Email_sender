import smtplib , ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time 
import os


My_Email_Address = raw_input('Enter Your Email_Address : ')
Password = raw_input('Enter Your Password : ')
time.sleep(2)
os.system('clear')

print('Hello_Your Email_Address_Is : {} '.format(My_Email_Address))
print('\n')
print('Enter_The_Email_Address_Destination ! : ')
print('\n')
Email_Address_Destination =  raw_input()
print('\n')
print('Subject :')
print('\n') 
Subject = raw_input()
print('\n')
print('Your_Message : ')
print('\n')
Message = raw_input()

server = smtplib.SMTP_SSL('smtp.gmail.com','465')
server.ehlo()
server.login(My_Email_Address , Password)

msg = MIMEMultipart()
msg['From'] = My_Email_Address
msg['To'] = Email_Address_Destination
msg['Subject'] = Subject

msg.attach(MIMEText(Message , 'plain'))


Message = msg.as_string()

server.sendmail(My_Email_Address , Email_Address_Destination , Message)
server.close()
print('Mail Sent')


