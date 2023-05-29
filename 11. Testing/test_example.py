import unittest

# Code to be tested
def add(a, b):
    return a + b

# Test case
class AddTestCase(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

        result = add(0, 0)
        self.assertEqual(result, 0)

        result = add(-1, 1)
        self.assertEqual(result, 0)

        result = add(10, -5)
        self.assertEqual(result, 5)

# Run the tests
if __name__ == '__main__':
    unittest.main()