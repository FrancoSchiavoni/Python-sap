class Lecturas:
  
  def __init__(self,sap):
    self.id = ""
    self.sap = sap
    self.trxCreateOrd = "/nEL01"
    self.motivo_Lectura = "01"
    self.fecha_Ord_Lectura_Desde = "31.01.2023"
    self.fecha_Ord_Lectura_Hasta = ""
    self.trxCargaLecturas = "/nEL28"
    self.lectura_Pot_P   = "1000"
    self.lectura_Pot_R   = "150"
    self.lectura_Pot_V   = "350"
    self.lectura_E_act_P = "2500"
    self.lectura_E_act_R = "2000"
    self.lectura_E_act_V = "3000"
    self.lectura_Pot_P2   = ""
    self.lectura_Pot_R2   = ""
    self.lectura_Pot_V2   = ""
    self.lectura_E_act_P2 = ""
    self.lectura_E_act_R2 = ""
    self.lectura_E_act_V2 = ""
    self.lectura_E_act_P3 = ""
    self.lectura_E_act_R3 = ""
    self.lectura_E_act_V3 = ""
    self.lectura_E_act_P4 = ""
    self.lectura_E_act_R4 = ""
    self.lectura_E_act_V4 = ""
    self.lectura_E_react = "7500"
    self.trxCalculo = "/nEA00"
    self.fecha_Calculo = "10.02.2023"
    self.trxFactura = "/nEA19"
    self.clave_rec = "240321-001"
    self.doc_calculo = ""
  
  def CreaOrdenLectura(self,INS):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL01-ANLAGE").text = INS
    self.sap.session.findById("wnd[0]/usr/ctxtREL01-ABLESGR").text = self.motivo_Lectura
    self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    self.sap.session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").firstVisibleRow = 12
    self.sap.session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").pressToolbarButton("&MB_FILTER")
    self.sap.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").currentCellRow = 3
    self.sap.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/cntlCONTAINER1_FILT/shellcont/shell").selectedRows = "3"
    self.sap.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btnAPP_WL_SING").press()
    self.sap.session.findById("wnd[1]/usr/subSUB_DYN0500:SAPLSKBH:0600/btn600_BUTTON").press()
    self.sap.session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").text = self.fecha_Ord_Lectura_Desde
    self.sap.session.findById("wnd[2]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN001-LOW").caretPosition = 10
    self.sap.session.findById("wnd[2]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").currentCellColumn = "ADATSOLL"
    self.sap.session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").selectedRows = "0"
    self.sap.session.findById("wnd[0]/usr/cntlD0100_CONTAINER/shellcont/shell").clickCurrentCell()
    self.sap.session.findById("wnd[0]/tbar[1]/btn[19]").press()
    
  def CargaLecturas(self,INS):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL28D-ANLAGE").text = INS
    self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = self.lectura_E_act_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = self.lectura_Pot_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = self.lectura_E_act_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = self.lectura_Pot_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = self.lectura_E_act_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = self.lectura_Pot_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = self.lectura_E_act_R
    self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").caretPosition = 1
    self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
  
  def GeneraCalculo(self,INS):
    self.sap.session.findById("wnd[0]/usr/radEBISID-ANLAGERAD").select()
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ANLAGE").text = INS
    self.sap.session.findById("wnd[0]/usr/radEBISID-BITRIGRAD").select()
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").text = self.fecha_Calculo
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").setFocus()
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").caretPosition = 10
    self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()


  def DescargarFactura(self):
    self.sap.session.findById("wnd[1]/tbar[0]/btn[18]").press()
    self.sap.session.findById("wnd[0]/tbar[1]/btn[24]").press()
    self.sap.session.findById("wnd[1]/usr/ctxtSSFPP-TDDEST").text = "locl"
    self.sap.session.findById("wnd[1]/usr/ctxtSSFPP-TDDEST").caretPosition = 4
    self.sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[86]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
    self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()


  def GenerarFactura(self, CC, descargar):
    self.sap.session.findById("wnd[0]/usr/ctxtBUDAT").text = self.fecha_Calculo
    self.sap.session.findById("wnd[0]/usr/ctxtFIKEY").text = self.clave_rec 
    self.sap.session.findById("wnd[0]/usr/ctxtVKONT").text = CC
    self.sap.session.findById("wnd[0]/usr/ctxtVKONT").setFocus()
    self.sap.session.findById("wnd[0]/usr/ctxtVKONT").caretPosition = 9
    self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    #self.sap.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
    self.doc_calculo = self.sap.session.findById("wnd[1]/usr/lbl[24,1]").text
    self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    if descargar:
      self.DescargarFactura()
    else:
      self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()