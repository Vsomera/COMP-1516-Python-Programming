from unittest import TestCase
import unittest
import os

import book_order_utils


class TestBookOrderDetails(TestCase):

    grade = 0

    @classmethod
    def setUpClass(cls):
        """ Sets up the Test Case """
        TestBookOrderDetails.grade = 0.0
        print("Grading your Book Orders Util Module... ")

    @classmethod
    def tearDownClass(cls):
        """ Tears down the Test Case """
        print("Your grade for this part of the lab is: %.1f/11.0" % TestBookOrderDetails.grade)

    def test_valid_book_success(self):
        """ Tests that valid values for a book order pass validation """

        # None of these should raise exceptions
        book_order_utils.validate_book_order_details( \
            "1", "Intro to Python", "Bill Smith", "12345", "2000", "10", "100.45")

        book_order_utils.validate_book_order_details( \
            "12", "Advanced Python", "D'Arcy Jones", "12345678901234567890", "2100", "999", "10000.45")

        book_order_utils.validate_book_order_details( \
            "123", "Object Oriented Python", "", "12345678", "2000", "99", "1000.45")

        book_order_utils.validate_book_order_details( \
            "1234", "DataScience", "Sally Lee", "1234", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 1

    def test_validate_book_errors(self):
        """ Tests that invalid values raise exceptions """

        # Invalid Order - Special Characters
        self.assertRaisesRegex(ValueError,
                               "Order Number is invalid",
                               book_order_utils.validate_book_order_details,
                               "1$@&*", "DataScience$", "Sally Lee", "1234", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Order - Special Letter
        self.assertRaisesRegex(ValueError,
                               "Order Number is invalid",
                               book_order_utils.validate_book_order_details,
                               "ABC2", "DataScience$", "Sally Lee", "1234", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Title - Special Characters
        self.assertRaisesRegex(ValueError,
                               "Title is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "DataScience$", "Sally Lee", "1234", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Title - Empty
        self.assertRaisesRegex(ValueError,
                               "Title is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "", "Sally Lee", "1234", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Author - Special Characters
        self.assertRaisesRegex(ValueError,
                               "Author is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee@", "1234", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid ISBN - Letters
        self.assertRaisesRegex(TypeError,
                               "ISBN must be an integer",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "AB1234CD", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid ISBN - Too Short and Too Long
        self.assertRaisesRegex(ValueError,
                               "ISBN is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "123", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        self.assertRaisesRegex(ValueError,
                               "ISBN is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "123456789012345678901", "1900", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Year - Letters
        self.assertRaisesRegex(TypeError,
                               "Year must be an integer",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "1234", "A1900b", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Year - Too Short and Too Long
        self.assertRaisesRegex(ValueError,
                               "Year is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "1234", "190", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        self.assertRaisesRegex(ValueError,
                               "Year is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "1234", "19000", "0", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Quantity - Letters and Special Characters
        self.assertRaisesRegex(TypeError,
                               "Quantity must be an integer",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "1234", "1900", "0.4Aa", "0.00")

        TestBookOrderDetails.grade += 0.5

        # Invalid Quantity - Too Long
        self.assertRaisesRegex(ValueError,
                               "Quantity is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "1234", "1900", "1001", "0.00")

        # Invalid Cost - Letters and Special Characters
        self.assertRaisesRegex(ValueError,
                               "Cost is invalid",
                               book_order_utils.validate_book_order_details,
                               "1", "Data Science", "Sally Lee", "1234", "1900", "0", "$0.00Aa")

        TestBookOrderDetails.grade += 0.5

    def test_valid_book_unit_cost_cad(self):
        """ Tests valid inputs to calculate_per_book_cost_cad """

        result1 = book_order_utils.calculate_per_book_cost_cad(100.0, 10)
        self.assertEqual(10.0, result1)

        result2 = book_order_utils.calculate_per_book_cost_cad(101.0, 5)
        self.assertEqual(20.2, result2)

        result3 = book_order_utils.calculate_per_book_cost_cad(999.99, 9)
        self.assertEqual(111.11, result3)

        TestBookOrderDetails.grade += 1

    def test_invalid_book_unit_cost_cad(self):
        """ Tests valid inputs to calculate_per_book_cost_cad """

        self.assertRaisesRegex(ZeroDivisionError, "float division by zero",
                               book_order_utils.calculate_per_book_cost_cad, 100.0, 0)

        TestBookOrderDetails.grade += 1

    def test_valid_write_book_order_details(self):
        """ Tests valid inputs to write_book_order_details """

        if os.path.isfile("test.txt"):
            os.remove("test.txt")

        book_order_utils.write_book_order_details("test.txt", "Intro to Python", "Bill Smith", "12345", "2000", "10", "100.45", 10.045)

        self.assertTrue(os.path.isfile("test.txt"))
        os.remove("test.txt")

        TestBookOrderDetails.grade += 0.5

    def test_write_book_order_details(self):
        """ Tests valid inputs to calculate_per_book_cost_cad """

        with open("test.txt", "w") as file_handle:
            file_handle.write("Sample Output")

        self.assertRaisesRegex(ValueError, "Order file name already exists!",
                               book_order_utils.write_book_order_details,
                               "test.txt", "Intro to Python", "Bill Smith", "12345", "2000", "10", "100.45", 10.045)

        os.remove("test.txt")

        TestBookOrderDetails.grade += 1

if __name__ == "__main__":
    unittest.main()
