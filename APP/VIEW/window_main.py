from tkinter import *
from datetime import datetime

root = Tk()
root.title("DCS System Dashboard")
#root.geometry("800x400")
#root.resizable(False, False)
def traduction(data,type):
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


sidebar = Frame(root, bg="black")
sidebar.pack(side="left", fill="y")

Label(sidebar, text="Admin", fg="white", bg="black", font=("Arial", 12, "bold")).pack(pady=10)
f_menu = Frame(sidebar, bg="black")
f_menu.pack(pady=10,fill="both", expand=True)
f_btn = Frame(f_menu, bg="black")
f_btn.pack(expand=True)

menu_items = ["Inicio", "Maestros", "Cursos", "Reportes", "Alumnos", "Calendario", "Finanzas", "Almacén", "Perfil", "Configuración"]
for item in menu_items:
    Button(f_btn, text=item,font= ("Arial", 12, "bold"), fg="white", bg="black", relief="flat", anchor="center", width=15).pack(fill="x", padx=10, pady=2)

Button(sidebar, text="Cerrar sesión", font = ("Arial", 12, "bold"), fg="white", bg="red", relief="flat").pack(fill="x",side="bottom")


main_frame = Frame(root, bg="white")
main_frame.pack(side="right", fill="both", expand=True)

topframe = Frame(main_frame)
topframe.pack(fill="x", side = "top")

Label(topframe, text="DCS System Dashboard", font=("Arial", 14, "bold"), bg="white").pack(pady=10,side="left")
f_reloj = Frame(topframe)
f_reloj.pack(side="right")

clock_label = Label(f_reloj,font=("Arial", 20, "bold"), bg="white")
clock_label.pack(side="top")
date_label = Label(f_reloj, font=("Arial", 12), bg="white")
date_label.pack(side="bottom")

def update_clock():
    day_today = traduction(datetime.now().strftime("%A"),"day")
    month_today = traduction(datetime.now().strftime("%B"),"month")
    clock_label.config(text=datetime.now().strftime("%I:%M:%S %p"))
    date_label.config(text=datetime.now().strftime(f"{day_today} %d de {month_today} del %Y"))
    root.after(1000, update_clock)

update_clock()


metrics_frame = Frame(main_frame, bg="white")
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

root.mainloop()
