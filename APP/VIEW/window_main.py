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
            if item == "Inicio":
                bg = "white"; fg = "black"
            else:
                bg = "black"; fg = "white"
            btn = Button(
                f_btn,
                text=item,
                font=("Arial", 12, "bold"),
                fg=fg,
                bg=bg,
                relief="flat",
                anchor="center",
                width=15,
                cursor="hand2"
            )
            btn.config(command=partial(self.navigator_tab, btn))
            btn.pack(fill="x", padx=10, pady=2)
            self.botones.append(btn)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)

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
        """This function is responsible for the visibility and selection of the tabs."""
        
        #Return to initial settings with background and foreground for default
        for i in self.botones[:]:
            if i.cget("text") != btn_press.cget("text"):
                i.config(bg="black",fg="white")
        #Set bg and fg to button selected
        btn_press.config(bg="white",fg="black")

        # Disable all tabs where the button text is different from the selected one
        for clave, valor in self.tab_items.items():
            if clave != btn_press['text']:
                valor.view_off()
                print(clave, "OFF")

        # Activated tab for button selected        
        self.tab_items[btn_press['text']].view_on()
        
    def on_enter(self,e):
        if e.widget.cget("fg") != "black" and e.widget.cget("bg") != "white":
            e.widget.config(bg="gray", fg="white")

    def on_leave(self,e):
        # print("CONFIGURACION WIDGET :",e.widget.configure(),e.widget.cget("bg"),e.widget.cget("fg"))
        
        if e.widget.cget("fg") != "black" and e.widget.cget("bg") != "white":
            e.widget.config(bg="black", fg="white")