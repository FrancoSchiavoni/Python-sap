import os
import shutil
import glob

class Lecturas:
  
  def __init__(self,sap):
    self.id = ""
    self.sap = sap
    self.ins = ""
    self.cc = ""
    self.tipo_cliente = ""
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
    self.doc_impresion = ""
  
  def CreaOrdenLectura(self):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL01-ANLAGE").text = self.ins
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
    
  def CargaLecturasGD(self, mdt):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL28D-ANLAGE").text = self.ins
    self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = self.lectura_E_act_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = self.lectura_Pot_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = self.lectura_E_act_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = self.lectura_Pot_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = self.lectura_E_act_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = self.lectura_Pot_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = self.lectura_E_act_R
    self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    if mdt == "398":
      self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").caretPosition = 1
      self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

  def CargaLecturasCOOP(self):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL28D-ANLAGE").text = self.ins
    self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text  = self.lectura_Pot_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text  = self.lectura_Pot_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text  = self.lectura_E_react
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text  = self.lectura_E_act_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text  = self.lectura_E_act_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text  = self.lectura_E_act_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text  = self.lectura_E_act_P2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,7]").text  = self.lectura_E_act_R2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,8]").text  = self.lectura_E_act_V2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,9]").text  = self.lectura_E_act_P3
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").text = self.lectura_E_act_R3
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,11]").text = self.lectura_E_act_V3
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,12]").text = self.lectura_E_act_P4
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,13]").text = self.lectura_E_act_R4
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,14]").text = self.lectura_E_act_V4
    self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
  
  def CargaLecturasPROSU(self,mdt):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL28D-ANLAGE").text = self.ins
    self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = self.lectura_E_act_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = self.lectura_Pot_R
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = self.lectura_E_act_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = self.lectura_Pot_P
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = self.lectura_E_act_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = self.lectura_Pot_V
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = self.lectura_E_react
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,7]").text = self.lectura_E_act_R2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,8]").text = self.lectura_Pot_R2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,9]").text = self.lectura_E_act_P2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").text = self.lectura_Pot_P2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,11]").text = self.lectura_E_act_V2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,12]").text = self.lectura_Pot_V2
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,15]").text = self.lectura_E_act_P3
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,16]").text = self.lectura_E_act_R3
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,14]").text = self.lectura_E_act_V3
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,14]").setFocus()
    self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,14]").caretPosition = 3
    self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    if mdt == "398":
      self.sap.session.findById("wnd[0]").sendVKey(0)
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = "0"
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").setFocus()
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").caretPosition = 1
      self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

  
  def GeneraCalculo(self):
    self.sap.session.findById("wnd[0]/usr/radEBISID-ANLAGERAD").select()
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ANLAGE").text = self.ins
    self.sap.session.findById("wnd[0]/usr/radEBISID-BITRIGRAD").select()
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").text = self.fecha_Calculo
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").setFocus()
    self.sap.session.findById("wnd[0]/usr/ctxtEBISID-ABRDATS").caretPosition = 10
    self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()


  def DescargarFactura(self, path_destino):
    self.sap.session.findById("wnd[1]/tbar[0]/btn[18]").press()
    self.doc_impresion = self.sap.session.findById("wnd[0]/usr/tabsTAB_PRINTDOC/tabpCMD_HEAD/ssubSUB_PRINTDOC:SAPLE22A:0501/ctxtERDK-OPBEL").text
    self.sap.session.findById("wnd[0]/tbar[1]/btn[24]").press()
    self.sap.session.findById("wnd[1]/usr/ctxtSSFPP-TDDEST").text = "locl"
    self.sap.session.findById("wnd[1]/usr/ctxtSSFPP-TDDEST").caretPosition = 4
    self.sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "PDF!"
    self.sap.session.findById("wnd[0]").sendVKey(0)

    carpeta_temporal = os.path.join(os.getenv('LOCALAPPDATA'), 'Temp')
    print(carpeta_temporal)
    
    patron_pdf = os.path.join(carpeta_temporal, '*smart*.pdf')
    archivos_pdf = glob.glob(patron_pdf)

    if archivos_pdf:
      ruta_pdf = archivos_pdf[0]
      carpeta_destino = path_destino
      nuevo_nombre = self.ins + "_" + self.doc_impresion + ".pdf"
      ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
      shutil.copy(ruta_pdf, ruta_destino)
      print("PDF movido exitosamente a la carpeta de destino.")
    else:
      print("No se encontraron archivos PDF en la carpeta temporal.")

    self.sap.session.findById("wnd[1]").close()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
    self.sap.session.findById("wnd[1]").close()



  def GenerarFactura(self, descargar, path_destino):
    self.sap.session.findById("wnd[0]/usr/ctxtBUDAT").text = self.fecha_Calculo
    self.sap.session.findById("wnd[0]/usr/ctxtFIKEY").text = self.clave_rec 
    self.sap.session.findById("wnd[0]/usr/ctxtVKONT").text = self.cc
    self.sap.session.findById("wnd[0]/usr/ctxtVKONT").setFocus()
    self.sap.session.findById("wnd[0]/usr/ctxtVKONT").caretPosition = 9
    self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    #self.sap.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
    self.doc_calculo = self.sap.session.findById("wnd[1]/usr/lbl[24,1]").text
    self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    if descargar:
      self.DescargarFactura(path_destino)
    else:
      self.sap.session.findById("wnd[1]/tbar[0]/btn[18]").press()
      self.doc_impresion = self.sap.session.findById("wnd[0]/usr/tabsTAB_PRINTDOC/tabpCMD_HEAD/ssubSUB_PRINTDOC:SAPLE22A:0501/ctxtERDK-OPBEL").text
      self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
      self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()