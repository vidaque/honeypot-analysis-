#!/bin/bash

echo "🔐 [1/6] Activating Cowrie virtual environment..."
source cowrie/cowrie-env/bin/activate || { echo "❌ Failed to activate Cowrie virtualenv"; exit 1; }

echo "🚀 [2/6] Starting Cowrie honeypot..."
cd cowrie
bin/cowrie start
cd ..

echo "🧪 [3/6] Simulating fake brute-force SSH attacks..."
python3 scripts/fake_ssh_brute.py

echo "📥 [4/6] Copying latest Cowrie log..."
cp cowrie/var/log/cowrie.json logs/ || { echo "❌ Log not found! Did Cowrie run properly?"; exit 1; }

echo "📊 [5/6] Running full log analysis and visualizations..."
python3 scripts/full_analysis.py

echo "🌍 [6/6] Running GeoIP country analysis from fake IPs..."
python3 scripts/fake_ips_geo.py

echo "✅ All steps complete. Check the /logs folder for CSVs and view charts in terminal output."
