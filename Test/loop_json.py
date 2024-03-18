import json

def read_json(): 
    with open('C:\\Github\\Python-sap\\Inputs\\datos.json', 'r') as f:
        datos_json = json.load(f)
        return datos_json
    

data = read_json()

for row in data:
    datos = row.get('Create_OPERAND', {})
    print (datos)
    for key, value in datos.items():
            if value["carga"]:
                if value["tipo"] == "RATE":
                    print(key,value)
                if value["tipo"] == "FLAG":
                    print(key,value)