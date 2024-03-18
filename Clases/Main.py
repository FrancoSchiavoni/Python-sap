import cuenta_contrato as cc
import connector as s


sap = s.SapConnector()

for row in input:

    #Cuenta Contrato
    CuentaContrato = cc.CuentaContrato()
    CuentaContrato.StartCuentaContrato()
    CuentaContrato.SetDatosGenerales()
    CuentaContrato.SetPagosImpuestos()
    CuentaContrato.SetReclamacion()
    CuentaContrato.BuscaNroCC()
    print(CuentaContrato.id)
    CuentaContrato.SetNroReferencia()

    #

