# getting started with stingray DB

# make sure to use `pip install pymongo` (or install pymongo another way)
from pymongo import MongoClient

#######  set up db connection 
# uri
uri = "mongodb://root:example@38.70.48.137:8081"

client = MongoClient(uri)

db = client["test"]
#my_collection can be whatever you wants 

collection = db["my_collection"]



#############   store data ##################
# doc = {"_id": 2, "name": "bill", "age": 18}

# collection.insert_one(doc)


#############   get the data ############
results = collection.find_one({})

print(results)





