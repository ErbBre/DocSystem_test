from tkinter import*


class tab_perfil:
    def __init__(self,main_frame):
        self.__main_tab_frame = Frame(main_frame, bg="grey")
        self.__main_tab_frame.pack(expand=True,fill=BOTH)

        topframe = Frame(self.__main_tab_frame)
        topframe.pack()
        Label(topframe, text="TAB PERFIL").pack()

        #INICIALIZA EL TAB COMO OCULTO
        self.view_off()

    def view_on(self):
        """Enabled visibility of the tab"""
        self.__main_tab_frame.pack(expand=True,fill=BOTH)

    def view_off(self):
         """Disabled visibility of the tab"""
         self.__main_tab_frame.pack_forget()