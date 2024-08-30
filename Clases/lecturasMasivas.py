import os
import shutil
import glob

class LecturasMasivas:
  
  def __init__(self,sap):
    self.id = ""
    self.sap = sap
    self.ins = ""
    self.tipo_cliente = ""
    self.motivo_Lectura = "01"
    self.fecha_Ord_Lectura_Desde = ""
    self.trxCargaLecturas = "/nEL28"
    self.lectura_Pot_P   = []
    self.lectura_Pot_R   = []
    self.lectura_Pot_V   = []
    self.lectura_E_act_P = []
    self.lectura_E_act_R = []
    self.lectura_E_act_V = []
    self.lectura_E_act_P2 = []
    self.lectura_E_act_R2 = []
    self.lectura_E_act_V2 = []
    self.lectura_E_act_P3 = []
    self.lectura_E_act_R3 = []
    self.lectura_E_act_V3 = []
    self.lectura_E_act_P4 = []
    self.lectura_E_act_R4 = []
    self.lectura_E_act_V4 = []
    self.lectura_E_react = []