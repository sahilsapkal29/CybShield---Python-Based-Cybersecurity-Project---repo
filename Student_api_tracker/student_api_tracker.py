import requests
from datetime import datetime
import sys

url = "https://api.github.com/users/octocat"

try:
  
    response = requests.get(url)

    
    if response.status_code == 200:
        data = response.json()

        
        username = data["login"]
        user_id = data["id"]
        public_repos = data["public_repos"]
        followers = data["followers"]

       
        fetch_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        
        print("===== GitHub User Information =====")
        print("Username           :", username)
        print("User ID            :", user_id)
        print("Public Repositories:", public_repos)
        print("Followers          :", followers)
        print("Fetch Time         :", fetch_time)

        
        with open("api_log.txt", "w") as file:
            file.write("===== GitHub User Information =====\n")
            file.write(f"Username            : {username}\n")
            file.write(f"User ID             : {user_id}\n")
            file.write(f"Public Repositories : {public_repos}\n")
            file.write(f"Followers           : {followers}\n")
            file.write(f"Fetch Time          : {fetch_time}\n")

        print("\nData saved successfully in 'api_log.txt'.")

       
        print("\n===== Reading Saved Data =====")
        with open("api_log.txt", "r") as file:
            print(file.read())

    else:
        print("Failed to fetch data.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", e)


print("===== Python Version =====")
print(sys.version)