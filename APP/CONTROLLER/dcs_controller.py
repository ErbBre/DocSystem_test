"""
=====================================================
  Módulo: controlador.py (Controller)
  Descripción:
      Este módulo actúa como intermediario entre la Vista y el Modelo.
      Se encarga de procesar las acciones del usuario y actualizar la vista 
      o el modelo según corresponda.

  Funcionalidades principales:
      - Recibir entradas del usuario desde la Vista.
      - Llamar a las funciones adecuadas del Modelo.
      - Actualizar la interfaz de usuario con nueva información.

  Uso:
      from controlador import Controlador
      app = Controlador()
      app.ejecutar()

  Requisitos:
      - Dependencias: modelo.py, vista.py.

  Autor(es): [Nombre(s)]
  Versión: 1.0.0
  Última actualización: [DD/MM/AAAA]
=====================================================
"""
from tkinter import *
from APP.MODEL.dcs_model import ModeloDB
from APP.VIEW.window_main import VistaPrincipal

class Controlador:
    def __init__(self):
        self.db = ModeloDB()
    def iniciar_sesion(self,root, usuario, contrasena):
        """
        Funcionalidades:
        - Validación de credenciales.
        - Mensajes de error en caso de datos incorrectos.
        """
    
        if self.db.get_user_verify(usuario, contrasena):
            # Si el proceso de login es correcto entonces limpiamos 
            # los widgets de la ventana del login para crear la interfaz 
            # principal
            for widget in root.winfo_children():
                widget.destroy()  # Elimina cada widget del frame
            
            # Ejecuta el metodo que crea los elementos de la ventana principal
            self.mostrar_ventana_principal(root)
        else:
            print("Ha ocurrido un error al iniciar sesion")

    def mostrar_ventana_principal(self,main_root):
        
        #Habilita ventana redimensionable
        main_root.resizable(1, 1)
        # Ejecuta el modulo de la vista principal
        VistaPrincipal(main_root)
