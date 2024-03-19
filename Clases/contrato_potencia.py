class ContratoPotencia:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCP = "/nZDM_CONTRATOS_GC"
        self.sap = sap
        self.fecha_ini = ""
        self.periodo = "00"
        self.contratadaP = "50"
        self.contratadaFP = "50"
        self.descripcion = "Test CP"
        

    def InitContratoPotencia(self, IC,CC,INS):
        self.sap.session.findById("wnd[0]/tbar[1]/btn[18]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPARTNER").text = IC
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZVKONT").text = CC
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZANLAGE").text = INS
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZFECHA_DESDE").text = self.fecha_ini
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").caretPosition = 2
        self.sap.session.findById("wnd[0]").sendVKey(4)
        self.sap.session.findById("wnd[1]").close()

    def SetValoresCP(self):
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").text = self.periodo
        self.sap.session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_PIC").text = self.contratadaP
        self.sap.session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_FPIC").text = self.contratadaFP
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/btnBUTTON_1").press()

    def GuardarCP(self):
        self.sap.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").text = self.descripcion
        self.sap.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").caretPosition = 3
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/txtMESSTXT2").setFocus()
        self.sap.session.findById("wnd[1]/usr/txtMESSTXT2").caretPosition = 9
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").caretPosition = 10
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").text 

    
