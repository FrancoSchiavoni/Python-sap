class Montaje:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCreateMON = "/nEG31"
        self.sap = sap
        self.f_alta = ""
        self.dipositivo = ""
        self.tp_aparato = ""
        self.motivo = ""

    def SetDatosGenerales(self,UA,INS):
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-DEVLOC").text = UA
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-ANLAGE").text = INS
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-EADAT").text = self.f_alta
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-GERAETNEU").text = self.dipositivo
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-MATNR").text = self.tp_aparato
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-MATNR").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-MATNR").caretPosition = 6
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-GERWECHS").text = self.motivo
        self.sap.session.findById("wnd[0]/usr/ctxtREG30-GERWECHS").caretPosition = 2

    def SetNumeradores(self):
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").text = "ENACTRE"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").caretPosition = 9
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 7
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,5]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").text = "ENACTP"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,1]").text = "CAPPI"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,2]").text = "ENACTV"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,4]").text = "ENREACT"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,5]").text = "CAPFP"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,1]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,2]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,4]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,5]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 0
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/tbar[1]/btn[32]").press()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,4]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,5]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,6]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,7]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,7]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,7]").caretPosition = 1
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()


    def Guardar(self):
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    
