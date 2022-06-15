import requests

API_URL = "http://127.0.0.1:8000/api"

def access_token_request(username, password):
    req = requests.post(f"{API_URL}/token/", json={
        "username": username,
        "password": password
    })
    req_data = req.json()
    return req_data


def users_list_request(access_token):
    req = requests.get(f"{API_URL}/profiles/", headers={
        "Authorization": f"Bearer {access_token}"
    })
    req_data = req.json()
    return req_data