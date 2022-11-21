from flask import Flask,request
import pymongo
from bson.json_util import dumps
connectionString = "mongodb+srv://shivamgalve:<password>@cluster0.m3axv2c.mongodb.net/test"

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def insertDocument(obj):
    contact = obj
    collection.insert_one(contact).inserted_id


def readDocuments():
    contacts = collection.find({})
    list_cur = list(contacts)
    json_data = dumps(list_cur)
    return json_data


def updateDocuments(obj):
    collection.update_one({'id':obj['contact_id']},{'$set':{"name":obj["update"]["name"]}})


def deleteDocuments(obj):
    r = collection.delete_one({"id": obj['contact_id']})
    print(r.deleted_count)


@app.route('/', methods=['GET', 'POST'])
def getAllContacts():
    if request.method =='GET':
        return readDocuments()

@app.route('/add', methods=['GET', 'POST'])
def addContact():
    if request.method=='POST':
        obj = request.get_json()
        insertDocument(obj)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        obj = request.get_json()
        print(obj)
        updateDocuments(obj)
        return "successfully updated"

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method=='POST':
        obj = request.get_json()
        deleteDocuments(obj)
        return 'delted successfully'


if __name__ == "__main__":
    client = pymongo.MongoClient(connectionString)

    db = client['contact_handbook'] 

    collection = db.contacts
    
    app.run(debug=True, port=8000)