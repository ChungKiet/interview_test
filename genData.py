import csv
import random
import string

# Constant definition
DATA_FILE_PATH = 'data.csv'
TITLE=0
FIRST_NAME=1
LAST_NAME=2
EMAIL=3
NUM_OF_COL=4
TITLE_LENGTH_MIN=5
TITLE_LENGTH_MAX=10
FIRST_NAME_MIN=5
FIRST_NAME_MAX=10
LAST_NAME_MIN=5
LAST_NAME_MAX=10
EMAIL_ADDRESS_MIN=6
EMAIL_ADDRESS_MAX=10
EMAIL_POST_FIX='@example.com'
HEADER = ['TITLE', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

def genCSV(n: int):
   # gen a file with 4 column without constant
   data = []
   templateRow=[""]*NUM_OF_COL

   # writerFile = csv.writer(dataFile)

   # writerFile.writerow(HEADER)

   for i in range(n):
   # create a row with random string then create a row by template
      TTLen = random.randint(TITLE_LENGTH_MIN, TITLE_LENGTH_MAX)
      templateRow[TITLE] = randStr(chars=string.ascii_lowercase, N=TTLen)

      FNLen = random.randint(FIRST_NAME_MIN, FIRST_NAME_MAX)
      templateRow[FIRST_NAME]=randStr(chars=string.ascii_uppercase, N=FNLen)

      LNLen = random.randint(LAST_NAME_MIN, LAST_NAME_MAX)
      templateRow[LAST_NAME]=randStr(chars=string.ascii_uppercase, N=LNLen)

      EMLen = random.randint(EMAIL_ADDRESS_MIN, EMAIL_ADDRESS_MAX)
      templateRow[EMAIL]=randStr(chars=string.ascii_uppercase + string.ascii_lowercase + string.digits, N=EMLen) \
                        + EMAIL_POST_FIX

      data.append(templateRow)
      templateRow=[""]*NUM_OF_COL

   with open(DATA_FILE_PATH, 'w', encoding='UTF8', newline='') as f:
      writer = csv.writer(f)

      # write the header
      writer.writerow(HEADER)

      # write multiple rows
      writer.writerows(data)

   return   

NUM_OF_RECORDS=10
genCSV(n=NUM_OF_RECORDS)