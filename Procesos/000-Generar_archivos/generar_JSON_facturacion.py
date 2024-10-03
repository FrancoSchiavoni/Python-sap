import csv
import json
import os

def generar_JSON_facturacion(input_csv):

    # Ruta a la carpeta Inputs
    carpeta_inputs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Inputs'))

    # Definir la ruta de salida del JSON
    ruta_json = os.path.join(carpeta_inputs, 'facturacion_contrato.json')
    ruta_log = os.path.join(carpeta_inputs, 'log_errores_facturacion_contrato.txt')

    objetos_json = []
    registros_por_id = {}
    errores = []

    # Abrir el archivo CSV
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Agrupar las filas por ID
        for row in reader:
            id_actual = row.get('ID', '')
            if id_actual not in registros_por_id:
                registros_por_id[id_actual] = []
            registros_por_id[id_actual].append(row)

        # Procesar cada grupo de registros con el mismo ID
        for id_actual, registros in registros_por_id.items():
            if len(registros) != 12:
                errores.append(f"ID {id_actual} tiene {len(registros)} registros en lugar de 12")
                continue  # Ignorar IDs que no tienen exactamente 12 filas

            # Tomar solo los valores de la primera fila del grupo
            primer_registro = registros[0]

            try:
                # Extraer campos necesarios del primer registro
                ic = primer_registro.get('IC', '')
                ins = primer_registro.get('Instalacion', '')
                cc = primer_registro.get('CC', '')
                tipo = primer_registro.get('Tipo', '')
                tipo_contrato = primer_registro.get('Tipo de Contrato', '')

                # Determinar tipo_cliente según la presencia de "COOP" en el campo "Tipo"
                tipo_cliente = "DP" if "COOP" in tipo else "GD"

                # Determinar tipo_contrato según la columna "Tipo de contrato"
                if tipo_contrato in ["EA", "EB"]:
                    tipo_contrato_salida = "E"
                elif tipo_contrato == "U" or tipo_contrato == "P":
                    tipo_contrato_salida = "U"
                else:
                    errores.append(f"Contrato no válido en el ID {id_actual}, no se reconoce tipo de contrato")
                    continue

                # Crear el objeto JSON con los datos del primer registro
                objeto = {
                    "id": "",
                    "IC": ic,
                    "INS": ins,
                    "CC": cc,
                    "tipo_cliente": tipo_cliente,
                    "tipo_contrato": tipo_contrato_salida,
                    "fecha_Ord_Lectura_Desde": "31.01.2022",
                    "fecha_Inicio_Contrato": "01.01.2022"
                }

                # Agregar el objeto a la lista general
                objetos_json.append(objeto)
                
            except KeyError as e:
                errores.append(f"Faltan columnas en el ID {id_actual}: {str(e)}")
    
    # Guardar el JSON resultante en un archivo
    with open(ruta_json, 'w') as jsonfile:
        json.dump(objetos_json, jsonfile, indent=4)


file_path = (r'Inputs\Prueba_Contratos_CSV.csv')

if os.path.exists(file_path):
    print("Archivo leído correctamente.")
    generar_JSON_facturacion(file_path)
else:
    print(f"El archivo no existe en la ruta: {file_path}")
# Ejecutar la función

