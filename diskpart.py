from symbol import comparison
import pwinput
import subprocess
import os
from GOST_34_11_2012 import Hash
from fs import open_fs
import keyring
import psutil
# #присвоение пути
# vhd_path = "C:\\MyDrive"
# #Присвоение размера  
# vhd_size = "1024" # 1 GB
# #надпись
# label="test2"
fs="ntfs"
# letter="G"
# #Cвободное место

def free_space():
    # Получение информации о всех дисках
    disks = psutil.disk_partitions(all=True)
    # Перебор всех дисков и вывод свободного места на каждом диске в гигабайтах
    for disk in disks:
        usage = psutil.disk_usage(disk.mountpoint)
        free_space_gb = usage.free / (1024 ** 3)
        ds=str(f"Диск {disk.device} ({disk.mountpoint}) - свободно {free_space_gb:.2f} ГБ")
        print(ds)
        if free_space_gb < 2.0:
            print(f"Недостаточно места на диске {disk.device}")
            
            #Создание виртуального диска

def create_virtual_disk(vhd_path,vhd_size,label,letter):
    #Создание виртуального диска
    diskpart_script_create = (
        f'select vdisk file="{vhd_path}"\n'
        f'create vdisk file="{vhd_path}" maximum={vhd_size}\n'
        'attach vdisk\n'
        'create partition primary\n'
        f'format fs={fs} label={label} quick\n'
        f'assign letter={letter}\n'
        'exit\n'
    )
    #Запуск скрипта Diskpart
    subprocess.run(['diskpart'], input=diskpart_script_create.encode(), check=True)
    return(print("Виртуальный диск успешно создан "))
#Подключение виртуального диска
def attach_virtual_disk(vhd_path):
    file_path = vhd_path

    # желаемое расширение
    extension = '.vhd'

    # создаем новое имя файла с расширением
    new_file_path = file_path + extension
  
    #переименовываем файл
    os.rename(file_path, new_file_path)

    #Подключение виртуального диска
    attach_disk_script = (
        f'select vdisk file="{new_file_path}"\n'
        'attach vdisk \n'
        'exit\n'
    )

    # Выполнение скрипта diskpart
    subprocess.run(['diskpart'], input=attach_disk_script.encode(), check=True)
#Подключение диска в режиме только чтение
def attach_virtual_disk_read_only(vhd_path):
    file_path = vhd_path

    # желаемое расширение
    extension = '.vhd'

    # создаем новое имя файла с расширением
    new_file_path = file_path + extension
  
    #переименовываем файл
    os.rename(file_path, new_file_path)

    #Подключение виртуального диска
    attach_disk_script_readonly = (
        f'select vdisk file="{new_file_path}"\n'
        'attach vdisk readonly\n'
        'exit\n'
    )

    # Выполнение скрипта diskpart
    subprocess.run(['diskpart'], input=attach_disk_script_readonly.encode(), check=True)

#Отключение виртуального диска
def detach_virtual_disk(vhd_path2):
    #Отключение виртуального диска
    detach_disk_script = (
        f'select vdisk file="{vhd_path2}"\n'
        'detach vdisk\n'
        'exit\n'
    ) 

    # Запуск скрипта diskpart
    subprocess.run(['diskpart'], input=detach_disk_script.encode(), check=True)
    # путь к файлу

    # получаем название файла без расширения
    filename, extension = os.path.splitext(vhd_path2)
    print(filename)  # /path/to/file
    os.rename(vhd_path2, filename)
    print('Виртуальный диск отключен')

def view_tree():
    my_fs=open_fs('C:')
    my_fs.tree()
   
    
def get_pass():
    pd=pwinput.pwinput(prompt='Пароль:',mask='·')
    print(pd)


def add_hash():
    y=Hash('pass',256)
    y1=Hash('pass',256)
    print('Хэш',y)
    #Присвоение хэша пароля в хранилище
    keyring.set_password('system','test',y)
    #Извлечение хэша из хранилища
    password=keyring.get_password('system','test')
    print(password)
    y1=str(y1)
    password=str(password)
    if y1==password:
        print('Пароль верный:')
        print(y1)
        print(password)
    else:
        print('Пароль неверный:')
        print(y1)
        print(password)
free_space()
def hash_comparisson(passw):
#Извлечение хэша из хранилища
    password=keyring.get_password('system','test')
    y=Hash(passw,256)
    y=str(y)
    password=str(password)
    if y==password:
        print('Пароль верный:')
        return True
    else:
        print('Пароль неверный:')
        return False
import os
import shutil
import datetime
def backup(vhd_path,backup_folder):
    
    # Указываем путь к файлу vhd и папке для сохранения бэкапа
    vhd_path = 'C:\\MyDrive'
    backup_folder = 'C:\\back'

    # Создаем папку для бэкапа, если ее нет
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Генерируем название файла бэкапа с использованием текущего времени
    now = datetime.datetime.now()
    backup_file_name = f'backup_{now.strftime("%Y-%m-%d_%H-%M-%S")}'
    backup_file_path = os.path.join(backup_folder, backup_file_name)

    # Копируем файл vhd в папку бэкапа с новым именем
    shutil.copy2(vhd_path, backup_file_path)
    print(f'Создан бэкап файла {vhd_path} в {backup_file_path}')
