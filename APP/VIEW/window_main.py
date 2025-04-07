"""
=====================================================
  Módulo: window_main.py (View)
  Descripción:
      Este módulo gestiona la interfaz de usuario del sistema.
      Se encarga de mostrar la información y recibir entradas del usuario.

  Funcionalidades principales:
      - Renderizar la interfaz gráfica (GUI).
      - Capturar la interacción del usuario.
      - Mostrar los datos obtenidos del modelo.

  Uso:
    from APP.VIEW.window_main import VistaPrincipal
    self.mostrar_ventana_principal(root)

  Requisitos:
      - Librerías necesarias: Tkinter

  Autor(es):  
    - Mijael Medina
  Versión: 1.0.0
  Última actualización: [17/03/2025]
=====================================================
"""
from tkinter import *
from functools import partial
from APP.VIEW.tab.tab_inicio     import tab_inicio
from APP.VIEW.tab.tab_teacher    import tab_teacher
from APP.VIEW.tab.tab_curso      import tab_curso
from APP.VIEW.tab.tab_report     import tab_report
from APP.VIEW.tab.tab_student    import tab_student
from APP.VIEW.tab.tab_calendario import tab_calendario
from APP.VIEW.tab.tab_finance    import tab_finance
from APP.VIEW.tab.tab_almacen    import tab_almacen
from APP.VIEW.tab.tab_perfil     import tab_perfil
from APP.VIEW.tab.tab_config     import tab_config
class VistaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("DCS System Dashboard")
        
        sidebar = Frame(self.root, bg="black")
        sidebar.pack(side="left", fill="y")

        Label(sidebar, text="Admin", fg="white", bg="black", font=("Arial", 12, "bold")).pack(pady=10)
        f_menu = Frame(sidebar, bg="black")
        f_menu.pack(pady=10,fill="both", expand=True)
        f_btn = Frame(f_menu, bg="black")
        f_btn.pack(expand=True)

        menu_items = ["Inicio", "Maestros", "Cursos", "Reportes", "Alumnos", "Calendario", "Finanzas", "Almacén", "Perfil", "Configuración"]
        
        self.botones = []  # Lista para guardar los botones
        
        for item in menu_items:
            btn = Button(
                f_btn,
                text=item,
                font=("Arial", 12, "bold"),
                fg="white",
                bg="black",
                relief="flat",
                anchor="center",
                width=15
            )
            btn.config(command=partial(self.navigator_tab, btn))
            btn.pack(fill="x", padx=10, pady=2)
            self.botones.append(btn)

        Button(sidebar, text="Cerrar sesión", font = ("Arial", 12, "bold"), fg="white", bg="red", relief="flat").pack(fill="x",side="bottom")


        main_frame = Frame(self.root)
        main_frame.pack(side="right", fill="both", expand=True)

        self.tab_items = {"Inicio":       tab_inicio(main_frame), 
                          "Maestros":     tab_teacher(main_frame), 
                          "Cursos":       tab_curso(main_frame), 
                          "Reportes":     tab_report(main_frame), 
                          "Alumnos":      tab_student(main_frame), 
                          "Calendario":   tab_calendario(main_frame), 
                          "Finanzas":     tab_finance(main_frame), 
                          "Almacén":      tab_almacen(main_frame), 
                          "Perfil":       tab_perfil(main_frame), 
                          "Configuración":tab_config(main_frame)
        }
        
        # self.tab_items["Inicio"].view_on()
        # teacher = tab_teacher(main_frame)
        # self.navigator_tab("Inicio")

    def navigator_tab(self,btn_press):
        # print(btn_press['text'])
        self.tab_items[btn_press['text']].view_on()
        for clave, valor in self.tab_items.items():
            if clave != btn_press['text']:
                valor.view_off()
                print(clave, "OFF")
            # else:
            #     valor.view_on()
            #     print(clave, "ON")
            
            # print(f"Clave: {clave} - Valor: {valor}")   