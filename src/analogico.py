from tkinter import *
from tkinter import messagebox
import serial
import time

class Analogico(Tk):

    def __init__(self):

        # ATRIBUTOS PARA LOS WIDGETS
        self.__lb_titulo = None
        self.__lb_seleccion = None
        self.__sc_angulo = None

        # Variable conexion arduino
        self.__con_arduino = None

        # METODOS PARA LA VENTANA
        super().__init__()
        self.__iniciar_caracteristicas_ventana()

        # METODOS PARA LA INICIALIZACION DE LOS WIDGETS
        self.__iniciar_componentes()

        # INTERCEPATR EL EVENTO DE CERRAR LA VENTANA
        self.protocol("WM_DELETE_WINDOW", self.__cerrar_ventana)

        # CONEXION A ARDUINO
        self.__conectar_arduino()

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

    def __iniciar_componentes(self):
        self.__iniciar_labels()
        self.__iniciar_scale()

    def __iniciar_labels(self):
        self.__lb_titulo = Label(text='ANALÓGICO')
        self.__lb_titulo.config(bg='white', fg='black', font='arial 20')
        self.__lb_titulo.place(x=10, y=10)

        self.__lb_seleccion = Label(text="Angulo: 0")
        self.__lb_seleccion.config(bg='white', fg='black', font='arial 12')
        self.__lb_seleccion.place(x=20, y=60)

    def __iniciar_scale(self):
        self.__sc_angulo = Scale(self, from_=0, to=180, orient=HORIZONTAL, command=self.__enviar_angulos_arduino)
        self.__sc_angulo.config(bg='white', fg='black', font='arial 10', length=400, sliderlength=20)
        self.__sc_angulo.place(x=20, y=90)

    def __enviar_angulos_arduino(self, angulo):
        text = f'Angulo: {angulo}'
        self.__lb_seleccion.config(text=text)
        self.__con_arduino.write(f'{angulo}\n'.encode())
        print(f"Conectado con Arduino Servomotor. Grados: {angulo}")


    def __conectar_arduino(self):
        try:
            self.__con_arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)
            time.sleep(2)
        except:
            messagebox.showerror("Error", "No se pudo conectar con arduino\nAsegurate de conectarla al COM5 de tu PC")
            self.__con_arduino = None
            self.destroy()
            from src.Principal import Principal
            frame_prin = Principal()

    def __cerrar_ventana(self):

        if messagebox.askokcancel("Salir", "¿Estás seguro de volver al menu principal?"):
            self.__con_arduino.close()
            self.destroy()
            from src.Principal import Principal
            frame_prin = Principal()