# **comprobar csv 
# **generar json para carga de datos
# **validar json
## ejecutar carga de datos
# completar csv con datos
# generar json lecturas
# generar json para facturacion de contrato
## ejecutar proceso de facturacion


import subprocess
import os

# Definir la ruta a las carpetas de scripts
procesos_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../000-Generar_archivos'))
carga_datos_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../001-Carga_datos_SAP'))
facturacion_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../004-Facturacion_Contratos'))

script_gen_carga_datos = 'generar_JSON_carga_datos.py'
script_gen_lecturas = 'generar_JSON_lecturas.py'
script_gen_facturacion = 'generar_JSON_facturacion.py'
script_modificar_csv = 'modificar_csv_carga_datos.py'  

script_carga_datos_sap = 'carga_datos_sap.py'  
script_facturacion_contratos = 'facturacion_contratos.py' 

def ejecutar_script(script_name, path):
    script_path = os.path.join(path, script_name)
    subprocess.run(['python', script_path], check=True)

if __name__ == "__main__":
    ejecutar_script(script_gen_carga_datos, procesos_path)
    print(f"Script ejecutado: {script_gen_carga_datos}")
    
    ejecutar_script(script_carga_datos_sap, carga_datos_path)
    # print(f"Script ejecutado: {script_carga_datos_sap}")

    ejecutar_script(script_modificar_csv, procesos_path) 
    # print(f"Script ejecutado: {script_modificar_csv}")

    ejecutar_script(script_gen_lecturas, procesos_path)
    # print(f"Script ejecutado: {script_gen_lecturas}")

    ejecutar_script(script_gen_facturacion, procesos_path)
    # print(f"Script ejecutado: {script_gen_facturacion}")

    ejecutar_script(script_facturacion_contratos, facturacion_path)
    #print(f"Script ejecutado: {script_facturacion_contratos}")
    