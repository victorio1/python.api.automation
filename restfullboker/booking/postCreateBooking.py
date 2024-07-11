import requests
import json

def post_createBooking():
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking"
    url = base_url + path

    headers = {
        "Content-Type": "application/json"
    }

    request_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url, headers=headers, json=request_payload)

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
post_createBooking()
