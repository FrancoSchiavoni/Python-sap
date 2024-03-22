# Import System
import os
import sys
from datetime import datetime

# Import Utils 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Utils', '')))
import connector as s

SAPtables = ["EQUI","EGERH"]
folderdir = "C:\\_tmp\\"

sap = s.SapConnector()
resultados = []


output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Outputs'))
print(output_folder)
now = datetime.now()
date_string = now.strftime("-%Y%m%d_%H%M%S")


# Ingresa Tabla

for table in SAPtables:
    sap.session.findById("wnd[0]/usr/ctxtGD-TAB").text = table
    sap.session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = "50"
    sap.session.findById("wnd[0]/usr/txtGD-MAX_LINES").setFocus()
    sap.session.findById("wnd[0]/usr/txtGD-MAX_LINES").caretPosition = 4
    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    sap.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
    sap.session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem("&XXL")
    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    sap.session.findById("wnd[1]/usr/ctxtDY_PATH").text = output_folder
    sap.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = table + date_string + ".XLSX"
    sap.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 5
    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()

connection = None
application = None
SapGuiAuto = None