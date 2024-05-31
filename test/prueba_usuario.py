import requests

def eliminar_usuario(id_usuario):
    url = f'http://127.0.0.1:5000/usuarios/{id_usuario}'
    response = requests.delete(url)

    if response.status_code == 200:
        print('Usuario eliminado correctamente.')
    elif response.status_code == 404:
        print('El usuario no fue encontrado.')
    else:
        print('Ocurrió un error al eliminar el usuario.')

# Llama a la función para eliminar un usuario (reemplaza 'id_del_usuario' con el ID real)
eliminar_usuario(5)
