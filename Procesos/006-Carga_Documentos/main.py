import pandas as pd
from openpyxl import load_workbook
import os
import sys
import datetime

# Ajusta las rutas según tu estructura de carpetas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Utils', '')))
import connector as s


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Clases', '')))
import documento as doc_class 

# Configuración del archivo de entrada
INPUT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Inputs', 'ajuste_seg_t4_202511_error.xlsx'))

SHEET_NAME = 'Hoja1'
STATUS_COL = 'estado'
MESSAGE_COL = 'mensaje'
DOC_SAP_COL = 'documento_sap' 

def cargar_datos():
    # Se leen las columnas como string para evitar problemas de formato
    df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME, engine='openpyxl', 
                       dtype={
                           "IC": str, 
                           "CC": str, 
                           "Contrato": str,
                           "Op. Pppal.": str,
                           "Op. Parcial": str,
                           "Clase Doc.": str
                       })
    if STATUS_COL not in df.columns:
        df[STATUS_COL] = ''
    if MESSAGE_COL not in df.columns:
        df[MESSAGE_COL] = ''
    if DOC_SAP_COL not in df.columns:
        df[DOC_SAP_COL] = ''

    # Validar fila por fila y marcar errores antes de procesar
    for index, row in df.iterrows():
        is_valid, message = validar_fila(row)
        if not is_valid:
            df.at[index, STATUS_COL] = 'ED'
            df.at[index, MESSAGE_COL] = message

    # Guardar resultados de la validación inicial
    guardar_estado(df)
    return df

def validar_fila(row):
    """
    - 'Clase Doc.' debe ser 'BC' o 'BD'
    - Si 'Clase Doc.' == 'BC' entonces 'Importe' debe ser negativo
    - Si 'Clase Doc.' == 'BD' entonces 'Importe' debe ser positivo
    - 'Op. Pppal.' no puede estar vacío
    - 'Op. Parcial' no puede estar vacío
    - 'Op. Pppal.' debe ser '6000'
    - Si 'Clase Doc.' == 'BD' entonces 'Op. Parcial' debe ser '3002'
    - Si 'Clase Doc.' == 'BC' entonces 'Op. Parcial' debe ser '3003'
    """
    mensajes = []
    
    # Validar clase de documento
    try:
        clase = str(row.get("Clase Doc.", "")).strip().upper()
    except:
        clase = ""

    if clase not in ("BC", "BD"):
        mensajes.append("Clase Doc. debe ser 'BC' o 'BD'")

    # Validar importe
    importe_raw = row.get("Importe", None)
    try:
        # convertir a float si es posible
        importe = float(importe_raw)
        if clase == "BC" and importe >= 0:
            mensajes.append("Para Clase Doc. 'BC' el Importe debe ser negativo")
        if clase == "BD" and importe <= 0:
            mensajes.append("Para Clase Doc. 'BD' el Importe debe ser positivo")
    except Exception:
        mensajes.append("Importe inválido o faltante")

    # Valida operaciones principales y parciales 
    if not str(row.get("Op. Pppal.", "")).strip():
        mensajes.append("Op. Pppal. no puede estar vacío")
    
    if not str(row.get("Op. Parcial", "")).strip():
        mensajes.append("Op. Parcial no puede estar vacío")
    
    # Valida operacion principal = 6000
    if str(row.get("Op. Pppal.", "")).strip() != "6000":
        mensajes.append("Op. Pppal. debe ser '6000'")
    
    # Valida si es BD, la operacion parcial = 3002
    if clase == "BD" and str(row.get("Op. Parcial", "")).strip() != "3002":
        mensajes.append("Para Clase Doc. 'BD', Op. Parcial debe ser '3002'")
    # Valida si es BC, la operacion parcial = 3003
    if clase == "BC" and str(row.get("Op. Parcial", "")).strip() != "3003":
        mensajes.append("Para Clase Doc. 'BC', Op. Parcial debe ser '3003'")

    if mensajes:
        return False, "; ".join(mensajes)
    return True, ""

def crear_documento(row, sap):
    documento = doc_class.DocumentoFica(sap)
    
    documento.cargar_datos_cabecera(
        clase_doc=row["Clase Doc."],       
        moneda="ARS",                     
        lugar_comercial="0069",           
        fecha_contabilizacion=datetime.datetime.now()
    )

    documento.cargar_datos_posicion(
        socio_comercial=row["IC"], 
        sociedad="1000",                        
        cuenta_contrato=row["CC"], 
        op_princ=row["Op. Pppal."],               
        op_parc=row["Op. Parcial"],                 
        importe=row["Importe"],                 
        contrato=row["Contrato"]                
    )
    
    return documento

def procesar_item(sap, documento: doc_class.DocumentoFica):
    try:

        print(f"Procesando contrato: {documento.contrato}")
        documento.InitTransaccion()
        documento.CompletarPosiciones()
        documento.AjustarImporteConImpuestos()
        documento.Guardar()

        message = str(sap.session.findById("wnd[0]/sbar").Text)
        message_type = str(sap.session.findById("wnd[0]/sbar").MessageType)

        return message_type, message

    except Exception as e:
        # Manejo de errores genérico
        try:
            message_error = str(sap.session.findById("wnd[0]/sbar").Text)
            message_type  = str(sap.session.findById("wnd[0]/sbar").MessageType)
        except:
            message_error = str(e)
            message_type = 'E'
        return message_type, message_error, ""

def guardar_estado(df):
    with pd.ExcelWriter(INPUT_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=SHEET_NAME, index=False)

def main():
    df = cargar_datos()
    sap = s.SapConnector()
    
    for index, row in df.iterrows():
        print("-----------")
        print(f"Indice: {index}")
        
        if row[STATUS_COL] in ['S', 'ED']:
            continue
            
        documento = crear_documento(row, sap)
        
        if hasattr(documento, 'trx_code'):
            sap.StartTransaction(documento.trx_code)
        else:
            sap.StartTransaction("FPE1")

        estado, mensaje = procesar_item(sap, documento)
        
        # Actualizamos DataFrame
        df.at[index, STATUS_COL] = estado
        df.at[index, MESSAGE_COL] = mensaje
            
        print(f"{estado}: {mensaje}")
        guardar_estado(df)
        
    print("Proceso finalizado.")

if __name__ == '__main__':
    main()