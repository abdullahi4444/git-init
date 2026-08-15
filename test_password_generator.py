import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        pw = generate_password()
        self.assertEqual(len(pw), 12)
        
    def test_custom_length(self):
        pw = generate_password(length=16)
        self.assertEqual(len(pw), 16)
        
    def test_length_too_short(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)
            
    def test_uppercase_inclusion(self):
        pw = generate_password(use_uppercase=True, use_numbers=False, use_special=False)
        has_upper = any(c in string.ascii_uppercase for c in pw)
        self.assertTrue(has_upper)

    def test_numbers_inclusion(self):
        pw = generate_password(use_uppercase=False, use_numbers=True, use_special=False)
        has_digit = any(c in string.digits for c in pw)
        self.assertTrue(has_digit)

if __name__ == "__main__":
    unittest.main()

# End of unit tests

