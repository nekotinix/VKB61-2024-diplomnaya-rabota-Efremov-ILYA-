# import fs
# from fs import open_fs
# my_fs = open_fs('.')
# my_fs.tree()
print()
print("""
Введите путь до виртуального диска: С:/mydrive.vhd
Введите команду:decrypt namefiles    
Введите ваш пароль: ·········· 
Каталог файлов расшифрован""")
print("""
virtual-secret-disk      
├── test1
│   └── secret.txt
├── test2
│   ├── sec_content.xml
│   ├── sec_data.xml
│   ├── manifest.xml
│   └── secret2.txt
├── lib.ini
└── test3    
    """)
print("""Введите команду:mount disk
Введите ваш пароль: ··········      
Виртуальный диск успешно примонтирован      
Введите команду:decrypt disk   
Введите ваш пароль: ·········· 
Виртуальный диск расшифрован     
""")
print()