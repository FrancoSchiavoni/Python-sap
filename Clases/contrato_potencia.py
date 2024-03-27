class ContratoPotencia:
        
    def __init__(self, sap):
        self.id = ""
        self.trx_cp = "/nZDM_CONTRATOS_GC"
        self.sap = sap
        self.fecha_ini = ""
        self.periodo = "00"
        self.contratada_p = "50"
        self.contratada_fp = "50"
        self.descripcion = "Test CP"

    def crear_contrato_potencia(self, ic, cc, ins):
        self.sap.session.findById("wnd[0]/tbar[1]/btn[18]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPARTNER").text = ic
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZVKONT").text = cc
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZANLAGE").text = ins
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZFECHA_DESDE").text = self.fecha_ini
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").caretPosition = 2
        self.sap.session.findById("wnd[0]").sendVKey(4)
        self.sap.session.findById("wnd[1]").close()

    def cargar_datos_cp(self):
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").text = self.periodo
        self.sap.session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_PIC").text = self.contratada_p
        self.sap.session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_FPIC").text = self.contratada_fp
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/btnBUTTON_1").press()

    def guardar_cp(self):
        self.sap.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").text = self.descripcion
        self.sap.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").caretPosition = 3
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/txtMESSTXT2").setFocus()
        self.sap.session.findById("wnd[1]/usr/txtMESSTXT2").caretPosition = 9
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").caretPosition = 10
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").text 