import os
import hashlib
import re
import requests
from datetime import datetime

print("=== Malware Detection & Log Analyzer Toolkit ===")

# Known suspicious file extensions
suspicious_extensions = [".exe", ".bat", ".vbs", ".ps1"]

# 1. Detect Suspicious Files
def detect_suspicious_files(path):
   print("\n[+] Scanning for Suspicious Files in:", path)
   try:
       files = os.listdir(path)
       for file in files:
           for ext in suspicious_extensions:
               if file.endswith(ext):
                   print(f"[!] Suspicious File Found: {file}")
   except Exception as e:
       print("Error:", e)

# 2. File Hash Checker (Compare with blacklist)
def check_file_hash(file_path):
   print("\n[+] Checking File Hash:", file_path)
  
   # Example malicious hash (demo)
   blacklist_hashes = [
       "5d41402abc4b2a76b9719d911017c592"
   ]
  
   try:
       with open(file_path, "rb") as f:
           data = f.read()
           hash_value = hashlib.md5(data).hexdigest()
           print("File Hash:", hash_value)
          
           if hash_value in blacklist_hashes:
               print("[!!!] ALERT: File is MALICIOUS!")
           else:
               print("[OK] File appears safe")
   except Exception as e:
       print("Error:", e)

# 3. Log File Analyzer
def analyze_log(file_path):
   print("\n[+] Analyzing Log File:", file_path)
  
   keywords = ["failed", "error", "unauthorized", "attack"]
  
   try:
       with open(file_path, "r") as f:
           lines = f.readlines()
          
           for line in lines:
               for word in keywords:
                   if re.search(word, line, re.IGNORECASE):
                       print("[!] Suspicious Log:", line.strip())
   except Exception as e:
       print("Error:", e)

# 4. Fetch Online Blacklist (Demo)
def fetch_blacklist():
   print("\n[+] Fetching Threat Blacklist")
   try:
       url = input("Enter the URL: ")
       response = requests.get(url)
       print("Status Code:", response.status_code)
       print("Data Preview:\n", response.text[:150])
   except Exception as e:
       print("Error:", e)

# 5. Log Events
def log_event(message):
   with open("forensic_log.txt", "a") as log:
       log.write(f"{datetime.now()} - {message}\n")

# ===== MAIN MENU =====
while True:
   print("\n1. Detect Suspicious Files")
   print("2. Check File Hash")
   print("3. Analyze Log File")
   print("4. Fetch Blacklist")
   print("5. Exit")

   choice = input("Enter your choice: ")

   if choice == "1":
       path = input("Enter directory path: ")
       detect_suspicious_files(path)
       log_event("Suspicious file scan completed")

   elif choice == "2":
       file_path = input("Enter file path: ")
       check_file_hash(file_path)
       log_event("File hash checked")

   elif choice == "3":
       log_file = input("Enter log file path: ")
       analyze_log(log_file)
       log_event("Log analysis completed")

   elif choice == "4":
       fetch_blacklist()
       log_event("Blacklist fetched")

   elif choice == "5":
       print("Exiting Toolkit...")
       break

   else:
       print("Invalid choice!")