#!/usr/bin/env python3

import xlrd
import csv
import os

def csv_from_excel(fileName, sheetName):
    '''This function opens the spreadsheet with .xlsx or .xlx format and convert it to .csv format'''

    #Opening spreadhseey having extension .xlsx or .xlx fromat
    wb = xlrd.open_workbook(fileName)

    #Opening Sheet of the spreadsheet
    sh = wb.sheet_by_name(sheetName)

    #Extracting filename without extension
    newFileName, _ = os.path.splitext(fileName)

    #Creating new file with same fileName but with .csv extension
    with open(newFileName+'.csv', 'w') as your_csv_file:
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))
        your_csv_file.close()
    return newFileName+'temp.csv'
