from flask import Flask
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient()
db = client['map']

@app.route('/')
def index():
    return "Hello World!"
@app.route('/mongo')

def mongodb():
    collection = db['map_canada_level_1']
    data = {"name": "Canada", "value": "British Columbia, Quebec"}
    data_id = collection.insert_one(data).inserted_id
    return str(data_id)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
