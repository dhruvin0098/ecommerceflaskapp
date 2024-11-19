import unittest
from pymongo import MongoClient
from app import mongodb_username, mongodb_password

class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        # Setup MongoDB client
        self.client = MongoClient(
            f"mongodb+srv://{mongodb_username}:{mongodb_password}@cluster0.9jy65.mongodb.net/?retryWrites=true&w=majority"
        )

    def test_mongodb_connection(self):
        # Test connection using ping
        try:
            self.client.admin.command('ping')
            connection_successful = True
        except Exception as e:
            print(f"Error: {e}")
            connection_successful = False

        self.assertTrue(connection_successful)

    def tearDown(self):
        # Close client
        self.client.close()

if __name__ == "__main__":
    unittest.main()
