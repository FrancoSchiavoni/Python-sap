# Import System
import os
import sys

# Import Utils 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', 'Utils', '')))
import finish_process as f
import json_magnament as j
import connector as s
import post_outputs as po

resultados = ""
path = "c:\\Github\\Python-sap\\Outputs\\carga_datos_sap_json\\carga_datos_sap_2024-03-22_11-20-24.json"
po.post_outputs(resultados ,path, "COPY")