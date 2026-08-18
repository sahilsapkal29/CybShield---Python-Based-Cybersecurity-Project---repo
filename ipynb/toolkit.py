import re
import hashlib
import os
import requests

print("=== Password Audit & Data Leakage Toolkit ===")

# 1. Password Strength Checker
def check_password_strength(password):
   print("\n[+] Checking Password Strength")
  
   strength = 0
  
   if len(password) >= 8:
       strength += 1
   if re.search("[A-Z]", password):
       strength += 1
   if re.search("[a-z]", password):
       strength += 1
   if re.search("[0-9]", password):
       strength += 1
   if re.search("[@#$%^&+=]", password):
       strength += 1

   if strength <= 2:
       print("[!] Weak Password")
   elif strength == 3 or strength == 4:
       print("[*] Medium Password")
   else:
       print("[OK] Strong Password")

# 2. Detect Emails in Files (Data Leakage)
def detect_emails(file_path):
   print("\n[+] Scanning for Emails in File:", file_path)
  
try:
      with open(file_path, "r") as f:
        data = f.read()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", data)
          
        if emails:
               print("[!] Emails Found:")
               for email in set(emails):
                   print(" -", email)
        else:
               print("[OK] No emails found")
except Exception as e:
       print("Error:", e)

# 3. Password Hash Generator (SHA-1 for breach simulation)
def generate_password_hash(password):
   print("\n[+] Generating Password Hash")
  
   hash_value = hashlib.sha1(password.encode()).hexdigest()
   print("SHA-1 Hash:", hash_value)
   return hash_value

# 4. Simulated Breach Check (Demo API call)
def check_breach(password):
   print("\n[+] Checking Password Breach (Simulated)")
  
   try:
       hash_value = hashlib.sha1(password.encode()).hexdigest()
      
       # Demo request (not real API)
       url = "https://example.com"
       response = requests.get(url)
      
       print("Status Code:", response.status_code)
       print("Password Hash Checked:", hash_value[:10], "...")
       print("[*] (Simulation) No breach found or API not connected")
      
   except Exception as e:
       print("Error:", e)

# 5. Scan Directory for Credential Files
def scan_for_credentials(path):
   print("\n[+] Scanning for Credential Files")
  
   keywords = ["password", "cred", "login"]
  
   try:
       files = os.listdir(path)
       for file in files:
           for word in keywords:
               if word.lower() in file.lower():
                   print(f"[!] Possible Credential File: {file}")
   except Exception as e:
       print("Error:", e)

# ===== MAIN MENU =====
while True:
   print("\n1. Check Password Strength")
   print("2. Detect Emails in File")
   print("3. Generate Password Hash")
   print("4. Check Password Breach")
   print("5. Scan for Credential Files")
   print("6. Exit")

   choice = input("Enter your choice: ")

   if choice == "1":
       password = input("Enter password: ")
       check_password_strength(password)

   elif choice == "2":
       file_path = input("Enter file path: ")
       detect_emails(file_path)

   elif choice == "3":
       password = input("Enter password: ")
       generate_password_hash(password)

   elif choice == "4":
       password = input("Enter password: ")
       check_breach(password)

   elif choice == "5":
       path = input("Enter directory path: ")
       scan_for_credentials(path)

   elif choice == "6":
       print("Exiting Toolkit...")
       break

   else:
       print("Invalid choice!")
