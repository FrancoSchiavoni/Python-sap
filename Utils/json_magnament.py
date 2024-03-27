import json

def read_json(json_path):
    with open(json_path, 'r+') as f:
        datos_json = json.load(f)
        return datos_json


def escribir_json(json_path,columna,i,valor):
    with open(json_path, 'r+') as f:
        datos_json = json.load(f)
        datos_json[i]['OBJETOS'][columna] = valor
        f.seek(0)
        json.dump(datos_json, f, indent=4)
        f.truncate()

def escribir_jsonObjetos(json_path,rowObj,i):
    with open(json_path, 'r+') as f:
        datos_json = json.load(f)
        for clave,valor in rowObj.items():
            datos_json[i]['OBJETOS'][clave] = valor
        f.seek(0)
        json.dump(datos_json, f, indent=4)
        f.truncate()

def escribir_jsonFacturacion(json_path,column,value,i):
    with open(json_path, 'r+') as f:
        datos_json = json.load(f)
        datos_json[i][column] = value
        f.seek(0)
        json.dump(datos_json, f, indent=4)
        f.truncate()

