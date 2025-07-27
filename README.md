README  

* Overview
* Features
* Setup & usage
* Visuals
* File structure
* Skills demonstrated
* Credits


```markdown
# 🛡️ Cowrie Honeypot Log Analysis & GeoIP Visualization

This project simulates real-world SSH brute-force attacks against a honeypot, logs the events, and visualizes the attacks using Python. It also performs IP-based threat geolocation using MaxMind's GeoLite2 database.

Designed as a hands-on **threat intelligence pipeline**, this project is ideal for cybersecurity learners and blue teamers who want to understand attacker behavior, log analysis, and threat mapping.

---

## 🚀 Features

- 🐍 Deployed [Cowrie honeypot](https://github.com/cowrie/cowrie) on port `2222`
- 🧪 Simulated SSH brute-force attacks using Python (`paramiko`)
- 📂 Parsed Cowrie JSON logs into CSV using `pandas`
- 📊 Created visualizations with `matplotlib` and `seaborn`
- 🌍 Mapped attacker IPs to countries/cities with GeoIP
- 📄 Saved results to CSV for forensic or SIEM integration

---

## 📸 Sample Visuals

*(Replace with actual screenshots if available)*

| Top Source IPs | Top Countries |
|----------------|----------------|
| ![IP Chart](path/to/ip_chart.png) | ![Country Chart](path/to/country_chart.png) |

---

## 🧠 Skills Demonstrated

- Honeypot deployment (Cowrie)
- SSH attack simulation
- Log parsing and credential extraction
- Threat mapping with GeoIP
- Data visualization and analysis
- Python scripting & automation
- Git/GitHub project structure

---

## 📁 File Structure

```

honeypot-analysis/
├── cowrie/                  # Honeypot (not included in Git)
├── data/
│   └── GeoLite2-City.mmdb   # GeoIP database (user must add manually)
├── logs/
│   ├── cowrie.json          # Honeypot output log (copied here)
│   ├── login\_attempts.csv   # Parsed login data
│   └── geoip\_attack\_summary.csv
├── scripts/
│   ├── full\_analysis.py     # Parses Cowrie logs + charts
│   ├── fake\_ssh\_brute.py    # Simulates SSH login attempts
│   └── fake\_ips\_geo.py      # Generates fake IPs + GeoIP mapping
├── run\_honeypot\_analysis.sh # Automates full pipeline
├── requirements.txt
└── README.md

````

---

## 🛠️ Requirements

- Python 3.10+
- Cowrie honeypot installed and configured
- GeoLite2-City.mmdb (download it manually)

Install Python libraries:

```bash
pip install -r requirements.txt
````

---

## 🌍 Setup for GeoIP (Important)

1. Create a free account on [MaxMind](https://www.maxmind.com/en/geolite2/signup)
2. Download `GeoLite2-City.mmdb`
3. Move it into the `/data` directory:

```bash
mkdir -p data
mv ~/Downloads/GeoLite2-City.mmdb data/
```

---

## ▶️ Usage

### 🔁 Option A: Run Entire Workflow Automatically

```bash
./run_honeypot_analysis.sh
```

This script:

* Starts Cowrie honeypot
* Simulates SSH attacks
* Copies logs
* Parses data and creates charts
* Generates fake GeoIP data and maps it

---

### ⚙️ Option B: Manual Steps

```bash
# Start honeypot
cd cowrie
source cowrie-env/bin/activate
bin/cowrie start

# In another terminal:
python3 scripts/fake_ssh_brute.py
cp cowrie/var/log/cowrie.json logs/
python3 scripts/full_analysis.py
python3 scripts/fake_ips_geo.py
```

---

## 📦 Outputs

* `logs/login_attempts.csv` – parsed login attempts
* `logs/geoip_attack_summary.csv` – fake IPs with Geo data
* Interactive charts shown on screen

---

## ✅ .gitignore Highlights

The following are excluded from GitHub:

```
cowrie/
*.mmdb
*.log
logs/*.csv
__pycache__/
```

---

## 📌 Disclaimer

This project is for **educational and research purposes** only. It simulates attacks in a **controlled local environment** and does not target or interact with external systems.

---

## 🙌 Credits

* [Cowrie SSH Honeypot](https://github.com/cowrie/cowrie)
* [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geolite2/)
* Python Libraries: `pandas`, `seaborn`, `matplotlib`, `geoip2`, `paramiko`

---

## 🧑‍💼 Author

**Aadithkv**
[GitHub](https://github.com/vidaque) • [LinkedIn](https://www.linkedin.com/in/aadith-k-v-6a1a06323)

---

````

---

## ✅ Final Step: Commit It

```bash
git add README.md
git commit -m "📝 Add full project documentation to README"
git push
````

