# Week 4 - Exercise 1
# Failed Login Detector

login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]

print("Checking login attempts...")

failed_counts = {}

# Count failed attempts
for username, status in login_attempts:
    if status == "failed":
        if username in failed_counts:
            failed_counts[username] += 1
        else:
            failed_counts[username] = 1

# Check for alerts
for user in failed_counts:
    if failed_counts[user] >= 3:
        print("ALERT: User", user, "has", failed_counts[user], "failed login attempts")

print("Security check complete")