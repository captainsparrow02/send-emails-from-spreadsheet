#!/usr/bin/env python3

import os
import emailingList
import emails

spreadsheet = '' #Enter the filename of your spreadsheet.

nameOfSheet = '' #Enter the Sheet name in which Emails are listed in your Spreadsheet.

#Enter your credentials below.
your_Name = '' #Sender's name that will appear in the Email.
your_LogIn_EmailID = '' #Your Gmail Email ID.
your_EmailID_Password = '' #Your Gmail Email ID's password.

#Create your Email below.
subject_line_of_email = '' #Subject of your Email.
body_content_of_email = '' #Main body/text-area of your Email.

list_of_recipients_from_spreadsheet = emailingList.generateEmailList(spreadsheet, nameOfSheet)

#Sending Email
for recipient in list_of_recipients_from_spreadsheet:
    message = emails.generateEmail(your_Name, recipient, subject_line_of_email, body_content_of_email)
    emails.sendEmail(your_LogIn_EmailID, your_EmailID_Password, message)
