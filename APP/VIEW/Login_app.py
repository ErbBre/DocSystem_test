"""
=====================================================
  Módulo: Interfaz de Inicio de Sesión (Login)
  Descripción:
    Este módulo define la ventana de inicio de sesión para los usuarios.
    Permite la autenticación mediante nombre de usuario y contraseña.
    
  Funcionalidades:
    - Entrada de usuario y contraseña.
    - Botón para iniciar sesión y salir de la aplicación.
    
  Tecnologías:
    - Python con Tkinter
    - Base de datos: Supabase
    
  Autor(es): 
    - Mijael Medina 
    - Breyner Morales 
  Fecha de creación: [17/03/2025]
  Última actualización: [17/03/2025]
=====================================================
"""
from tkinter import *

class Login_app:
    def __init__(self,root,controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Login DCSystem - Versión 1.0.0")
        self.root.geometry("960x540")
        self.root.resizable(0, 0)

        # ====================================================================
        # FRAME 2 (Imagen de Portada)
        # ====================================================================
        FR2 = Frame(self.root, width=480, height=540, bg="lightgray")
        FR2.pack(fill="both", side=RIGHT)

        self.imagen = PhotoImage(file="SOURCE/portadaPNG.png")
        self.imagen = self.imagen.subsample(1)
        label_imagen = Label(FR2, image=self.imagen, bg="white", border=0)
        label_imagen.pack(expand=True)

        # ====================================================================
        # FRAME 1 (Formulario de Login)
        # ====================================================================
        FR1 = Frame(self.root, width=480, height=540)
        FR1.pack(fill="both", expand=True, side=LEFT)

        Label(FR1, text="DCSYSTEM", font=("Arial", 30, "bold"), bg="white").pack(pady=20)
        # ====================================================================
        # Icono debajo del nombre
        # ====================================================================
        self.icono = PhotoImage(file="SOURCE/portadaPNG.png")
        self.icono = self.icono.subsample(8)  # Redimensionar a 60x60 px
        Label(FR1, image = self.icono, bg = "white").pack(pady=5)

        # ====================================================================
        # Usuario
        # ====================================================================
        Label(FR1, text = "Usuario", font = ("Arial", 12, "bold"), bg = "white").pack(pady=5)
        self.EN_USER = Entry(FR1, font = ("Arial", 12))
        self.EN_USER.pack(pady=5)

        # ====================================================================
        # Contraseña con botón de mostrar/ocultar
        # ====================================================================
        Label(FR1, text = "Contraseña", font = ("Arial", 12, "bold"), bg = "white").pack(pady=5)

        def toggle_password():
            if self.EN_PASS["show"] == "*":
                self.EN_PASS.config(show="")
            else:
                self.EN_PASS.config(show="*")

        frame_pass = Frame(FR1, bg = "white")
        frame_pass.pack(pady = 5)

        self.EN_PASS = Entry(frame_pass, font = ("Arial", 12), show = "*")
        self.EN_PASS.pack(side = LEFT)

        BTN_TOGGLE = Button(frame_pass, text= "BTN", command = toggle_password)
        BTN_TOGGLE.pack(side=LEFT, padx=5)

        # ====================================================================
        # Botón de inicio de sesión
        # ====================================================================
        self.BTN_LOGIN = Button(FR1, text="Iniciar Sesión", font=("Arial", 12, "bold"),command=lambda:self.user_login())
        self.BTN_LOGIN.pack(pady=20)
    def user_login(self):
        """Funcion que envia datos ingresados por el usuario al controlador"""
        usuario = self.EN_USER.get()
        contrasena = self.EN_PASS.get()
        
        #Ejecuta metodo del controlador para iniciar sesion
        self.controlador.iniciar_sesion(self.root,usuario, contrasena)