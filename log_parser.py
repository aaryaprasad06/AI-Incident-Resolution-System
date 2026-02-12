import random
from datetime import datetime, timedelta


def generate_logs(count=1000):
    log_types = ["ERROR", "WARNING", "INFO"]
    incidents = [
        "Memory usage at 95%",
        "Network latency 500ms", 
        "CPU overload detected",
        "Database connection failed",
        "Security breach attempt",
        "Disk space critical 5%",
        "Authentication failed x10"
    ]
    
    logs = []
    start_time = datetime.now() - timedelta(hours=24)
    
    for i in range(count):
        log_type = random.choice(log_types)
        incident = random.choice(incidents)
        timestamp = start_time + timedelta(minutes=random.randint(0, 1440))
        log = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} [{log_type}] {incident}"
        logs.append(log)
    
    return logs

fake_logs = generate_logs(1000)
print("=== AI Incident Detection System (1000 Logs Analyzed) ===")
errors = warnings = normal = 0

for log in fake_logs[:50]:  ~
    if "ERROR" in log:
        print(f"🚨 INCIDENT: {log}")
        errors += 1
    elif "WARNING" in log:
        print(f"⚠️  ALERT: {log}")
        warnings += 1
    else:
        print(f"✅ OK: {log}")
        normal += 1

print(f"\n📊 SUMMARY: {errors} Errors, {warnings} Warnings, {normal} Normal (from first 50)")
print(f"💾 Total logs generated: {len(fake_logs)}")
