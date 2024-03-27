class CuentaContrato:
    
    def __init__(self, sap ):
        self.id = ""
        self.trx_create_cc = "/nCAA1"
        self.trx_update_cc = "/nCAA2"
        self.tp_cta_contrato = ""
        self.estr_region = ""
        self.name = ""
        self.cdc = ""
        self.catcta = ""
        self.condicion_pago = ""
        self.gpo_sociedades = ""
        self.soc_std = ""
        self.clase_impuesto = ""
        self.lugar_comercial = ""
        self.region = ""
        self.condado = ""
        self.proc_rec_tension = ""
        self.tipo_documento = "ZFACTURA_GD"
        self.tipo_compensacion = "Z001"
        self.ikey = "50"
        self.togru = "Z001"
        self.sap = sap
        self.reclamacion = "Z1"
        self.mail = "MAIL"
        self.nro_referencia = ""
        self.bloqueo_interes = ""

    def crear_cuenta_contrato(self, ic):
        self.sap.session.findById("wnd[0]/usr/subA01P01:SAPLFKKC:0100/ctxtFKKVKP-GPART").text = ic
        self.sap.session.findById("wnd[0]/usr/subA01P01:SAPLFKKC:0100/ctxtFKKVK-VKTYP").setFocus()
        self.sap.session.findById("wnd[0]/usr/subA01P01:SAPLFKKC:0100/ctxtFKKVK-VKTYP").text = self.tp_cta_contrato
        self.sap.session.findById("wnd[0]/usr/subA01P01:SAPLFKKC:0100/ctxtFKKVK-VKTYP").setFocus()
        self.sap.session.findById("wnd[0]/usr/subA01P01:SAPLFKKC:0100/ctxtFKKVK-VKTYP").caretPosition = 2
        self.sap.session.findById("wnd[0]").sendVKey(0)

    def cargar_datos_generales(self):
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P01:SAPLFKKC:0210/txtFKKVK-VKBEZ").text = self.name
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P03:SAPLFKKC:0260/cmbFKKVKP-TOGRU").key = self.togru
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P03:SAPLFKKC:0260/cmbFKKVKP-IKEY").key = self.ikey
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P04:SAPLES35:0320/ctxtSI_FKKVKPR-REGIOGR_CA_T").text = self.estr_region
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P04:SAPLES35:0320/ctxtSI_FKKVKPR-REGIOGR_CA_B").text = self.estr_region
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P03:SAPLFKKC:0260/cmbFKKVKP-VERTYP").key = self.tipo_compensacion
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P06:SAPLES35:0275/ctxtSI_FKKVKPSICA-ZAHLKOND").text = self.condicion_pago
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P06:SAPLES35:0275/ctxtSI_FKKVKPR-KTOKL").text = self.catcta
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P06:SAPLES35:0275/ctxtSI_FKKVKPSICA-KOFIZ_SD").text = self.cdc
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA04P02:SAPLES35:0280/ctxtISU_FKKVKD-FORMKEY_CA").text = self.tipo_documento
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P02:SAPLFKKC:0265/ctxtFKKVKD-POST_LOCK").text = self.bloqueo_interes
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02").select()

    def cargar_pagos_impuestos(self):
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA02P01:SAPLFKKC:0300/ctxtFKKVKP-OPBUK").text = self.gpo_sociedades
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA02P01:SAPLFKKC:0300/ctxtFKKVKP-STDBK").text = self.soc_std
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA05P04:SAPLFKKC:0321/cmbFKKVKP-FITYP").key = self.clase_impuesto
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA05P04:SAPLFKKC:0321/ctxtFKKVKP-PROVINCE").text = self.region
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA05P04:SAPLFKKC:0321/ctxtFKKVKP-COUNTY").text = self.condado
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA05P06:SAPLFKKC:0322/ctxtFKKVKP-BUPLA").text = self.lugar_comercial
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA05P04:SAPLFKKC:0321/ctxtFKKVKP-COUNTY").setFocus
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR02/ssubGENSUB:SAPLBUSS:7038/subA05P04:SAPLFKKC:0321/ctxtFKKVKP-COUNTY").caretPosition = 3
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR03").select()


    def cargar_reclamacion(self, ic):
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR03/ssubGENSUB:SAPLBUSS:7006/subA02P01:SAPLFKKC:0220/ctxtFKKVKP-ABWMA").text = ic
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR03/ssubGENSUB:SAPLBUSS:7006/subA02P01:SAPLFKKC:0220/cmbFKKVKP-MGRUP").key = "Z1"
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR03/ssubGENSUB:SAPLBUSS:7006/subA02P01:SAPLFKKC:0220/cmbFKKVKP-MAHNV").key = self.proc_rec_tension
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR03/ssubGENSUB:SAPLBUSS:7006/subA03P02:SAPLES35:0240/ctxtSI_FKKVKPR-SENDCONTROL_GP").text = self.mail
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR03/ssubGENSUB:SAPLBUSS:7006/subA02P01:SAPLFKKC:0220/ctxtFKKVKD-DUN_REASON").text = self.bloqueo_interes
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()

    def busca_nro_cc(self):
        self.id = self.sap.session.findById("wnd[0]/usr/subA01P01:SAPLFKKC:0100/ctxtFKKVKP-VKONT").text

    @classmethod
    def gen_nro_referencia(cls, valor):
        codigo_izquierda = valor[:1]
        codigo_derecha = valor[-7:]
        resultado = "285" + codigo_izquierda + "9" + codigo_derecha
        return resultado

    def carga_nro_referencia(self, nro_cc):
        self.sap.session.findById("wnd[0]").sendVKey(0)
        self.nro_referencia = str(self.gen_nro_referencia(nro_cc))
        self.sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpBUSCR01/ssubGENSUB:SAPLBUSS:7005/subA03P02:SAPLFKKC:0265/txtFKKVKP-EXVKO").text = self.nro_referencia
        self.sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
        self.sap.session.findById("wnd[0]/tbar[0]/btn[15]").press()