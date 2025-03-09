from tkinter import *

class DataEntry():
    def __init__(self, frame_container, text, required=True):
        self.required = required  # Guardar el valor de required
        self.__FR_COMPONENT = Frame(frame_container)
        self.__FR_COMPONENT.pack()

        self.__LBL_DATA = Label(self.__FR_COMPONENT, text=text, font=("Arial", 10, "bold"), anchor="w")
        self.__LBL_DATA.pack(fill=X)

        self.__IN_DATA = Entry(self.__FR_COMPONENT, font=("Arial"), bd=0, highlightbackground="red",highlightcolor="red")
        self.__IN_DATA.pack()

        self.__IN_DATA.bind("<Key>", self.reset_warning)  
    
    def reset_warning(self, event):
        """Elimina alerta"""
        self.__IN_DATA.config(highlightthickness=0)

    def get_data(self):
        """Obtiene datos ingresados"""
        if self.required and len(self.__IN_DATA.get()) == 0:
            self.__IN_DATA.config(highlightthickness=1)  # Mostrar borde rojo si está vacío
        else:
            return self.__IN_DATA.get()

root = Tk()
root.geometry("400x250")
user = DataEntry(root, "Usuario")
pasw = DataEntry(root, "Contraseña")
def execute_login():
    print(pasw.get_data(),user.get_data())
Button(root, text="Execute function", command=lambda: execute_login()).pack()

root.mainloop()
