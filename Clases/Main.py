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

    #Cuenta Contrato
    CuentaContrato = cc.CuentaContrato()
    CuentaContrato.StartCuentaContrato()
    CuentaContrato.SetDatosGenerales()
    CuentaContrato.SetPagosImpuestos()
    CuentaContrato.SetReclamacion()
    CuentaContrato.BuscaNroCC()
    print("CC: ", CuentaContrato.id)
    CuentaContrato.SetNroReferencia()

    #Punto Suministro
    PuntoSuministro = ps.PuntoSuministro()
    PuntoSuministro.CreatePS()
    PuntoSuministro.UpdatePS()
    print("PS: ",PuntoSuministro.id)

    #Ubicacion de Aparato
    UbicacionAparato = ua.UbicacionAparato()
    UbicacionAparato.CreateUA()
    UbicacionAparato.UpdateUA()
    print("UA: ",UbicacionAparato.id)

    #Instalacion
    Instalacion = ins.Instalacion()
    Instalacion.StartInst()
    Instalacion.SetDatosIniciales()
    Instalacion.CargaOperandos()
    Instalacion.GuardaInstalacion()
    print("INS ",UbicacionAparato.id)

    #MoveIN
    MoveIn = mi.Movein()
    MoveIn.StartContrato()
    MoveIn.InitContrato()
    MoveIn.SetValoresContrato()
    MoveIn.GuardaContrato()

    #Montaje
    Montaje = mon.Montaje()
    Montaje.SetDatosGenerales()
    Montaje.SetNumeradores()
    Montaje.Guardar()

    #ContratoPotencia
    ContratoPotencia = cp.ContratoPotencia()
    ContratoPotencia.InitContratoPotencia()
    ContratoPotencia.SetValoresCP()
    ContratoPotencia.GuardarCP()

sap.Close_connection()




