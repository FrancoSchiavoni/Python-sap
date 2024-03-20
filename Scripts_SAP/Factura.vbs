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
session.findById("wnd[0]/usr/ctxtBLDAT").text = "10.02.2022"
session.findById("wnd[0]/usr/ctxtBUDAT").text = "10.02.2022"
session.findById("wnd[0]/usr/ctxtVKONT").text = "700011241"
session.findById("wnd[0]/usr/ctxtVKONT").setFocus
session.findById("wnd[0]/usr/ctxtVKONT").caretPosition = 9
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[1]/usr/btnSPOP-OPTION1").press
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/tbar[0]/btn[0]").press
