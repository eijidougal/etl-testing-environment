from pymongo import MongoClient

def seed_mongodb():
    client = MongoClient("mongodb://root:password@localhost:27017")
    db = client["testdb"]
    collection = db["test_collection"]

    # Drop the collection if it exists to start fresh
    collection.drop()

    # Insert sample data
    sample_data = [
        {"id": 1, "value": "value_1"},
        {"id": 2, "value": "value_2"},
        {"id": 3, "value": "value_3"}
    ]
    collection.insert_many(sample_data)
    print("MongoDB seeded successfully with sample data.")

if __name__ == "__main__":
    seed_mongodb()
