import csv
import json
import pandas as pd
import calendar
from constants import *
import datetime

def sol(path):
   # read the template replace
   emailJSONFile = open(TEMPLATE_REPLACE_PATH)
   templateEmail = json.load(emailJSONFile)
   arrOfAddValue = templateEmail[ADD]
   arrOfReplaceValue= templateEmail[REPLACE]
   arrOfSpecificReplaceValue = templateEmail[SPECIFIC_REPLACE]

   # Create the array of properties which will be add into the JSON (Exp: 'to')
   arrOfAddProperties = []
   arrOfAddCol = []
   for keyValueObject in arrOfAddValue:
      for k in keyValueObject.keys():
         arrOfAddProperties.append(k)
         arrOfAddCol.append(keyValueObject[k])

   # Create the array of properties which will be replace by field in CSV file
   arrOfReplaceProperties = []
   arrOfReplaceInStr = []
   arrOfReplaceCol = []
   for keyValueObject in arrOfReplaceValue:
      arrOfReplaceProperties.append(keyValueObject[PROPERTY])
      replaceCol = keyValueObject[COL]
      replaceValue = []
      arrOfReplaceCol.append(replaceCol)
      for col in replaceCol:
         replaceValue.append(keyValueObject[PREFIX] + col + keyValueObject[POSTFIX])
      arrOfReplaceInStr.append(replaceValue)

   # Create the array of properties which will be replace by the specific way
   arrOfSpecReplaceProperties = []
   arrOfSpecReplaceCol = []
   arrOfSpecReplaceInStr = []
   for keyValueObject in arrOfSpecificReplaceValue:
      arrOfSpecReplaceProperties.append(keyValueObject[PROPERTY])
      arrOfSpecReplaceCol.append(keyValueObject[VALUE])
      arrOfSpecReplaceInStr.append(keyValueObject[PREFIX] + keyValueObject[VALUE] + keyValueObject[POSTFIX])

   # Read data from CSV file
   df = pd.read_csv('data.csv')

   header = [h for h in df]
   numOfRecord = len(df[header[TITLE]])

   templateJSONFile = open(TEMPLATE_JSON_PATH)
   templateObjectEmail = json.load(templateJSONFile)
   templateRow=[""]*NUM_OF_COL # use for errors file
   dataErrors = []

   # Get today and transfer to string
   today = datetime.datetime.now()
   DAY = str(today.day)
   MONTH = calendar.month_abbr[today.month]
   YEAR = str(today.year)
   todayStr = DAY + ' ' + MONTH + ' ' + YEAR 
   
   # For each record check the email then replace or add with the above arrays
   for i in range(numOfRecord):
      email = df[header[EMAIL]][i]
      if len(email) > 0 and EMAIL_POST_FIX in email:
         for j in range(len(arrOfAddProperties)):
            templateObjectEmail.update({arrOfAddProperties[j]: df[arrOfAddCol[j]][i]})

         for j in range(len(arrOfReplaceProperties)):
            for k in range(len(arrOfReplaceInStr[j])):
               replaceInStr = arrOfReplaceInStr[j][k]
               colName = arrOfReplaceCol[j][k]
               valueReplace = df[colName][i]
               templateObjectEmail[arrOfReplaceProperties[j]] = \
                  templateObjectEmail[arrOfReplaceProperties[j]].replace(replaceInStr, valueReplace)

         for j in range(len(arrOfSpecReplaceProperties)):
            replaceInStr = arrOfSpecReplaceInStr[j]
            templateObjectEmail[arrOfSpecReplaceProperties[j]] = \
               templateObjectEmail[arrOfSpecReplaceProperties[j]].replace(replaceInStr, todayStr)
         
         with open(JSON_FOLDER_PATH + '\\' + df[header[EMAIL]][i] + '.json', 'w', encoding='UTF8', newline='') as result:
            result.write(json.dumps(templateObjectEmail))

      else:
         # Append the records which miss the email field
         templateRow[TITLE] = df[header[TITLE]][i]
         templateRow[FIRST_NAME] = df[header[FIRST_NAME]][i]
         templateRow[LAST_NAME] = df[header[LAST_NAME]][i]
         templateRow[EMAIL] = df[header[EMAIL]][i]
         dataErrors.append(templateRow)
         templateRow=[""]*NUM_OF_COL

   with open(FILE_ERROR_PATH, 'w', encoding='UTF8', newline='') as errorFile:
      writer = csv.writer(errorFile)

      # write the header
      writer.writerow(HEADER)

      # write multiple rows
      writer.writerows(dataErrors)

sol(CSV_PATH)

# NOTE:
"""
   Think about the case REST API and embedding the EMAIL service
   Create a constants file
"""