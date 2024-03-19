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
session.findById("wnd[0]/usr/cntlIMAGE_CONTAINER/shellcont/shell/shellcont[0]/shell").doubleClickNode "F00068"
session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select
session.findById("wnd[0]/usr/ctxtREL01-ANLAGE").text = "400002133"
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]").sendVKey 2
session.findById("wnd[0]/usr/ctxtREL01-ABLESGR").text = "01"
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").firstVisibleRow = 12
session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").pressToolbarButton "&MB_FILTER"
session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").currentCellRow = 3
session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").selectedRows = "3"
session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press
session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btn600_BUTTON").press
session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = "31.01.2022"
session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 10
session.findById("wnd[2]/tbar[0]/btn[0]").press
session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").currentCellColumn = "ADATSOLL"
session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").selectedRows = "0"
session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").clickCurrentCell
session.findById("wnd[0]/tbar[1]/btn[19]").press
