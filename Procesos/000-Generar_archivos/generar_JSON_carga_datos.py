import csv
import json
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def procesar_csv(input_csv):
    # Obtener la variable de entorno DISPOSITIVO_ACTUAL
    dispositivo_actual = int(os.getenv('DISPOSITIVO_ACTUAL'))
    # Mostrar el valor de la variable
    print(f"El dispositivo actual es: {dispositivo_actual}")

    # Ruta a la carpeta Inputs
    carpeta_inputs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Inputs'))

    # Definir la ruta de salidas
    ruta_json = os.path.join(carpeta_inputs, 'carga_datos_sap.json')
    ruta_log = os.path.join(carpeta_inputs, 'log_errores_carga_datos_sap.txt')

    objetos_json = []

    # Abrimos el archivo CSV
    with open(input_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        # print(reader.fieldnames)  # Esto imprimirá los nombres de las columnas
        registros_por_id = {}
        errores = []

        # Agrupar registros por ID
        for row in reader:
            id_actual = row['ID']
            if id_actual not in registros_por_id:
                registros_por_id[id_actual] = []
            registros_por_id[id_actual].append(row)

        for id_actual, registros in registros_por_id.items():
            if len(registros) != 12:
                errores.append(f"ID {id_actual} tiene {len(registros)} registros en lugar de 12")
                continue  # Salta el procesamiento de este ID y sigue con el siguiente
            else:
                print(f"Contrato {id_actual} - tiene 12 periodos")
            # Verificar si el grupo tiene "COOP" en algún registro
            es_coop = any('COOP' in registro['Tipo'] for registro in registros)
            # Crear el objeto base
            if es_coop:
                objeto = {
                    "OBJETOS": {
                        "IC": "200003112",
                        "OC": "610000000001005",
                        "CC": "",
                        "PS": "",
                        "UA": "",
                        "UA_GEN": "",
                        "INS": "",
                        "CONTRATO": "",
                        "CP": "",
                        "ID": f"{id_actual}"
                    },
                    "Create_CC": {
                        "tp_cta_contrato": "DP",
                        "estrRegion": "S6020A21",
                        "nombre": f"DP-CONTRATO-{dispositivo_actual}",
                        "cdc": "CG",
                        "catcta": "G001",
                        "condicion_pago": "Z003",
                        "gpo_sociedades": "Z001",
                        "soc_std": "1000",
                        "clase_impuesto": "01",
                        "lugar_comercial": "0069",
                        "region": "12",
                        "condado": "011",
                        "proc_rec_tension": "P2",
                        "bloqueo_interes": ""
                    },
                    "Create_PS": {
                        "clae": "239900"
                    },
                    "Create_UA": {
                        "denominacion": f"DP-CONTRATO-{dispositivo_actual}",
                        "centro_empl": "6000"
                    },
                    "Create_INST": {
                        "dia_fijado": "01.12.2024",
                        "sector": "EN",
                        "nivTension": "G1",
                        "clCal": "CEPE",
                        "tp_tarifa": "GD_T4",
                        "unidad_lectura": "GSFCO"
                    },
                    "Create_OPERAND": {
                        "RT_CAT_CLI": {
                            "tipo": "RATE",
                            "carga": True,
                            "f_hasta": "31.12.9999",
                            "clase tarifa": "GD_NORM",
                            "grValoresConcretos": "T4_BT"
                        },
                        "RT_PROSUM": {
                            "tipo": "RATE",
                            "carga": False,
                            "f_hasta": "31.12.9999",
                            "clase tarifa": "",
                            "grValoresConcretos": ""
                        },
                        "QU_CUPOGEN": {
                            "tipo": "QUANT",
                            "carga": False,
                            "hasta": "31.12.9999",
                            "cantidad": "0"
                        },
                        "FL_GUDIS": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_NO_CAP": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_EMP_REC": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_PRG_IND": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_CLUB": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_COO_UNI": {
                            "tipo": "FLAG",
                            "carga": True,
                            "hasta": "31.12.9999"
                        },
                        "FL_COO_MAS": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_BEN_INF": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        }
                    },
                    "Create_movein": {
                        "f_alta": "01.12.2024",
                        "imputacion": "S2010",
                        "segmento": "103",
                        "cdc": "CG",
                        "fac_conj": "2"
                    },
                    "Create_montaje": {
                        "f_alta": "01.12.2024",
                        "dipositivo": str(dispositivo_actual),  # Usar el dispositivo actual
                        "dispotivoGen": "",
                        "tp_aparato": "600000",
                        "motivo": "05"
                    },
                    "Create_CP": {
                        "fecha_ini": "01.12.2024",
                        "periodo": "40",
                        "contratadaP": "50",
                        "contratadaFP": "50",
                        "descripcion": "CASO: CASO COOP"
                    }
                }
                # Agregar el objeto a la lista general
                objetos_json.append(objeto)

                # Incrementar el dispositivo para que no se repita
                dispositivo_actual += 1
                with open('.env', 'w') as f:
                    f.write(f"DISPOSITIVO_ACTUAL={dispositivo_actual}\n")
            else:
                objeto = {
                    "OBJETOS": {
                        "IC": "200003112",
                        "OC": "610000000001005",
                        "CC": "",
                        "PS": "",
                        "UA": "",
                        "UA_GEN": "",
                        "INS": "",
                        "CONTRATO": "",
                        "CP": "",
                        "ID": f"{id_actual}"
                    },
                    "Create_CC": {
                        "tp_cta_contrato": "GD",
                        "estrRegion": "S6020A21",
                        "nombre": f"GD-CONTRATO-{dispositivo_actual}",
                        "cdc": "CU",
                        "catcta": "G003",
                        "condicion_pago": "Z002",
                        "gpo_sociedades": "Z001",
                        "soc_std": "1000",
                        "clase_impuesto": "01",
                        "lugar_comercial": "0069",
                        "region": "12",
                        "condado": "123",
                        "proc_rec_tension": "P2",
                        "bloqueo_interes": ""
                    },
                    "Create_PS": {
                        "clae": "239900"
                    },
                    "Create_UA": {
                        "denominacion": f"GD-CONTRATO-{dispositivo_actual}",
                        "centro_empl": "6000"
                    },
                    "Create_INST": {
                        "dia_fijado": "01.12.2024",
                        "sector": "EN",
                        "nivTension": "G1",
                        "clCal": "CEPE",
                        "tp_tarifa": "GD_T2",
                        "unidad_lectura": "GROCC"
                    },
                    "Create_OPERAND": {
                        "RT_CAT_CLI": {
                            "tipo": "RATE",
                            "carga": True,
                            "f_hasta": "31.12.9999",
                            "clase tarifa": "GD_PARQ",
                            "grValoresConcretos": "PI_BAJA"
                        },
                        "RT_PROSUM": {
                            "tipo": "RATE",
                            "carga": False,
                            "f_hasta": "31.12.9999",
                            "clase tarifa": "",
                            "grValoresConcretos": ""
                        },
                        "QU_CUPOGEN": {
                            "tipo": "QUANT",
                            "carga": False,
                            "hasta": "31.12.9999",
                            "cantidad": "0"
                        },
                        "FL_GUDIS": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_NO_CAP": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_EMP_REC": {
                            "tipo": "FLAG",
                            "carga": True,
                            "hasta": "31.12.9999"
                        },
                        "FL_PRG_IND": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_CLUB": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_COO_UNI": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_COO_MAS": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        },
                        "FL_BEN_INF": {
                            "tipo": "FLAG",
                            "carga": False,
                            "hasta": "31.12.9999"
                        }
                    },
                    "Create_movein": {
                        "f_alta": "01.12.2024",
                        "imputacion": "S4010",
                        "segmento": "111",
                        "cdc": "CU",
                        "fac_conj": "2"
                    },
                    "Create_montaje": {
                        "f_alta": "01.12.2024",
                        "dipositivo": str(dispositivo_actual),  # Usar el dispositivo actual
                        "dispotivoGen": "",
                        "tp_aparato": "600000",
                        "motivo": "05"
                    },
                    "Create_CP": {
                        "fecha_ini": "01.12.2024",
                        "periodo": "00",
                        "contratadaP": "50",
                        "contratadaFP": "100",
                        "descripcion": "CASO: <300"
                    }
                }
                # Agregar el objeto a la lista general
                objetos_json.append(objeto)

                # Incrementar el dispositivo para que no se repita
                dispositivo_actual += 1
                with open('.env', 'w') as f:
                    f.write(f"DISPOSITIVO_ACTUAL={dispositivo_actual}\n")

    # Guardar el JSON resultante en un archivo
    with open(ruta_json, 'w') as jsonfile:
        json.dump(objetos_json, jsonfile, indent=4)



file_path = (r'Inputs\Prueba_Contratos_CSV.csv')

if os.path.exists(file_path):
    print("Archivo leído correctamente.")
    procesar_csv(file_path)
else:
    print(f"El archivo no existe en la ruta: {file_path}")
# Ejecutar la función

 