# Import System
import os
import sys
from datetime import datetime

# Import Utils 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Utils', '')))
import finish_process as f
import json_magnament as j
import connector as s
import post_outputs as po
import show_console_logs

#Imports Clases
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Clases', '')))
import lecturas as l

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#Input
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Inputs', 'facturacion.json'))
datos = j.read_json(json_path)

# Output dir path / facturacion
facturacion_output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Outputs', 'facturacion' , 'facturacion_' + date))
os.makedirs(facturacion_output_folder, exist_ok=True)

# Add date to file names
error_file_pahtName = f"error_log_{date}"
facturacion_path = f"facturacion_{date}"

# Errors file path
error_log_path = os.path.join(facturacion_output_folder, error_file_pahtName + ".txt")

# JSON file path
json_log_path = os.path.join(facturacion_output_folder, facturacion_path + ".json")

#Input Parameter MDT
#mdt = sys.argv[1]
mdt = "390"
#Conexion con SAP
sap = s.SapConnector()

outputs = []
errores = [] # Variable para almacenar los errores
i=0 # Contador
x=0 # Contador de errores
total_iterations = len(datos) 

for iteration, row in enumerate(datos):
    try:
        resultados = []
        #Crea Objeto Lecturas
        Lecturas = l.Lecturas(sap)
        Lecturas.trxCreateOrd = row.get('trxCreateOrd', '/nEL01')
        Lecturas.motivo_Lectura = row.get('motivo_Lectura', '01')
        Lecturas.fecha_Ord_Lectura_Desde = row.get('fecha_Ord_Lectura_Desde', '31.01.2023')
        Lecturas.fecha_Ord_Lectura_Hasta = row.get('fecha_Ord_Lectura_Hasta', '')
        Lecturas.trxCargaLecturas = row.get('trxCargaLecturas', '/nEL28')
        Lecturas.ins = row.get('INS', '')
        Lecturas.cc = row.get('CC', '')
        Lecturas.tipo_cliente = row.get('tipo_cliente', '')
        Lecturas.lectura_E_react = row.get('lectura_E_react', '7500')
        Lecturas.lectura_Pot_P = row.get('lectura_Pot_P', '1000')
        Lecturas.lectura_Pot_R = row.get('lectura_Pot_R', '150')
        Lecturas.lectura_Pot_V = row.get('lectura_Pot_V', '350')
        Lecturas.lectura_E_act_P = row.get('lectura_E_act_P', '2500')
        Lecturas.lectura_E_act_R = row.get('lectura_E_act_R', '2000')
        Lecturas.lectura_E_act_V = row.get('lectura_E_act_V', '3000')
        Lecturas.lectura_Pot_P2 = row.get('lectura_Pot_P2', '')
        Lecturas.lectura_Pot_R2 = row.get('lectura_Pot_R2', '')
        Lecturas.lectura_Pot_V2 = row.get('lectura_Pot_V2', '')
        Lecturas.lectura_E_act_P2 = row.get('lectura_E_act_P2', '')
        Lecturas.lectura_E_act_R2 = row.get('lectura_E_act_R2', '')
        Lecturas.lectura_E_act_V2 = row.get('lectura_E_act_V2', '')
        Lecturas.lectura_E_act_P3 = row.get('lectura_E_act_P3', '')
        Lecturas.lectura_E_act_R3 = row.get('lectura_E_act_R3', '')
        Lecturas.lectura_E_act_V3 = row.get('lectura_E_act_V3', '')
        Lecturas.lectura_E_act_P4 = row.get('lectura_E_act_P4', '')
        Lecturas.lectura_E_act_R4 = row.get('lectura_E_act_R4', '')
        Lecturas.lectura_E_act_V4 = row.get('lectura_E_act_V4', '')
        Lecturas.lectura_E_react = row.get('lectura_E_react', '7500')
        Lecturas.trxCalculo = row.get('trxCalculo', '/nEA00')
        Lecturas.fecha_Calculo = row.get('fecha_Calculo', '10.02.2023')
        Lecturas.trxFactura = row.get('trxFactura', '/nEA19')
        Lecturas.clave_rec = row.get('clave_rec', '240418-001')

        #Crear Orden de Lectura
        sap.StartTransaction(Lecturas.trxCreateOrd)
        Lecturas.CreaOrdenLectura()
        resultados.append("Orden de lectura : "+ Lecturas.fecha_Ord_Lectura_Desde)

        #Carga Lecturas
        sap.StartTransaction(Lecturas.trxCargaLecturas)
        
        if Lecturas.tipo_cliente == "GD":
            Lecturas.CargaLecturasGD(mdt)
        elif Lecturas.tipo_cliente == "COOP":  
            Lecturas.CargaLecturasCOOP()
        elif Lecturas.tipo_cliente == "PROSU": 
                if mdt =="398": 
                    Lecturas.CargaLecturasPROSU(mdt)        
                elif mdt =="390":
                    Lecturas.CargaLecturasPROSU390(mdt)
        
        resultados.append("Lecturas cargadas")

        #Generar Calculo
        sap.StartTransaction(Lecturas.trxCalculo)
        Lecturas.GeneraCalculo()
        resultados.append("Calculo generado: " + Lecturas.fecha_Calculo)

        #Generar Facturas
        sap.StartTransaction(Lecturas.trxFactura)
        Lecturas.GenerarFactura(descargar=True, path_destino = facturacion_output_folder)

        row['doc_calculo'] = Lecturas.doc_calculo
        j.escribir_jsonFacturacion(json_path=json_path, column='doc_calculo', value= Lecturas.doc_calculo, i = i)
        j.escribir_jsonFacturacion(json_path=json_path, column='doc_impresion', value= Lecturas.doc_impresion, i = i)
        
        resultados.append("Factura: " + Lecturas.doc_impresion)
        outputs.append(resultados)
        # Llamamos a mostrar_progreso después de cada iteración
        show_console_logs.show_iteration_bar(iteration, total_iterations)

    except Exception as e:
        # Manejo de excepción
        description = f"{row.get('INS', '')} -- Error: {e} | Fila: {iteration} | Acciones Realizadas: {resultados}\n"
        # Agregar el mensaje de error a la lista de errores
        show_console_logs.show_error(e)
        po.post_outputs(description=description, path=error_log_path, event='POST', proceso="facturacion")
        sap.StartTransaction("/n")
        x += 1
        i += 1
        continue

    i = i + 1
    #Fin Loop

sap.StartTransaction("/n")
sap.Close_connection()

resultados.append({'Total de errores registrados': x})
# errores.append(f"Total de errores registrados: {x}\n")

# Registro total de errores
po.post_outputs(description=(f"Total de errores registrados: {x}\n"), path=error_log_path, event='POST', proceso="facturacion")
# Registro de json
po.post_outputs(content_file=resultados, path=json_log_path, event='COPY', proceso="facturacion")