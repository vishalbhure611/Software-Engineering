import random #random module to get random integers to create OTP
import senders_data #email and password of sender from another file
import smtplib #simple message transfer protocol#library to send email to users email address

n=6
def generate_otp(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9)) 
    return (OTP)

server =smtplib.SMTP('smtp.gmail.com',587)

Senders_email = senders_data.email
Senders_password= senders_data.password

def login_into_sendersemail():
    server.starttls()
    server.login(Senders_email, password=Senders_password) 
receivers_name=input("Enter receivers name ")
receivers_email=input("Enter receivers email ")

def send_email():
    login_into_sendersemail()
    otp_var=generate_otp👎
    msg=("Hi "+ receivers_name +"\n"+ str(otp_var)+" is your OTP ")
    print (msg)
    server.sendmail (Senders_email, receivers_email,msg)
    server.quit() 
    print("email has been sent!")
send_email()
