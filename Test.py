from pywinauto.application import Application

app = Application(backend="uia").start(r"C:\Program Files (x86)\1cv8\8.3.15.1869\bin\chdbfl.exe")
#app = Application(backend="uia").start(r"c:\windows\system32\notepad.exe")
print(app.windows())
#dlg = app['Безымянный – Блокнот']
dlg = app['Проверка физической целостности файла БД']
dlg.print_control_identifiers()
app.dlg.control
#dlg.Toolbar("Закрыть")

#dlg.print_control_identifiers()
