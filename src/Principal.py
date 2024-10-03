from tkinter import *

class Principal(Tk):

    def __init__(self):

        #ATRIBUTOS PARA LOS WIDGETS
        self.__opcion_analogico_digital = None
        self.__lb_titulo = None
        self.__lb_seleccion = None
        self.__rb_analogico = None
        self.__rb_digital = None
        self.__bt_conectar = None

        #METODOS PARA LA VENTANA
        super().__init__()
        self.__iniciar_caracteristicas_ventana()

        # METODOS PARA LA INICIALIZACION DE LOS WIDGETS
        self.__iniciar_componentes()

        #LOOP PRINCIPAL
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
        self.title("ARDUINO SERVOMOTOR")
        self.config(bg='white')

    def __iniciar_componentes(self):
        self.__iniciar_radio_button()
        self.__iniciar_botones()
        self.__iniciar_labels()

    def __iniciar_labels(self):
        self.__lb_titulo = Label(text='SERVMOTOR')
        self.__lb_titulo.config(bg='white', fg='black', font='arial 20')
        self.__lb_titulo.place(x=10, y=10)

        self.__lb_seleccion = Label(text="Seleccione el tipo de sensor")
        self.__lb_seleccion.config(bg='white', fg='black', font='arial 12')
        self.__lb_seleccion.place(x=20, y=60)

    def __iniciar_radio_button(self):
        self.__opcion_analogico_digital = IntVar()
        self.__opcion_analogico_digital.set(1)

        self.__rb_analogico = Radiobutton(self, text="Analogico", variable=self.__opcion_analogico_digital, value=1)
        self.__rb_analogico.config(bg='white', fg='black', font='arial 12')
        self.__rb_analogico.place(x=20, y=90)

        self.__rb_digital = Radiobutton(self, text="Digital", variable=self.__opcion_analogico_digital, value=2)
        self.__rb_digital.config(bg='white', fg='black', font='arial 12', cursor='hand2')
        self.__rb_digital.place(x=120, y=90)

    def __iniciar_botones(self):
        self.__bt_conectar = Button(self, text="Aceptar", command=self.__configuracion_arduino)
        self.__bt_conectar.config(bg='#3498db', fg='white', font='arial 10', activebackground="#21618c", activeforeground="#fff")
        self.__bt_conectar.place(x=20, y=140)

    def __configuracion_arduino(self):
        if self.__opcion_analogico_digital.get() == 1:
            self.destroy()
            from src.analogico import Analogico
            frame_analogico = Analogico()
        else:
            self.destroy()
            from src.digital import Digital
            frame_digital = Digital()


