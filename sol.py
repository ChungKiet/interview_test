import csv
import json
import pandas as pd
from constants import *

# Get arr of add and value
# One arr for key and one arr for value

CSV_PATH='data.csv'

def sol(path):
   # TODO
   # read the template replace
   emailJSONFile = open(TEMPLATE_REPLACE_PATH)
   templateEmail = json.load(emailJSONFile)
   arrOfAddValue = templateEmail[ADD]
   arrOfReplaceValue= templateEmail[REPLACE]
   arrOfSpecificReplaceValue = templateEmail[SPECIFIC_REPLACE]

   arrOfAddProperties = []
   arrOfAddCol = []
   for keyValueObject in arrOfAddValue:
      for k in keyValueObject.keys():
         arrOfAddProperties.append(k)
         arrOfAddCol.append(keyValueObject[k])

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

   # specific replace no col
   arrOfSpecReplaceProperties = []
   arrOfSpecReplaceCol = []
   arrOfSpecReplaceInStr = []
   for keyValueObject in arrOfSpecificReplaceValue:
      arrOfSpecReplaceProperties.append(keyValueObject[PROPERTY])
      arrOfSpecReplaceCol.append(keyValueObject[VALUE])
      arrOfSpecReplaceInStr.append(keyValueObject[PREFIX] + keyValueObject[VALUE] + keyValueObject[POSTFIX])

   # read the CSV and get the column name then replace follow above template
   fileResult =  open(FILE_RESULT_PATH, 'w', encoding='UTF8', newline='')
   fileError = open(FILE_ERROR_PATH, 'w', encoding='UTF8', newline='')

   # test by read and print csv file
   df = pd.read_csv('data.csv')

   header = [h for h in df]
   numOfRecord = len(df[TITLE])

   templateJSONFile = open(TEMPLATE_JSON_PATH)
   templateObjectEmail = json.load(templateJSONFile)
   templateRow=[""]*NUM_OF_COL # use for errors file
   dataErrors = []

   for i in range(numOfRecord):
      email = df[header[EMAIL]][i]
      if len(email) > 0 and EMAIL_POST_FIX in email:
         for j in range(len(arrOfAddProperties)):
            templateObjectEmail[arrOfAddProperties[j]] = df[arrOfAddValue[j]][i]

         for j in range(len(arrOfReplaceProperties)):
            for k in range(len(arrOfReplaceInStr[j])):
               replaceInStr = arrOfReplaceInStr[j][k]
               colName = arrOfReplaceCol[j][k]
               valueReplace = df[colName][i]
               templateObjectEmail[arrOfReplaceProperties[j]] = \
                  templateObjectEmail[arrOfReplaceProperties[j]].replace(replaceInStr, valueReplace)

         for j in range(len(arrOfSpecReplaceProperties)):
            valueReplace = "31 Dec 2000"
            replaceInStr = arrOfSpecReplaceInStr[j]
            templateObjectEmail[arrOfSpecReplaceProperties[j]] = \
               templateObjectEmail[arrOfSpecReplaceProperties[j]].replace(replaceInStr, valueReplace)
         #change template and add into JSON
      else:
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
         # write into error file
   # call for 
   # then for add
   # for replace
   # for spec replace
   # insert into object

   # write result
   # add into error and continue if there are no email

   # read all rows 
   # replace each row with the JSON template then insert into array objects

   # add the data into template json by create a array of objects

   # write the array of objects into the JSON

   return

sol(CSV_PATH)

# NOTE:
"""
   Think about the case REST API and embedding the EMAIL service
   Create a constants file
"""

# import calendar

# for month_idx in range(1, 13):
#     print (calendar.month_name[month_idx])
#     print (calendar.month_abbr[month_idx])
#     print ("")