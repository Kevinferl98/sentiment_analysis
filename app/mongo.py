from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri, database, collection):
        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]