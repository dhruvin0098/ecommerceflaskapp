import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_invalid_method_on_home(self):
        # Test POST method on a route that accepts GET
        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()
