"""create connection to database"""

from pymongo import MongoClient


class DBConnection:

    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def find_one(self, collection_name, filters):
        collection = self.db[collection_name]
        return collection.find_one(filters)
