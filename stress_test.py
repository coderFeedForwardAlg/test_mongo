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


#outling of posible plan to test the db 

# make a loop to add an arbitrary number of 
# json objects like {"_id": 2, "name": "bill", "age": 18} to the database  
# with increasing id
# every hundred (or thousend) adds, time how long it takes to get all the data out of the database

# add the number of documents and time it takes into to arrays (or pandas df if you want)

# use plotly to make a graph of your data and how long it takes to retreve data
# consiter saving the data to disk and making the graph in a new file 

# thier should be a drop off in speed after 1 GB of data becasue the cash is set to 1 GB









