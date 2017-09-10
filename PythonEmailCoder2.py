import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

print("Enter a phrase that requires encryption, an email will be sent to your email address")


input= input('Enter All Your Private Info:')
input= input.lower()
encrypt = []
for letter in input:
    number = ord(letter)
    #you can add or minus from the above line to change the encryption numbers ex. number = ord(letter) -5 would make a = 92 instead of 97
    encrypt.append(number)
    with open('file.txt', 'w') as f:
        print(encrypt, file=f)
#We are opening a new text document named file, printing encrypt into it and assigning it to 'f'

#enter the email address it is going from and the email address it is going to.
fromaddr = "pythonmeir@gmail.com"
toaddr = "elizahab@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
#Type the subject
msg['Subject'] = "Python Email Encoder"
#Type the body message
body = ("Dear Mr ELi Belli, Above is your encoded Message from Meir Lebowitz, to DECRYPT this message, use this Conversion Key or download python and il give u a code that you can just copy and paste it into: \n a = 97 \n b = 98 \n etc\ space = 32")
        #\n A=1 \n , B=2 \n C=3  \n D=4 \n E=5 \nF =6\n G=7\n H=8\n I =9\n J = 10\n K = 11\n L = 12\n M = 13\n N = 14\n O = 15 \n P = 16\n Q = 17\n R = 18\nS = 19 \n T = 20\nU = 21\n V = 22\n W = 23\n X = 24\n Y = 25\n Z = 26 \n space = -64")
fp = open('file.txt', 'r')
msg.attach(MIMEText(fp.read()))
#In the above line i am attaching the file named file.txt that we have our encryption in to the email
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

#Enter your login information
server.login("pythonmeir@gmail.com", "pythonjava")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
