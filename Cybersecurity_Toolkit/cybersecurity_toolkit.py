import re
import socket


def password_checker():
    print("\n========== PASSWORD STRENGTH CHECKER ==========")

    password = input("Enter Password: ")

    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([bool(length), bool(upper), bool(lower), bool(digit), bool(special)])

    print("\nPassword Analysis")
    print("Minimum 8 Characters :", "Yes" if length else "No")
    print("Uppercase Letter     :", "Yes" if upper else "No")
    print("Lowercase Letter     :", "Yes" if lower else "No")
    print("Number               :", "Yes" if digit else "No")
    print("Special Character    :", "Yes" if special else "No")

    if score <= 2:
        print("\nPassword Strength : WEAK")
    elif score == 3 or score == 4:
        print("\nPassword Strength : MODERATE")
    else:
        print("\nPassword Strength : STRONG")



def log_scanner():
    print("\n========== LOG FILE SCANNER ==========")

    filename = "security_log.txt"

    try:
        with open(filename, "r") as file:
            data = file.read().upper()

        error = data.count("ERROR")
        failed = data.count("FAILED LOGIN")
        warning = data.count("WARNING")

        print("\nScan Results")
        print("ERROR          :", error)
        print("FAILED LOGIN   :", failed)
        print("WARNING        :", warning)

    except FileNotFoundError:
        print("security_log.txt not found.")


def port_scanner():
    print("\n========== BASIC PORT SCANNER ==========")

    ip = input("Enter IP Address (Example: 127.0.0.1): ")

    ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    print("\nScanning...\n")

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port} ({service}) : OPEN")
        else:
            print(f"Port {port} ({service}) : CLOSED")

        sock.close()

while True:

    print("\n========================================")
    print(" CYBERSECURITY AUTOMATION TOOLKIT ")
    print("========================================")
    print("1. Password Strength Checker")
    print("2. Log File Scanner")
    print("3. Basic Port Scanner")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        password_checker()

    elif choice == "2":
        log_scanner()

    elif choice == "3":
        port_scanner()

    elif choice == "4":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")