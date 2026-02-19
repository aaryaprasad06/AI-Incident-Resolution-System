import random
from datetime import datetime, timedelta
from pymongo import MongoClient
import json

# YOUR MongoDB Atlas connection (PASTE YOURS)
MONGO_URI = "mongodb+srv://aarya06:D0twbBAM7jA4Uh73@cluster0.pxphyhl.mongodb.net/?appName=Cluster0"
DB_NAME = "incident_system"
COLLECTION_NAME = "logs"

def generate_logs(count=1000):
    log_types = ["ERROR", "WARNING", "INFO"]
    incidents = [
        "Memory usage at 95%", "Network latency 500ms", "CPU overload detected",
        "Database connection failed", "Security breach attempt", "Disk space critical 5%",
        "Authentication failed x10", "Service unavailable", "High garbage collection"
    ]
    logs = []
    start_time = datetime.now() - timedelta(hours=24)
    
    for i in range(count):
        log_type = random.choice(log_types)
        incident = random.choice(incidents)
        timestamp = start_time + timedelta(minutes=random.randint(0, 1440))
        log = {
            "timestamp": timestamp.isoformat(),
            "level": log_type,
            "message": incident,
            "incident_id": f"INC-{i+1:06d}",
            "severity": "HIGH" if log_type == "ERROR" else "MEDIUM" if log_type == "WARNING" else "LOW"
        }
        logs.append(log)
    return logs

# Connect to YOUR MongoDB Atlas
print("🔌 Connecting to MongoDB Atlas...")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Generate & Store 1000 enterprise logs
logs = generate_logs(1000)
result = collection.insert_many(logs)
print(f"💾 SAVED {len(result.inserted_ids)} logs to MongoDB Atlas!")

# AI Analysis Dashboard (first 20 logs)
print("\n=== AI INCIDENT ANALYSIS ===")
errors = warnings = 0
for log in logs[:20]:
    if log["level"] == "ERROR":
        print(f"🚨 HIGH: {log['message']} (ID: {log['incident_id']})")
        errors += 1
    elif log["level"] == "WARNING":
        print(f"⚠️ MEDIUM: {log['message']} (ID: {log['incident_id']})")
        warnings += 1
    else:
        print(f"✅ LOW: {log['message']}")

# Final Stats
pipeline = [{"$group": {"_id": "$level", "count": {"$sum": 1}}}]
stats = list(collection.aggregate(pipeline))
print(f"\n📊 ENTERPRISE STATS: {json.dumps(stats, indent=2)}")
print("✅ DATABASE LAYER COMPLETE - 20% PROJECT DONE!")
print("🎉 Check your data: Atlas → incident_system → logs collection")
