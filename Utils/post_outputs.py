import os
import shutil

def post_outputs(description, path, event, proceso):
    if event == "POST":
        with open(path, 'a') as path_log_file:  # Abrir en modo de añadir ('a')
            # Escribir cada error en una nueva línea del archivo
            path_log_file.write(description + '\n')
    elif event == "COPY":
        # Copiar el archivo JSON desde INPUTS a OUTPUTS y renombrarlo
        input_path = os.path.abspath(os.path.join(os.path.dirname(__file__) ,'./../Inputs/'+ proceso + '.json'))
        shutil.copy(input_path, path)
        print("Archivo de salida creado en:", path)
    