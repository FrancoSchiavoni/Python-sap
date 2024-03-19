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
session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select
session.findById("wnd[0]/tbar[0]/btn[0]").press
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "2000"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = "150"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = "2500"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = "1000"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = "3000"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = "350"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = "7500"
session.findById("wnd[0]/tbar[0]/btn[11]").press
session.findById("wnd[0]/tbar[0]/btn[0]").press
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").caretPosition = 1
session.findById("wnd[0]/tbar[0]/btn[11]").press
