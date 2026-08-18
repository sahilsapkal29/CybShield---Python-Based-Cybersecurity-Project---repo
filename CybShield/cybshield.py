import os
import re
import socket
import ipaddress
import requests
from datetime import datetime


LOG_FILE = "activity_log.txt"

def log_activity(activity):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()}\n")
        file.write(activity + "\n")
        file.write("-" * 40 + "\n")


def password_checker():
    print("\n========== PASSWORD STRENGTH CHECKER ==========")

    password = input("Enter Password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    print("Password Strength :", strength)

    log_activity(f"Password Checked : {strength}")

def log_scanner():

    print("\n========== LOG FILE SCANNER ==========")

    filename = "security_log.txt"

    if not os.path.exists(filename):

        with open(filename, "w") as file:
            file.write("INFO User Logged In\n")
            file.write("ERROR Invalid Password\n")
            file.write("FAILED LOGIN admin\n")
            file.write("WARNING Low Disk Space\n")
            file.write("UNAUTHORIZED ACCESS\n")
            file.write("ATTACK DETECTED\n")

    with open(filename, "r") as file:
        data = file.read().upper()

    keywords = [
        "ERROR",
        "FAILED LOGIN",
        "WARNING",
        "UNAUTHORIZED",
        "ATTACK"
    ]

    print()

    for word in keywords:
        count = data.count(word)
        print(f"{word:15} : {count}")

    log_activity("Security Log Scanned")


def validate_ip(ip):

    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False


def port_scanner():

    print("\n========== PORT SCANNER ==========")

    ip = input("Enter IP Address: ")

    if not validate_ip(ip):
        print("Invalid IP Address")
        return

    ports = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        443: "HTTPS"
    }

    print("\nScanning...\n")

    for port, service in ports.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"{service:10} Port {port} : OPEN")
        else:
            print(f"{service:10} Port {port} : CLOSED")

        sock.close()

    log_activity(f"Port Scan Completed for {ip}")

def login_monitor():

    print("\n========== LOGIN MONITOR ==========")

    username = "admin"
    password = "admin123"

    attempts = 3

    while attempts > 0:

        user = input("Username : ")
        pwd = input("Password : ")

        if user == username and pwd == password:

            print("Login Successful")

            with open("log_history.txt", "a") as file:
                file.write(f"{datetime.now()} Login Successful\n")

            log_activity("Successful Login")

            return

        else:

            attempts -= 1

            print("Invalid Credentials")
            print("Attempts Left :", attempts)

            with open("login_history.txt", "a") as file:
                file.write(f"{datetime.now()} Failed Login\n")

    print("Account Locked")

    log_activity("Account Locked")


def view_logs():

    print("\n========== ACTIVITY LOG ==========")

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as file:
            print(file.read())

    else:
        print("No Activity Found")


def public_ip():

    print("\n========== PUBLIC IP ==========")

    try:
        ip = requests.get("https://api.ipify.org").text
        print("Your Public IP :", ip)
        log_activity(f"Public IP Checked : {ip}")

    except:
        print("Unable to fetch Public IP")


while True:

    print("\n")
    print("=" * 45)
    print("     CYBERSHIELD SECURITY TOOLKIT")
    print("=" * 45)
    print("1. Password Strength Checker")
    print("2. Security Log Scanner")
    print("3. Port Scanner")
    print("4. Login Monitor")
    print("5. View Activity Log")
    print("6. Show Public IP")
    print("7. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        password_checker()

    elif choice == "2":
        log_scanner()

    elif choice == "3":
        port_scanner()

    elif choice == "4":
        login_monitor()

    elif choice == "5":
        view_logs()

    elif choice == "6":
        public_ip()

    elif choice == "7":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice")