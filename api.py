from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)  # React can connect

# YOUR MongoDB connection
MONGO_URI = "mongodb+srv://aarya06:D0twbBAM7jA4Uh73@cluster0.pxphyhl.mongodb.net/?appName=Cluster0"  # Update cluster URL
client = MongoClient(MONGO_URI)
db = client.incident_system
logs_collection = db.logs

@app.route('/api/stats')
def get_stats():
    pipeline = [{"$group": {"_id": "$level", "count": {"$sum": 1}}}]
    stats = list(logs_collection.aggregate(pipeline))
    return jsonify({"stats": stats, "total": logs_collection.count_documents({})})

@app.route('/api/recent')
def get_recent():
    recent = list(logs_collection.find().sort("timestamp", -1).limit(50))
    for log in recent:
        log["_id"] = str(log["_id"])
    return jsonify(recent)

@app.route('/api/incidents')
def get_incidents():
    incidents = list(logs_collection.find({"level": "ERROR"}).sort("timestamp", -1).limit(20))
    for inc in incidents:
        inc["_id"] = str(inc["_id"])
    return jsonify(incidents)

@app.route('/')
def home():
    return jsonify({"message": "AIOps API Live! 🚀", "logs": logs_collection.count_documents({})})

if __name__ == '__main__':
    print("🚀 AIOps API starting on http://localhost:5000")
    app.run(debug=True, port=5000)
