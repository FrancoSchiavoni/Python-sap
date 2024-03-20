import os
import shutil
from datetime import datetime

def finalizar_proceso(nombre_proceso, ruta_input_json):

    #Crea directorio
    fecha_hora_finalizacion = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_directorio_salida = f"{nombre_proceso}_{fecha_hora_finalizacion}"
    ruta_directorio_salida = os.path.join("OUTPUTS", nombre_directorio_salida)
    os.makedirs(ruta_directorio_salida)

    # Copiar el archivo JSON desde INPUTS a OUTPUTS y renombrarlo
    nombre_archivo = os.path.basename(ruta_input_json)
    ruta_output_json = os.path.join(ruta_directorio_salida, f"{nombre_archivo}_{fecha_hora_finalizacion}.json")
    shutil.copy(ruta_input_json, ruta_output_json)

    print("Proceso finalizado. Archivo de salida creado en:", ruta_directorio_salida)