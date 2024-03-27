# Import System
import os
import sys
from datetime import datetime
# Import Utils 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Utils', '')))
import finish_process as f
import post_outputs as po
import json_management as j
import connector as s
#Imports Clases
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Clases', '')))
import cuenta_contrato as cc
import punto_suministro as ps
import ubicacion_aparto as ua
import instalacion as ins
import move_in as mi
import montaje as mon
import contrato_potencia as cp
import aparato as ap
import params


date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Output dir path
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.OUTPUTS_STR))
# Output dir path / carga_datos_sap_json
carga_datos_sap_json_output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.OUTPUTS_STR, params.DATOS_JSON_FILE_NAME))
# Add date to file names
error_file_pahtName = f"error_log_{date}"
carga_datos_path = f"carga_datos_sap_{date}"
# Errors file path
error_log_path = os.path.join(carga_datos_sap_json_output_folder, error_file_pahtName + params.TXT_EXT)
# JSON file path
json_log_path = os.path.join(carga_datos_sap_json_output_folder, carga_datos_path + params.JSON_EXT)
#Input
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.INPUTS_STR, params.DATOS_JSON_FILE_NAME))
datos = j.read_json(json_path)

#Conexion con SAP
sap = s.SapConnector()
resultados = []
errores = [] # Variable para almacenar los errores
i = 0 # Contador
x = 0 # Contador de errores
for row in datos:
    try:
        #### OBJETO CUENTA CONTRATO
        cuenta_contrato = cc.CuentaContrato(sap)
        cc_data = row.get('Create_CC', {})
        cuenta_contrato.trx_create_cc = cc_data.get('trxCreateCC', '/nCAA1')
        cuenta_contrato.trx_update_cc = cc_data.get('trxUpdateCC', '/nCAA2')
        cuenta_contrato.tp_cta_contrato = cc_data.get('tp_cta_contrato', '')
        cuenta_contrato.estr_region = cc_data.get('estrRegion', '')
        cuenta_contrato.name = cc_data.get('nombre', '')
        cuenta_contrato.cdc = cc_data.get('cdc', '')
        cuenta_contrato.catcta = cc_data.get('catcta', '')
        cuenta_contrato.condicion_pago = cc_data.get('condicion_pago', '')
        cuenta_contrato.gpo_sociedades = cc_data.get('gpo_sociedades', '')
        cuenta_contrato.soc_std = cc_data.get('soc_std', '')
        cuenta_contrato.clase_impuesto = cc_data.get('clase_impuesto', '')
        cuenta_contrato.lugar_comercial = cc_data.get('lugar_comercial', '')
        cuenta_contrato.region = cc_data.get('region', '')
        cuenta_contrato.condado = cc_data.get('condado', '')
        cuenta_contrato.proc_rec_tension = cc_data.get('proc_rec_tension', '')
        if cuenta_contrato.cdc == "CG":
            cuenta_contrato.tipo_documento = cc_data.get('tipo_documento', 'ZBI_FACTURA_COOP')
        else:
            cuenta_contrato.tipo_documento = cc_data.get('tipo_documento', 'ZFACTURA_GD')
        cuenta_contrato.tipo_compensacion = cc_data.get('tipo_compensacion', 'Z001')
        cuenta_contrato.ikey = cc_data.get('ikey', '50')
        cuenta_contrato.togru = cc_data.get('togru', 'Z001')
        cuenta_contrato.reclamacion = cc_data.get('reclamacion', 'Z1')
        cuenta_contrato.mail = cc_data.get('mail', 'MAIL')
        cuenta_contrato.bloqueo = cc_data.get('bloqueo_interes', '')

        #### OBJETO PUNTO SUMINISTRO
        punto_suministro = ps.PuntoSuministro(sap)
        ps_data = row.get('Create_PS', {})
        punto_suministro.trx_create_ps = ps_data.get('trxCreatePS', '/nES60')
        punto_suministro.trx_update_ps = ps_data.get('trxUpdatePS', '/nES61')
        punto_suministro.clae = ps_data.get('clae', '')

        ### OBJETO UBICACION APARATO
        ubicacion_aparato = ua.UbicacionAparato(sap)
        ua_data = row.get('Create_UA', {})
        ubicacion_aparato.trx_create_ua = ua_data.get('trxCreateUA', '/nES65')
        ubicacion_aparato.trx_update_ua = ua_data.get('trxUpdateUA', '/nES66')
        ubicacion_aparato.centro_empl = ua_data.get('centro_empl', '')
        ubicacion_aparato.denominacion = ua_data.get('denominacion', '')

        #### OBJETO INSTALACION
        instalacion = ins.Instalacion(sap)
        ins_data = row.get('Create_INST', {})
        instalacion.trx_create_ins = ins_data.get('trxCreateINS', '/nES30')
        instalacion.trx_update_ins = ins_data.get('trxUpdateINS', '/nES31')
        instalacion.dia_fijado = ins_data.get('dia_fijado', '')
        instalacion.sector = ins_data.get('sector', '')
        instalacion.niv_tension = ins_data.get('nivTension', '')
        instalacion.cl_cal = ins_data.get('clCal', '')
        instalacion.tp_tarifa = ins_data.get('tp_tarifa', '')
        instalacion.unidad_lectura = ins_data.get('unidad_lectura', '')

        ### OBJETO MOVE IN
        move_in = mi.Movein(sap)
        move_in_data = row.get('Create_movein', {})
        move_in.id = move_in_data.get('id', '')
        move_in.trx_create_move_in = move_in_data.get('trxCreateMovein', '/nEC50E')
        move_in.f_alta = move_in_data.get('f_alta', '')
        move_in.imputacion = move_in_data.get('imputacion', '')
        move_in.segmento = move_in_data.get('segmento', '')
        move_in.cdc = move_in_data.get('cdc', '')
        move_in.fac_conj = move_in_data.get('fac_conj', '')

        ### OBJETO MONTAJE
        montaje = mon.Montaje(sap)
        montaje_data = row.get('Create_montaje', {})
        montaje.trx_create_mon = montaje_data.get('trxCreateMON', '/nEG31')
        montaje.f_alta = montaje_data.get('f_alta', '')
        montaje.dipositivo = montaje_data.get('dipositivo', '')
        montaje.tp_aparato = montaje_data.get('tp_aparato', '')
        montaje.motivo = montaje_data.get('motivo', '')

        ### OBJETO CONTRATO POTENCIA
        contrato_potencia = cp.ContratoPotencia(sap)
        cp_data = row.get('Create_CP', {})
        contrato_potencia.trx_cp = cp_data.get('trxCP', '/nZDM_CONTRATOS_GC')
        contrato_potencia.fecha_ini = cp_data.get('fecha_ini', '')
        contrato_potencia.periodo = cp_data.get('periodo', '00')
        contrato_potencia.contratada_p = cp_data.get('contratadaP', '50')
        contrato_potencia.contratada_fp = cp_data.get('contratadaFP', '50')
        contrato_potencia.descripcion = cp_data.get('descripcion', '')

        obj_data = row.get('OBJETOS', {})

        ### CUENTA CONTRATO FUNCTIONS
        sap.crear_transaccion(cuenta_contrato.trx_create_cc)
        cuenta_contrato.crear_cuenta_contrato(IC = obj_data['IC'])
        cuenta_contrato.cargar_datos_generales()
        cuenta_contrato.cargar_pagos_impuestos()
        cuenta_contrato.cargar_reclamacion(ic = obj_data['IC'])
        sap.crear_transaccion(cuenta_contrato.trx_update_cc)
        cuenta_contrato.busca_nro_cc()
        cuenta_contrato.carga_nro_referencia(cuenta_contrato.id)
        row['OBJETOS']['CC'] = cuenta_contrato.id # GUARDA CUENTA CONTRATO

        ### PUNTO SUMINISTRO
        sap.crear_transaccion(punto_suministro.trx_create_ps)
        punto_suministro.crear_ps(obj_data['OC'])
        punto_suministro.update_ps()
        row['OBJETOS']['PS'] = punto_suministro.id # GUARDA CUENTA CONTRATO


        ### UBICACION DE APARATO
        sap.crear_transaccion(ubicacion_aparato.trx_create_ua)
        ubicacion_aparato.crear_ua(punto_suministro.id, obj_data['OC'],"")
        ubicacion_aparato.update_ua()
        f_flag_prosumidor = False
        ubicacion_aparatoGen = None
        datos_operandos = row.get('Create_OPERAND', {})
        for key, value in datos_operandos.items():
                if value["carga"]:
                        if key == "RT_PROSUM":
                            f_flag_prosumidor = True
        if f_flag_prosumidor:
            ubicacion_aparato_gen = ua.UbicacionAparato(sap)
            ubicacion_aparato_gen.trx_create_ua = ua_data.get('trxCreateUA', '/nES65')
            ubicacion_aparato_gen.trx_update_ua = ua_data.get('trxUpdateUA', '/nES66')
            ubicacion_aparato_gen.centro_empl = ua_data.get('centro_empl', '')
            sap.crear_transaccion(ubicacion_aparato_gen.trx_create_ua)
            ubicacion_aparato_gen.CreateUA(punto_suministro.id, obj_data['OC'], ubicacion_aparato.denominacion + " - GEN")
            ubicacion_aparato_gen.UpdateUA() 
        row['OBJETOS']['UA'] = ubicacion_aparato.id + ubicacion_aparato_gen.id if ubicacion_aparato_gen is not None else ubicacion_aparato.id # GUARDA UBICACION DE APARATO

        ### INSTALACION
        sap.crear_transaccion(instalacion.trx_create_inst)
        instalacion.crear_inst()
        instalacion.cargar_datos_iniciales(punto_suministro.id)
        instalacion.carga_operandos(datos_operandos)
        instalacion.guarda_instalacion()
        row['OBJETOS']['INS'] = instalacion.id # GUARDA INSTALACION
    
        ### MOVE IN
        sap.crear_transaccion(move_in.trx_create_move_in)
        move_in.iniciar_contrato(punto_suministro.id, cuenta_contrato.id, instalacion.id)
        move_in.crear_contrato()
        move_in.cargar_valores_contrato()
        move_in.guardar_contrato(instalacion.id)
        row['OBJETOS']['CONTRATO'] = move_in.id # GUARDA CONTRATO SAP

        ### APARATO
        if f_flag_prosumidor == True:
            aparato = ap.Aparato(sap, id=montaje.dipositivo, material= montaje.tp_aparato)
            sap.crear_transaccion(aparato.trx_modificar_gn)
            aparato.update_gn("GC-04315")
            ##Aparato de Generacion
            aparato_gen = ap.Aparato(sap, id=montaje_data.get('dispotivoGen', ''), material=montaje_data.get('tp_aparato', ''))
            sap.crear_transaccion(aparato_gen.trx_modificar_gn)
            aparato_gen.update_gn("GC-04316")
        elif instalacion.tp_tarifa == "GD_T4":
            ##Aparato
            aparato = ap.Aparato(sap, id=montaje.dipositivo, material= montaje.tp_aparato)
            sap.crear_transaccion(aparato.trx_modificar_gn)
            aparato.update_gn("GC-04313")  

        ### MONTAJE
        sap.crear_transaccion(montaje.trx_create_mon)
        montaje.cargar_datos_generales(ubicacion_aparato.id, instalacion.id)
        # DETERMINA LOS NUMERADORES A CARGAR
        if f_flag_prosumidor == True:
            montaje.cargar_numeradores_prosum()
        elif instalacion.tp_tarifa == "GD_T4":
            montaje.cargar_numeradores_cooperativa()
        else:
            montaje.cargar_numeradores()
        montaje.guardar()
        ### MONTAJE MEDIDORES DE GENERACION
        montaje_gen = None
        if f_flag_prosumidor == True:
            montaje_gen = mon.Montaje(sap)
            montaje_gen.trx_create_mon = montaje_data.get('trxCreateMON', '/nEG31')
            montaje_gen.f_alta = montaje_data.get('f_alta', '')
            montaje_gen.dipositivo = montaje_data.get('dispotivoGen', '')  # Como me pasa el nuevo numero de dispositivo
            montaje_gen.tp_aparato = montaje_data.get('tp_aparato', '')
            montaje_gen.motivo = montaje_data.get('motivo', '')
            sap.crear_transaccion(montaje.trx_create_mon)
            montaje_gen.cargar_datos_generales(ubicacion_aparato_gen.id, instalacion.id)
            montaje_gen.cargar_numeradores_generacion()
            montaje_gen.guardar()
            sap.crear_transaccion(aparato_gen.trx_modificar_gn)
            aparato_gen.update_numerador_gen()

        ### CONTRATO POTENCIA
        sap.crear_transaccion(contrato_potencia.trx_cp)
        contrato_potencia.crear_contrato_potencia(obj_data['IC'], cuenta_contrato.id, instalacion.id)
        contrato_potencia.cargar_datos_cp()
        contrato_potencia.guardar_cp()
        row['OBJETOS']['CP'] = contrato_potencia.id # GUARDA CODIGO POTENCIA
        
        ###### GUARDAR VALORES
        resultados.append(row['OBJETOS'])
        ###### ESCRIBIR EN OUTPUT JSON
        j.escribir_json_obj(json_path,row['OBJETOS'],i)
    
    except Exception as e:
        # Manejo de excepción
        error_message = f"Error: {e} | Fila: {i} | Objetos Creados: {row['OBJETOS']}\n"
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

### REGISTRO DE ERRORES
po.post_outputs(content_file=errores, path=error_log_path, event=params.EVENT_POST, proceso=params.PROCESS_CARGA_DATOS)
### REGISTRO DE JSON
po.post_outputs(content_file=resultados, path=json_log_path, event=params.EVENT_COPY, proceso=params.PROCESS_CARGA_DATOS)

print("Resultado Final")
print(resultados)




