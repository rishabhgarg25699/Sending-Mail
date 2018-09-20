import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("\n"*10000)

print("----- Welcome To CUI Mail -----")
print("\n"*3)
print(" If You are using Gmail please allow acess to \n less secure apps.")
print(' Thank You')

print("\n Press Any Key ")
input()

# Getting Username
print("{a:25}:- ".format(a = " Enter Your User Name "),end="")
username = input()

# Detrmining Host service
mail_detecter = username.partition("@")
host = "smtp." + mail_detecter[2]

# Connecting to Host Service
try:
    server = smtplib.SMTP(host, 587)
    server.starttls()
except:
    print(" Connection Error !!! ")
    print(" Check Your Connection !!! ")
    exit(0)

print("\n Connection To Host Succesfull !!! \n\n")

# Getting Password After Sucessfull Connection With Host
#print(" {a:20}:- ".format(a = "Enter Your PassWord"),end='')
password = getpass.getpass()

# Login Phase
try:
    server.login(username,password) # login(username,password)
except:
    print(" Authentication Error !!!")
    print(" Make Sure you Have Enabled Acesse to Less Secure App ")
    exit(1)

# Getting Reciver's e-mail addresse
print("\n\n Enter Reciver's E-mail Addresse :- ",end='')
reciever = input()

print("\n\n")

# Message Part
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = reciever

print(" {s:20} :- ".format(s=" Enter Subject"),end='')
subject = input()
msg['Subject'] = subject

print(" {m:20} :- ".format(m=" Enter Your Message"),end='')
message = input()

msg.attach(MIMEText(message,'plain'))

text = msg.as_string()

print("""

Your Final mail Look Like This
-------------------------------------------------
To      :- {r}
From    :- {f}
Subject :- {s}

Body    :- {b}
-------------------------------------------------
""".format(r=reciever,f=username,s=subject,b=message))
while True:
    choice = input(" Press Y to Send or N to Discard ")
    if choice == 'Y':
        try:
            server.sendmail(username, reciever, text)  # sendmail(from,to,message)
        except:
            print(" Error Unable To Send Mail Sorry !!! ")
            exit(3)
        print(" Mail Sent ....")
        server.quit()
        exit(4)
    elif choice == 'N':
        print(" Message Discarded !!!")
        break;
    else:
        print(" Wrong choice !!!")
#
# try:
#   server.sendmail(username,reciever,text) # sendmail(from,to,message)
# except:
#   print(" Error Unable To Send Mail Sorry !!! ")
#   exit(3)
# print(" Mail Sent ....")
# server.quit()
