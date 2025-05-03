from tkinter import*
from datetime import datetime


class tab_inicio:
    def __init__(self,main_frame):
        
        self.__main_tab_frame = Frame(main_frame)
        self.__main_tab_frame.pack(expand=True,fill=BOTH)
        topframe = Frame(self.__main_tab_frame, bg="white")
        topframe.pack(fill="x", side = "top")

        Label(topframe, text="DCS System Dashboard", font=("Arial", 20, "bold"), bg="white").pack(pady=10,side="left")
        f_reloj = Frame(topframe, bg="white")
        f_reloj.pack(side="right")

        clock_label = Label(f_reloj,font=("Arial", 20, "bold"), bg="white")
        clock_label.pack(side="top")
        date_label = Label(f_reloj, font=("Arial", 12), bg="white")
        date_label.pack(side="bottom")

        def update_clock():
            day_today = self.traduction(datetime.now().strftime("%A"),"day")
            month_today = self.traduction(datetime.now().strftime("%B"),"month")
            clock_label.config(text=datetime.now().strftime("%I:%M:%S %p"))
            date_label.config(text=datetime.now().strftime(f"{day_today} %d de {month_today} de %Y"))
            topframe.after(1000, update_clock)

        update_clock()


        metrics_frame = Frame(self.__main_tab_frame, bg="white")
        metrics_frame.pack(pady=20)

        metricas = [
            ("Alumnos inscritos", 156),
            ("Promedio general", 17),
            ("Maestros activos", 60),
            ("Estudiantes en AE", 14)
        ]

        for text, value in metricas:
            frame = Frame(metrics_frame, relief="solid", borderwidth=1, padx=10, pady=5)
            frame.pack(side="left", padx=10)
            
            Label(frame, text=value, font=("Helvetica", 45, "bold")).pack()
            Label(frame, text=text, font=("Arial", 20, "bold")).pack()
        
    def traduction(self,data,type):
            if type == "month":
                months = {"January":"Enero", "February":"Febrero", "March":"Marzo", 
                        "April":"Abril", "May":"Mayo", "June":"Junio", "July":"Julio", 
                        "Agust":"Agosto", "September":"Septiembre", "November":"Noviembre", 
                        "December":"Diciembre"}
                return months[data]
            
            elif type == "day":
                days = {"Monday":"Lunes", "Tuesday":"Martes", 
                        "Wednesday":"Miercoles", "Thursday":"Jueves", 
                        "Friday":"Viernes", "Saturday":"Sabado", "Sunday":"Domingo"}
                return days[data]
    
    def view_on(self):
        """Enabled visibility of the tab"""
        self.__main_tab_frame.pack(expand=True,fill=BOTH)

    def view_off(self):
         """Disabled visibility of the tab"""
         self.__main_tab_frame.pack_forget()
