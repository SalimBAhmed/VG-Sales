from pymongo import MongoClient
import os

host = os.getenv('DATABASE_HOST', 'mongodb')
port = os.getenv('DATABASE_PORT', 27017)
user = os.getenv('DATABASE_USERNAME', 'rootuser')
password = os.getenv('DATABASE_PASSWORD', 'rootpass')


database = "mongodb://"+user+":"+password+"@"+host+":"+str(port)+"/"

client = MongoClient(database)

db = client.vg_sales