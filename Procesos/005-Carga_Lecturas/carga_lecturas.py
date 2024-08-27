import pandas as pd
import json
import os

file_path = (r"C:\Users\lfasolato\Desktop\TT_Estacionales_SAP.csv")

if os.path.exists(file_path):
    # df = pd.read_csv(file_path, encoding='ISO-8859-1', header=0)
    df = pd.read_csv(file_path, encoding='ISO-8859-1', header=1)
    print("Archivo leído correctamente.")
else:
    print(f"El archivo no existe en la ruta: {file_path}")

df.columns = df.columns.str.strip()
print(df.columns)

import json

# Limpia los valores faltantes en 'Anio' y 'Mes' reemplazándolos con 0 (o con un valor apropiado)
df['Anio'] = df['Anio'].fillna(0).astype(int)
df['Mes'] = df['Mes'].fillna(0).astype(int)

# Asegúrate de que las columnas relevantes no contengan valores no numéricos
df['Dem.Reg. Pico'] = pd.to_numeric(df['Dem.Reg. Pico'], errors='coerce').fillna(0)
df['Dem.Reg. F.Pico'] = pd.to_numeric(df['Dem.Reg. F.Pico'], errors='coerce').fillna(0)

# Agrupa por año
grouped = df.groupby('Anio')

result = {}

for anio, group in grouped:
    # Crea dos arrays de 12 espacios para cada año
    dem_reg_pico = [0] * 12
    dem_reg_fpico = [0] * 12

    # Rellena los arrays con las lecturas del mes correspondiente
    for _, row in group.iterrows():
        mes = int(row['Mes']) - 1  # Ajusta el índice para que sea de 0 a 11
        if 0 <= mes < 12:  # Verifica que el mes esté en el rango correcto
            dem_reg_pico[mes] = int(row['Dem.Reg. Pico'])
            dem_reg_fpico[mes] = int(row['Dem.Reg. F.Pico'])

    result[anio] = {
        'Dem_Reg_Pico': dem_reg_pico,
        'Dem_Reg_F_Pico': dem_reg_fpico
    }

# Convierte el resultado a JSON
json_result = json.dumps(result, indent=4)

# Guarda el JSON en un archivo
with open('resultado.json', 'w') as f:
    f.write(json_result)