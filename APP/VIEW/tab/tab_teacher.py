from tkinter import*
from tkinter.ttk import Notebook

class tab_teacher:
    def __init__(self,main_frame):
        self.__main_tab_frame = Frame(main_frame, bg="red")
        self.__main_tab_frame.pack(expand=True,fill='both')

        topframe = Frame(self.__main_tab_frame)
        topframe.pack(expand=True,fill='both')
        # Label(topframe, text="TAB MAESTRO").pack()
        
        notebook = Notebook(topframe)
        notebook.pack(expand=True, fill='both')

        
        # Crear los marcos (frames) que serán las pestañas
        tab1 = Frame(notebook, bg='lightblue')
        tab2 = Frame(notebook, bg='lightgreen')
        tab3 = Frame(notebook, bg='lightgreen')
        tab4 = Frame(notebook, bg='lightgreen')
        tab5 = Frame(notebook, bg='lightgreen')
        tab6 = Frame(notebook, bg='lightgreen')
        tab7 = Frame(notebook, bg='lightgreen')
        tab8 = Frame(notebook, bg='lightgreen')
        tab9 = Frame(notebook, bg='lightgreen')

        # Agregar pestañas al notebook
        notebook.add(tab1, text='Pestaña 1')
        notebook.add(tab2, text='Pestaña 2')
        notebook.add(tab3, text='Pestaña 2')
        notebook.add(tab4, text='Pestaña 2')
        notebook.add(tab5, text='Pestaña 2')
        notebook.add(tab6, text='Pestaña 2')
        notebook.add(tab7, text='Pestaña 2')
        notebook.add(tab8, text='Pestaña 2')
        notebook.add(tab9, text='Pestaña 2')
        
        # Agregar contenido a cada pestaña
        Label(tab1, text="Contenido de la pestaña 1").pack(pady=20)
        Label(tab2, text="Contenido de la pestaña 2").pack(pady=20)
        #INICIALIZA EL TAB COMO OCULTO
        self.view_off()

    def view_on(self):
        """Enabled visibility of the tab"""
        self.__main_tab_frame.pack(expand=True,fill=BOTH)

    def view_off(self):
         """Disabled visibility of the tab"""
         self.__main_tab_frame.pack_forget()