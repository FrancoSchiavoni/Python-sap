class PuntoSuministro:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCreatePS = "/nES60"
        self.trxUpdatePS = "/nES61"
        self.clae = ""
        self.sap = sap

    def CreatePS(self, OC):
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-HAUS").text = OC
        self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-VBSART").text = self.clae
        self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-VBSART").caretPosition = 6
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    def UpdatePS(self):
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "/nES61"
        self.sap.session.findById("wnd[0]").sendVKey (0)
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-VSTELLE").text


    
