from tkinter import *

#v_title = "Titulo"
v_message = "MAMAHUEVO"

root = Tk()
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
v_sizew, v_sizeh = [int(s_width/6), int(s_height/5)]
v_coorx, v_coory = [int((s_width/2) - (v_sizew/2)), int((s_height/2) - (v_sizeh/2))] 

root.geometry(f"{v_sizew}x{v_sizeh}+{v_coorx}+{v_coory}")


#root.title(v_title)
root.overrideredirect(True)
root.resizable(0,0)


f_main = Frame(root, bg = "green")
f_main.pack(fill = BOTH, expand = TRUE, padx = 10, pady = 10)
f_top = Frame(f_main, bg = "blue")
f_top.pack(fill = X)
f_below = Frame(f_main, bg = "red")
f_below.pack(fill = X)
Label(f_top , text = v_message, bg = "blue", fg = "white", font = ("Arial", 12)).pack(fill = X)

f_btn = Frame(root)
f_btn.pack()
f_btnok = Button(f_btn, text = "Aceptar", font = ("Arial", 12, "bold"))
f_btnok.pack(side = LEFT)
f_btncancel = Button(f_btn, text = "Cancelar", font = ("Arial", 12, "bold"))
f_btncancel.pack(side = RIGHT)


root.mainloop()