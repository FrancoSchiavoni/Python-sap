import json

def read_json(): 
    with open('C:\\Github\\Python-sap\\Inputs\\datos.json', 'r+') as f:
        datos_json = json.load(f)
        return datos_json


def escribir_json(columna, valor):
    with open('C:\\Github\\Python-sap\\Inputs\\datos.json', 'r+') as f:
        datos_json = json.load(f)
        datos_json['OBJETOS'][columna] = valor
        f.seek(0)
        json.dump(datos_json, f, indent=4)
        f.truncate()



