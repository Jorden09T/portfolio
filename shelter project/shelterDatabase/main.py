from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient

import os

from pymongo import MongoClient

app = Flask(__name__)
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Jothomas:{password}@cluster0.ipmbjcw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_string)
aac_db = client['aac']
collection = aac_db['aacshelter']


@app.route("/search", methods=["GET"])
def search():
    search_term = request.args.get('query')
    results = collection.find({ '$text': { '$search': search_term } })
    return render_template("index.html", results=results)


@app.route("/")
def index():
    data = collection.find()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
