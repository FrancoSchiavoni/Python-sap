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

    def SetNumeradoresCooperativa(self):
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").text = "CAPPI"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,1]").text = "CAPFP"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,2]").text = "ENREACT"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,3]").text = "ERET4_G1"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,4]").text = "EPIT4_G1"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,5]").text = "EVAT4_G1"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,6]").text = "ERET4_G2"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,7]").text = "EPIT4_G2"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,8]").text = "EVAT4_G2"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,1]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,2]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,3]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,4]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,5]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,6]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,7]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,8]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 9
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 12
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 6
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,3]").text = "ERET4_G3"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,4]").text = "EPIT4_G3"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,5]").text = "EVAT4_G3"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,6]").text = "ERET4_G4"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,7]").text = "EPIT4_G4"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,8]").text = "EVAT4_G4"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,3]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,4]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,5]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,6]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,7]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,8]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 9
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,3]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,5]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 6
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,3]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 0
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
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
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,8]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,9]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,8]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,9]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").caretPosition = 1
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()
        #self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press() VALIDAR SI EXISTE

    def SetNumeradoresProsum(self):
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").text = "ENACTRE"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,2]").text = "ENACTP"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,3]").text = "CAPPI"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,4]").text = "ENACTV"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,6]").text = "ENREACT"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,7]").text = "ENACTR_R"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,2]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,3]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,4]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,6]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,7]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").caretPosition = 0
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 9
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 12
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 6
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,3]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,4]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,5]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,7]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,8]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,3]").text = "ENACTP_R"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,4]").text = "CAPPI_R"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,5]").text = "ENACTV_R"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,7]").text = "CAPFP"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,8]").text = "CAPFP_R"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,3]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,4]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,5]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,7]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,8]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST").verticalScrollbar.position = 0
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
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
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,8]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,9]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,10]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT").verticalScrollbar.position = 3
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT").verticalScrollbar.position = 9
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT").verticalScrollbar.position = 14
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT").verticalScrollbar.position = 11
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,3]").caretPosition = 1
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT").verticalScrollbar.position = 8
        self.sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()

    def SetNumeradoresGeneracion(self):
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,0]").text = "ENACTP_G"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,1]").text = "ENACTR_G"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-TARIFART[9,2]").text = "ENACTV_G"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,0]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,1]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/ctxtREG30-KONDIGRE[10,2]").text = "GENERALES"
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLE30DCONTROL_RE_INST/txtREG30-PERVERBR[7,0]").caretPosition = 1
        self.sap.session.findById("wnd[0]/tbar[1]/btn[32]").press()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,0]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,1]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").text = "0"
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").setFocus()
        self.sap.session.findById("wnd[0]/usr/tblSAPLEL01CONTROL_SINGENT/txtREABLD-ZWSTAND[6,2]").caretPosition = 1
        self.sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()

    def Guardar(self):
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    
