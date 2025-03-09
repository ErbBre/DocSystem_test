from tkinter import *

#Show information operation succesfully with Buttom ok 
#Show Error whit Buttom Ok
#show question Yes No before execute process

class ShowMessageQuestion():
    def __init__(self,root,title_window,p_message,type_icon):
        
        s_width, s_height = [root.winfo_screenwidth(), root.winfo_screenheight()] 
        v_sizew, v_sizeh = [int(s_width/5), int(s_height/5)]
        v_coorx, v_coory = [int((s_width/2) - (v_sizew/2)), int((s_height/2) - (v_sizeh/2))] 

        root.geometry(f"{v_sizew}x{v_sizeh}+{v_coorx}+{v_coory}")

        root.overrideredirect(True)
        root.resizable(0,0)
        root.config(bg="white")
        Label(root, text=title_window, font=("Arial",12,"bold"), anchor="w", bg="#0aa06e",fg="white").pack(fill=X)
        self.imagen = PhotoImage(file="APP/VIEW/SOURCE/comprobado.png")
        Label(root, image=self.imagen, bg="white").pack(fill=X,padx=10,pady=10)
        
        Label(root , text = p_message, bg = "white", fg = "black", font = ("Arial", 11,"bold")).pack(fill = X)

        f_btn = Frame(root,bg="white")
        f_btn.pack()
        f_btnok = Button(f_btn, text = "Ok", font = ("Arial", 12, "bold"),bg="#0aa06e",fg="white", border=0,width=10, cursor="hand2")
        f_btnok.pack(side = LEFT,pady=10)
        # f_btncancel = Button(f_btn, text = "Cancelar", font = ("Arial", 12, "bold"))
        # f_btncancel.pack(side = RIGHT)

v_title = "DCSystem"
v_message = "Actualizado correctamente"

root = Tk()
Message=ShowMessageQuestion(root, v_title,v_message,"warning")
root.mainloop()