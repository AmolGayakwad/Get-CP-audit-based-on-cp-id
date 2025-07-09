import requests
import json

base_url = "https://demo.openspecimen.org"
username = "amol@krishagni.com"
password = "Login@123"
domain = "openspecimen"

def get_token():
    url = f"{base_url}/rest/ng/sessions"
    data = {
        "loginName": username,
        "password": password,
        "domainName": domain
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("token")
    else:
        print("Failed to login:", response.status_code)
        return None

def get_cp(cp_id, token):
    url = f"{base_url}/rest/ng/collection-protocols/{cp_id}"
    headers = {
        "X-OS-API-TOKEN": token,
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        cp = response.json()
        file_name = f"cp_{cp_id}.json"
        with open(file_name, "w") as f:
            json.dump(cp, f, indent=2)
        print(f"CP details saved to {file_name}")
    else:
        print("Failed to get CP:", response.status_code)

def main():
    token = get_token()
    if not token:
        return

    cp_id = input("Enter CP ID: ")
    if cp_id.isdigit():
        get_cp(int(cp_id), token)
    else:
        print("Invalid CP ID")

if __name__ == "__main__":
    main()
