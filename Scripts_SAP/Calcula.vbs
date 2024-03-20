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
session.findById("wnd[0]/usr/radEBISID-ANLAGERAD").select
session.findById("wnd[0]/usr/radEBISID-BITRIGRAD").select
session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").text = "10.02.2022"
session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").setFocus
session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").caretPosition = 10
session.findById("wnd[0]/tbar[1]/btn[8]").press
