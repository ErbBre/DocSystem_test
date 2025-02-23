import tkinter as tk
from time import strftime
import datetime

def actualizar_reloj():

    hora_actual = strftime('%I:%M:%S %p')
    label_hora.config(text=hora_actual)
    
    fecha_actual = datetime.datetime.now().strftime('%A %d de %B del %Y')
    label_fecha.config(text=fecha_actual.capitalize())

    root.after(1000, actualizar_reloj)

root = tk.Tk()
root.title("Reloj en Tiempo Real")

label_hora = tk.Label(root, font=('Arial', 50, 'bold'), fg='black')
label_hora.pack(pady=10)

label_fecha = tk.Label(root, font=('Arial', 25), fg='black')
label_fecha.pack(pady=10)

actualizar_reloj()

root.mainloop()

