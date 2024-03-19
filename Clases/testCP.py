import json_magnament as j


datos = j.read_json()
i=0
resultados = []

for row in datos:
    
    #Escribir Json
    row['OBJETOS']['CC'] = "700011233333"
    row['OBJETOS']['PS'] = "600002150"
    row['OBJETOS']['UA'] = "650000000002194"
    row['OBJETOS']['INS'] = "400002128"
    row['OBJETOS']['CONTRATO'] = "300002057"
    row['OBJETOS']['CP'] = "0000041019"


    j.escribir_jsonObjetos(row['OBJETOS'],i)

    i = i + 1
    print("----------------------------")


print(i)




