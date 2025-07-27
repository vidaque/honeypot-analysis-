import paramiko
import random
import time

host = "127.0.0.1"
port = 2222  # Cowrie default

usernames = ["admin", "root", "test", "oracle", "guest", "ftp"]
passwords = ["123456", "admin", "toor", "password", "guest", "root"]

for i in range(30):
    username = random.choice(usernames)
    password = random.choice(passwords)

    print(f"[{i+1}] Trying {username}/{password}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, port=port, username=username, password=password, timeout=3)
    except paramiko.AuthenticationException:
        print("❌ Login failed (expected)")
    except Exception as e:
        print("⚠️  Error:", e)
    finally:
        ssh.close()

    time.sleep(random.uniform(0.2, 0.5))
