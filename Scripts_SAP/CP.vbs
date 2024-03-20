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
session.findById("wnd[0]/tbar[1]/btn[18]").press
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPARTNER").text = "200001277"
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZVKONT").text = "700011224"
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZANLAGE").text = "400002124"
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZFECHA_DESDE").text = "01.01.2023"
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").setFocus
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").caretPosition = 2
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]").close
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").text = "00"
session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_PIC").text = "50"
session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_FPIC").text = "50"
session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_FPIC").setFocus
session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_FPIC").caretPosition = 4
session.findById("wnd[0]/tbar[0]/btn[11]").press
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/btnBUTTON_1").press
session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").text = "ASD"
session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").caretPosition = 3
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[1]/usr/txtMESSTXT2").setFocus
session.findById("wnd[1]/usr/txtMESSTXT2").caretPosition = 9
session.findById("wnd[1]/tbar[0]/btn[0]").press
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").setFocus
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").caretPosition = 10
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]").close
session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").caretPosition = 8
