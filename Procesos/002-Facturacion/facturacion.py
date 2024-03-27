# Import System
import os
import sys
from datetime import datetime
# Import Utils 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.UTILS_STR, '')))
import finish_process as f # SE PUEDE ELIMINAR
import json_management as j
import connector as s
import post_outputs as po
#Imports Clases
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS , params.CLASES_STR, '')))
import lecturas as l
import params

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.INPUTS_STR, params.FACTURACION_STR_LC , params.JSON_EXT))
datos = j.read_json(json_path)

# Output dir path / facturacion
facturacion_output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.OUTPUTS_STR, params.FACTURACION_STR_LC , params.FACTURACION_STR_LC + '_' + date))
os.makedirs(facturacion_output_folder, exist_ok=True)

# Add date to file names
error_file_pahtName = f"error_log_{date}"
facturacion_path = f"facturacion_{date}"

# Errors file path
error_log_path = os.path.join(facturacion_output_folder, error_file_pahtName + params.TXT_EXT)

# JSON file path
json_log_path = os.path.join(facturacion_output_folder, facturacion_path + params.JSON_EXT)

#Conexion con SAP
sap = s.SapConnector()
outputs = []
errores = [] # Variable para almacenar los errores
i = 0 # Contador
x = 0 # Contador de errores

for row in datos:
    try:
        resultados = []
        # OBJETO DE LECTURAS
        lecturas = l.Lecturas(sap)
        lecturas.trx_create_ord = row.get('trxCreateOrd', '/nEL01')
        lecturas.motivo_lectura = row.get('motivo_Lectura', '01')
        lecturas.fecha_ord_lectura_desde = row.get('fecha_Ord_Lectura_Desde', '31.01.2023')
        lecturas.fecha_ord_lectura_hasta = row.get('fecha_Ord_Lectura_Hasta', '')
        lecturas.trx_carga_lecturas = row.get('trxCargaLecturas', '/nEL28')
        lecturas.ins = row.get('INS', '')
        lecturas.cc = row.get('CC', '')
        lecturas.lectura_pot_p = row.get('lectura_Pot_P', '1000')
        lecturas.lectura_pot_r = row.get('lectura_Pot_R', '150')
        lecturas.lectura_pot_v = row.get('lectura_Pot_V', '350')
        lecturas.lectura_e_act_p = row.get('lectura_E_act_P', '2500')
        lecturas.lectura_e_act_r = row.get('lectura_E_act_R', '2000')
        lecturas.lectura_e_act_v = row.get('lectura_E_act_V', '3000')
        lecturas.lectura_pot_p2 = row.get('lectura_Pot_P2', '')
        lecturas.lectura_pot_r2 = row.get('lectura_Pot_R2', '')
        lecturas.lectura_pot_v2 = row.get('lectura_Pot_V2', '')
        lecturas.lectura_e_act_p2 = row.get('lectura_E_act_P2', '')
        lecturas.lectura_e_act_r2 = row.get('lectura_E_act_R2', '')
        lecturas.lectura_e_act_v2 = row.get('lectura_E_act_V2', '')
        lecturas.lectura_e_act_p3 = row.get('lectura_E_act_P3', '')
        lecturas.lectura_e_act_r3 = row.get('lectura_E_act_R3', '')
        lecturas.lectura_e_act_v3 = row.get('lectura_E_act_V3', '')
        lecturas.lectura_e_act_p4 = row.get('lectura_E_act_P4', '')
        lecturas.lectura_e_act_r4 = row.get('lectura_E_act_R4', '')
        lecturas.lectura_e_act_v4 = row.get('lectura_E_act_V4', '')
        lecturas.lectura_e_react = row.get('lectura_E_react', '7500')
        lecturas.trx_calculo = row.get('trxCalculo', '/nEA00')
        lecturas.fecha_calculo = row.get('fecha_Calculo', '10.02.2023')
        lecturas.trx_factura = row.get('trxFactura', '/nEA19')
        lecturas.clave_rec = row.get('clave_rec', '240321-001')
        ### CREAR ORDEN DE LECTURA
        sap.crear_transaccion(lecturas.trx_create_ord)
        lecturas.crear_orden_lectura()
        resultados.append("Orden de lectura : "+ lecturas.fecha_ord_lectura_desde)
        ### CARGA DE LECTURAS
        sap.StartTransaction(lecturas.trx_carga_lecturas)
        lecturas.carga_lecturas()
        resultados.append("Lecturas cargadas")
        ### GENERAR CALCULO
        sap.crear_transaccion(lecturas.trx_calculo)
        lecturas.genera_calculo()
        resultados.append("Calculo generado: " + lecturas.fecha_calculo)

        #Generar Facturas
        sap.crear_transaccion(lecturas.trx_factura)
        lecturas.generar_factura(descargar=True, path_destino = facturacion_output_folder)

        row['doc_calculo'] = lecturas.doc_calculo
        j.escribir_json_facturacion(json_path=json_path, column='doc_calculo', value= lecturas.doc_calculo, i = i)
        j.escribir_json_facturacion(json_path=json_path, column='doc_impresion', value= lecturas.doc_impresion, i = i)
        
        resultados.append("Factura: " + lecturas.doc_impresion)
        outputs.append(resultados)

    except Exception as e:
        # Manejo de excepción
        error_message = f"Error: {e} | Fila: {i} | Acciones Realizadas: {resultados}\n"
        # Agregar el mensaje de error a la lista de errores
        errores.append(error_message)
        x += 1
        i += 1
        continue

    i = i + 1
    # FIN LOOP FOR
sap.crear_transaccion("/n")
sap.cerrar_conexion()

resultados.append({params.TOTAL_ERROR_MESSAGE: x})
errores.append({params.TOTAL_ERROR_MESSAGE: x})

# CARGO REGISTRO DE ERRORES
po.post_outputs(content_file=errores, path=error_log_path, event=params.EVENT_POST, proceso=params.PROCESS_FACTURACION)
# CARGO REGISTRO DE JSON
po.post_outputs(content_file=resultados, path=json_log_path, event=params.EVENT_COPY, proceso=params.PROCESS_FACTURACION)