import pandas as pd
import json
import os

file_path = (r'Procesos\004-Facturacion_Contratos\Lecturas\TT_Estacionales_SAP_TEST.csv')

if os.path.exists(file_path):
    # df = pd.read_csv(file_path, encoding='ISO-8859-1', header=0)
    df = pd.read_csv(file_path, header=1, decimal=',')
    print("Archivo leído correctamente.")
else:
    print(f"El archivo no existe en la ruta: {file_path}")

df.columns = df.columns.str.strip()


import json

# Agrupa por instalación y número de contrato
grouped = df.groupby(['Instalacion', 'NroContrato'])

result = {}

for (instalacion, nro_contrato), group in grouped:
    # Crea dos arrays de 12 espacios para cada agrupación
    dem_reg_pico = [0] * 12
    dem_reg_fpico = [0] * 12
    dem_reg_fpico2 = [0] * 12
    dem_reg_energ_consu1 = [0] * 12
    dem_reg_energ_consu2 = [0] * 12
    dem_reg_energ_consu3 = [0] * 12
    dem_reg_energ_consu4 = [0] * 12

    # Rellena los arrays con las lecturas del index correspondiente
    for index, row in group.iterrows():      
        dem_reg_pico[index] = int(row['Dem.Reg. Pico'])
        dem_reg_fpico[index] = int(row['Dem.Reg. F.Pico'])
        dem_reg_fpico2[index] = int(row['Dem.Reg. F.Pico'])
        dem_reg_energ_consu1[index] = 1000
        dem_reg_energ_consu2[index] = 2000
        dem_reg_energ_consu3[index] = 3000
        dem_reg_energ_consu4[index] = 4000

    # Estructura de la clave para el diccionario
    key = f"{str(int(instalacion))}"

    # Guarda los arrays en el resultado
    result[key] = {
        'lectura_Pot_P': dem_reg_pico,
        'lectura_Pot_R': dem_reg_fpico,
        'lectura_Pot_V': dem_reg_fpico2,
        'lectura_E_act_P': dem_reg_energ_consu1,
        'lectura_E_act_R': dem_reg_energ_consu2,
        'lectura_E_act_V': dem_reg_energ_consu3,
        'lectura_E_react': dem_reg_energ_consu4,
    }

# Convierte el resultado a JSON
json_result = json.dumps(result, indent=4)

# Guarda el JSON en un archivo
with open(r'Procesos\004-Facturacion_Contratos\Lecturas\lecturas.json', 'w') as f:
    f.write(json_result)

