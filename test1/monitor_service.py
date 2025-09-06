import os
import socket
import json
import datetime
import subprocess

# List of services to monitor
services = ["httpd", "rabbitmq-server", "postgresql"]

def check_service(service):
    """Check if a service is running using systemctl"""
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True, text=True
        )
        return "UP" if result.stdout.strip() == "active" else "DOWN"
    except Exception:
        return "DOWN"

# Get hostname
host = socket.gethostname()
# Timestamp for filenames
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Create output folder
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for service in services:
    status = check_service(service)
    payload = {
        "service_name": service,
        "service_status": status,
        "host_name": host
    }

    # Save JSON file in output folder
    filename = os.path.join(output_dir, f"{service}-status-{timestamp}.json")
    with open(filename, "w") as f:
        json.dump(payload, f, indent=4)

    print(f"Saved: {filename}")
