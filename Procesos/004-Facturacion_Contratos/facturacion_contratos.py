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
import get_fechas_lecturas as fl

#Imports Clases
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Clases', '')))
import lecturas as l
import contrato_potencia as cp
import lecturasMasivas as lm

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#Input
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Inputs', 'facturacion_contrato.json'))
datos = j.read_json(json_path)

# Output dir path / facturacion
facturacion_output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Outputs', 'facturacion_contrato' , 'facturacion_contrato_' + date))
notas_output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Outputs', 'facturacion_contrato' , 'notas_contrato_' + date))
os.makedirs(facturacion_output_folder, exist_ok=True)
os.makedirs(notas_output_folder, exist_ok=True)


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


# Import Json Lecturas
json_path_lecturas = r"Procesos\004-Facturacion_Contratos\Lecturas\lecturas.json"
datos_lecturas = j.read_json(json_path_lecturas)

for iteration, row in enumerate(datos):
    try:
        resultados = []
        #Crea Objeto Lecturas
        Lecturas = l.Lecturas(sap)
        Lecturas.ins = row.get('INS', '')
        Lecturas.cc = row.get('CC', '')
        Lecturas.tipo_cliente = row.get('tipo_cliente', '')
        Lecturas.trxCreateOrd = row.get('trxCreateOrd', '/nEL01')
        Lecturas.motivo_Lectura = row.get('motivo_Lectura', '01')
        Lecturas.fecha_Ord_Lectura_Desde = row.get('fecha_Ord_Lectura_Desde', '31.01.2023')
        Lecturas.trxCalculo = row.get('trxCalculo', '/nEA00')
        Lecturas.fecha_Calculo = row.get('fecha_Calculo', '10.02.2023')
        Lecturas.trxFactura = row.get('trxFactura', '/nEA19')
        Lecturas.clave_rec = row.get('clave_rec', '240905-001')

        # Fechas Lecturas y Calculo
        fechas_lecturas, fechas_calculo = fl.generar_fechas(Lecturas.fecha_Ord_Lectura_Desde)

        #Crear Orden de Lectura
        #sap.StartTransaction(Lecturas.trxCreateOrd)
        #Lecturas.GenerarOrdenLecturaMasiva(fechas_lecturas)

        # Carga de Lecturas
        Lecturas_Masivas = lm.LecturasMasivas(sap=sap)
        datos_lecturas_ins = datos_lecturas[Lecturas.ins]
        Lecturas_Masivas.ins = Lecturas.ins
        Lecturas_Masivas.lectura_Pot_P = datos_lecturas_ins.get('lectura_Pot_P', Lecturas_Masivas.lectura_Pot_P)
        Lecturas_Masivas.lectura_Pot_R = datos_lecturas_ins.get('lectura_Pot_R', Lecturas_Masivas.lectura_Pot_R)
        Lecturas_Masivas.lectura_Pot_V = datos_lecturas_ins.get('lectura_Pot_V', Lecturas_Masivas.lectura_Pot_V)
        Lecturas_Masivas.lectura_E_act_P = datos_lecturas_ins.get('lectura_E_act_P', Lecturas_Masivas.lectura_E_act_P)
        Lecturas_Masivas.lectura_E_act_R = datos_lecturas_ins.get('lectura_E_act_R', Lecturas_Masivas.lectura_E_act_R)
        Lecturas_Masivas.lectura_E_act_V = datos_lecturas_ins.get('lectura_E_act_V', Lecturas_Masivas.lectura_E_act_V)
        Lecturas_Masivas.lectura_E_react = datos_lecturas_ins.get('lectura_E_react', Lecturas_Masivas.lectura_E_react)
        Lecturas_Masivas.lectura_E_act_P2 = datos_lecturas_ins.get('lectura_E_act_P2', '')
        Lecturas_Masivas.lectura_E_act_R2 = datos_lecturas_ins.get('lectura_E_act_R2', '')
        Lecturas_Masivas.lectura_E_act_V2 = datos_lecturas_ins.get('lectura_E_act_V2', '')
        Lecturas_Masivas.lectura_E_act_P3 = datos_lecturas_ins.get('lectura_E_act_P3', '')
        Lecturas_Masivas.lectura_E_act_R3 = datos_lecturas_ins.get('lectura_E_act_R3', '')
        Lecturas_Masivas.lectura_E_act_V3 = datos_lecturas_ins.get('lectura_E_act_V3', '')
        Lecturas_Masivas.lectura_E_act_P4 = datos_lecturas_ins.get('lectura_E_act_P4', '')
        Lecturas_Masivas.lectura_E_act_R4 = datos_lecturas_ins.get('lectura_E_act_R4', '')
        Lecturas_Masivas.lectura_E_act_V4 = datos_lecturas_ins.get('lectura_E_act_V4', '')

        #sap.StartTransaction(Lecturas_Masivas.trxCargaLecturas)
        
        tipo_cliente = row.get('tipo_cliente', '')
       # if tipo_cliente != 'DP':
       #     Lecturas_Masivas.CargaLecturasGD(mdt=mdt)
       # else:
       #     Lecturas_Masivas.CargaLecturasCOOP(mdt=mdt)

        # Crear Contrato
        IC = row.get('IC', '')
        CC = row.get('CC', '')
        INS = row.get('INS', '')

        tipo_contrato = row.get('tipo_contrato', '')
        Contrato_Potencia = cp.ContratoPotencia(sap=sap)
        Contrato_Potencia.id = row.get('id', '')
        Contrato_Potencia.periodo = tipo_contrato
        Contrato_Potencia.fecha_ini = row.get('fecha_Inicio_Contrato', '')

        if tipo_contrato == "U" and tipo_cliente == "GD":
            Contrato_Potencia.periodo = "00"
        elif tipo_contrato == "E" and tipo_cliente == "GD":
            Contrato_Potencia.periodo = "20"
        elif tipo_contrato == "U" and tipo_cliente == "DP":
            Contrato_Potencia.periodo = "40"
        elif tipo_contrato == "E" and tipo_cliente == "DP":
            Contrato_Potencia.periodo = "5O"

        sap.StartTransaction(Contrato_Potencia.trxCP)
        Contrato_Potencia.InitContratoPotencia(IC=IC, INS=INS, CC=CC)
        
        if tipo_contrato == "U":
            primer_index = datos_lecturas_ins['periodos'].index('U')
            Contrato_Potencia.contratadaP = datos_lecturas_ins['contratada_P'][primer_index]
            Contrato_Potencia.contratadaFP = datos_lecturas_ins['contratada_FP'][primer_index]
            Contrato_Potencia.SetValoresCP()

        if tipo_contrato == "E":
            primer_EA_index = datos_lecturas_ins['periodos'].index('EA')
            primer_EB_index = datos_lecturas_ins['periodos'].index('EB')

            Contrato_Potencia.contratadaP = datos_lecturas_ins['lectura_Pot_P'][primer_EA_index]
            Contrato_Potencia.contratadaFP = datos_lecturas_ins['lectura_Pot_V'][primer_EA_index]

            Contrato_Potencia.contratadaP_B = datos_lecturas_ins['lectura_Pot_P'][primer_EB_index]
            Contrato_Potencia.contratadaFP_B = datos_lecturas_ins['lectura_Pot_R'][primer_EB_index]
            Contrato_Potencia.SetValoresCP()
            Contrato_Potencia.CargaEstacionalidad()

        Contrato_Potencia.GuardarCP()


        ## Calculo y Facturacion
        periodo = 0
        for f in fechas_calculo:
            try:
                periodo = periodo + 1
                # Calculo
                sap.StartTransaction(Lecturas.trxCalculo)
                Lecturas.GeneraCalculo(fecha_C=f)

                # Facturacion
                sap.StartTransaction(Lecturas.trxFactura)
                Lecturas.GenerarFactura(descargar=True, path_destino = facturacion_output_folder, fecha_C=f)

                # Validar
                sap.StartTransaction(Contrato_Potencia.trxValidaCP)
                Contrato_Potencia.ValidarCP()

                # Notificar
                sap.StartTransaction(Contrato_Potencia.trxNotificaCP)
                Contrato_Potencia.NotificarExceso(path_destino=notas_output_folder ,periodo= str(periodo))

                if periodo == 12:
                    sap.StartTransaction(Contrato_Potencia.trxNotificaCP)
                    Contrato_Potencia.NotificarFin(path_destino=notas_output_folder ,periodo= str(periodo))
            
            except Exception as eFact:
                print(eFact)
                continue

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


sap.Close_connection()

resultados.append({'Total de errores registrados': x})
