import os
import shutil
import glob


class ContratoPotencia:
        
    def __init__(self,sap):
        self.id = ""
        self.trxCP = "/nZDM_CONTRATOS_GC"
        self.trxValidaCP = "/nZDM_VALIDA_GC"
        self.trxNotificaCP = "/nZDM_NOTIFICA_GC"
        self.sap = sap
        self.fecha_ini = ""
        self.periodo = ""
        self.contratadaP = ""
        self.contratadaFP = ""
        self.descripcion = "Test CP"
        self.periodos = []
        self.contratadaP_B = ""
        self.contratadaFP_B = ""

    def InitContratoPotencia(self, IC,CC,INS):
        self.sap.session.findById("wnd[0]/tbar[1]/btn[18]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPARTNER").text = IC
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZVKONT").text = CC
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZANLAGE").text = INS
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZFECHA_DESDE").text = self.fecha_ini

    def SetValoresCP(self):
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").text = str((self.periodo))
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.sap.session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_PIC").text = self.contratadaP
        self.sap.session.findById("wnd[0]/usr/txtZZCONT_GC_CAB-ZZPOT_CONTRATADA_FPIC").text = self.contratadaFP
        self.sap.session.findById("wnd[0]").sendVKey(0)
    

    def MostarGrilla(self, tipo_cliente):
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZPERIODO_TIPO").text = str((self.periodo))
        if (tipo_cliente == "DP"):
            self.sap.session.findById("wnd[0]").sendVKey(4)
            self.sap.session.findById("wnd[1]/usr/lbl[1,6]").setFocus()
            self.sap.session.findById("wnd[1]/usr/lbl[1,6]").caretPosition = 2
            self.sap.session.findById("wnd[1]").sendVKey(2)
            self.sap.session.findById("wnd[0]").sendVKey(0)
        else:
            self.sap.session.findById("wnd[0]").sendVKey(4)
            self.sap.session.findById("wnd[1]/usr/lbl[1,4]").setFocus()
            self.sap.session.findById("wnd[1]/usr/lbl[1,4]").caretPosition = 0
            self.sap.session.findById("wnd[1]").sendVKey(2)
            self.sap.session.findById("wnd[0]").sendVKey(0)
            self.sap.session.findById("wnd[1]/usr/btnBUTTON_1").press()
        

    def CargaEstacionalidad(self):
        for index,mes in enumerate(self.periodos):
            if mes == "EA":
                self.sap.session.findById("wnd[0]/usr/tblZDM_CONTRATOS_GCZZPERIODOS/ctxtZZCONT_GC_PERIOD-ZZPERIODO_CLASE[3," + str(index) + "]").text = "A  "
            else:
                self.sap.session.findById("wnd[0]/usr/tblZDM_CONTRATOS_GCZZPERIODOS/txtZZCONT_GC_PERIOD-ZZPOT_CONTRATADA_PIC[4," + str(index) + "]").text = self.contratadaP_B
                self.sap.session.findById("wnd[0]/usr/tblZDM_CONTRATOS_GCZZPERIODOS/txtZZCONT_GC_PERIOD-ZZPOT_CONTRATADA_FPIC[6," + str(index) + "]").text = self.contratadaFP_B
        self.sap.session.findById("wnd[0]").sendVKey(0)

    def GuardarCP(self):
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/btnBUTTON_1").press()
        self.sap.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").text = self.descripcion
        self.sap.session.findById("wnd[1]/usr/sub:SAPLSPO4:0300/txtSVALD-VALUE[0,21]").caretPosition = 3
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[1]/usr/txtMESSTXT2").setFocus()
        self.sap.session.findById("wnd[1]/usr/txtMESSTXT2").caretPosition = 9
        self.sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").caretPosition = 10
        self.id = self.sap.session.findById("wnd[0]/usr/ctxtZZCONT_GC_CAB-ZZCONTRATOGC").text 

    def ValidarCP(self):
        self.sap.session.findById("wnd[0]/usr/ctxtS_CONTR-LOW").text = self.id
        self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()

    def NotificarExceso(self, path_destino, periodo):
        self.sap.session.findById("wnd[0]/usr/txtP_IMPRE").text = "locl"
        self.sap.session.findById("wnd[0]/usr/txtP_IN").text = "x"
        self.sap.session.findById("wnd[0]/usr/ctxtS_CONTR-LOW").text = self.id
        self.sap.session.findById("wnd[0]/usr/ctxtS_CONTR-LOW").setFocus
        self.sap.session.findById("wnd[0]/usr/ctxtS_CONTR-LOW").caretPosition = 10
        self.sap.session.findById("wnd[0]/usr/ctxtP_ZZTIPO").text = "2"
        self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
        try:
            # Intentamos obtener el elemento
            element = self.sap.session.findById("wnd[1]/usr/txtIK1")
            exists = True
        except:
            exists = False
        
        if exists:
            self.sap.session.findById("wnd[1]").close()
            self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press() #Finalizar
        else:
            self.sap.session.findById("wnd[1]/usr/ctxtSSFPP-TDDEST").text = "locl"
            self.sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()
            self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "pdf!"
            self.sap.session.findById("wnd[0]").sendVKey(0)

            carpeta_temporal = os.path.join(os.getenv('LOCALAPPDATA'), 'Temp')
            print(carpeta_temporal)

            patron_pdf = os.path.join(carpeta_temporal, '*smart*.pdf')
            archivos_pdf = glob.glob(patron_pdf)

            if archivos_pdf:
              ruta_pdf = archivos_pdf[0]
              carpeta_destino = path_destino
              nuevo_nombre = self.id + "_" + periodo + ".pdf"
              ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
              shutil.copy(ruta_pdf, ruta_destino)
              print("PDF movido exitosamente a la carpeta de destino.")
            else:
              print("No se encontraron archivos PDF en la carpeta temporal.")

            self.sap.session.findById("wnd[1]").close()
            self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
            self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
            self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()


    def NotificarFin(self, path_destino, periodo):
        self.sap.session.findById("wnd[0]").maximize()
        self.sap.session.findById("wnd[0]/usr/txtP_IMPRE").text = "locl"
        self.sap.session.findById("wnd[0]/usr/txtP_IN").text = "x"
        self.sap.session.findById("wnd[0]/usr/ctxtS_CONTR-LOW").text = self.id
        self.sap.session.findById("wnd[0]/usr/ctxtP_ZZTIPO").setFocus()
        self.sap.session.findById("wnd[0]/usr/ctxtP_ZZTIPO").text = "1"
        self.sap.session.findById("wnd[0]/usr/chkP_REIMP").selected = True
        self.sap.session.findById("wnd[0]/usr/ctxtP_ZZTIPO").caretPosition = 1
        self.sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
        self.sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/okcd").text = "pdf!"
        self.sap.session.findById("wnd[0]").sendVKey(0)

        carpeta_temporal = os.path.join(os.getenv('LOCALAPPDATA'), 'Temp')
        print(carpeta_temporal)

        patron_pdf = os.path.join(carpeta_temporal, '*smart*.pdf')
        archivos_pdf = glob.glob(patron_pdf)
        if archivos_pdf:
          ruta_pdf = archivos_pdf[0]
          carpeta_destino = path_destino
          nuevo_nombre = self.id + "_" + periodo + "_fin" +".pdf"
          ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
          shutil.copy(ruta_pdf, ruta_destino)
          print("PDF movido exitosamente a la carpeta de destino.")
        else:
          print("No se encontraron archivos PDF en la carpeta temporal.")
        
        self.sap.session.findById("wnd[1]").close()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()

