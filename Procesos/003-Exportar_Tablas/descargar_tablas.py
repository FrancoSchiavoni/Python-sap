# Import System
import os
import sys
from datetime import datetime
# Import Utils 
import params
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.UTILS_STR, '')))
import connector as s
import json_management as j
#Input File
json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS , params.INPUTS_STR, params.DESCARGAR_TABLAS_STR_LC + params.JSON_EXT))
datos = j.read_json(json_path)
#Output Folder 
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), params.BACK_TWO_FOLDERS, params.OUTPUTS_STR, params.DESCARGAR_TABLAS_STR_LC))
#DateTime 
now = datetime.now()
date_string = now.strftime("-%Y%m%d_%H%M%S")

class FilterInput:
    def __init__(self, table_name, filters, rows):
        self.table_name = table_name
        self.filters = filters
        self.maxrows = rows

sap = s.SapConnector()

def aplicar_filtro(column, value):
    sap.session.findById("wnd[0]/usr/ctxtGD_ADD_COLUMN").text = column
    sap.session.findById("wnd[0]/usr/ctxtGD_ADD_COLUMN").setFocus()
    sap.session.findById("wnd[0]/usr/ctxtGD_ADD_COLUMN").caretPosition = 8
    sap.session.findById("wnd[0]").sendVKey(0)
    sap.session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,1]").text = value
    sap.session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,1]").setFocus()
    sap.session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/ctxtGS_SELFIELDS-LOW[2,1]").caretPosition = 2
    sap.session.findById("wnd[0]").sendVKey(0)

sap.crear_transaccion("/nSE16N")

for table_data in datos["tables"]:
    input_data = FilterInput(table_data["name"], table_data["filters"], table_data["maxrows"])
    sap.session.findById("wnd[0]/usr/ctxtGD-TAB").text = input_data.table_name
    sap.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = input_data.maxrows
    sap.session.findById("wnd[0]/usr/txtGD-MAX_LINES").setFocus()
    sap.session.findById("wnd[0]/usr/txtGD-MAX_LINES").caretPosition = 4
    sap.session.findById("wnd[0]").sendVKey(0)

    for column, filter_range in input_data.filters.items():
        aplicar_filtro(column, filter_range[0])
    
    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    sap.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
    sap.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem("&XXL")
    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    sap.session.findById("wnd[1]/usr/ctxtDY_PATH").text = output_folder
    sap.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = input_data.table_name + date_string + ".XLSX"
    sap.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 5
    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()

sap.crear_transaccion("/n")
connection = None
application = None
SapGuiAuto = None