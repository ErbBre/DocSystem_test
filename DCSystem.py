import tkinter as tk
from tkinter import ttk, PhotoImage

<<<<<<< HEAD
# Crear ventana principal
root = tk.Tk()
root.title("Login DCSystem - Versión 1.0.0")
root.geometry("960x540")
root.resizable(False, False)
=======
root = Tk()
root.title("Login DCSystem - Versión 1.0.0")
>>>>>>> 5f2b95c8817b1c92b8f25e4a1afed52579f7de40

# Dividir en dos secciones
left_frame = tk.Frame(root, width=480, height=540, bg='white')
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

right_frame = tk.Frame(root, width=480, height=540, bg='gray')
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# Agregar título
title_label = tk.Label(left_frame, text="DCSYSTEM", font=("Arial", 30, "bold"), bg='white')
title_label.pack(pady=20)

# Icono debajo del título (60x60 px)
icon_photo = PhotoImage(file="icon.png")
icon_label = tk.Label(left_frame, image=icon_photo, bg='white')
icon_label.pack()

# Labels y entradas
user_label = tk.Label(left_frame, text="Usuario", font=("Arial", 12, "bold"), bg='white')
user_label.pack(pady=5)
user_entry = ttk.Entry(left_frame)
user_entry.pack()

pass_label = tk.Label(left_frame, text="Contraseña", font=("Arial", 12, "bold"), bg='white')
pass_label.pack(pady=5)
password_entry = ttk.Entry(left_frame, show='*')
password_entry.pack()

def toggle_password(event):
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

password_entry.bind("<Button-3>", toggle_password)

# Botón de inicio de sesión
login_button = ttk.Button(left_frame, text="Iniciar sesión", style='TButton')
login_button.pack(pady=20)

# Cargar imagen de portada en el lado derecho
cover_photo = PhotoImage(file="cover.png")
cover_label = tk.Label(right_frame, image=cover_photo, bg='gray')
cover_label.pack()

# Ejecutar la aplicación
root.mainloop()
