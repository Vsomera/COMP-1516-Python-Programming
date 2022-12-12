from unittest import TestCase
import unittest
import sys
import io
import os
import re

import book_order


class TestBookOrderDetails(TestCase):

    grade = 0

    @classmethod
    def setUpClass(cls):
        """ Sets up the Test Case """
        TestBookOrderDetails.grade = 0
        print("Grading your Main Script... ")

    @classmethod
    def tearDownClass(cls):
        """ Tears down the Test Case """
        print("Your grade for this part of the lab is: %d/4" % TestBookOrderDetails.grade)

    def test_main_output_valid(self):
        """ Tests the Output from the Main Script """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "book_test.py",
                "0001",
                "Intro to Python",
                "Sally Lee",
                "123456",
                "1990",
                "10",
                "101.10"
            ]

            if os.path.isfile("0001.txt",):
                os.remove("0001.txt")

            book_order.main()

            output = out.getvalue()

            self.assertTrue(os.path.isfile("0001.txt"))
            os.remove("0001.txt")

            TestBookOrderDetails.grade += 1

        finally:
            sys.stdout = saved_stdout
            print(output)

    def test_main_output_invalid_value(self):
        """ Tests the Output from the Main Script """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "book_test.py",
                "0001",
                "Intro to Python@",
                "Sally Lee",
                "123456",
                "1990",
                "10",
                "101.10"
            ]

            book_order.main()

            output = out.getvalue()
            self.assertEqual("Value Error: Title is invalid\n", output)

            TestBookOrderDetails.grade += 1

        finally:
            sys.stdout = saved_stdout

    def test_main_output_invalid_type(self):
        """ Tests the Output from the Main Script """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "book_test.py",
                "0001",
                "Intro to Python",
                "Sally Lee",
                "123456A",
                "1990",
                "10",
                "101.10"
            ]

            book_order.main()

            output = out.getvalue()
            self.assertEqual("Type Error: ISBN must be an integer\n", output)

            TestBookOrderDetails.grade += 1

        finally:
            sys.stdout = saved_stdout


    def test_main_output_divide_by_zero(self):
        """ Tests the Output from the Main Script """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            sys.argv = [
                "book_test.py",
                "0001",
                "Intro to Python",
                "Sally Lee",
                "123456",
                "1990",
                "0",
                "101.10"
            ]

            book_order.main()

            output = out.getvalue()
            self.assertEqual("No Books in Order\n", output)

            TestBookOrderDetails.grade += 1

        finally:
            sys.stdout = saved_stdout


if __name__ == "__main__":
    unittest.main()
