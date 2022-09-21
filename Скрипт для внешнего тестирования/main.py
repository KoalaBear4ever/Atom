import os
import shutil
import time
import datetime
import click


# Указываем папку в которой производить поиск
path='D:\Тест 1'
#Поиск по имени файла с записью пути и даты
for rootdir, dirs, files in os.walk(path):
    for file in files:
        ##if((file.split('.')[-1])=='txt'): old ver.
        if file == "TEST.txt":
            pathfile = os.path.join(rootdir, file)
            TimePath = time.strftime("%d.%m.%y", time.gmtime(os.path.getmtime(pathfile)))
            today = datetime.datetime.today().strftime("%d.%m.%y")
            if TimePath == today:
                filename = file
                TimeArch = time.strftime("%Y%m%d", time.gmtime(os.path.getmtime(pathfile)))
                mainDir = rootdir
                break

rootDirArch = mainDir + "\Архив"
# Папки из которой и в которую будет происходить перемещение
moveFrom = f"{mainDir}\{filename}"
moveTo = f"{rootDirArch}\{filename}"
moveTo = '.'.join(moveTo.split('.')[:-1])
moveTo = f"{moveTo}({TimeArch}).txt"
# Копируем файл из папки в папку
#shutil.copyfile(moveFrom, moveTo, follow_symlinks=True)

# Путь и запуск внешнего тестирования
SearchTest = "C:\Program Files\\1cv8\8.3.15.1869\\bin\chdbfl.exe"
#click.launch(moveTo)
print (SearchTest)

#Открытие приложения chdbfl
app = Application(backend="uia").start(SearchTest)
dlg = app['Проверка физической целостности файла БД']

#Взятие его под "контроль"
dlg.print_control_identifiers()
app.dlg.control

#Вносим данные
print(dlg.pane3.Edit.wrapper_object().type_keys('D:\A64\\1Cv8.1CD'))    #Расположение БД
print(dlg.pane3.CheckBox.wrapper_object().click_input())                #Ставим галочку об исправлении ошибок
print(dlg.pane3.Edit2.wrapper_object().click_input())                   #Щелкаем на пустом месте, чтобы никаких всплывающих окон не было
print(dlg.pane3.button.wrapper_object().click())                        #Нажимаем на кнопку выполнить
