from tkinter import *
from src.digital import Digital

class Frame(Tk):

    def __init__(self, x, y, title):

        self.__x = x
        self.__y = y
        self.__title = title

        #METODOS PARA LA VENTANA
        super().__init__()
        self.__iniciar_caracteristicas_ventana()

        #LOOP PRINCIPAL
        self.mainloop()

    def __iniciar_caracteristicas_ventana(self):
        self.__tamano_ventana()
        self.__color_titulo_ventana()

    def __tamano_ventana(self):

        self.resizable(False, False)
        ancho = self.__x
        alto = self.__y

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        x = (screen_w - ancho) // 2
        y = (screen_h - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")
    def __color_titulo_ventana(self):
        self.title(f"{self.__title}")
        self.config(bg='white')


