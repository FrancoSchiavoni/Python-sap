class Movein:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCreateMovein = "/nEC50E"
        self.f_alta = ""
        self.imputacion = ""
        self.segmento = ""
        self.cdc = ""        
        self.fac_conj = ""

    def StartContrato(self, PS, CC, INS):
        self.sap.session.findById("wnd[0]/usr/subMIMOTABSTRIP:SAPLEC60:1120/subMIKOPF:SAPLEC60:1002/ctxtEUMZDKOPF-EINZDAT").text = self.f_alta
        self.sap.session.findById("wnd[0]/usr/subMIMOTABSTRIP:SAPLEC60:1120/subMIGP:SAPLEC60:1121/ctxtEUMZDMIBP-VKONT").text = CC
        self.sap.session.findById("wnd[0]/usr/subMIMOTABSTRIP:SAPLEC60:1120/subMIVS:SAPLEC60:1118/subVBST:SAPLEC60:1122/ctxtEUMZDMIVBS-VSTELLE").text = PS
        self.sap.session.findById("wnd[0]/usr/subMIMOTABSTRIP:SAPLEC60:1120/subMIVS:SAPLEC60:1118/subVBST:SAPLEC60:1122/ctxtEUMZDMIVBS-ANLAGE").text = INS


    def InitContrato(self):
        self.sap.session.findById("wnd[0]/usr/subMIMOTABSTRIP:SAPLEC60:1120/subMIKOPF:SAPLEC60:1002/ctxtEUMZDKOPF-EINZDAT").caretPosition = 10
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()


    def SetValoresContrato(self):
        self.sap.session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB05").select()
        self.sap.session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB05/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLEC50_CONTR:0100/tabsCONTRDTABSTRIP/tabp041B01/ssubCONTRDSUB:SAPLEC50_CONTR:0300/subSUB01:SAPLES20:0502/ctxtEVERD-COKEY").text = self.imputacion
        self.sap.session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB05/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLEC50_CONTR:0100/tabsCONTRDTABSTRIP/tabp041B01/ssubCONTRDSUB:SAPLEC50_CONTR:0300/subSUB01:SAPLES20:0502/ctxtEVERD-SEGMENT").text = self.segmento
        self.sap.session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB05/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLEC50_CONTR:0100/tabsCONTRDTABSTRIP/tabp041B01/ssubCONTRDSUB:SAPLEC50_CONTR:0300/subSUB02:SAPLES20:0501/ctxtEVERD-KOFIZ").text = self.cdc
        self.sap.session.findById("wnd[0]/usr/subTABSTRIP:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB05/ssubSUBSC:SAPLATAB:0201/subAREA1:SAPLEC50_CONTR:0100/tabsCONTRDTABSTRIP/tabp041B01/ssubCONTRDSUB:SAPLEC50_CONTR:0300/subSUB02:SAPLES20:0501/ctxtEVERD-GEMFAKT").text = self.fac_conj
            

    def GuardaContrato(self, INS):
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
        self.sap.session.findById("wnd[0]/usr/subMIMOTABSTRIP:SAPLEC60:1120/subMIKOPF:SAPLEC60:1002/ctxtEUMZDKOPF-ZULEINZBEL").setFocus()
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "/nES32"
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtEANLD-ANLAGE").text = INS
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.id = self.sap.session.findById("wnd[0]/usr/txtEANLD-VERTRAG").text
        print("Contrato SAP: ", self.id)