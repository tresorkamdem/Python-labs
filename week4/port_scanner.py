# Week 4 - Exercise 2
# Port Security Scanner

devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]

print("Scanning network devices...")

risk_count = 0

for ip, open_ports in devices:
    for port in open_ports:
        if port in risky_ports:
            print("WARNING:", ip, "has risky port", port, "open")
            risk_count += 1

print("Scan complete:", risk_count, "security risks found")