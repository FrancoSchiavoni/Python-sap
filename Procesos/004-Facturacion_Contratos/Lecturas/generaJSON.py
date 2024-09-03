import pandas as pd
import json
import os

file_path = (r'Procesos\004-Facturacion_Contratos\Lecturas\TT_Estacionales_SAP_MASIVO.csv')

if os.path.exists(file_path):
    df = pd.read_csv(file_path, decimal=',')
    print("Archivo leído correctamente.")
else:
    print(f"El archivo no existe en la ruta: {file_path}")

df.columns = df.columns.str.strip()


import json

grouped = df.groupby('Instalacion')

result = {}

# Iterar sobre cada instalación y crear los arrays correspondientes
for instalacion, group in grouped:
    # Inicializar arrays para las columnas relevantes
    dem_reg_pico = group['Dem.Reg.Pico'].tolist()
    dem_reg_fpico = group['Dem.Reg.F.Pico'].tolist()
    dem_reg_fpico2 = group['Dem.Reg.F.Pico'].tolist()  # Reutilizando el mismo valor
    dem_reg_energ_consu1 = [1000] * len(group)  # Valores fijos
    dem_reg_energ_consu2 = [2000] * len(group)  # Valores fijos
    dem_reg_energ_consu3 = [3000] * len(group)  # Valores fijos
    dem_reg_energ_consu4 = [4000] * len(group)  # Valores fijos

    # Estructurar el diccionario
    key = str(int(instalacion))
    result[key] = {
        'lectura_Pot_P': list(map(int, dem_reg_pico)),
        'lectura_Pot_R':  list(map(int, dem_reg_fpico)),
        'lectura_Pot_V': list(map(int, dem_reg_fpico2)),
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

