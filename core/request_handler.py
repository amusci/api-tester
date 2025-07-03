import json
import requests

def send_request(url, method, body, headers):
    # CRUD implementation
    try:
        json_body = json.loads(body) if body else None

        method = method.upper()
        headers = headers or {}

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=json_body)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=json_body)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, json=json_body)
        elif method == "HEAD":
            response = requests.head(url, headers=headers)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers)
            }
        elif method == "OPTIONS":
            response = requests.options(url, headers=headers)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "allow": response.headers.get("Allow")
            }
        else:
            return {"error": f"Unsupported method: {method}"}

        # Return JSON response if available
        try:
            return response.json()
        except ValueError:
            return {
                "status_code": response.status_code,
                "text": response.text
            }

    except Exception as e:
        return {"error": str(e)}
