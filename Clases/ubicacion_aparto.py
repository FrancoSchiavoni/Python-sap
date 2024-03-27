class UbicacionAparato:
        
    def __init__(self, sap):
        self.id = ""
        self.trx_create_ua = "/nES65"
        self.trx_update_ua = "/nES66"
        self.sap = sap
        self.centro_empl = ""
        self.denominacion = ""

    def crear_ua(self, ps, oc, denominacion_auxiliar):
        self.sap.session.findById("wnd[0]").sendVKey(0)
        if len(denominacion_auxiliar) == 0:
            self.sap.session.findById("wnd[0]/usr/txtEGPLD-PLTXT").text = self.denominacion
        else:
            self.sap.session.findById("wnd[0]/usr/txtEGPLD-PLTXT").text = denominacion_auxiliar
        self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-HAUS").text = oc
        self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-SWERK").text = self.centro_empl
        self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-VSTELLE").text = ps
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    def update_ua(self):
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = self.trx_update_ua
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtEGPLD-DEVLOC").text