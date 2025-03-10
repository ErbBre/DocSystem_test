from tkinter import *

class Login_app:
    def __init__(self,root):
        
        root.title("Login DCSystem - Versión 1.0.0")
        root.geometry("960x540")
        root.resizable(0, 0)

        # ====================================================================
        # FRAME 2 (Imagen de Portada)
        # ====================================================================
        FR2 = Frame(root, width=480, height=540, bg="lightgray")
        FR2.pack(fill="both", side=RIGHT)

        self.imagen = PhotoImage(file="SOURCE/portadaPNG.png")
        self.imagen = self.imagen.subsample(1)
        label_imagen = Label(FR2, image=self.imagen, bg="white", border=0)
        label_imagen.pack(expand=True)

        # ====================================================================
        # FRAME 1 (Formulario de Login)
        # ====================================================================
        FR1 = Frame(root, width=480, height=540)
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
        EN_USER = Entry(FR1, font = ("Arial", 12))
        EN_USER.pack(pady=5)

        # ====================================================================
        # Contraseña con botón de mostrar/ocultar
        # ====================================================================
        Label(FR1, text = "Contraseña", font = ("Arial", 12, "bold"), bg = "white").pack(pady=5)

        def toggle_password():
            if EN_PASS["show"] == "*":
                EN_PASS.config(show="")
            else:
                EN_PASS.config(show="*")

        frame_pass = Frame(FR1, bg = "white")
        frame_pass.pack(pady = 5)

        EN_PASS = Entry(frame_pass, font = ("Arial", 12), show = "*")
        EN_PASS.pack(side = LEFT)

        BTN_TOGGLE = Button(frame_pass, text= "BTN", command = toggle_password)
        BTN_TOGGLE.pack(side=LEFT, padx=5)

        # ====================================================================
        # Botón de inicio de sesión
        # ====================================================================
        BTN_LOGIN = Button(FR1, text="Iniciar Sesión", font=("Arial", 12, "bold"))
        BTN_LOGIN.pack(pady=20)
    def test_function(self):
        """Hola my dog"""
        pass