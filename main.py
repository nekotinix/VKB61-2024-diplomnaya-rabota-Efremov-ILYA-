from contextlib import closing
import customtkinter
import os
from PIL import Image
import diskpart
from tkinter import filedialog
path_vdisks=[]
extension=".vhd"
print('path_diskov',path_vdisks)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Шифрование Виртуальных Дисков")
        self.geometry("700x450")
        self.iconbitmap('x_icon.ico')
        # Уставновка вывода 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # подгрузка тем
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # создание гланого окна
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        # количество строк в разделе меню
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Меню",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Главная",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Шифрование",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Бэкапы",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Настройки",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # Домашний экран меню
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame,text='')
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Создание виртуального диска",command=self.open_input_dialog_event)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.checkbox_1=customtkinter.CTkCheckBox(self.home_frame,text="только для чтения")
        self.checkbox_1.grid(row=2, column=1, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Подключение виртуального диска",command=self.add_disk_button_event)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Отключение виртуального диска",command=self.remove_disk_event)
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="Автомонтирование")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.home_frame_text_box1=customtkinter.CTkTextbox(self.home_frame,height=160, width=400)
        self.home_frame_text_box1.grid(row=5, column=0,padx=20,pady=20)
        # self.home_frame_text_box1.insert('0.1',)
        # Создание второго подменю
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame_image_label = customtkinter.CTkLabel(self.second_frame,text='')
        self.second_frame_image_label.grid(row=0, column=0, padx=20, pady=20)
        # self.secondframe_textlb_1=customtkinter.CTkTextbox(self.second_frame,width=250,height=250)
        # self.secondframe_textlb_1.grid(row=0, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.second_frame_button1=customtkinter.CTkButton(self.second_frame,text='Зашифровать файл')
        self.second_frame_button1.grid(row=1,column=0,padx=20,pady=10)
        self.second_frame_button2=customtkinter.CTkButton(self.second_frame,text='Расшифровать файл')
        self.second_frame_button2.grid(row=2,column=0,padx=20,pady=10)
        self.second_frame_text_box1=customtkinter.CTkTextbox(self.second_frame,height=160, width=400)
        self.second_frame_text_box1.grid(row=5, column=0,padx=20,pady=20)
        # Создание 3 подменю
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame_image_label = customtkinter.CTkLabel(self.third_frame,text='')
        self.third_frame_image_label.grid(row=0, column=0, padx=20, pady=20)
        self.third_frame_button1=customtkinter.CTkButton(self.third_frame,text='Создать Бэкап',command=self.create_backup_event)
        self.third_frame_button1.grid(row=1,column=0,padx=20,pady=10)
        self.third_frame_option_menu_1=customtkinter.CTkOptionMenu(self.third_frame, values=["NUL"],
                                                                )
        self.third_frame_option_menu_1.grid(row=1, column=1, padx=20, pady=10, sticky="s")
        self.third_frame_button2=customtkinter.CTkButton(self.third_frame,text='Перейти к папке',command=self.open_file_dialog)
        self.third_frame_button2.grid(row=2,column=0,padx=20,pady=10)
        self.third_frame_text_box1=customtkinter.CTkTextbox(self.third_frame,height=160, width=400)
        self.third_frame_text_box1.grid(row=5, column=0,padx=20,pady=20)
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        
        # Выбор подменю по молчанию
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # установка цвета кнопки при наведении на неё
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # Показать выбранную кнопку
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()    
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")    
        else:
            self.fourth_frame.grid_forget()

    #Призвести действия заданные по кнопке
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")
        
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Введите путь хранения диска", title="Путь хранения")
        print("CTkInputDialog:", dialog.get_input())
        if dialog.get_input== None:
            print('Введите значение')
        dialog1=customtkinter.CTkInputDialog(text="Введите размер в Гб", title="Размер")
        print("CTkInputDialog:", dialog1.get_input())
        dialog2=customtkinter.CTkInputDialog(text="Введите имя подключения диска", title="Имя диска")
        print("CTkInputDialog:", dialog2.get_input())
        dialog3=customtkinter.CTkInputDialog(text="Введите пароль", title="пароль")
        print("CTkInputDialog:",dialog3.get_input())
        
        
    def add_disk_button_event(self):
        if self.checkbox_1.get() ==1:
            # dialog1=customtkinter.CTkInputDialog(text="Введите путь", title="Путь")
            # vdisk_path=dialog1.get_input()
            filename = filedialog.askopenfilename()
            filename=filename.replace("/",'\\')
            path_vdisks.append(filename+extension)
            dialog3=customtkinter.CTkInputDialog(text="Введите пароль", title="пароль")
            passw=dialog3.get_input()
            if diskpart.hash_comparisson(passw) == True:
                self.home_frame_text_box1.insert('0.1' ,'Пароль верный\n')
                x=diskpart.attach_virtual_disk_read_only(filename)
                print(filename)
                self.home_frame_text_box1.insert('0.1' ,f'Диск  {filename} подключен в режиме чтения\n')
            else:
                self.home_frame_text_box1.insert('0.1' ,'Пароль неверный\n')
            
        elif self.checkbox_1.get()==0:
           
            # dialog1=customtkinter.CTkInputDialog(text="Введите путь", title="Путь")
            # vdisk_path=dialog1.get_input()
            filename = filedialog.askopenfilename()
            filename=filename.replace("/",'\\')
            path_vdisks.append(filename+extension)
            print('pvd',path_vdisks)
            dialog3=customtkinter.CTkInputDialog(text="Введите пароль", title="пароль")
            passw=dialog3.get_input()
            if diskpart.hash_comparisson(passw) == True:
                self.home_frame_text_box1.insert('0.1' ,'Пароль верный\n')
                diskpart.attach_virtual_disk(filename)
                print(filename)
                self.home_frame_text_box1.insert('0.1' ,f'Диск{filename} Подключен\n')
            else:
                self.home_frame_text_box1.insert('0.1' ,'Пароль неверный\n')   
    def remove_disk_event(self):
        # dialog1=customtkinter.CTkInputDialog(text="Введите путь", title="Путь")
        filename = filedialog.askopenfilename()
        filename=filename.replace("/",'\\')
        diskpart.detach_virtual_disk(filename)
        self.home_frame_text_box1.insert('0.1' ,f'Диск {filename} Отключен\n')
    def create_backup_event(self):
        dialog1=customtkinter.CTkInputDialog(text="Введите путь виртуального диска", title="Путь к виртуальному диску")
        vhd_path=dialog1.get_input()
        dialog2=customtkinter.CTkInputDialog(text="Введите путь сохранения бэкапа", title="Путь к сохрание бэкапа")
        backup_path=dialog2.get_input()
        d= diskpart.backup(vhd_path,backup_path)
        success=str(f'Создан бэкап файла {vhd_path} в {backup_path}\n')                   
        self.third_frame_text_box1.insert('0.1' ,success ,'\n')
    def open_file_dialog(self):
    # Открываем окно выбора файла
        filename = filedialog.askopenfilename()
    # Выводим путь к выбранному файлу на customtkinter
        self.third_frame_text_box1.insert('0.1',filename)
def on_closing():
    for disk in range(len(path_vdisks)):
        if len(path_vdisks) !=0:
            diskpart.detach_virtual_disk(path_vdisks[disk])
    app.destroy()       

    
if __name__ == "__main__":
    app = App()
    #app.protocol("WM_DELETE_WINDOW",on_closing)
    app.mainloop()
