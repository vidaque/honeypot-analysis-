import json
from collections import Counter

# Path to Cowrie log
log_file_path = "logs/cowrie.json"

# Lists to store extracted data
usernames = []
passwords = []
src_ips = []

# Parse the JSON log line by line
try:
    with open(log_file_path, "r") as f:
        for line in f:
            try:
                log = json.loads(line.strip())
                event = log.get("eventid")

                if event == "cowrie.login.failed":
                    usernames.append(log.get("username"))
                    passwords.append(log.get("password"))
                    src_ips.append(log.get("src_ip"))

            except json.JSONDecodeError:
                continue

except FileNotFoundError:
    print(f"❌ File not found: {log_file_path}")
    exit()

# Display Summary
print("\n🛡️  Cowrie Honeypot Attack Summary")
print("────────────────────────────────────")
print(f"🔢 Total login attempts: {len(usernames)}")
print(f"👥 Unique usernames tried: {len(set(usernames))}")
print(f"🔐 Unique passwords tried: {len(set(passwords))}")
print(f"🌍 Unique attacker IPs: {len(set(src_ips))}")

# Top attackers and methods
def show_top(data, title, top_n=5):
    print(f"\n🔝 Top {top_n} {title}")
    print("──────────────────────")
    for item, count in Counter(data).most_common(top_n):
        print(f"{item}: {count}")

show_top(src_ips, "Source IPs")
show_top(usernames, "Usernames")
show_top(passwords, "Passwords")
