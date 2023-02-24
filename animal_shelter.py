from pymongo import MongoClient


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username="aacuser", password="twoDogs@1Cat"):
        # Initializing the MongoClient to connect to the db with authentication
        self.client = MongoClient('localhost:27017',
                                  username=username,
                                  password=password,
                                  authSource='AAC')

        # Setting database and collection as class variables
        self.database = self.client.AAC
        self.collection = self.database.animals

    # Creates and inserts documents in the animal collection (C)RUD
    def create(self, data) -> bool:
        # the document cannot be empty
        if data:
            # The document should be of type dict
            if isinstance(data, dict):
                # All keys should be of type str
                for key in data.keys():
                    if not isinstance(key, str):
                        return False
                self.collection.insert_one(data)
                return True
            # Creating multiple documents requires checks for each document
            if (isinstance(data, list)):
                # Each document should be dicts that are not empty
                for doc in data:
                    if not doc or not isinstance(doc, dict):
                        return False
                    # All keys should be of type str
                    for key in doc.keys():
                        if not isinstance(key, str):
                            return False
                self.collection.insert_many(data)
                return True
            return False
        else:
            return False

    # Reads data from the animal collection C(R)UD else raise an exception
    def read(self, query):
        try:
            # return a pymongo cursor, essentially an itterator
            return self.collection.find(query)
        except Exception:
            raise Exception("Cannot read from AAC.animals, invalid query")

    # Updates data from the animal collection CR(U)D else raise an exception
    def update(self, query, data):
        try:
            # return data in BSON format
            retrieved_data = self.collection.update_many(query, data)
            return retrieved_data.raw_result
        except Exception:
            raise Exception("Cannot update document(s) in AAC.animals, invalid input")

    # Deletes data from the animal collection CRU(D) else raise an exception
    def delete(self, query):
        try:
            # return data in BSON format
            retrieved_data = self.collection.delete_many(query)
            return retrieved_data.raw_result
        except Exception:
            raise Exception("Cannot delete document(s) in AAC.animals, invalid input")

from dash_leaflet import DivMarker
