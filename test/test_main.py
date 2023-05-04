
import unittest
from src.main import generate_password

class TestMain(unittest.TestCase):

    def test_generate_password(self):
        password = generate_password()
        self.assertTrue(password.isalnum())
        self.assertTrue(len(password) <= 20)

if __name__ == "__main__":
    unittest.main()
