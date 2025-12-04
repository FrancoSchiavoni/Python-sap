import datetime

class DocumentoFica:
    
    def __init__(self, sap):    
        self.sap = sap
        self.trx_code = "/nFPE1"
        
        # Atributos de Cabecera
        self.clase_doc = None
        self.moneda = None
        self.lugar_comercial = None
        self.fecha_contabilizacion = None
        
        # Atributos de Posición
        self.socio_comercial = None
        self.sociedad = None
        self.cuenta_contrato = None
        self.op_princ = None
        self.op_parc = None
        self.importe = None 
        self.contrato = None

    def cargar_datos_cabecera(self, clase_doc, moneda, lugar_comercial, fecha_contabilizacion):
        self.clase_doc = clase_doc
        self.moneda = moneda
        self.lugar_comercial = lugar_comercial
        
        # Formateo de fecha para SAP (dd.mm.yyyy)
        if isinstance(fecha_contabilizacion, (datetime.datetime, datetime.date)):
            self.fecha_contabilizacion = fecha_contabilizacion.strftime('%d.%m.%Y')
        else:
            self.fecha_contabilizacion = str(fecha_contabilizacion)

    def cargar_datos_posicion(self, socio_comercial, sociedad, cuenta_contrato, op_princ, op_parc, importe, contrato):
        self.socio_comercial = str(socio_comercial)
        self.sociedad = str(sociedad)
        self.cuenta_contrato = str(cuenta_contrato)
        self.op_princ = str(op_princ)
        self.op_parc = str(op_parc)
        self.contrato = str(contrato)
        self.importe = importe 

    def InitTransaccion(self):
        # Asegurar ventana maximizada
        try:
            self.sap.session.findById("wnd[0]").maximize()
        except:
            pass

        #self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-BLDAT").text = self.fecha_contabilizacion # Fecha documento
        #self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-BUDAT").text = self.fecha_contabilizacion # Fecha contab.
        
        self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-BLART").text = self.clase_doc
        self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-WAERS").text = self.moneda
        self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-BRANCH").text = self.lugar_comercial
        self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-FIKEY").setFocus
        self.sap.session.findById("wnd[0]/usr/ctxtFKKKO-FIKEY").caretPosition = 5
        self.sap.session.findById("wnd[0]").sendVKey(0)
        
        # Busca si existe una ventana modal (wnd[1]) y presiona "Sí".
        try:
            if self.sap.session.findById("wnd[1]").Text == "Verificación clave reconcil.":
                self.sap.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press() 
        except:
            pass 
        
        try:
            if self.sap.session.findById("wnd[1]").Type == "GuiModalWindow":
                self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press() 
        except:
            pass

    def CompletarPosiciones(self):
        # Referencia a la tabla de posiciones (Grid superior)
        grid_posiciones = "wnd[0]/usr/tblSAPLFKPPCTRL_0500"
        
        # Llenamos la primera línea (row 0) con los datos obligatorios [cite: 32-38]
        self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-GPART[1,0]").text = self.socio_comercial
        self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-BUKRS[2,0]").text = self.sociedad
        #self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-FAEDN[3,0]").text = 
        self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-VKONT[4,0]").text = self.cuenta_contrato
        self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-HVORG[5,0]").text = self.op_princ
        self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-TVORG[6,0]").text = self.op_parc
        
        # Formateo del importe inicial para SAP (string con coma)
        importe_str = f"{float(self.importe):.2f}".replace('.', ',')
        self.sap.session.findById(f"{grid_posiciones}/txtFKKOPLST-BETRW[7,0]").text = importe_str
        
        self.sap.session.findById(f"{grid_posiciones}/ctxtFKKOPLST-VTREF[8,0]").text = self.contrato

    def AjustarImporteConImpuestos(self):
        self.sap.session.findById("wnd[0]").sendVKey(0) 

        grid_impuestos = "wnd[0]/usr/subTAX:SAPLFKPP:1201/tblSAPLFKPPCTRL_1201"
        grid_posiciones = "wnd[0]/usr/tblSAPLFKPPCTRL_0500"

        try:
            impuesto_sap_str = self.sap.session.findById(f"{grid_impuestos}/txtFKKOPK-BETRW[5,0]").text
            
            impuesto_clean = impuesto_sap_str.replace('.', '').replace(',', '.').replace('-', '').replace(' ', '')
            impuesto_float = float(impuesto_clean)
            print(impuesto_float)    
            
            importe_base_float = float(self.importe)
            
            
            if importe_base_float < 0:
                nuevo_total = importe_base_float - abs(impuesto_float)
            else:
                nuevo_total = importe_base_float + abs(impuesto_float)

            nuevo_total_str = f"{nuevo_total:.2f}".replace('.', ',')
            self.sap.session.findById(f"{grid_posiciones}/txtFKKOPLST-BETRW[7,0]").text = nuevo_total_str
    

        except Exception as e:
            # Si falla la lectura de impuestos (ej. exento), no bloqueamos, pero imprimimos error en consola
            print(f"Advertencia calculando impuestos: {e}")

    def Guardar(self):
        print("guardado documento...")
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()