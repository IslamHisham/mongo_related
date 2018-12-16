from pymongo import MongoClient
import json

''' This script takes a json file and insert the records inside it into a Mongo DB '''

username = "accountAdmin01"
password = "changeMe"
db_name = "fifi"
collection_name = "last_test"
host_IP = "localhost"
port = 27017  # default port

try:
    engine = MongoClient(host=host_IP, port=port, username=username, password=password)
    print(engine)
except:
    print("can't connect to database")

db = engine[db_name]  # create a DB with the name mentioned or switch to it if it exists and saving it to var db
collection = db[collection_name]  # creating a collection or switching to it if it exists and saving it to var tests
data = open('./restaurants_data_imp.txt','r')

counter = 0
for line in data:
    counter += 1
    line = json.loads(line.replace('}]},', '}]}'))
    print(counter,"line is:", line)
    clients = db[collection_name].insert(line)

data.close()