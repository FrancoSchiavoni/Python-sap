import json_magnament as j

datos = j.read_json()

for key, value in datos["Create_OPERAND"].items():
    print("------")
    if value["carga"]:
        if value["tipo"] == "RATE":
            print(key, value["f_hasta"], value["clase tarifa"], value['grValoresConcretos'])
        if value["tipo"] == "FLAG":
            print(key, value["hasta"])
