# Automating Sending Emails from Spreadsheets
This project helps you to automate the whole process of sending E-mails recorded in Spreadsheets in just one go.

# Requirements
- You can either manually install all the dependencies listed in the `extensions.txt` file  or  Run the given command to install all the packages at once
```
pip install extensions.txt
```
Adapt the command according to your operating system

- Make sure that your Spreadsheet is in the same folder ,that is, `send-emails-from-spreadsheet`

- If you are going to use Gmail as your E-mail service then turn on your account's [Less Secure App Access](https://myaccount.google.com/lesssecureapps)

# Usage

Open the `userApp.py` and fill the following details.

```py
# The name of your Spreadsheet with extension.
spreadsheet = "exampleSpreadsheet.xlsx"

# The sheet name in which all the E-mails are listed.
nameOfSheet = "Sheet 1"

# Enter your own name which will reflect in the E-mail.
your_Name = "Tabish Naved"

# Your E-mail ID from which E-mails will be sent.
your_LogIn_EmailID = "myemail@example.com"

# Your password.
your_EmailID_Password = "helloworld"

# Compose your E-mail by giving a subject line and the main-content/body of the E-mail.
subject_line_of_email = "Test Email"
body_content_of_email = "Success. This works!"
```
The above mentioned details is just an illustration of how a user will enter the details.
