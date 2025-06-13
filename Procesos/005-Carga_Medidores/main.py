import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Utils', '')))
import connector as s

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Clases', '')))
import aparato as ap
date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

INPUT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Inputs', 'medidores_input.xlsx'))

SHEET_NAME = 'input'
STATUS_COL = 'estado'
MESSAGE_COL = 'mensaje'

def cargar_datos():
    df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME, engine='openpyxl', dtype={"tipo_stock": str, "relev_verific": str})
    if STATUS_COL not in df.columns:
        df[STATUS_COL] = ''
    if MESSAGE_COL not in df.columns:
        df[MESSAGE_COL] = ''
    return df

def crear_aparato(row, sap):
    aparato = ap.Aparato(sap, row["nro_de_serie"], row["material"])
    
    aparato.cargar_datos_medidor(
        tipo=row["tipo"],
        fabricante=row["fabricante"],
        anio_constr=row["año_constr"],
        valido_de=row["valido_de"],
        grupo_numerador=row["gr_numerador"],
        relev_verific=str(row["relev_verific"]),
        tipo_stock=str(row["tipo_stock"]),
        centro=row["centro"],
        almacen=row["almacen"],
        nro_activo_fijo=row["nro_activo_fijo"]
    )
    
    return aparato

def procesar_item(sap,aparato: ap.Aparato):
    try:
        print(f"Procesando medidor: {aparato.id}")
        aparato.InitCreacion()
        aparato.DetalleCreacion()
        aparato.DatosSerie()
        aparato.Guardar()
        message = str(sap.session.findById("wnd[0]/sbar").Text)
        message_type = str(sap.session.findById("wnd[0]/sbar").MessageType)
        return message_type, message
    except Exception as e:
        message_error = str(sap.session.findById("wnd[0]/sbar").Text)
        message_type  = str(sap.session.findById("wnd[0]/sbar").MessageType)
        return message_type, message_error

def guardar_estado(df):
    with pd.ExcelWriter(INPUT_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=SHEET_NAME, index=False)

def main():
    df = cargar_datos()
    sap = s.SapConnector()

    for idx, row in df.iterrows():
        if row[STATUS_COL] in ['S']:
            continue
        aparato: ap.Aparato = crear_aparato(row, sap)
        sap.StartTransaction(aparato.trxCreateAparato)
        estado, mensaje = procesar_item(sap, aparato)
        df.at[idx, STATUS_COL] = estado
        df.at[idx, MESSAGE_COL] = mensaje

        guardar_estado(df)

    print("Proceso finalizado.")

if __name__ == '__main__':
    main()
