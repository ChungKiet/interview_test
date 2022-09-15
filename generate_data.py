import csv
import random
import string
from constants import *

class generateData():
   def __init__(self, path, numOfRecords):
      self.filePath = path
      self.numOfRecords = numOfRecords

   def randStr(self, chars = string.ascii_uppercase + string.digits, N=10):
      return ''.join(random.choice(chars) for _ in range(N))

   def run(self):
      # gen a file with 4 column without constant
      data = []
      templateRow=[""]*NUM_OF_COL

      # writerFile = csv.writer(dataFile)

      # writerFile.writerow(HEADER)

      for i in range(self.numOfRecords):
      # create a row with random string then create a row by template
         TTLen = random.randint(TITLE_LENGTH_MIN, TITLE_LENGTH_MAX)
         templateRow[TITLE] = self.randStr(chars=string.ascii_lowercase, N=TTLen)

         FNLen = random.randint(FIRST_NAME_MIN, FIRST_NAME_MAX)
         templateRow[FIRST_NAME]= self.randStr(chars=string.ascii_uppercase, N=FNLen)

         LNLen = random.randint(LAST_NAME_MIN, LAST_NAME_MAX)
         templateRow[LAST_NAME]= self.randStr(chars=string.ascii_uppercase, N=LNLen)

         EMLen = random.randint(EMAIL_ADDRESS_MIN, EMAIL_ADDRESS_MAX)
         templateRow[EMAIL]= self.randStr(chars=string.ascii_uppercase + string.ascii_lowercase + string.digits, N=EMLen) \
                           + EMAIL_POST_FIX

         data.append(templateRow)
         templateRow=[""]*NUM_OF_COL

      with open(self.filePath, 'w', encoding='UTF8', newline='') as f:
         writer = csv.writer(f)

         # write the header
         writer.writerow(HEADER)

         # write multiple rows
         writer.writerows(data)

      return   

generateDataObject = generateData(DATA_FILE_PATH, NUM_OF_PEOPLE) # data.csv, 10
generateDataObject.run()