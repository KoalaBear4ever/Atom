from pywinauto.application import Application

#Открытие приложения chdbfl
app = Application(backend="uia").start(r"C:\Program Files (x86)\1cv8\8.3.15.1869\bin\chdbfl.exe")
dlg = app['Проверка физической целостности файла БД']

#Взятие его под "контроль"
dlg.print_control_identifiers()
app.dlg.control

#Вносим данные
print(dlg.pane3.Edit.wrapper_object().type_keys('D:\A64\\1Cv8.1CD'))    #Расположение БД
print(dlg.pane3.CheckBox.wrapper_object().click_input())                #Ставим галочку об исправлении ошибок
print(dlg.pane3.Edit2.wrapper_object().click_input())                   #Щелкаем на пустом месте, чтобы никаких всплывающих окон не было
print(dlg.pane3.button.wrapper_object().click())                        #Нажимаем на кнопку выполнить

#Проверка подключения к chdbfl, чтобы в дальнейшем собрать логи.
#Application(backend="uia").connect(r"C:\Program Files (x86)\1cv8\8.3.15.1869\bin\chdbfl.exe")
#dlg = app['Проверка физической целостности файла БД']
#dlg.print_control_identifiers()
