#import statements
import smtplib
from socket import gaierror
import csv
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

#globally scoped server
server = smtplib.SMTP('smtp.gmail.com', 587)
sender_email = input("Please enter your email address with no spaces and the '@gmail.com' \n(E.g. ->janedoe@gmail.com)\n")

#ask for password once
def signin():
    password = input("please enter your password")
    server.starttls()
    server.login(sender_email, password)
    print("login success")
    loader()

#loader that loads values into a dictionary
def loader():
    file = input("enter the name of your CSV file")
    with open(file) as f:
        full_list = dict(filter(None, csv.reader(f)))
        subject = input("What would you like the subject of the email to be? \n(Note: This will be sent to everyone)")
    for email in full_list:
        rec_email = email
        person = full_list[email]
        message_creator(person, rec_email)

#creates the personalized message
def message_creator(person, rec_email, subject):
    # message = EmailMessage()
    # message['Subject'] = 'Python Emailer Client'
    # message['From'] = sender_email
    # message['To'] = rec_email
    # message.set_content('Welcome to Python Emailer client, Dear {}, \nWe appreciate your time and effort in considering us.'.format(person))

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = rec_email

    #HTML signature (personalized)

    html = """\
    
    """.format(person)

    # Record the MIME types of both parts - text/plain and text/html.

    htmlFull = MIMEText(html, 'html')
    msg.attach(htmlFull)


    email_login(rec_email, msg)


#email login and sending method
def email_login(rec_email, message):
    # server.sendmail(sender_email, rec_email, message)
    server.send_message(message)
    print("sent")


signin()
