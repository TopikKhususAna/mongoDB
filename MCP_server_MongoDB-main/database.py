from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, uri="mongodb://localhost:27017", db_name="mcp_db"):
        # Membuat koneksi ke MongoDB
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_user(self, user_data):
        """Fungsi untuk memasukkan data ke koleksi users"""
        collection = self.db['users']
        result = collection.insert_one(user_data)
        return result.inserted_id

    def get_user_by_name(self, name):
        """Fungsi untuk mencari data berdasarkan nama"""
        collection = self.db['users']
        return collection.find_one({"nama": name})

    def close_connection(self):
        self.client.close()