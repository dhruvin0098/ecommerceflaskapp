import unittest
from pymongo import MongoClient
from app import mongodb_username, mongodb_password

class TestDatabaseWriteOperation(unittest.TestCase):
    def setUp(self):
        # Setup MongoDB client
        self.client = MongoClient(
            f"mongodb+srv://{mongodb_username}:{mongodb_password}@cluster0.9jy65.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client["test_database"]
        self.collection = self.db["test_collection"]

    def test_write_data_to_db(self):
        # Insert data and verify insertion
        new_data = {"field": "new_value"}
        insert_result = self.collection.insert_one(new_data)
        inserted_data = self.collection.find_one({"_id": insert_result.inserted_id})

        self.assertIsNotNone(inserted_data)
        self.assertEqual(inserted_data["field"], "new_value")

    def tearDown(self):
        # Clean up test collection
        self.collection.delete_many({})
        self.client.close()

if __name__ == "__main__":
    unittest.main()
