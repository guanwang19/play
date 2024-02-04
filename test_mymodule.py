# test_mymodule.py

import unittest
from mymodule import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)  # Assert that the result is equal to 8

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -4)
        self.assertEqual(result, -6)  # Assert that the result is equal to -6

    def test_add_mixed_numbers(self):
        result = add_numbers(2, -3)
        self.assertEqual(result, -1)  # Assert that the result is equal to -1

if __name__ == '__main__':
    print(f"I am in {__name__}")
    unittest.main()
# In this example:

# Each test case is defined as a method within a class that inherits from unittest.TestCase.
# Inside each test method, you perform the actual function call (e.g., add_numbers(3, 5)) and use assertion methods like assertEqual to check if the result is as expected.
# To run the tests, you can execute the test_mymodule.py file. If all tests pass, there should be no output. If there are failures, the test runner will provide information about which tests failed and why.

# You can run the tests from the command line like this:

# python test_mymodule.py
# Alternatively, if you want to use pytest, you can create a test file with similar test functions and run it using the pytest command. pytest often requires less boilerplate code than unittest.

# pytest test_mymodule.py
# This is a basic example, and in real-world scenarios, you might want to explore more advanced features of testing frameworks, such as fixtures, mocking, and parameterized testing.





