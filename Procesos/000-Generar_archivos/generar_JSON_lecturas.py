import pandas as pd
import json
import os

file_path = (r'Inputs\TT_Estacionales_SAP_PY.csv')

if os.path.exists(file_path):
    df = pd.read_csv(file_path, decimal=',', delimiter = ";")
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
    periodos = group['Tipo de Contrato'].tolist()
    dem_reg_pico = group['Dem.Reg.Pico'].tolist()
    dem_reg_fpico = group['Dem.Reg.F.Pico'].tolist()
    dem_reg_fpico2 = group['Dem.Reg.F.Pico'].tolist()  # Reutilizando el mismo valor
    dem_cont_pico = group['Cap.Sum.Contratada Pico'].tolist() 
    dem_cont_fpico = group['Cap.Sum.Contratada F.Pico'].tolist()
    dem_reg_energ_consu1 = [1000] * len(group)  # Valores fijos
    dem_reg_energ_consu2 = [2000] * len(group)  # Valores fijos
    dem_reg_energ_consu3 = [3000] * len(group)  # Valores fijos
    dem_reg_energ_consu4 = [4000] * len(group)  # Valores fijos

    if group['Tipo'].iloc[0] == 'COOP':
        dem_reg_energ_consu5 = [2001] * len(group)
        dem_reg_energ_consu6 = [1001] * len(group)
        dem_reg_energ_consu7 = [3001] * len(group)
        dem_reg_energ_consu8 = [2001] * len(group)
        dem_reg_energ_consu9 = [1001] * len(group)
        dem_reg_energ_consu10= [3001] * len(group)
        dem_reg_energ_consu11= [2001] * len(group)
        dem_reg_energ_consu12= [1001] * len(group)
        dem_reg_energ_consu13= [3001] * len(group)
    else:
        dem_reg_energ_consu5 = [0] * len(group)
        dem_reg_energ_consu6 = [0] * len(group)
        dem_reg_energ_consu7 = [0] * len(group)
        dem_reg_energ_consu8 = [0] * len(group)
        dem_reg_energ_consu9 = [0] * len(group)
        dem_reg_energ_consu10= [0] * len(group)
        dem_reg_energ_consu11= [0] * len(group)
        dem_reg_energ_consu12= [0] * len(group)
        dem_reg_energ_consu13= [0] * len(group)


    # Estructurar el diccionario
    key = str(int(instalacion))
    result[key] = {
        'periodos': periodos,
        'contratada_P' : list(map(int,[int(num.replace('.', '')) for num in dem_cont_pico])),
        'contratada_FP' : list(map(int,[int(num.replace('.', '')) for num in dem_cont_fpico])),
        'lectura_Pot_P': list(map(int,[int(num.replace('.', '')) for num in dem_reg_pico])),
        'lectura_Pot_R':  list(map(int, [int(num.replace('.', '')) for num in dem_reg_fpico])),
        'lectura_Pot_V': list(map(int, [int(num.replace('.', '')) for num in dem_reg_fpico2])),
        'lectura_E_act_P': dem_reg_energ_consu1,
        'lectura_E_act_R': dem_reg_energ_consu2,
        'lectura_E_act_V': dem_reg_energ_consu3,
        'lectura_E_react': dem_reg_energ_consu4,
        'lectura_E_act_R2': dem_reg_energ_consu5,
        'lectura_E_act_P2': dem_reg_energ_consu6,
        'lectura_E_act_V2': dem_reg_energ_consu7,
        'lectura_E_act_R3': dem_reg_energ_consu8,
        'lectura_E_act_P3': dem_reg_energ_consu9,
        'lectura_E_act_V3': dem_reg_energ_consu10,
        'lectura_E_act_R4': dem_reg_energ_consu11,
        'lectura_E_act_P4': dem_reg_energ_consu12,
        'lectura_E_act_V4': dem_reg_energ_consu13,
    }
# Convierte el resultado a JSON
json_result = json.dumps(result, indent=4)

# Guarda el JSON en un archivo
with open(r'Inputs\lecturas.json', 'w') as f:
    f.write(json_result)

