class Instalacion:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCreateINS = "/nES30"
        self.trxUpdateINS = "/nES31"
        self.sap = sap
        self.dia_fijado = ""
        self.sector = ""
        self.nivTension = ""
        self.clCal = ""
        self.tp_tarifa = ""
        self.unidad_lectura = ""

    def StartInst(self):
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-STICHTAG").text = self.dia_fijado
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-SPARTE").text = self.sector
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-SPARTE").setFocus
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-SPARTE").caretPosition = 2
        self.sap.session.findById("wnd[0]").sendVKey(0)

    def SetDatosIniciales(self,PS):
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-VSTELLE").text = PS
        self.sap.session.findById("wnd[0]/usr/tblSAPLES30TC_TIMESL/ctxtEANLD-AKLASSE[2,0]").text = self.clCal
        self.sap.session.findById("wnd[0]/usr/tblSAPLES30TC_TIMESL/ctxtEANLD-TARIFTYP[3,0]").text = self.tp_tarifa
        self.sap.session.findById("wnd[0]/usr/tblSAPLES30TC_TIMESL/ctxtEANLD-ABLEINH[9,0]").text = self.unidad_lectura
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-SPEBENE").text = self.nivTension
        self.sap.session.findById("wnd[0]/usr/tblSAPLES30TC_TIMESL/ctxtEANLD-ABLEINH[9,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLES30TC_TIMESL/ctxtEANLD-ABLEINH[9,0]").caretPosition = 5
        self.sap.session.findById("wnd[0]").sendVKey(0)

    def elemento_presente(self,id_elemento):
        try:
            self.sap.session.findById(id_elemento)
            return True
        except:
            return False
        

    def carga_operando_rate(self, operando, hasta, tarifa, tension):
        if not self.elemento_presente("wnd[1]/usr/ctxtRE20B-OPERAND"):
            self.sap.session.findById("wnd[0]/tbar[1]/btn[18]").press()
        self.sap.session.findById("wnd[1]/usr/ctxtRE20B-OPERAND").text = operando
        self.sap.session.findById("wnd[1]/usr/ctxtRE20B-OPERAND").caretPosition = 10
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CRTYPE_TC/ctxtRE20CL-BIS[1,0]").text = hasta
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CRTYPE_TC/ctxtRE20CL-TARIFART[2,0]").text = tarifa
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CRTYPE_TC/ctxtRE20CL-KONDIGR[3,0]").text = tension
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CRTYPE_TC/ctxtRE20CL-KONDIGR[3,0]").setFocus()
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CRTYPE_TC/ctxtRE20CL-KONDIGR[3,0]").caretPosition = 4
        self.sap.session.findById("wnd[1]/tbar[0]/btn[5]").press()

    def carga_flag(self, operando, hasta):
        if not self.elemento_presente("wnd[1]/usr/ctxtRE20B-OPERAND"):
            self.sap.session.findById("wnd[0]/tbar[1]/btn[18]").press()
        self.sap.session.findById("wnd[1]/usr/ctxtRE20B-OPERAND").text = operando
        self.sap.session.findById("wnd[1]/usr/ctxtRE20B-OPERAND").caretPosition = 9
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CFLAG_TC/ctxtRE20CL-BIS[1,0]").text = hasta
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CFLAG_TC/chkRE20CL-BOOLKZ[2,0]").setFocus()
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CFLAG_TC/chkRE20CL-BOOLKZ[2,0]").selected = True
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CFLAG_TC/ctxtRE20CL-BIS[1,0]").caretPosition = 10
        self.sap.session.findById("wnd[1]/tbar[0]/btn[5]").press()
    
    def carga_quant(self, operando, hasta,cantidad):
        if not self.elemento_presente("wnd[1]/usr/ctxtRE20B-OPERAND"):
            self.sap.session.findById("wnd[0]/tbar[1]/btn[18]").press()
        self.sap.session.findById("wnd[1]/usr/ctxtRE20B-OPERAND").text = operando
        self.sap.session.findById("wnd[1]/usr/ctxtRE20B-OPERAND").caretPosition = 9
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CQUANT_TC/ctxtRE20CL-BIS[1,0]").text = hasta
        self.sap.session.findById("wnd[1]/usr/tblSAPLE20CQUANT_TC/txtRE20CL-MENGE[2,0]").text = cantidad
        self.sap.session.findById("wnd[1]/tbar[0]/btn[5]").press()

    
    def CargaOperandos(self, datosOperandos):
        self.sap.session.findById("wnd[0]/usr/btnEANLD-FACTSBUT").press() 
        for key, value in datosOperandos.items():
            if value["carga"]:
                if value["tipo"] == "RATE":
                    self.carga_operando_rate(key, value["f_hasta"], value["clase tarifa"], value['grValoresConcretos'])
                if value["tipo"] == "FLAG":
                    self.carga_flag(key,value['hasta'])
                if value["tipo"] == "QUANT":
                    self.carga_quant(key,value['hasta'], value['cantidad'])


        #Guarda Operandos
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()

    def GuardaInstalacion(self):
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "/nes32"
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtEANLD-ANLAGE").text
