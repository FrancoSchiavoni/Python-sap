class Aparato:  
    
    def __init__(self,sap, id, material):    
        self.id = id
        self.sap = sap
        self.material = material
        self.grupo_Numerador = ""
        self.trxCreateAparato = "/nIQ01"
        self.trxModificarGN = "/nEG41"
        self.tipo = None
        self.fabricante = None
        self.anio_constr = None
        self.valido_de = None
        self.relev_verific = None
        self.tipo_stock = None
        self.centro = None
        self.almacen = None
        self.nro_activo_fijo = None
        self.subnumero = None

    def cargar_datos_medidor(self, tipo, fabricante, anio_constr, valido_de,
                          grupo_numerador, relev_verific, tipo_stock:str,
                          centro, almacen, nro_activo_fijo, subnumero):
        self.tipo = tipo
        self.fabricante = fabricante
        self.anio_constr = anio_constr
        self.valido_de = valido_de
        self.grupo_Numerador = grupo_numerador
        self.relev_verific = str(relev_verific)
        self.tipo_stock = str(tipo_stock)
        self.centro = centro
        self.almacen = almacen
        self.nro_activo_fijo = nro_activo_fijo
        self.subnumero = subnumero

    def UpdateGN(self, grupo_num):
        self.grupo_Numerador = grupo_num 
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-DEVICE").text = self.id
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").text = self.material
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").setFocus
        self.sap.session.findById("wnd[0]/usr/ctxtREG42_INTERFACE-MATNR").caretPosition = 6
        self.sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIB_DEVMOD/tabpDEV_LEV/ssubTABSTRIP_SUB:SAPLEG42:0300/ctxtREG42_DEV-ZWGRUPPE").setFocus()
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIB_DEVMOD/tabpDEV_LEV/ssubTABSTRIP_SUB:SAPLEG42:0300/ctxtREG42_DEV-ZWGRUPPE").text = self.grupo_Numerador
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    
    def UpdateNumeradorGen(self):
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

    def InitCreacion(self):
        self.sap.session.findById("wnd[0]").maximize
        self.sap.session.findById("wnd[0]/usr/ctxtRISA0-MATNR").text = self.material
        self.sap.session.findById("wnd[0]/usr/ctxtRISA0-SERNR").text = self.id
        self.sap.session.findById("wnd[0]/usr/ctxtRM63E-EQTYP").text = self.tipo
        self.sap.session.findById("wnd[0]/usr/ctxtRM63E-EQTYP").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtRM63E-EQTYP").caretPosition = 1
        self.sap.session.findById("wnd[0]").sendVKey(0)

    def DetalleCreacion(self):
        self.sap.session.findById("wnd[1]/usr/ctxtEDEVICED-HERST").text = self.fabricante
        self.sap.session.findById("wnd[1]/usr/txtEDEVICED-BAUJJ").text = self.anio_constr
        self.sap.session.findById("wnd[1]/usr/ctxtEDEVICED-ZWGRUPPE").text = self.grupo_Numerador
        self.sap.session.findById("wnd[1]/usr/ctxtEDEVICED-BESITZ").text = self.relev_verific
        self.sap.session.findById("wnd[1]/usr/ctxtEDEVICED-AB").text = self.valido_de
        self.sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()

    def DatosSerie(self):
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\06").select()
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\06/ssubSUB_DATA:SAPLITO0:0122/subSUB_0122C:SAPLITO0:1220/txtEQBS-LBBSA").text = self.tipo_stock
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\06/ssubSUB_DATA:SAPLITO0:0122/subSUB_0122C:SAPLITO0:1220/ctxtEQBS-B_WERK").text = self.centro
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\06/ssubSUB_DATA:SAPLITO0:0122/subSUB_0122C:SAPLITO0:1220/ctxtEQBS-B_LAGER").text = self.almacen

    def Guardar(self):
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\03").select()
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\03/ssubSUB_DATA:SAPLITO0:0102/subSUB_0102A:SAPLITO0:1052/ctxtITOB-BUKRS").text = "1000"
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\03/ssubSUB_DATA:SAPLITO0:0102/subSUB_0102A:SAPLITO0:1052/ctxtITOB-ANLNR").text = self.nro_activo_fijo
        if self.subnumero != 0:
            self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\03/ssubSUB_DATA:SAPLITO0:0102/subSUB_0102A:SAPLITO0:1052/ctxtITOB-ANLUN").text = self.subnumero
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        try:
            self.sap.session.findById("wnd[1]/usr/txtMESSTXT1")
            self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        except:
            pass