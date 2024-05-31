import requests

api_url = "https://sisvita-pbaq.onrender.com/login"
login_data = {
    "correo_electronico": "nuevo_usuario@example.com",
    "contrasena": "contrasena_segura"
}

response = requests.post(api_url, json=login_data)

# Comprobar el estado de la respuesta
if response.status_code == 200:
    print("Inicio de sesión exitoso.")
    print("Respuesta:", response.json())
else:
    print(f"Error al iniciar sesión. Estado: {response.status_code}")
    print("Respuesta:", response.json())