#!/usr/bin/env python3

import os
import smtplib
from email.message import EmailMessage

def generateEmail(yourName, recipient, subject, body):
    '''This functions creates the whole Email filling out the necessary fileds and returns the created Email.'''

    #Creating an instance of EmailMessage class.
    message = EmailMessage()

    #Setting the required Email parameters.
    message['From'] = yourName
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    return message

def sendEmail(loginEmailID, password, message):
    '''This functions sends the Email through Gmail server by logging in the Gmail account of the user.'''

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()

        #Logging In the user Gmail account.
        server.login(loginEmailID, password)

        #Sending the Email from the user Gmail account.
        server.send_message(message)
        server.quit()
