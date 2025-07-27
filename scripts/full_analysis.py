import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from collections import Counter

# === Step 1: Load and Parse Cowrie JSON Log ===
log_file_path = "logs/cowrie.json"
events = []

print("📥 Reading cowrie.json log...")
with open(log_file_path, "r") as f:
    for line in f:
        try:
            log = json.loads(line.strip())
            if log.get("eventid") == "cowrie.login.failed":
                events.append({
                    "timestamp": log.get("timestamp"),
                    "src_ip": log.get("src_ip"),
                    "username": log.get("username"),
                    "password": log.get("password")
                })
        except json.JSONDecodeError:
            continue

# === Step 2: Convert to DataFrame ===
df = pd.DataFrame(events)
print(f"✅ Parsed {len(df)} failed login attempts.\n")

if df.empty:
    print("⚠️ No login events found. Try simulating attacks first.")
    exit()

# === Step 3: Save to CSV ===
csv_path = "logs/login_attempts.csv"
df.to_csv(csv_path, index=False)
print(f"📄 Exported login attempts to {csv_path}")

# === Step 4: Summary Stats ===
print("\n🔍 Summary Statistics")
print("-------------------------")
print(f"🌐 Unique IPs: {df['src_ip'].nunique()}")
print(f"👤 Unique Usernames: {df['username'].nunique()}")
print(f"🔐 Unique Passwords: {df['password'].nunique()}")

top_ips = df['src_ip'].value_counts().nlargest(5)
top_users = df['username'].value_counts().nlargest(5)
top_passwords = df['password'].value_counts().nlargest(5)

print("\nTop Source IPs:\n", top_ips)
print("\nTop Usernames:\n", top_users)
print("\nTop Passwords:\n", top_passwords)

# === Step 5: Bar Chart of Top IPs ===
plt.figure(figsize=(8, 4))
sns.barplot(x=top_ips.index, y=top_ips.values, palette="Reds_d")
plt.title("🔐 Top 5 Attacker IPs by Login Attempts")
plt.xlabel("Source IP")
plt.ylabel("Attempt Count")
plt.tight_layout()
plt.show()

# === Step 6: Timeline of Login Attempts (Hourly) ===
df["timestamp"] = pd.to_datetime(df["timestamp"])
timeline = df.set_index("timestamp").resample("1H").size()

plt.figure(figsize=(10, 4))
timeline.plot(kind="line", marker="o", color="purple")
plt.title("🕒 Login Attempts Over Time (Hourly)")
plt.xlabel("Time")
plt.ylabel("Number of Attempts")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Step 7: Stacked Bar of Usernames Per IP ===
grouped = df.groupby(["src_ip", "username"]).size().unstack().fillna(0)
grouped.plot(kind="bar", stacked=True, figsize=(10, 5), colormap="viridis")
plt.title("🧑‍💻 Usernames Tried Per Attacker IP")
plt.xlabel("Source IP")
plt.ylabel("Attempts")
plt.tight_layout()
plt.show()

# === Step 8: Heatmap of Username vs Password ===
if df["username"].nunique() <= 20 and df["password"].nunique() <= 20:
    pivot = df.pivot_table(index="username", columns="password", aggfunc="size", fill_value=0)
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, cmap="YlGnBu", linewidths=0.5, annot=True, fmt="d")
    plt.title("🧭 Heatmap: Username vs Password Frequency")
    plt.xlabel("Password")
    plt.ylabel("Username")
    plt.tight_layout()
    plt.show()
else:
    print("\nℹ️ Too many unique usernames/passwords for heatmap. Try with smaller dataset.")
