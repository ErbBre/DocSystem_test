"""
=====================================================
  Archivo: DCSystem.py (Punto de entrada)
  Descripción:
      Este es el punto de inicio de la aplicación.
      Se encarga de inicializar y ejecutar la aplicación
      siguiendo el patrón Modelo-Vista-Controlador (MVC).

  Funcionalidades principales:
      - Importar y configurar los módulos del sistema.
      - Crear instancias del Controlador y ejecutar la aplicación.
      - Manejar posibles errores globales.

  Uso:
      Ejecutar el script desde la terminal o un entorno de desarrollo:
      
          python main.py

  Dependencias:
      - dcs_model.py (Manejo de datos)
      - window_main.py (Interfaz de usuario)
      - dcs_controller.py (Lógica de negocio)

  Autor(es):
    - Breyner Morales 
    - Mijael Medina 
  Versión: 1.0.0
  Última actualización: [17/03/2025]
=====================================================
"""
from tkinter import*
from APP.CONTROLLER.dcs_controller import Controlador
from APP.VIEW.Login_app import Login_app

if __name__ == "__main__":
    try:
        root = Tk()

        # INSTANCIA DEL CONTROLADOR
        controlador = Controlador()

        Login_app(root, controlador)
        
        root.mainloop()
    except ValueError:
        print("Ha ocurrido un error")