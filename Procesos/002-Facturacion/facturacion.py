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
import lecturas as l

#Input
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Inputs', 'facturacion.json'))
datos = j.read_json(json_path)

#Conexion con SAP
sap = s.SapConnector()

#Crea Objeto Lecturas
Lecturas = l.Lecturas(sap)

CC = "700011253"
INS = "400002144"

#Crear Orden de Lectura
#sap.StartTransaction(Lecturas.trxCreateOrd)
#Lecturas.CreaOrdenLectura(INS)

#Carga Lecturas
#sap.StartTransaction(Lecturas.trxCargaLecturas)
#Lecturas.CargaLecturas(INS)

#Generar Calculo
#sap.StartTransaction(Lecturas.trxCalculo)
#Lecturas.GeneraCalculo(INS)

#Generar Facturas
#sap.StartTransaction(Lecturas.trxFactura)
#Lecturas.GenerarFactura(CC)