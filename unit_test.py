import csv
import json
import unittest
import pandas as pd
from constants import *
from send_email_class import sendEmail
class TestStringMethods(unittest.TestCase):
   def createFile(self, path, header, values):
      with open(path, 'w', encoding='UTF8', newline='') as f:
         writer = csv.writer(f)

         # write the header
         writer.writerow(header)

         # write multiple rows
         writer.writerows(values)

   def test_result(self):
      # Create data file
      test_values = [['Dear You', 'Tester', 'Nguyen', 'tester@example.com']]
      self.createFile(path='./unit_test_file/unit_test.csv', header=HEADER, values=test_values)

      # Run test
      sendEmailObject = sendEmail('./template.json', \
         './unit_test_file/unit_test.csv', './unit_test_file/', './unit_test_file/unit_test_errors.csv')
      sendEmailObject.send()

      # Compare the result
      resultFile = open('./unit_test_file/tester@example.com.json')
      result = json.load(resultFile)
      body = result["body"]
      sendTo = result["to"]
      self.assertTrue(sendTo == 'tester@example.com')
      self.assertTrue('Dear You Tester Nguyen' in body)

   def test_err_file(self):
      # Create data file
      test_values = [['Dear You', 'Tester', 'Nguyen', ' ']]
      self.createFile(path='./unit_test_file/unit_test.csv', header=HEADER, values=test_values)

      # Run test
      sendEmailObject = sendEmail('./template.json', \
         './unit_test_file/unit_test.csv', './unit_test_json/', './unit_test_file/unit_test_errors.csv')
      sendEmailObject.send()

      # Compare the result
      df = pd.read_csv('./unit_test_file/unit_test_errors.csv')
      self.assertTrue(df[HEADER[TITLE]][0] == 'Dear You')
      self.assertTrue(df[HEADER[FIRST_NAME]][0] == 'Tester')
      self.assertTrue(df[HEADER[LAST_NAME]][0] == 'Nguyen')
      self.assertTrue(df[HEADER[EMAIL]][0] == ' ')

if __name__ == '__main__':
   unittest.main()