import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_home(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.data, b"Hello from CI/CD!")12

if __name__ == '__main__':
    unittest.main()