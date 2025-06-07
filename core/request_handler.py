import json
import requests

def send_request(url, method, body, headers):
    # CRUD implementation
    try:
        json_body = json.loads(body) if body else None

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=json_body)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=json_body)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            return {"error": "Unsupported method"}

        return response.json()

    except Exception as e:
        return {"error": str(e)}
