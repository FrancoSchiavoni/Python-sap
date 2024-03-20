import win32com.client

class SapConnector:

    def __init__(self):
        self.SapGuiAuto = win32com.client.GetObject('SAPGUI')
        self.application = self.SapGuiAuto.GetScriptingEngine
        self.connection = self.application.Children(0)
        self.session = self.connection.Children(0)

    def Close_connection(self):
        self.connection = None
        self.application = None  
        self.SapGuiAuto = None

    def StartTransaction(self,trx):
        self.session.findById("wnd[0]").maximize()
        self.session.findById("wnd[0]/tbar[0]/okcd").text = trx
        self.session.findById("wnd[0]").sendVKey(0)