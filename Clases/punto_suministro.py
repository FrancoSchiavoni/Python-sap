class PuntoSuministro:
        
    def __init__(self, sap):
        self.id = ""
        self.trx_create_ps = "/nES60"
        self.trx_update_ps = "/nES61"
        self.clae = ""
        self.sap = sap

    def crear_ps(self, oc):
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-HAUS").text = oc
        self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-VBSART").text = self.clae
        self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-VBSART").caretPosition = 6
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    def update_ps(self):
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "/nES61"
        self.sap.session.findById("wnd[0]").sendVKey (0)
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtEVBSD-VSTELLE").text