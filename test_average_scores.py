"""
Program: test_average_scores.py
Author: Duroje Gwamna
Date Last Modified: 11/14/2021

This program will run three tests on the average_scores() function from
the scores.py file. 
"""


import unittest
from scores import average_scores

class MyTestCase(unittest.TestCase):
    
    def test_average(self):
        self.scores_dict = {"Test 1":86, "Test 2":94, "Test 3":92}
        expected = 90.66666666
        actual= average_scores(self.scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        self.scores_dict = {"Test 1":96, "Test 2":94, "Test 3":98,
                            "Test 4":99, "Test 5":97}
        expected = 96.8
        actual = average_scores(self.scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_zero(self):
        self.scores_dict = dict()
        expected = ValueError
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)
        

if __name__ == "__main__":
   unittest.main()
