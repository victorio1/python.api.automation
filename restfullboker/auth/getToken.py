import requests
import json

def get_token():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/auth"
    url = base_url + path

    headers = {
        "Content-Type": "application/json"
    }

    request = {
        "username" : "admin",
        "password" : "password123"
    }

    response = requests.post(url, headers=headers, json=request)

    # Verificar el código de estado
    if response.status_code == 200:
        print("Request was successful.")
        # Formatear la respuesta JSON
        response_json = response.json()
        pretty_json = json.dumps(response_json, indent=4)
        print(pretty_json)
    else:
        print("Request failed.")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")

# Llamar a la función para ejecutar la solicitud
get_token()
