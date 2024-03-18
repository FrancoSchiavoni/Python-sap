import cuenta_contrato as cc
import punto_suministro as ps
import ubicacion_aparto as ua
import instalacion as ins
import move_in as mi
import montaje as mon
import contrato_potencia as cp
import connector as s


import json_magnament as j
datos = j.read_json()

sap = s.SapConnector()

for row in input:
    # Objeto Cuenta Contrato
    CuentaContrato = cc.CuentaContrato(sap)
    cc_data = row.get('Create_CC', {})
    # Asigna los valores correspondientes a las variables de tu objeto CuentaContrato
    CuentaContrato.id = cc_data.get('id', '')
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
    CuentaContrato.sap = cc_data.get('sap', sap)
    CuentaContrato.reclamacion = cc_data.get('reclamacion', 'Z1')
    CuentaContrato.mail = cc_data.get('mail', 'MAIL')

    # Objeto Punto Suministro
    PuntoSuministro = ps.PuntoSuministro(sap)
    ps_data = row.get('Create_PS', {})
    # Asigna los valores correspondientes a las variables de tu objeto PuntoSuministro
    PuntoSuministro.id = ps_data.get('id', '')
    PuntoSuministro.trxCreatePS = ps_data.get('trxCreatePS', '/nES60')
    PuntoSuministro.trxUpdatePS = ps_data.get('trxUpdatePS', '/nES61')
    PuntoSuministro.clae = ps_data.get('clae', '')
    PuntoSuministro.sap = ps_data.get('sap', sap)

    # Objeto UbicacionAparato
    UbicacionAparato = ua.UbicacionAparato(sap)
    ua_data = row.get('Create_UA', {})
    # Asigna los valores correspondientes a las variables de tu objeto UbicacionAparato
    UbicacionAparato.id = ua_data.get('id', '')
    UbicacionAparato.trxCreateUA = ua_data.get('trxCreateUA', '/nES65')
    UbicacionAparato.trxUpdateUA = ua_data.get('trxUpdateUA', '/nES66')
    UbicacionAparato.sap = ua_data.get('sap', sap)
    UbicacionAparato.centro_empl = ua_data.get('centro_empl', '')
    UbicacionAparato.denominacion = ua_data.get('denominacion', '')

    # Objeto Instalacion
    Instalacion = ins.Instalacion(sap)
    ins_data = row.get('Create_INST', {})
    # Asigna los valores correspondientes a las variables de tu objeto Instalacion
    Instalacion.id = ins_data.get('id', '')
    Instalacion.trxCreateINS = ins_data.get('trxCreateINS', '/nES30')
    Instalacion.trxUpdateINS = ins_data.get('trxUpdateINS', '/nES31')
    Instalacion.sap = ins_data.get('sap', sap)
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
    Montaje.id = montaje_data.get('id', '')
    Montaje.trxCreateMON = montaje_data.get('trxCreateMON', '/nEG31')
    Montaje.sap = montaje_data.get('sap', sap)
    Montaje.f_alta = montaje_data.get('f_alta', '')
    Montaje.dipositivo = montaje_data.get('dipositivo', '')
    Montaje.tp_aparato = montaje_data.get('tp_aparato', '')
    Montaje.motivo = montaje_data.get('motivo', '')

    # Objeto ContratoPotencia
    ContratoPotencia = cp.ContratoPotencia(sap)
    cp_data = row.get('Create_CP', {})
    # Asigna los valores correspondientes a las variables de tu objeto ContratoPotencia
    ContratoPotencia.id = cp_data.get('id', '')
    ContratoPotencia.trxCP = cp_data.get('trxCP', '/nZDM_CONTRATOS_GC')
    ContratoPotencia.sap = cp_data.get('sap', sap)
    ContratoPotencia.fecha_ini = cp_data.get('fecha_ini', '')
    ContratoPotencia.periodo = cp_data.get('periodo', '00')
    ContratoPotencia.contratadaP = cp_data.get('contratadaP', '50')
    ContratoPotencia.contratadaFP = cp_data.get('contratadaFP', '50')
    ContratoPotencia.descripcion = cp_data.get('descripcion', '')

    ####################################################################################

    obj_data = row.get('OBJETOS', {})
    # #Cuenta Contrato
    CuentaContrato.StartCuentaContrato(obj_data.IC)
    CuentaContrato.SetDatosGenerales()
    CuentaContrato.SetPagosImpuestos()
    CuentaContrato.SetReclamacion()
    CuentaContrato.BuscaNroCC()
    print("CC: ", CuentaContrato.id)
    CuentaContrato.SetNroReferencia()

    # #Punto Suministro
    PuntoSuministro.CreatePS(obj_data.OC)
    PuntoSuministro.UpdatePS()
    print("PS: ",PuntoSuministro.id)

    # #Ubicacion de Aparato
    UbicacionAparato.CreateUA(PuntoSuministro.id, obj_data.OC)
    UbicacionAparato.UpdateUA()
    print("UA: ",UbicacionAparato.id)

    # #Instalacion
    Instalacion.StartInst()
    Instalacion.SetDatosIniciales(PuntoSuministro.id)
    Instalacion.CargaOperandos()
    Instalacion.GuardaInstalacion()
    print("INS ",UbicacionAparato.id)

    # #MoveIN
    Movein.StartContrato(PuntoSuministro.id, CuentaContrato.id, Instalacion.id)
    Movein.InitContrato()
    Movein.SetValoresContrato()
    Movein.GuardaContrato(Instalacion.id)

    # #Montaje
    Montaje.SetDatosGenerales(UbicacionAparato.id, Instalacion.id)
    Montaje.SetNumeradores()
    Montaje.Guardar()

    # #ContratoPotencia
    ContratoPotencia.InitContratoPotencia(obj_data.IC, CuentaContrato.id, Instalacion.id)
    ContratoPotencia.SetValoresCP()
    ContratoPotencia.GuardarCP()

sap.Close_connection()




