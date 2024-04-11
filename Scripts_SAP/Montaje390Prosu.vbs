If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If
session.findById("wnd[0]").maximize
session.findById("wnd[0]/usr/ctxtREG30-HAUS").text = "610000000000164"
session.findById("wnd[0]/usr/ctxtREG30-DEVLOC").text = "650000000000193"
session.findById("wnd[0]/usr/ctxtREG30-ANLAGE").text = "400000161"
session.findById("wnd[0]/usr/ctxtREG30-EADAT").text = "01.02.2022"
session.findById("wnd[0]/usr/ctxtREG30-GERAETNEU").text = "101"
session.findById("wnd[0]/usr/ctxtREG30-MATNR").text = "700034"
session.findById("wnd[0]/usr/ctxtREG30-MATNR").setFocus
session.findById("wnd[0]/usr/ctxtREG30-MATNR").caretPosition = 6
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtREG30-GERWECHS").text = "05"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").text = "ENACTRE"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,1]").text = "CAPFP"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,2]").text = "ENACTP"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,3]").text = "CAPPI"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,4]").text = "ENACTV"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,5]").text = "CAPVA"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,6]").text = "ENREACT"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,7]").text = "ENACTR_R"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,8]").text = "CAPFP_R"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,1]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,2]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,3]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,4]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,5]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,6]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,7]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,8]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").setFocus
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").caretPosition = 0
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 3
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,6]").text = "ENACTP_R"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,7]").text = "CAPPI_R"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,8]").text = "ENACTV_R"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,6]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,7]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,8]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 6
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,5]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,6]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,6]").text = "CAPVA_R"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,6]").text = "GENERALES"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").setFocus
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").caretPosition = 1
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,3]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").setFocus
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").caretPosition = 1
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").caretPosition = 1
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 2
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 0
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus
session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
session.findById("wnd[0]/tbar[1]/btn[32]").press
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,7]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,8]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,9]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,11]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,12]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,12]").setFocus
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,12]").caretPosition = 1
session.findById("wnd[0]/tbar[0]/btn[3]").press
session.findById("wnd[0]/tbar[0]/btn[11]").press
