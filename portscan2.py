#  SafeBank Log Analysis Tool

import re

# Thresholds
FAILED_LOGIN_THRESHOLD = 3
TRANSACTION_THRESHOLD = 10000  # large transaction amount

# Data storage
failed_logins = {}
ip_activity = {}
suspicious_transactions = []
suspicious_logs = []

try:
   with open("bank.log", "r") as file:
       logs = file.readlines()

   print(" Running Log Analysis Tool...\n")

   with open("fraud_report.log", "w") as report:

       for line in logs:
           line = line.strip()

           # Extract IP address
           ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
           ip = ip_match.group() if ip_match else "Unknown"

           ip_activity[ip] = ip_activity.get(ip, 0) + 1

           # Detect failed login
           if "FAILED LOGIN user" in line:
               user = line.split("user")[-1].strip()
               failed_logins[user] = failed_logins.get(user, 0) + 1
               suspicious_logs.append(f" Failed Login: {line}")
               report.write(f"FAILED_LOGIN: {line}\n")

           # Detect large transactions
           if "AMOUNT" in line:
               amount_match = re.search(r'AMOUNT:(\d+)', line)
               if amount_match:
                   amount = int(amount_match.group(1))
                   if amount > TRANSACTION_THRESHOLD:
                       suspicious_transactions.append(line)
                       suspicious_logs.append(f" Large Transaction: {line}")
                       report.write(f"LARGE_TXN: {line}\n")

           # Detect unauthorized access
           if "UNAUTHORIZED ACCESS" in line:
               suspicious_logs.append(f" Unauthorized Access: {line}")
               report.write(f"UNAUTHORIZED: {line}\n")

   # Output suspicious logs
   print(" Suspicious Activities:\n")
   for log in suspicious_logs:
       print(log)

   # Summary Report
   print("\n Security Summary:")

   print("\nFailed Login Attempts:")
   for user, count in failed_logins.items():
       print(f"{user}: {count}")

   print("\n IP Activity:")
   for ip, count in ip_activity.items():
       print(f"{ip}: {count} requests")

   # Detect brute-force attack
   print("\n Possible Brute Force Attacks:")
   brute_found = False
   for user, count in failed_logins.items():
       if count >= FAILED_LOGIN_THRESHOLD:
           print(f"User '{user}' has {count} failed attempts!")
           brute_found = True

   if not brute_found:
       print("No brute-force attack detected.")

   print("\n Suspicious Transactions Detected:", len(suspicious_transactions))

   print("\n Fraud report saved to 'fraud_report.log'")
except FileNotFoundError:
   print(" Error: 'bank.log' file not found. Please create the log file first.")
