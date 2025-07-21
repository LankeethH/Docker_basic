from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (Docker Compose name or cloud link)
client = MongoClient("mongodb+srv://OGGY:123@cluster0.jgyykay.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
collection = db["students"]

@app.route("/")
def index():
    students = collection.find()
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
