import json
import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils', '')))
import finish_process as f

def read_json(json_path):
    with open(json_path, 'r') as f:
        datos_json = json.load(f)
        return datos_json
    

json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Inputs', 'carga_datos_sap.json'))
f.finalizar_proceso(os.path.splitext(os.path.basename(__file__))[0],json_path) 
