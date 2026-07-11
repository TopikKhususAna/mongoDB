from database import MongoDBManager

manager = MongoDBManager()
collection = manager.db['users']

print("--- DAFTAR DATA DI MONGODB ---")
for doc in collection.find():
    print(doc)

manager.close_connection()