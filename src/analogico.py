from tkinter import *

class Analogico(Tk):

    def __init__(self):


        # METODOS PARA LA VENTANA
        super().__init__()
        self.__iniciar_caracteristicas_ventana()

        # METODOS PARA LA INICIALIZACION DE LOS WIDGETS
        # self.__iniciar_componentes()

        # LOOP PRINCIPAL
        self.mainloop()

    def __iniciar_caracteristicas_ventana(self):
        self.__tamano_ventana()
        self.__color_titulo_ventana()

    def __tamano_ventana(self):
        self.resizable(False, False)
        ancho = 500
        alto = 200

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - ancho) // 2
        y = (screen_h - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def __color_titulo_ventana(self):
        self.title("SERVOMOTOR ANALOGICO")
        self.config(bg='white')