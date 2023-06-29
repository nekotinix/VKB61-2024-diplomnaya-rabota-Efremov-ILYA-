import customtkinter 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("Шифрование Виртуальных Дисков")
        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)
        self.button.configure(text="new text")
        # add checkbox in class
        self.checkbox=customtkinter.CTkCheckBox(self,command=self.button_click)
        self.checkbox.grid(row=5, column=5, padx=20, pady=10)
        # add progressbar in program
        self.progressbar=customtkinter.CTkProgressBar(self)
        self.progressbar.grid(row=1,column=3,padx=20, pady=10)
        # add switch
        self.switch_var = customtkinter.StringVar()
        self.switch_mode = customtkinter.CTkSwitch(self.main_frame,text="🌙",font=("Arial", 25), variable=self.switch_var,onvalue="on", offvalue="off",command=self.change_appearance_mode_event)
        self.switch_mode.grid(row=5, column=0, pady=10, padx=20, sticky="n")
        #add entry
        self.entry=customtkinter.CTkEntry(self)
        self.entry.configure(width=20, height=1,placeholder_text="CTkEntry")
    # add methods to app
    def button_click(self):
        print("button click")
    def change_appearance_mode_event(self):
            if self.switch_var.get() == "on":
                customtkinter.set_appearance_mode("light")
                self.switch_mode.configure(text="☀👍")
            else:
                customtkinter.set_appearance_mode("dark")
                self.switch_mode.configure(text="😬🌙")
if __name__ == "__main__":
    app = App()
    app.resizable(width=False, height=False)
    app.mainloop()