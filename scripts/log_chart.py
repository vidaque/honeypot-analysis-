import json
from collections import Counter
import matplotlib.pyplot as plt

# Path to log
log_file_path = "logs/cowrie.json"

# Data lists
usernames = []
passwords = []
src_ips = []

# Parse cowrie JSON logs
with open(log_file_path, "r") as f:
    for line in f:
        try:
            log = json.loads(line.strip())
            if log.get("eventid") == "cowrie.login.failed":
                usernames.append(log.get("username"))
                passwords.append(log.get("password"))
                src_ips.append(log.get("src_ip"))
        except json.JSONDecodeError:
            continue

# Helper to draw bar charts
def draw_bar_chart(data, title, xlabel):
    counter = Counter(data).most_common(5)
    labels, values = zip(*counter)
    plt.figure(figsize=(8, 4))
    plt.bar(labels, values, color="skyblue")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Plot charts
draw_bar_chart(src_ips, "Top Attacker IPs", "IP Address")
draw_bar_chart(usernames, "Top Usernames Tried", "Username")
draw_bar_chart(passwords, "Top Passwords Tried", "Password")
