# VKB61-2024-diplomnaya-rabota-Efremov-ILYA-
Выпускная квалификационная работа 61 группы ВКБ , Ефремов Илья 2023-2024г.

Тема: Программное средство для создания виртуальных зашифрованных дисков

Работает с контейнерами формата: VHD (используя API Diskpart)

Главное окно программы:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/35434e98-f199-4e44-be72-33e273a7d658)

Подраздел меню Главное:

**Создание виртуального диска**

Требуемые данные:

Путь создания диска: -> C:\MyDrive

Размер в ГБ: -> 1

Имя подключения диска: -> MyDrive

Буква подключения диска: -> z

Пароль: -> ваш пароль

Вывод программы: 

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/aacc3c06-b68b-4934-b4d8-c24705676a45)

Пароль хэшируется алгоритмом ГОСТ Р 34.11.2012  и записывается в хранилище Windows, для дальнейшего сравнения при подключении диска в систему.

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/f99cd533-4b5e-492d-a938-6dd5ac961b33)

**- Подключение виртуального диска**

Подключение виртуального  диска имеет два режима:

**- Обычный**

Диск подключается и доступен в режиме чтения и записи файлов. Для защиты данных используется алгоритм шифрования Магма из ГОСТ 34.12.2015 совместно с технологией шифрования на лету.
Вывод программы:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/74588c91-fe14-4a81-96ec-289a7b08110d)

Пример вывода программы:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/7c08d57b-54e3-4a9c-a834-51550c3af4fa)

**Шифрование на лету:**

Записываем данные например в текстовый файл:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/38fd5e97-0948-4f30-9310-da71ab673142)

После закрытия файла данные зашифровались.

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/7051ac84-e9dc-4602-80b5-e23d006b263f)

При открытии данные снова доступны.

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/78caf98d-e0ed-4f2a-950a-bcc08e689e97)


**- Для чтения**

Диск доступен только для чтения, операции записи недоступны, возвращается ошибка. Шифрование на лету работает только на расшифровку данных.

Пример отображения в утилите diskpart:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/2daee2bb-599a-4c61-acf2-9272aa59d1b3)

**Отключение виртуального диска:**

Программа предусматривает автоматическое отключение дисков, при закрытии окна программы, все подключенные диски в результате работы программы накапливаются и автоматически отключаются при завершении работы программы.

Пример кода для отключения дисков при закрытии окна:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/068558a2-86f6-474c-8b31-92a0cdf32451)

А в программе по данной кнопке можно отключить виртуальный диск, прям во время работы программы.

Пример вывода программы:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/b901bab9-54b9-429d-9844-a92031f0ebd7)

**Бэкап**

 Для создания  защищенных бэкапов виртуального жесткого диска используется защита в виде создания папки с  именем зарезервированным ОС Windows.
 
 Например:  папка NUL .
 
 При попытке пользователя попасть в данную папку возникает ошибка:
 
 ![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/91a28156-cecc-44c0-adea-6134a6b80826)

Результат работы программы:

![image](https://github.com/nekotinix/VKB61-2024-diplomnaya-rabota-Efremov-ILYA-/assets/62836642/47d97841-f77e-4ffd-a9d9-4df861df0eb0)






