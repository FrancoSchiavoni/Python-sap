import os
import shutil

def post_outputs(content_file, path, event):
    if event == "POST":
        with open(path, 'w') as path_log_file:
            # Escribir cada error en el archivo
            for c in content_file:
                path_log_file.write(c)
    elif event == "COPY":
        # Copiar el archivo JSON desde INPUTS a OUTPUTS y renombrarlo
        input_path = os.path.basename('./../Inputs/carga_datos_sap.json')
        ruta_output_json = os.path.join(path, ".json")
        shutil.copy(input_path, ruta_output_json)

        print("Proceso finalizado. Archivo de salida creado en:", path)