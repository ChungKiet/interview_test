import sys
from sol import sol
from pathlib import Path
import os

def checkFormat(templateJson, customerFile, outputEmailFolder, errorFile):
   if (not Path(templateJson).exists() or not Path(customerFile).exists() or not Path(errorFile).exists()):
      return False
   
   if (not os.path.isdir(outputEmailFolder)):
      return False

   return True

def main():
   listArgs = sys.argv
   assert len(listArgs) == 5
   templateJson = listArgs[1]
   customerFile = listArgs[2]
   outputEmailFolder = listArgs[3]
   errorFile = listArgs[4]
   assert checkFormat(templateJson, customerFile, outputEmailFolder, errorFile) == True

   sol(templateJson, customerFile, outputEmailFolder, errorFile)

if __name__ == '__main__':
   main()