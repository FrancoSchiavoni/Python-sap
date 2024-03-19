import json

def read_json(): 
    with open('C:\\Github\\Python-sap\\Inputs\\datos.json', 'r+') as f:
        datos_json = json.load(f)
        return datos_json


def escribir_json(columna,i,valor):
    with open('C:\\Github\\Python-sap\\Inputs\\datos.json', 'r+') as f:
        datos_json = json.load(f)
        datos_json[i]['OBJETOS'][columna] = valor
        f.seek(0)
        json.dump(datos_json, f, indent=4)
        f.truncate()

def escribir_jsonObjetos(rowObj,i):
    with open('C:\\Github\\Python-sap\\Inputs\\datos.json', 'r+') as f:
        datos_json = json.load(f)
        for clave,valor in rowObj.items():
            datos_json[i]['OBJETOS'][clave] = valor
        f.seek(0)
        json.dump(datos_json, f, indent=4)
        f.truncate()



