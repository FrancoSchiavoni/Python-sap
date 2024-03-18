class UbicacionAparato:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCreateUA = "/nES65"
        self.trxUpdateUA = "/nES66"
        self.sap = sap
        self.centro_empl = ""
        self.denominacion = ""

    def CreateUA(self, PS, OC):
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.sap.session.findById("wnd[0]/usr/txtEGPLD-PLTXT").text = self.denominacion
        self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-HAUS").text = OC
        self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-SWERK").text = self.centro_empl
        self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-VSTELLE").text = PS
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    def UpdatePS(self):
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = self.trxUpdateUA
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-DEVLOC").text
        print("Ubicacion de aparato: " ,self.id)
       

    
