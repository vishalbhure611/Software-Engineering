from datetime import date
import mysql.connector
from email.message import EmailMessage, SEmailMessage 
import smtplib
import medium as M

today = date.today()
db=mysql.connector.connect(host="localhost",user="root",passwd="xxxxxxxxxxxxxxx",database="test")
cursor=db.cursor()

Holiday,Date = [],[]
Email_ID,Month,Name,Number = [],[],[],[]

def showData():
    cursor.execute('SELECT * FROM Data')
    data = cursor.fetchall()
    for d in data:
        print(d)

def getData():
    cursor.execute('SELECT * FROM Data')
    data = cursor.fetchall()
    for d in data:
        Email_ID += [d[1]]
        Month+=[(str(d[3])).split('-')]
        Name += [d[0]]
        Number += [d[2]]
    
def checkBirthday():
    getData()
    for i in range(len(Month)):
        for j in range(len(Month[i])):
            if Month[i][j]==str(today.month) and Month[i][j-1]==str(today.day):
                print("Name of person's who have birthday today")
                print(Name[i])
                M.sendMail(Name[i],Email_ID[i]) 
                M.sendWhatsApp(Name[i][j],Number[i]) 
checkBirthday()

msg = EmailMessage()
Sender_Mail = "xxxxxxxxxxxxxxxx@gmail.com" 
password = "xxxx xxxx xxxx xxxx" 

def sendMail(Name,Reciver_Mail):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.starttls()
    server.login(Sender_Mail,password) 
    msg['Subject'] = 'Testing of HAPPY BIRTHDAY Service!' 
    msg['From'] = Sender_Mail
    msg['To'] = Reciver_Mail
    msg.set_content(f'Happiest Birthday {Name}! have a great day.')
    server.send_message(msg)
    server.quit()

def sendWhatsApp(Name,Number):
    body = f'Many Many Returns of the Day {Name}!\nI hope all your birthday wishes and dreams come true.'
