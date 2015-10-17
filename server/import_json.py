from pymongo import MongoClient
client = MongoClient()
db = client['map']
import os
import json
dir = os.path.dirname(os.path.abspath(__file__))
data_dir = dir + '/data/canada'

file_list = []

for file in os.listdir(data_dir):
    if file.endswith('.geojson'):
        file_list.append(file)

print file_list

for file in file_list:
        collection = db[file[:-8]]
        print collection
        file_path = data_dir + '/' + file
        f = open(file_path, 'r')
        d = json.loads(f.read())
        count = 0
        for item in d['features']:
                count +=1
                collection.insert_one(item)
        print count
