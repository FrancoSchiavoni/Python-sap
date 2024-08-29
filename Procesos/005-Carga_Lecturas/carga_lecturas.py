import pandas as pd
import json
import os

file_path = (r"C:\Users\lfasolato\Desktop\TT_Estacionales_SAP_CSV.csv")

if os.path.exists(file_path):
    # df = pd.read_csv(file_path, encoding='ISO-8859-1', header=0)
    df = pd.read_csv(file_path, header=1, decimal=',')
    print("Archivo leído correctamente.")
else:
    print(f"El archivo no existe en la ruta: {file_path}")

df.columns = df.columns.str.strip()
print(df.columns)

import json

# Limpia los valores faltantes en 'Instalacion' y 'NroContrato' reemplazándolos con 0 (o con un valor apropiado)
df['Instalacion'] = df['Instalacion'].fillna(0).astype(int)
df['NroContrato'] = df['NroContrato'].fillna(0).astype(int)

# Asegúrate de que las columnas relevantes no contengan valores no numéricos
df['Dem.Reg. Pico'] = pd.to_numeric(df['Dem.Reg. Pico'], errors='coerce').fillna(0)
df['Dem.Reg. F.Pico'] = pd.to_numeric(df['Dem.Reg. F.Pico'], errors='coerce').fillna(0)

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

    # Rellena los arrays con las lecturas del mes correspondiente
    for _, row in group.iterrows():
        mes = int(row['Mes']) - 1  # Ajusta el índice para que sea de 0 a 11
        if 0 <= mes < 12:  # Verifica que el mes esté en el rango correcto
            dem_reg_pico[mes] = int(row['Dem.Reg. Pico'])
            dem_reg_fpico[mes] = int(row['Dem.Reg. F.Pico'])
            dem_reg_fpico2[mes] = int(row['Dem.Reg. F.Pico'])
            if(int(row['Dem.Reg. Pico']) > 3000 and int(row['Dem.Reg. Pico']) < 10000):
                dem_reg_energ_consu1[mes] = 1500
                dem_reg_energ_consu2[mes] = 2500
            elif (int(row['Dem.Reg. Pico']) < 3000):
                dem_reg_energ_consu1[mes] = 500
                dem_reg_energ_consu2[mes] = 1500
            elif (int(row['Dem.Reg. Pico']) > 10000):
                dem_reg_energ_consu1[mes] = 4500
                dem_reg_energ_consu2[mes] = 5500


    # Estructura de la clave para el diccionario
    key = f"inst-{instalacion}_cc-{nro_contrato}"

    # Guarda los arrays en el resultado
    result[key] = {
        'Dem_Reg_Pico': dem_reg_pico,
        'Dem_Reg_F_Pico': dem_reg_fpico,
        'Dem_Reg_F_Pico2': dem_reg_fpico2,
        'Dem_Reg_Energ_Consu1': dem_reg_energ_consu1,
        'Dem_Reg_Energ_Consu2': dem_reg_energ_consu2
    }

# Convierte el resultado a JSON
json_result = json.dumps(result, indent=4)

# Guarda el JSON en un archivo
with open('resultado.json', 'w') as f:
    f.write(json_result)