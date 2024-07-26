from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:1234@socialmedia.tjazmpi.mongodb.net/?retryWrites=true&w=majority&appName=SocialMedia"
client = MongoClient(mongo_uri)
db = client['MongoREST']
collection = db['RESTAPI']

def get_all_items():
    return list(collection.find({}, {'_id': 0}))

def add_item(item):
    result = collection.insert_one(item)
    return str(result.inserted_id)

"""def update_item(item):"""
