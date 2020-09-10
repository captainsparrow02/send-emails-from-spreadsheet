#!/usr/bin/env python3

import convertToCsv
import csv
import os
import re
import shutil

def extensionCheck(file):
    '''This function checks whether the file has .xlsx or .xlx extension and return boolean value.'''

    #Splitting basename and extension
    _, e = os.path.splitext(file)

    if e == '.xlsx' or e == '.xlx':
        return True
    return False

def findEmailField(headers):
    '''This function identifies the E-mail field in the Sheet of the spreadhseet and returns the E-mail field name.'''
    field = ''

    #Extracting each field name and checking for Email field using 'Regular Expressions'
    for header in headers:
        if re.search(r'email', header, re.IGNORECASE) or re.search(r'e-mail', header, re.IGNORECASE) or re.search(r'e mail', header, re.IGNORECASE):
            field = header
            break
    return field

def generateEmailList(fileName, sheetName):
    '''This function generates the list of Emails from the Email filed in the Sheet of spreadhseet.'''

    #Checking for .xlsx or .xlx extension
    if extensionCheck(fileName):
        fileName = convertToCsv.csv_from_excel(fileName, sheetName)
    else:
        #Creating a temporary file.
        original = r''+fileName
        target = r''+'temp'+fileName
        fileName = shutil.copy(original, target)

    emailList = []

    #Opening converted-csv-file/temporary-csv-file and reading Emails from Email field.
    with open(fileName, 'r') as f:
        reader = list(csv.DictReader(f))
        emailField = findEmailField(reader[0])
        for line in reader:
            emailList.append(line[emailField])

    #Deleting temporary-csv-file
    os.remove(fileName)
    emailList.sort()

    return emailList
