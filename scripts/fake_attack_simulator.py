import socket
import random
import time

# Cowrie SSH port
TARGET_HOST = "127.0.0.1"
TARGET_PORT = 2222

# Common brute-force lists
usernames = ["admin", "root", "oracle", "test", "guest", "user", "ftp"]
passwords = ["123456", "admin", "password", "toor", "guest", "root", "qwerty"]

# Simulate IP addresses
def random_ip():
    return f"{random.randint(11, 250)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

# Simulate attack loop
for i in range(30):  # simulate 30 attacks
    fake_ip = random_ip()
    user = random.choice(usernames)
    passwd = random.choice(passwords)
    
    print(f"[{i+1}] Attempt from {fake_ip}: {user}/{passwd}")
    
    try:
        # Connect to honeypot (doesn't complete handshake — just triggers connection event)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((TARGET_HOST, TARGET_PORT))
        sock.send(f"{user}:{passwd}".encode())
        sock.close()
    except Exception as e:
        print("⚠️  Connection failed:", e)

    time.sleep(random.uniform(0.1, 0.4))  # small delay to mimic real attack
