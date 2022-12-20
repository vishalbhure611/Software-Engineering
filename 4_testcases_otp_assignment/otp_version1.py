import random  #random mmdule to get random integers to create OTp
import Senders_data1 #email and password of sender from another file
import smtplib  #simple message transfer protocol#library to send email to users email_address

n=(int(input("Enter your range of otp ")))  #getting the input for length of otp

#function to generate otp 
def generate_otp(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9))
    return (OTP)

#create gmails server
server =smtplib.SMTP('smtp.gmail.com',587)

#get senders email from another file
Senders_email = Senders_data1.email
Senders_password= Senders_data1.password

def login_into_sendersemail():
    server.starttls()   #transfered layer security
    server.login(Senders_email,password=Senders_password)  #Login into sender mail


#function to send email
def send_email(receivers_name,receivers_email): 

    login_into_sendersemail()
    #generate_otp function called
    otp_var=generate_otp(n)
    msg=("Hi "+ receivers_name +"\n"+ str(otp_var)+" is your OTP ")
    print(msg)
    server.sendmail(Senders_email,receivers_email,msg)
    server.quit() #to quit the server
    print("email has been sent!")

#send emailfunction called
send_email("receivers_name","receivers_email@gmail.com")
