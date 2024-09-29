from pymongo import *

client1 = MongoClient("mongodb+srv://kparikh1104:Q1mYfHUQaRhwhcZK@cluster0.5hsdc.mongodb.net/trippo-ai")
db1 = client1['TRIPPO-AI']

collection = db1.create_collection("User")