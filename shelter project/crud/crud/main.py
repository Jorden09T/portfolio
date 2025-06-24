from pymongo import MongoClient
from bson.objectid import ObjectId

class animalCollection(object):
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:32269' %  (username, password))
        self.database = self.client['AAC']

    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, readData):
        if readData:
            data = self.database.animals.find(readData, {'_id': False})
        else:
            data = self.database.animals.find({}, {'_id': False})
        return data

    def update(self, query, new_data):
        if query is not None:
            result = self.database.animals.update_one(query, new_data)
            if result.modified_count > 0:
                return True
            else:
                return False
        else:
            raise Exception("No query provided for update")

    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result.delete_count > 0:
                return True
            else:
                return False
        else:
            raise Exception("No data provided for delete")

#Testing Script
shelter = animalCollection("aacuser", "1111")

#Test create method
data = {"Age": "2 years", "Type": "Dog"}
if shelter.create(data):
    print("Animal has been added.")
else:
    raise Exception("Error: Animal not updated, please try again.")
#Read Method
animals = shelter.read({"Type": "Dog"})
print(animals)

#Update Method
query = {"Type": "Dog"}
new_data = {'$set': {"Age": "1.5 years"}}
if shelter.update(query, new_data):
    print("Animal has been updated.")
else:
    raise Exception("Error: Animal not update, please try again.")

#Delete Method
if shelter.delete({"Type": "Dog"}):
    print("Animal has been deleted.")
else:
    raise Exception("Error: Animal not deleted, please")