from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://isBellihi:1234@cluster0-8mfpm.mongodb.net/Lionbridge-test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/items', methods=['GET'])
def get_all_itemss():
    items = mongo.db.items

    output = []
    for doc in items.find():
        output.append({'_id': str(ObjectId(doc['_id'])), 'name' : doc['name'], 'description' : doc['description']})

    return jsonify({'result' : output})

@app.route('/items/<name>', methods=['GET'])
def get_one_items(name):
    items = mongo.db.items

    item = items.find_one({'name' : name})

    if item:
        output = {'_id' : str(ObjectId(item['_id'])), 'name' : item['name'], 'description' : item['description']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})


@app.route('/items', methods=['POST'])
def add_items():
    items = mongo.db.items 

    name = request.json['name']
    description = request.json['description']

    item_id = items.insert({'name' : name, 'description' : language})
    new_item = items.find_one({'_id' : item_id})

    output = {'_id' : str(ObjectId(new_item['_id'])), 'name' : new_item['name'], 'description' : new_item['description']}

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)