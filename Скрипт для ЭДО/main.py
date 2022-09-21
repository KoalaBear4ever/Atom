import shutil
import datetime

# Указываем пути
path='//Hp/edo'
pathArch= 'D:\АрхивЭДО\Архив за'
today = datetime.datetime.today().strftime("%d.%m.%y")
pathArch += " " + today

# Копируем файл из папки в папку
shutil.copytree(path, pathArch)

print("Архивирование завершено!")
sleep(30)
