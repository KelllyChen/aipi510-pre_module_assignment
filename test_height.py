import unittest
import pandas as pd
from height import calculate_average

class TestMain(unittest.TestCase):
    def test_calculate_average(self):
        df=pd.read_csv('height.csv')

        # calculate the expected average height of people in the file
        expected_result=df['Heights'].mean()

        #calculate the average height using the calculate_average function from the height.py
        calculate_result = calculate_average()

        #check if the two results are the same
        self.assertEqual(expected_result, calculate_result)


if __name__=='__main__':
    #run unit test
    unittest.main()
