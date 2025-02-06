from tkinter import *

root = Tk()
root.geometry("940x560")

# Crear un Frame
FR = Frame(root)
FR.pack(fill=BOTH, expand=True)

# Cargar la imagen
img = PhotoImage(file="test/DocSystem_test/SOURCE/portadaPNG.png")

# Crear un Label con la imagen
label = Label(FR, image=img)
label.pack()

# Mantener la referencia a la imagen
label.image = img

# Iniciar el bucle principal
root.mainloop()
