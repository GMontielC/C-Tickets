import http.client
import json

# Especificar la URL y el endpoint del servidor
url = "URL_DEL_SERVIDOR"
endpoint = "/ruta_del_endpoint"

# Establecer una conexión con el servidor
connection = http.client.HTTPSConnection(url)

# Enviar la solicitud POST para recibir datos JSON
connection.request("POST", endpoint)

# Obtener la respuesta del servidor
response = connection.getresponse()

# Verificar si la solicitud se realizó con éxito
if response.status == 200:
    # Leer y decodificar la respuesta JSON
    response_data = response.read().decode("utf-8")
    data = json.loads(response_data)

    # Obtener una lista de todas las claves del JSON
    keys = data.keys()

    # Iterar sobre la lista de claves
    for key in keys:
        # Acceder al valor correspondiente
        value = data[key]
        print(key, ":", value)

else:
    print("Error en la solicitud")

# Cerrar la conexión
connection.close()