# Import System
import os
import sys

# Import Utils 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Utils', '')))
import finish_process as f
import json_magnament as j
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


#Input
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Inputs', 'carga_datos_sap.json'))
datos = j.read_json(json_path)

#Conexion con SAP
sap = s.SapConnector()
resultados = []

i=0 # Contador
for row in datos:
    # Objeto Cuenta Contrato
    CuentaContrato = cc.CuentaContrato(sap)
    cc_data = row.get('Create_CC', {})
        # Asigna los valores correspondientes a las variables de tu objeto CuentaContrato
    CuentaContrato.trxCreateCC = cc_data.get('trxCreateCC', '/nCAA1')
    CuentaContrato.trxUpdateCC = cc_data.get('trxUpdateCC', '/nCAA2')
    CuentaContrato.tp_cta_contrato = cc_data.get('tp_cta_contrato', '')
    CuentaContrato.estrRegion = cc_data.get('estrRegion', '')
    CuentaContrato.name = cc_data.get('nombre', '')
    CuentaContrato.cdc = cc_data.get('cdc', '')
    CuentaContrato.catcta = cc_data.get('catcta', '')
    CuentaContrato.condicion_pago = cc_data.get('condicion_pago', '')
    CuentaContrato.gpo_sociedades = cc_data.get('gpo_sociedades', '')
    CuentaContrato.soc_std = cc_data.get('soc_std', '')
    CuentaContrato.clase_impuesto = cc_data.get('clase_impuesto', '')
    CuentaContrato.lugar_comercial = cc_data.get('lugar_comercial', '')
    CuentaContrato.region = cc_data.get('region', '')
    CuentaContrato.condado = cc_data.get('condado', '')
    CuentaContrato.proc_rec_tension = cc_data.get('proc_rec_tension', '')
    CuentaContrato.tipo_documento = cc_data.get('tipo_documento', 'ZFACTURA_GD')
    CuentaContrato.tipo_compensacion = cc_data.get('tipo_compensacion', 'Z001')
    CuentaContrato.ikey = cc_data.get('ikey', '50')
    CuentaContrato.togru = cc_data.get('togru', 'Z001')
    CuentaContrato.reclamacion = cc_data.get('reclamacion', 'Z1')
    CuentaContrato.mail = cc_data.get('mail', 'MAIL')

    # Objeto Punto Suministro
    PuntoSuministro = ps.PuntoSuministro(sap)
    ps_data = row.get('Create_PS', {})
        # Asigna los valores correspondientes a las variables de tu objeto PuntoSuministro
    PuntoSuministro.trxCreatePS = ps_data.get('trxCreatePS', '/nES60')
    PuntoSuministro.trxUpdatePS = ps_data.get('trxUpdatePS', '/nES61')
    PuntoSuministro.clae = ps_data.get('clae', '')

    # Objeto UbicacionAparato
    UbicacionAparato = ua.UbicacionAparato(sap)
    ua_data = row.get('Create_UA', {})
        # Asigna los valores correspondientes a las variables de tu objeto UbicacionAparato
    UbicacionAparato.trxCreateUA = ua_data.get('trxCreateUA', '/nES65')
    UbicacionAparato.trxUpdateUA = ua_data.get('trxUpdateUA', '/nES66')
    UbicacionAparato.centro_empl = ua_data.get('centro_empl', '')
    UbicacionAparato.denominacion = ua_data.get('denominacion', '')

    # Objeto Instalacion
    Instalacion = ins.Instalacion(sap)
    ins_data = row.get('Create_INST', {})
        # Asigna los valores correspondientes a las variables de tu objeto Instalacion
    Instalacion.trxCreateINS = ins_data.get('trxCreateINS', '/nES30')
    Instalacion.trxUpdateINS = ins_data.get('trxUpdateINS', '/nES31')
    Instalacion.dia_fijado = ins_data.get('dia_fijado', '')
    Instalacion.sector = ins_data.get('sector', '')
    Instalacion.nivTension = ins_data.get('nivTension', '')
    Instalacion.clCal = ins_data.get('clCal', '')
    Instalacion.tp_tarifa = ins_data.get('tp_tarifa', '')
    Instalacion.unidad_lectura = ins_data.get('unidad_lectura', '')

    # Objeto Movein
    Movein = mi.Movein(sap)
    movein_data = row.get('Create_movein', {})
        # Asigna los valores correspondientes a las variables de tu objeto Movein
    Movein.id = movein_data.get('id', '')
    Movein.trxCreateMovein = movein_data.get('trxCreateMovein', '/nEC50E')
    Movein.f_alta = movein_data.get('f_alta', '')
    Movein.imputacion = movein_data.get('imputacion', '')
    Movein.segmento = movein_data.get('segmento', '')
    Movein.cdc = movein_data.get('cdc', '')
    Movein.fac_conj = movein_data.get('fac_conj', '')

    # Objeto Montaje
    Montaje = mon.Montaje(sap)
    montaje_data = row.get('Create_montaje', {})
        # Asigna los valores correspondientes a las variables de tu objeto Montaje
    Montaje.trxCreateMON = montaje_data.get('trxCreateMON', '/nEG31')
    Montaje.f_alta = montaje_data.get('f_alta', '')
    Montaje.dipositivo = montaje_data.get('dipositivo', '')
    Montaje.tp_aparato = montaje_data.get('tp_aparato', '')
    Montaje.motivo = montaje_data.get('motivo', '')

    # Objeto ContratoPotencia
    ContratoPotencia = cp.ContratoPotencia(sap)
    cp_data = row.get('Create_CP', {})
        # Asigna los valores correspondientes a las variables de tu objeto ContratoPotencia
    ContratoPotencia.trxCP = cp_data.get('trxCP', '/nZDM_CONTRATOS_GC')
    ContratoPotencia.fecha_ini = cp_data.get('fecha_ini', '')
    ContratoPotencia.periodo = cp_data.get('periodo', '00')
    ContratoPotencia.contratadaP = cp_data.get('contratadaP', '50')
    ContratoPotencia.contratadaFP = cp_data.get('contratadaFP', '50')
    ContratoPotencia.descripcion = cp_data.get('descripcion', '')

    ####################################################################################


    obj_data = row.get('OBJETOS', {})
    
    # #Cuenta Contrato
    sap.StartTransaction(CuentaContrato.trxCreateCC)
    CuentaContrato.StartCuentaContrato(IC = obj_data['IC'])
    CuentaContrato.SetDatosGenerales()
    CuentaContrato.SetPagosImpuestos()
    CuentaContrato.SetReclamacion(IC = obj_data['IC'])
    sap.StartTransaction(CuentaContrato.trxUpdateCC)
    CuentaContrato.BuscaNroCC()
    
    CuentaContrato.SetNroReferencia(CuentaContrato.id)

    # #Punto Suministro
    sap.StartTransaction(PuntoSuministro.trxCreatePS)
    PuntoSuministro.CreatePS(obj_data['OC'])
    PuntoSuministro.UpdatePS()
    
                         
    # #Ubicacion de Aparato
    sap.StartTransaction(UbicacionAparato.trxCreateUA)
    UbicacionAparato.CreateUA(PuntoSuministro.id, obj_data['OC'])
    UbicacionAparato.UpdateUA()
  
    f_flag_prosumidor = False
    UbicacionAparatoGen = None

    datosOperandos = row.get('Create_OPERAND', {})
    for key, value in datosOperandos.items():
            if value["carga"]:
                    if key == "RT_PROSUM":
                           f_flag_prosumidor = True
                           UbicacionAparatoGen = ua.UbicacionAparato(sap)
                           UbicacionAparatoGen.trxCreateUA = ua_data.get('trxCreateUA', '/nES65')
                           UbicacionAparatoGen.trxUpdateUA = ua_data.get('trxUpdateUA', '/nES66')
                           UbicacionAparatoGen.centro_empl = ua_data.get('centro_empl', '')
                           UbicacionAparatoGen.CreateUA(PuntoSuministro.id, obj_data['OC'])
                           UbicacionAparatoGen.UpdateUA(UbicacionAparato.denominacion + " - GEN")
  

    # #Instalacion
    sap.StartTransaction(Instalacion.trxCreateINS)
    Instalacion.StartInst()
    Instalacion.SetDatosIniciales(PuntoSuministro.id)
    Instalacion.CargaOperandos(datosOperandos)
    Instalacion.GuardaInstalacion()
  

    # #MoveIN
    sap.StartTransaction(Movein.trxCreateMovein)
    Movein.StartContrato(PuntoSuministro.id, CuentaContrato.id, Instalacion.id)
    Movein.InitContrato()
    Movein.SetValoresContrato()
    Movein.GuardaContrato(Instalacion.id)

    # #Aparato
    if f_flag_prosumidor == True:
        ##Aparato
        Aparato = ap.Aparato(sap, id=Montaje.dipositivo, material= Montaje.tp_aparato)
        sap.StartTransaction(Aparato.trxModificarGN)
        Aparato.UpdateGN("GC-04315")

        ##Aparato de Generacion
        AparatoGeneracion = ap.Aparato(sap, id=montaje_data.get('dispotivoGen', ''), material=montaje_data.get('tp_aparatoGen', ''))
        sap.StartTransaction(AparatoGeneracion.trxModificarGN)
        AparatoGeneracion.UpdateGN("GC-04316")
    elif Instalacion.tp_tarifa == "GD_T4":
        ##Aparato
        Aparato = ap.Aparato(sap, id=Montaje.dipositivo, material= Montaje.tp_aparato)
        sap.StartTransaction(Aparato.trxModificarGN)
        Aparato.UpdateGN("GC-04313")  

    # #Montaje
    sap.StartTransaction(Montaje.trxCreateMON)
    Montaje.SetDatosGenerales(UbicacionAparato.id, Instalacion.id)
    
    #Determina que numeradores debe cargar (Normal/Cooperativa/Prosumidor)
    if f_flag_prosumidor == True:
        Montaje.SetNumeradoresProsum()
    elif Instalacion.tp_tarifa == "GD_T4":
        Montaje.SetNumeradoresCooperativa()
    else:
        Montaje.SetNumeradores()
    Montaje.Guardar()

    ### Montaje medidor de Generacion
    MontajeGen = None
    if f_flag_prosumidor == True:
           MontajeGen = mon.Montaje(sap)
           MontajeGen.trxCreateMON = montaje_data.get('trxCreateMON', '/nEG31')
           MontajeGen.f_alta = montaje_data.get('f_alta', '')
           MontajeGen.dipositivo = montaje_data.get('dispotivoGen', '')  # Como me pasa el nuevo numero de dispositivo
           MontajeGen.tp_aparato = montaje_data.get('tp_aparatoGen', '')
           MontajeGen.motivo = montaje_data.get('motivo', '')
           sap.StartTransaction(Montaje.trxCreateMON)
           MontajeGen.SetDatosGenerales(UbicacionAparatoGen.id, Instalacion.id)
           MontajeGen.SetNumeradoresGeneracion()
           MontajeGen.Guardar()
           

    # #ContratoPotencia
    sap.StartTransaction(ContratoPotencia.trxCP)
    ContratoPotencia.InitContratoPotencia(obj_data['IC'], CuentaContrato.id, Instalacion.id)
    ContratoPotencia.SetValoresCP()
    ContratoPotencia.GuardarCP()

    #Guarda Valores
    row['OBJETOS']['CC'] = CuentaContrato.id
    row['OBJETOS']['PS'] = PuntoSuministro.id
    row['OBJETOS']['UA'] = UbicacionAparato.id + UbicacionAparatoGen.id if UbicacionAparatoGen is not None else UbicacionAparato.id
    row['OBJETOS']['INS'] = Instalacion.id
    row['OBJETOS']['CONTRATO'] = Movein.id
    row['OBJETOS']['CP'] = ContratoPotencia.id
    
    resultados.append(row['OBJETOS'])

    
    #Escribir Json
    j.escribir_jsonObjetos(json_path,row['OBJETOS'],i)

    i = i + 1
    #Fin Loop


sap.Close_connection()

f.finalizar_proceso(os.path.splitext(os.path.basename(__file__))[0], json_path)

print("Resultado Final")
print(resultados)




