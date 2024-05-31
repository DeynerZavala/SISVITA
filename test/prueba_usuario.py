import requests

# URL de la API para crear un nuevo usuario
api_url = "http://127.0.0.1:8000/login"
# Datos de inicio de sesión
login_data = {
    "correo_electronico": "nuevo_usuario@example.com",
    "contrasena": "contrasena_segura"
}

# Hacer la solicitud POST a la API
response = requests.post(api_url, json=login_data)

# Comprobar el estado de la respuesta
if response.status_code == 200:
    print("Inicio de sesión exitoso.")
    print("Respuesta:", response.json())
else:
    print(f"Error al iniciar sesión. Estado: {response.status_code}")
    print("Respuesta:", response.json())