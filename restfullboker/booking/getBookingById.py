import requests
import json

def get_booking():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/"
    bookingId = "329"
    url = base_url + path + bookingId

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

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
get_booking()
