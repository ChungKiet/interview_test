from ast import Constant
import json
import pandas as pd
import unittest
import csv
from constants import *
from sol import sol
class TestStringMethods(unittest.TestCase):
   def createFile(self, path, header, values):
      with open(path, 'w', encoding='UTF8', newline='') as f:
         writer = csv.writer(f)

         # write the header
         writer.writerow(header)

         # write multiple rows
         writer.writerows(values)

   def test_result(self):
      test_values = [['Dear You', 'Tester', 'Nguyen', 'tester@example.com']]
      self.createFile(path='./unit_test_file/unit_test.csv', header=HEADER, values=test_values)
      sol('./template.json', './unit_test_file/unit_test.csv', './unit_test_file/', './unit_test_file/unit_test_errors.csv')

      resultFile = open('./unit_test_file/tester@example.com.json')
      result = json.load(resultFile)
      print(result)
      body = result["body"]
      sendTo = result["to"]
      self.assertTrue(sendTo == 'tester@example.com')
      self.assertTrue('Dear You Tester Nguyen' in body)

   def test_err_file(self):
      test_values = [['Dear You', 'Tester', 'Nguyen', ' ']]
      self.createFile(path='./unit_test_file/unit_test.csv', header=HEADER, values=test_values)
      sol('./template.json', './unit_test_file/unit_test.csv', './unit_test_json/', './unit_test_file/unit_test_errors.csv')
      # read errors csv file then 
      df = pd.read_csv('./unit_test_file/unit_test_errors.csv')
      self.assertTrue(df[HEADER[TITLE]][0] == 'Dear You')
      self.assertTrue(df[HEADER[FIRST_NAME]][0] == 'Tester')
      self.assertTrue(df[HEADER[LAST_NAME]][0] == 'Nguyen')
      self.assertTrue(df[HEADER[EMAIL]][0] == ' ')

if __name__ == '__main__':
   unittest.main()