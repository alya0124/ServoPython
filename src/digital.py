from tkinter import *
from tkinter import messagebox
import serial
import time

class Digital(Tk):

    def __init__(self):

        # ATRIBUTOS PARA LOS WIDGETS
        self.__lb_titulo = None
        self.__lb_seleccion = None
        self.__entry_grados = None
        self.__bt_conectar_arduino = None

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
        self.title("SERVOMOTOR DIGITAL")
        self.config(bg='white')

    def __iniciar_componentes(self):
        self.__iniciar_labels()
        self.__iniciar_entry()
        self.__iniciar_botones()

    def __iniciar_labels(self):
        self.__lb_titulo = Label(text='DIGITAL')
        self.__lb_titulo.config(bg='white', fg='black', font='arial 20')
        self.__lb_titulo.place(x=10, y=10)

        self.__lb_seleccion = Label(text="Ingrese un valor de 0° a 180°")
        self.__lb_seleccion.config(bg='white', fg='black', font='arial 12')
        self.__lb_seleccion.place(x=20, y=60)
    def __iniciar_entry(self):
        self.__entry_grados = Entry()
        self.__entry_grados.config(bg="white", fg="black", font="arial 12")
        self.__entry_grados.place(x=20, y=90)

    def __iniciar_botones(self):
        self.__bt_conectar_arduino = Button(self, text="Aceptar", command=self.__enviar_angulos_arduino)
        self.__bt_conectar_arduino.config(bg='black', fg='white', font='arial 10', activebackground="#21618c", activeforeground="#fff")
        self.__bt_conectar_arduino.place(x=20, y=140)

    def __enviar_angulos_arduino(self):

        angulos = self.__entry_grados.get()

        if angulos.isdigit():
            angulo = int(angulos)
            if 0 <= angulo <= 180:
                self.__con_arduino.write(f'{angulo}\n'.encode())
                print(f"Conectado con Arduino Servomotor. Grados: {angulo}")
            else:
                messagebox.showerror("Error", "Solo se permiten numeros de 0° a 180°")
        else:
            messagebox.showerror("Error", "Solo se permiten numeros")

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
