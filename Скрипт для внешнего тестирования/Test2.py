from pywinauto.application import Application

#app = Application(backend="uia").connect(path=r"C:\Program Files (x86)\1cv8\8.3.15.1869\bin\chdbfl.exe")
app = Application(backend="uia").connect(title="Проверка физической целостности файла БД")
dlg = app['Проверка физической целостности файла БД']
dlg.print_control_identifiers()
app.dlg.control
print(dlg.pane3.Static2.wrapper_object())
