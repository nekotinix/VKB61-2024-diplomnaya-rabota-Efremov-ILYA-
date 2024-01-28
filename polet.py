import os
import time
import magma
import keyring
key=keyring.get_password('system','test')
def let_shifr(root_dir):
    # задаем путь к корневой директории на диске Z
    root_dir =str('')


    # создаем функцию для шифрования файла
    def encrypt_file(path):
        with open(path, 'rb') as f:
            data = f.read()

            encrypted_data = magma.encrypt(data,key)

            with open(path, 'wb') as f:
                f.write(encrypted_data)

    # создаем функцию для расшифровки файла
    def decrypt_file(path):
        with open(path, 'rb') as f:
            data = f.read()

            unencrypted_data = magma.decrypt(data,key)

            with open(path, 'wb') as f:
                f.write(unencrypted_data)

# запускаем цикл обработки файлов
    while True:
    # получаем список всех файлов в корневой директории
        files = os.listdir(root_dir)

        # обрабатываем каждый файл
        for file in files:
            # получаем полный путь к файлу
            path = os.path.join(root_dir, file)

            # проверяем, является ли файл файлом
            if os.path.isfile(path):
                # получаем атрибут st_mode файла
                st = os.stat(path)

                # проверяем, был ли файл открыт
                if st.st_mode & 0o200:
                # файл открыт, расшифровываем его
                    decrypt_file(path)
                else:
                    # файл закрыт, шифруем его
                    encrypt_file(path)
        time.sleep(10)
    
