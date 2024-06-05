from pymongo import MongoClient
class MongoAPI:
    def __init__(self, data) -> None:
        self.client = MongoClient("mongodb://mymongo_1:27017/")

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
    
    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
    
    def read_one(self, id: str):
        document = self.collection.find_one({'id': id})
        if document and '_id' in document:
            document['_id'] = str(document['_id'])
        return document
    def write(self, data):
        new_document = data
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self,id, data):
        filt = {"id":id}
        updated_data = {"$set": data}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output
    
    def delete(self, id):
        filt = {"id":id}
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted',
                  'Document_ID': id}
        return output
    

mongo_api = MongoAPI({"database": "courses-service", "collection": "students"})