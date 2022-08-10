from pywinauto.application import Application

app = Application(backend="uia").start(r"C:\Program Files (x86)\1cv8\8.3.15.1869\bin\chdbfl.exe")
dlg = app['Проверка физической целостности файла БД']
dlg.print_control_identifiers()
app.dlg.control
print(dlg.pane3.Edit.wrapper_object().type_keys('D:\A64\\1Cv8.1CD'))
print(dlg.pane3.CheckBox.wrapper_object().click_input())
print(dlg.pane3.Edit2.wrapper_object().click_input())
print(dlg.pane3.button.wrapper_object().click())
while Application(backend="uia").connect(r"C:\Program Files (x86)\1cv8\8.3.15.1869\bin\chdbfl.exe"):
    dlg = app['Проверка физической целостности файла БД']
    dlg.print_control_identifiers()
