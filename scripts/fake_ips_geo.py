import geoip2.database
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# === Step 1: Generate Fake Public IPs ===
def random_ip():
    return f"{random.randint(23, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

fake_ips = [random_ip() for _ in range(50)]

# === Step 2: GeoIP Lookup ===
reader = geoip2.database.Reader("data/GeoLite2-City.mmdb")
geo_data = []

for ip in fake_ips:
    try:
        response = reader.city(ip)
        geo_data.append({
            "ip": ip,
            "country": response.country.name or "Unknown",
            "city": response.city.name or "Unknown",
            "lat": response.location.latitude,
            "lon": response.location.longitude
        })
    except Exception:
        continue

reader.close()

# === Step 3: Convert to DataFrame ===
df = pd.DataFrame(geo_data)

if df.empty:
    print("❌ No valid GeoIP data retrieved.")
    exit()

# === Step 4: Show Summary in Terminal ===
print("\n📌 GeoIP Summary (Top Countries):")
print(df["country"].value_counts().head())

# === Step 5: Plot Country Attack Counts ===
plt.figure(figsize=(8, 4))
sns.countplot(y=df["country"], order=df["country"].value_counts().index, palette="mako")
plt.title("🌍 Simulated Attack Count by Country")
plt.xlabel("Number of Attacks")
plt.ylabel("Country")
plt.tight_layout()
plt.grid(axis="x", linestyle="--", alpha=0.4)
plt.show()

# === Step 6: Export CSV ===
df.to_csv("logs/geoip_attack_summary.csv", index=False)
print("\n✅ GeoIP data saved to logs/geoip_attack_summary.csv")
