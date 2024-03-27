class Aparato:  
    
    def __init__(self,sap, id, material):    
        self.id = id
        self.sap = sap
        self.material = material
        self.grupo_numerador = ""
        self.trx_modificar_gn = "/nEG41"
    
    def update_gn(self, grupo_num):
        self.grupo_numerador = grupo_num 
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-DEVICE").text = self.id
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").text = self.material
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").setFocus
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").caretPosition = 6
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIB_DEVMOD/tabpDEV_LEV/ssubTABSTRIP_SUB:SAPLEG42:0300/ctxtREG42_DEV-ZWGRUPPE").setFocus()
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIB_DEVMOD/tabpDEV_LEV/ssubTABSTRIP_SUB:SAPLEG42:0300/ctxtREG42_DEV-ZWGRUPPE").text = self.grupo_numerador
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    
    def update_numerador_gen(self):
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-DEVICE").text = self.id
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").text = self.material
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").setFocus
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").caretPosition = 6
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/tbar[1]/btn[27]").press()
        self.sap.session.findById("wnd[1]/usr/subEZWG_SUBSCREEN:SAPLE10A:1000/tblSAPLE10ATC_EZWG/ctxtEZWGD-ZWTYP[2,0]").text = "4"
        self.sap.session.findById("wnd[1]/usr/subEZWG_SUBSCREEN:SAPLE10A:1000/tblSAPLE10ATC_EZWG/ctxtEZWGD-ZWTYP[2,1]").text = "4"
        self.sap.session.findById("wnd[1]/usr/subEZWG_SUBSCREEN:SAPLE10A:1000/tblSAPLE10ATC_EZWG/ctxtEZWGD-ZWTYP[2,2]").text = "4"
        self.sap.session.findById("wnd[1]/usr/subEZWG_SUBSCREEN:SAPLE10A:1000/tblSAPLE10ATC_EZWG/ctxtEZWGD-ZWTYP[2,2]").setFocus()
        self.sap.session.findById("wnd[1]/usr/subEZWG_SUBSCREEN:SAPLE10A:1000/tblSAPLE10ATC_EZWG/ctxtEZWGD-ZWTYP[2,2]").caretPosition = 1
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()