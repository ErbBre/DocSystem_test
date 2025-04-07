"""
Este script define dos clases: `DataEntry` y `DataEntryPass`, que permiten crear entradas de datos personalizadas con un campo de texto y una etiqueta utilizando Tkinter.

La clase `DataEntry` proporciona una estructura básica para crear campos de entrada con etiquetas y la posibilidad de validar si el campo es obligatorio.
La clase `DataEntryPass` extiende la funcionalidad de `DataEntry` y agrega características específicas para crear un campo de entrada de contraseña, que permite al usuario alternar la visibilidad de la contraseña ingresada.

Clases:
`DataEntry`: 
    - Crea un campo de entrada con su etiqueta correspondiente.
    - Permite definir si el campo es obligatorio.
    - Implementa una validación visual (borde rojo) si el campo está vacío y es obligatorio.
    - Proporciona un `getter` y `setter` para modificar y acceder al widget `Entry`.
    
`DataEntryPass`: 
    - Hereda de `DataEntry` y modifica el campo de entrada para mostrar u ocultar la contraseña.
    - Añade un botón para alternar la visibilidad de la contraseña ingresada utilizando un ícono.
    
Métodos importantes:
    - `reset_warning`: Elimina el borde rojo de advertencia cuando el usuario comienza a escribir.
    - `get_data`: Devuelve el texto ingresado en el campo de entrada, mostrando una advertencia si el campo es obligatorio y está vacío.
    - `in_data`: Un `getter` y `setter` para modificar el campo de entrada.
    - `_show_password`: Alterna la visibilidad de la contraseña en la subclase `DataEntryPass`.

El script también proporciona un ejemplo comentado de cómo se pueden usar las clases para crear un formulario de inicio de sesión con usuario y contraseña.

Uso:
    1. Crear una instancia de `DataEntry` para campos estándar.
    2. Crear una instancia de `DataEntryPass` para campos de contraseña.
    3. Usar los métodos `get_data` para obtener la entrada del usuario.
    4. (Opcional) Usar el botón para alternar la visibilidad de la contraseña.


Tecnologías:
    - Python con Tkinter
    - Base de datos: Supabase

Autor(es):  
    - Breyner Morales 
Fecha de creación: [17/03/2025]
Última actualización: [17/03/2025]
"""
from tkinter import *

class DataEntry():
    def __init__(self, frame_container, text, required=True):
        self.required = required  # Guardar el valor de required
        self.__FR_COMPONENT = Frame(frame_container, bg="white")
        self.__FR_COMPONENT.pack()

        self.__LBL_DATA = Label(self.__FR_COMPONENT, text=text, font=("Arial", 11, "bold"), anchor="w", bg="white")
        self.__LBL_DATA.pack(fill=BOTH)
        self.__FR_ENTRY = Frame(self.__FR_COMPONENT, bg="white")
        self.__FR_ENTRY.pack()
        self.__IN_DATA = Entry(self.__FR_ENTRY, font=("Arial"), bd=0, highlightbackground="red",highlightcolor="red", bg="lightgrey")
        self.__IN_DATA.grid(column=0, row=0)

        self.__IN_DATA.bind("<Key>", self._reset_warning)  
    
    def _reset_warning(self, event):
        """Elimina alerta"""
        self.__IN_DATA.config(highlightthickness=0)

    def get_data(self):
        """Obtiene datos ingresados"""
        if self.required and len(self.__IN_DATA.get()) == 0:
            self.__IN_DATA.config(highlightthickness=1)  # Mostrar borde rojo si está vacío
        else:
            return self.__IN_DATA.get()
    def init_focus_entry(self):
        """Active focus in Entry"""
        self.__IN_DATA.focus_set()

    @property
    def in_data(self):
        """Getter para obtener __IN_DATA"""
        return self.__IN_DATA
    
    @in_data.setter
    def in_data(self, nuevo_widget):
        """Setter para cambiar __IN_DATA desde una subclase"""
        self.__IN_DATA = nuevo_widget
    
    @property
    def frame_in(self):
        """Propiedad para acceder al Frame"""
        return self.__FR_ENTRY

class DataEntryPass(DataEntry):
    def __init__(self, frame_container, text, required=True):
        super().__init__(frame_container, text, required)
        self.__pivot = True
        self.img_on = PhotoImage(file="SOURCE/pass_on.png")
        self.img_off = PhotoImage(file="SOURCE/pass_off.png")
        self.in_data.config(show="●")
        self.SHOW_PASS = Button(self.frame_in,image=self.img_on,command=lambda:self._show_password(),bd=0, bg="white")
        self.SHOW_PASS.grid(row=1,column=0,sticky="e")
    def _show_password(self):
        if self.__pivot:
            self.__pivot = False
            self.SHOW_PASS.config(image=self.img_off)
            self.in_data.config(show="")
        else:
            self.__pivot = True
            self.SHOW_PASS.config(image=self.img_on)
            self.in_data.config(show="●")


# root = Tk()
# root.geometry("400x250")
# user = DataEntry(root, "Usuario")
# pasw = DataEntryPass(root, "Contraseña")
# def execute_login():
#     print(pasw.get_data(),user.get_data())
# Button(root, text="Execute function", command=lambda: execute_login()).pack()

# root.mainloop()