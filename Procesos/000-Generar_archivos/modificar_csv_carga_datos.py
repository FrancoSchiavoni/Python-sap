import csv
import json
import os

def agregar_datos_al_csv(json_file, csv_file):
    # Leer el JSON y agrupar los datos por ID
    with open(json_file, 'r') as f:
        datos_json = json.load(f)
    
    datos_por_id = {}
    for item in datos_json:
        objetos = item.get("OBJETOS", {})
        id_actual = objetos.get("ID", "")
        instalacion = objetos.get("INS", "")
        ic = objetos.get("IC", "")
        cc = objetos.get("CC", "")
        
        if id_actual not in datos_por_id:
            datos_por_id[id_actual] = {'instalacion': '', 'IC': '', 'CC': ''}
        
        # Actualizar los valores en el diccionario
        datos_por_id[id_actual]['instalacion'] = instalacion
        datos_por_id[id_actual]['IC'] = ic
        datos_por_id[id_actual]['CC'] = cc
        
    # Leer el archivo CSV existente y agregar las nuevas columnas
    filas_actualizadas = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile, delimiter=';')
        campos = lector.fieldnames
        if 'Instalacion' not in campos:
            campos.append('Instalacion')
        if 'IC' not in campos:
            campos.append('IC')
        if 'CC' not in campos:
            campos.append('CC')
            
        for fila in lector:
            id_actual = fila.get('ID')
            if id_actual in datos_por_id:
                # Actualizar los valores en la fila
                fila['Instalacion'] = datos_por_id[id_actual]['instalacion']
                fila['IC'] = datos_por_id[id_actual]['IC']
                fila['CC'] = datos_por_id[id_actual]['CC']
            
            filas_actualizadas.append(fila)
    
    # Guardar los datos actualizados en el archivo CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')
        escritor.writeheader()
        escritor.writerows(filas_actualizadas)

# Rutas de los archivos
json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Inputs/carga_datos_sap.json'))
csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Inputs/TT_Estacionales_SAP_PY.csv'))

# Llamar a la función con las rutas de los archivos
agregar_datos_al_csv(json_file_path, csv_file_path)