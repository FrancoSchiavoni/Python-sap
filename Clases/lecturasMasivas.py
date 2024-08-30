class LecturasMasivas:
  
  def __init__(self,sap):
    self.id = ""
    self.sap = sap
    self.ins = ""
    self.tipo_cliente = ""
    self.motivo_Lectura = "01"
    self.fecha_Ord_Lectura_Desde = ""
    self.trxCargaLecturas = "/nEL28"
    self.lectura_Pot_P   = [1,1,1,1,1,1,1,1,1,1,1,1]
    self.lectura_Pot_R   = [1,1,1,1,1,1,1,1,1,1,1,1]
    self.lectura_Pot_V   = [1,1,1,1,1,1,1,1,1,1,1,1]
    self.lectura_E_act_P = [1,1,1,1,1,1,1,1,1,1,1,1]
    self.lectura_E_act_R = [1,1,1,1,1,1,1,1,1,1,1,1]
    self.lectura_E_act_V = [1,1,1,1,1,1,1,1,1,1,1,1]
    self.lectura_E_act_P2 = []
    self.lectura_E_act_R2 = []
    self.lectura_E_act_V2 = []
    self.lectura_E_act_P3 = []
    self.lectura_E_act_R3 = []
    self.lectura_E_act_V3 = []
    self.lectura_E_act_P4 = []
    self.lectura_E_act_R4 = []
    self.lectura_E_act_V4 = []
    self.lectura_E_react = [1,1,1,1,1,1,1,1,1,1,1,1]

  def CargaLecturasGD(self, mdt):
    self.sap.session.findById("wnd[0]/usr/radRELX1-ANLAGE_T").select()
    self.sap.session.findById("wnd[0]/usr/ctxtREL28D-ANLAGE").text = self.ins
    self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
    self.sap.session.findById("wnd[1]/tbar[0]/btn[5]").press()
    self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()

    for mes in range(12):
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = self.lectura_E_act_R[mes]
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = self.lectura_Pot_R[mes]
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = self.lectura_E_act_P[mes]
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = self.lectura_Pot_P[mes]
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = self.lectura_E_act_V[mes]
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = self.lectura_Pot_V[mes]
      self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = self.lectura_E_react[mes]
      self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()