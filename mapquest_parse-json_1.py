import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "8EIKnFNK15ncVheFmhYzKJFotGnkgqDn"


def calcular_combustible_requerido(kilometros):
    rendimiento_litros_km = 0.08  # Estimación del rendimiento del vehículo en litros por kilómetro
    combustible_requerido = kilometros * rendimiento_litros_km
    return combustible_requerido


while True:
    orig = input("Ciudad de origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    print ("URL: " + (url))
    json_data = requests.get (url) .json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
       print("API Status:” + str(json_status) + “= Una llamada de ruta exitosa.\ n")
 

       url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "unit": "k"})
       json_data = requests.get(url).json()
       json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

    if "distance" in json_data["route"]:
        distancia = json_data["route"]["distance"]
        distancia_decimal = "{:.2f}".format(distancia)  # Mostrar la distancia con dos decimales
        print(f"Distancia desde {orig} hasta {dest}: {distancia_decimal} km")

        combustible_necesario = calcular_combustible_requerido(distancia)
        print("Combustible requerido: " + str(combustible_necesario) + " litros.")

    if "formattedTime" in json_data["route"]:
        duracion_viaje = json_data["route"]["formattedTime"]
        print("Duración del viaje: " + duracion_viaje)

    if "realTime" in json_data["route"]:
        tiempo_llegada = json_data["route"]["realTime"]

    print("Instrucciones para llegar a " + dest + ":\n")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print(each["narrative"] + " (" + "{:.2f}".format(each["distance"]) + "km)")

        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    print ("")