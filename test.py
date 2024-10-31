import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"})

    
    
if __name__ == "__main__":
    unittest.main()