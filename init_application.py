def main():
    root = Tk()

    # Paso 1: Instanciar el Modelo
    model = LoginModel()

    # Paso 2: Instanciar la Vista
    view = LoginView(root)

    # Paso 3: Instanciar el Controlador
    controller = LoginController(view, model)

    # Paso 4: Ejecutar el bucle de eventos de Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
