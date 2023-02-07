import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import conexionDb
import test_face_mask
import contraseña


class Login(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.user_marcar = "Ingrese su usuario"
        self.contra_marcar = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.datos = conexionDb.Registro_datos()
        self.tapabocas = test_face_mask.tapabocas()
        self.vcontraseña = contraseña.validar_contraseña()
        self.id = -1
        self.ventanaInicioSesion()

    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)

        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = ""

        if self.entry2.get() != 'Ingrese su Usuario':
            self.entry2['show'] = "*"

    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)

        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = "*"

        if self.entry2.get() == 'Ingrese su contraseña':
            self.entry2['show'] = ""

    def salirDefinitivo(self):
        self.master.destroy()
        self.master.quit()

    def salir(self):
        self.ventana_dos.destroy()
        self.ventanaInicioSesion()

    def salirRegister(self):
        self.ventana_tres.destroy()
        self.ventanaRegister()

    def salirPerfil(self):
        self.ventana_Perfil.destroy()
        self.ventanaInicioSesion()

    def salirEditarPerfil(self):
        self.ventana_Editar_Perfil.destroy()
        self.ventanaInicioSesion()

    def salirConsultaUsuario(self):
        self.ventana_consultaUsuarios.destroy()
        self.ventanaInicioSesion()

    def salir2(self):
        self.ventana_Perfil.destroy()
        self.ventanaPerfil()

    def salirInicioSesion(self):
        self.ventana_Inicio_Sesion.destroy()
        self.ventanaInicioSesion()

    def irRegister(self):
        self.ventana_Inicio_Sesion.destroy()
        self.ventanaRegister()

    def irLogin(self):
        self.ventana_tres.destroy()
        self.ventanaInicioSesion()

    def irPerfilInicio(self):
        self.ventana_dos.destroy()
        self.ventanaPerfil()

    def irInicioPerfil(self):
        self.ventana_Perfil.destroy()
        self.accederInicio()

    def irConsultaUsuariosInicio(self):
        self.ventana_dos.destroy()
        self.ventanaConsultaUsuarios()

    def irInicioConsultaUsuarios(self):
        self.ventana_consultaUsuarios.destroy()
        self.accederInicio()

    def irEditarPerfilPerfil(self):
        self.ventana_Perfil.destroy()
        self.ventanaEditarPerfil()

    def irPerfilEditarPerfil(self):
        self.ventana_Editar_Perfil.destroy()
        self.ventanaPerfil()

    def actualizarCand(self):
        self.ventana_consultaUsuarios.destroy()
        self.ventanaConsultaUsuarios()

    def ventanaInicioSesion(self):
        self.master.withdraw()
        self.ventana_Inicio_Sesion = Toplevel()
        self.ventana_Inicio_Sesion.title('Inicio Sesion')
        self.ventana_Inicio_Sesion.geometry('350x630+500+50')
        self.ventana_Inicio_Sesion.protocol(
            "WM_DELETE_WINDOW", self.salirInicioSesion)
        self.ventana_Inicio_Sesion.config(bg='white')
        self.ventana_Inicio_Sesion.iconbitmap(
            'C:/Users/RYZEN/OneDrive/Documents/python/Tkinter_MySQL_Tapabocas/img/user.ico')

        self.widgets()

    def accederInicio(self):
        """ for i in range(90):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.001) """

        self.master.withdraw()
        self.ventana_dos = Toplevel()
        self.ventana_dos.title('Bienvenido')
        self.ventana_dos.protocol("WM_DELETE_WINDOW", self.salir)
        self.ventana_dos.config(bg='white')
        self.ventana_dos.resizable(0, 0)

        self.widgetsInicio()
        self.mostrarTodosTapabocas()

    def iniciarGrabacion(self):
        u = usuario[0][0]
        print(u)
        self.tapabocas.reconocimientoMascarilla(u)

    def ventanaPerfil(self):
        self.master.withdraw()
        self.ventana_Perfil = Toplevel()
        self.ventana_Perfil.title('Perfil')
        self.ventana_Perfil.geometry('1300x500')
        self.ventana_Perfil.protocol("WM_DELETE_WINDOW", self.salirPerfil)
        self.ventana_Perfil.config(bg='white')
        """ self.ventana_Perfil.state('zoomed') """

        self.widgetsPerfil()

    def ventanaEditarPerfil(self):
        self.ventana_Editar_Perfil = Toplevel()
        self.ventana_Editar_Perfil.title('Editar Perfil')
        self.ventana_Editar_Perfil.protocol(
            "WM_DELETE_WINDOW", self.salirEditarPerfil)
        self.ventana_Editar_Perfil.geometry('1000x460')
        self.ventana_Editar_Perfil.config(bg='white')

        self.widgetsEditarPerfil()
        self.mostrarModificarDatosPerfil()

    def ventanaRegister(self):
        self.master.withdraw()
        self.ventana_tres = Toplevel()
        self.ventana_tres.title('REGISTRO DE USUARIOS')
        self.ventana_tres.resizable(0, 0)
        self.ventana_tres.protocol("WM_DELETE_WINDOW", self.salirRegister)
        self.ventana_tres.config(bg='black')
        self.ventana_tres.iconbitmap(
            'C:/Users/RYZEN/OneDrive/Documents/python/Tkinter_MySQL_Tapabocas/img/user.ico')

        self.frame1 = Frame(self.ventana_tres, bg='gray15')
        self.frame1.grid(column=0, row=0, sticky='nsew')
        self.frame2 = Frame(self.ventana_tres, bg='gray16')
        self.frame2.grid(column=1, row=0, sticky='nsew')
        self.frame3 = Frame(self.frame2, bg='gray16')
        self.frame3.grid(column=1, row=0, sticky='nsew')

        Label(self.frame1, text='Cedula', width=10
              ).grid(column=0, row=0, pady=20, padx=10)
        self.entryCedula = Entry(self.frame1, width=20, font=(
            'Arial', 12), justify='center')
        self.entryCedula.grid(column=1, row=0)

        Label(self.frame1, text='Nombres',
              width=10).grid(column=0, row=1, pady=20, padx=10)
        self.entryNombres = Entry(self.frame1, font=(
            'Arial', 12), justify='center')
        self.entryNombres.grid(column=1, row=1)

        Label(self.frame1, text='Apellidos', width=10).grid(
            column=0, row=2, pady=20, padx=10)
        self.entryApellidos = Entry(self.frame1, width=20, font=(
            'Arial', 12), justify='center')
        self.entryApellidos.grid(column=1, row=2)

        Label(self.frame1, text='correo', width=10).grid(
            column=0, row=3, pady=20, padx=10)
        self.entryCorreo = Entry(self.frame1, width=20, font=(
            'Arial', 12), justify='center')
        self.entryCorreo.grid(column=1, row=3)

        Label(self.frame1, text='Usuario', width=10).grid(
            column=0, row=4, pady=20, padx=10)
        self.entryUsuario = Entry(self.frame1, width=20, font=(
            'Arial', 12), justify='center')
        self.entryUsuario.grid(column=1, row=4)

        Label(self.frame1, text='Contraseña', width=10).grid(
            column=0, row=5, pady=20, padx=10)
        self.entryContraseña = Entry(self.frame1, width=20, font=(
            'Arial', 12), show="*", justify='center')
        self.entryContraseña.grid(column=1, row=5)

        self.logo = PhotoImage(
            file='C:/Users/RYZEN/OneDrive\Documents/python/Tkinter_MySQL_Tapabocas/img/logo_itsa.png')
        Label(self.frame3, image=self.logo,
              bg='white', height=150, width=350).pack(pady=20, padx=10)

        Button(self.frame2, text='REGISTRAR', width=15, font='Arial 12',
               bg='#51d1f6', command=self.registroUsuarios).grid(column=1, row=2, pady=20, padx=20)

        Button(self.frame2, text='LOGIN', width=15, font='Arial 12',
               bg='green', command=self.irLogin).grid(column=1, row=3, pady=20, padx=20)

    def ventanaConsultaUsuarios(self):
        self.master.withdraw()
        self.ventana_consultaUsuarios = Toplevel()
        self.ventana_consultaUsuarios.title('Consulta Usuarios')
        self.ventana_consultaUsuarios.geometry('1220x500+400+80')
        self.ventana_consultaUsuarios.protocol(
            "WM_DELETE_WINDOW", self.salirConsultaUsuario)
        self.ventana_consultaUsuarios.config(bg='white')
        """ self.ventana_dos.resizable(0, 0) """
        """ self.ventana_consultaUsuarios.state('zoomed') """

        self.widgetsConsultaUsuarios()

        self.mostrarTodosUsuarios()

    def limpiarMostrarTapabocas(self):
        self.limpiarTablaTapabocas()

    def registroUsuarios(self):

        if messagebox.askyesno('Confirmación terminos y Condiciones', 'Al utilizar nuestros servicios, nos confías tus datos. Entendemos que es una gran responsabilidad y nos esforzamos al máximo para proteger tu información y permitirte controlarla.') == True:
            contraseña_entry = self.entryContraseña.get()

            if self.vcontraseña.contraseña_ok(contraseña_entry) == True:
                cedula_entry = self.entryCedula.get()
                nombres_entry = self.entryNombres.get().upper()
                apellidos_entry = self.entryApellidos.get().upper()
                correo_entry = self.entryCorreo.get()
                usuario_entry = self.entryUsuario.get()
                contraseña_entry = self.entryContraseña.get()
                rol = "2"
                datoUsuario = []

                cedula_entry = str(cedula_entry)
                nombres_entry = str(nombres_entry)
                apellidos_entry = str(apellidos_entry)
                correo_entry = str(correo_entry)
                usuario_entry = str(usuario_entry)
                contraseña_entry = str(contraseña_entry)
                rol = int(rol)
                print(len(apellidos_entry))
                if (len(cedula_entry) == 0 or len(nombres_entry) == 0 or len(apellidos_entry) == 0) or (len(usuario_entry) == 0 or len(contraseña_entry) == 0 or len(correo_entry) == 0):
                    messagebox.showinfo(
                        "ERROR", "No puede dejar campos vacios, por favor digite los campos")
                    print("vacio")
                else:
                    datoUsuario = self.datos.buscaUsuario(
                        str("'"+usuario_entry+"'"))
                    print("")
                if len(datoUsuario) == 0 and len(usuario_entry) != 0:
                    messagebox.showinfo(
                        "Nota", "Usuario registrado correctamente")
                    self.datos.registrarUsuario(
                        cedula_entry, nombres_entry, apellidos_entry, correo_entry, usuario_entry, contraseña_entry, rol)
                else:
                    if len(datoUsuario) != 0 and datoUsuario[0][5] == usuario_entry:
                        messagebox.showinfo(
                            "ERROR", 'Usuario digitado ya existe, por favor ingrese otro')
                print("Cumple")
            else:
                messagebox.showwarning(
                    'CONTRASEÑA NO SEGURA', 'La contraseña debe contener al menos:\n\n8. Caracteres Como Mínimo\n1. Mayuscula\n1. Minuscula\n1. Caracter Alfanumérico\n1. Caracter No Alfanumérico\n0. Espacios En Blanco')
                print("No cumple")
        else:
            messagebox.showinfo("ERROR AL REGISTRAR",
                                'Debe aceptar los terminos y condiciones para poder continuar con el registro')

    def verificacion_users(self):
        global usuario
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()
        if users_entry == "Ingrese su usuario":
            self.indica3['text'] = 'No puede dejar campos vacios'
        else:
            self.indica3['text'] = ''
        if password_entry == "Ingrese su contraseña":
            self.indica4['text'] = 'No puede dejar campos vacios'
        else:
            self.indica4['text'] = ''

        if users_entry != self.user_marcar or self.contra_marcar != password_entry:
            dato1 = self.datos.buscaUsuario(users_entry)
            print(len(dato1))
            if len(dato1) != 0:
                contraseña = dato1[0][6]  # contraseña
                usuario = dato1
                user = dato1[0][5]
                if users_entry != str(user) and password_entry != str(contraseña):
                    self.indica2['text'] = 'Contraseña incorrecta'
                    self.indica1['text'] = 'Usuario incorrecto'
                else:
                    self.accederInicio()
                    self.ventana_Inicio_Sesion.destroy()
            else:
                self.indica2['text'] = 'Contraseña incorrecta'
                self.indica1['text'] = 'Usuario incorrecto'

    def buscaUsuarioPerfil(self):
        print("aqui :")

        us = usuario[0][5]
        """ print(us) """
        user = self.datos.buscaUsuarioPerfilb(us)
        """ print("dato de la base")
        print(user) """
        return user

    def mostrarTodosUsuarios(self):
        usuarios = self.datos.consultaTodosUsuarios()

        for row in usuarios:
            self.tabla.insert("", END, text=row[0], values=(
                row[1], row[2].title(), row[3].title(), row[4], row[5], row[6].capitalize(), row[7]))

    def mostrarTodosTapabocas(self):
        if usuario[0][7] == 1:
            sintapaboca = self.datos.usuarioSinTapabocas()
            print("admin")
            print(sintapaboca)
            for row in sintapaboca:
                self.tablaTapabocas.insert("", END, text=row[0], values=(
                    row[1].title(), row[2], row[3]-1, row[4]))
        else:
            idu = usuario[0][0]
            sintapabocaUnico = self.datos.usuarioUnicoSinTapabocas(idu)
            print("mostrar datos-------------------xxxxxx---------------------")
            print(sintapabocaUnico)
            for row1 in sintapabocaUnico:
                self.tablaTapabocas.insert("", END, text=row1[0], values=(
                    row1[1].title(), row1[2], row1[3]-1, row1[4]))

    def limpiarTabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

    def limpiarTablaTapabocas(self):
        for item in self.tablaTapabocas.get_children():
            self.tablaTapabocas.delete(item)

    def widgets(self):
        self.logo = PhotoImage(
            file='C:/Users/RYZEN/OneDrive/Documents/python/Tkinter_MySQL_Tapabocas/img/logo_itsa.png')
        Label(self.ventana_Inicio_Sesion, image=self.logo,
              bg='white', height=150, width=350).pack()
        Label(self.ventana_Inicio_Sesion, text='Usuario', bg='white',
              fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry1 = Entry(self.ventana_Inicio_Sesion, font=('Comic Sans MS', 12), justify='center', fg='grey', highlightbackground="#E65561",
                            highlightcolor="green2", highlightthickness=5)
        self.entry1.insert(0, self.user_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(
            self.entry1, self.user_marcar))
        self.entry1.pack(pady=4)

        self.indica1 = Label(self.ventana_Inicio_Sesion, bg='white',
                             fg='black', font=('Arial', 8, 'bold'))
        self.indica1.pack(pady=2)
        self.indica3 = Label(self.ventana_Inicio_Sesion, bg='white',
                             fg='black', font=('Arial', 8, 'bold'))
        self.indica3.pack(pady=2)

        # contraseña y entry
        Label(self.ventana_Inicio_Sesion, text='Contraseña', bg='white',
              fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry2 = Entry(self.ventana_Inicio_Sesion, font=('Comic Sans MS', 12), justify='center',  fg='grey', highlightbackground="#E65561",
                            highlightcolor="green2", highlightthickness=5)
        self.entry2.insert(0, self.contra_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(
            self.entry2, self.contra_marcar))
        self.entry2.pack(pady=1)

        self.indica2 = Label(self.ventana_Inicio_Sesion, bg='white',
                             fg='black', font=('Arial', 8, 'bold'))
        self.indica2.pack(pady=2)
        self.indica4 = Label(self.ventana_Inicio_Sesion, bg='white',
                             fg='black', font=('Arial', 8, 'bold'))
        self.indica4.pack(pady=2)

        Button(self.ventana_Inicio_Sesion, text='Iniciar Sesion',  command=self.verificacion_users,
               activebackground='magenta', bg='#D64E40', font=('Arial', 12, 'bold')).pack(pady=10)

        """ estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TProgressbar", foreground='red', background='black', troughcolor='white',
                         bordercolor='#970BD9', lightcolor='#970BD9', darkcolor='black')
        self.barra = ttk.Progressbar(
            self.ventana_Inicio_Sesion, orient=HORIZONTAL, length=200, mode='determinate', maximum=100, style="TProgressbar")
        self.barra.pack() """

        Button(self.ventana_Inicio_Sesion, text='¿No tiene usuario?', bg='white', activebackground='white', bd=0,
               fg='blue', font=('Lucida Sans', 15, 'italic', 'underline'), command=self.irRegister).pack(pady=10)
        Button(self.ventana_Inicio_Sesion, text='Salir', bg='white', activebackground='white', bd=0,
               fg='black', font=('Lucida Sans', 15, 'italic'), command=self.salirDefinitivo).pack(pady=10)

    def widgetsInicio(self):

        # CREATE FRAMES
        self.frame_welcome = Frame(self.ventana_dos, bg='white')
        self.frame_welcome.grid(column=0, row=0, sticky='nsew')
        self.frame_dasboard = Frame(self.ventana_dos, bg='white')
        self.frame_dasboard.grid(column=0, row=5, sticky='nsew')

        # FRAME_WELCOME
        self.labelFrameInicio = LabelFrame(self.frame_welcome, text='Bienvenido '+usuario[0][2].title()+" "+usuario[0][3].title(),
                                           font=('Arial 12', 15, 'bold'), bg='white')
        self.labelFrameInicio.pack(fill="both", padx=10, ipadx=5)

        # FRAME_OPTIONS

        Button(self.labelFrameInicio, text='Grabar', width=10, font=('Comic Sans MS', 9, 'bold'),
               bg='#9ddba2', command=self.iniciarGrabacion, relief="raised", bd=10).pack(side='left', padx=20, pady=10)
        Button(self.labelFrameInicio, text='Perfil', width=10, font=('Comic Sans MS', 9, 'bold'),
               bg='#0dcaf0', command=self.irPerfilInicio, relief="raised", bd=10).pack(side='left', padx=20, pady=10)
        if usuario[0][7] == 1:
            Button(self.labelFrameInicio, text='Consultar Usuarios', width=15, font=('Comic Sans MS', 9, 'bold'),
                   bg='#646464', command=self.irConsultaUsuariosInicio, relief="raised", bd=10).pack(side='left', padx=20, pady=10)

        Button(self.labelFrameInicio, text='Salir ', width=10, font=('Comic Sans MS', 9, 'bold'),
               bg='#ee3a1f', command=self.salir, relief="raised", bd=10).pack(side='left', padx=20, pady=10)

        Label(self.ventana_dos, text='DASBOARD', bg='white',
              font='Arial 18').grid(column=0, row=2, pady=20, padx=10)
        if usuario[0][7] == 2:
            Label(self.ventana_dos, text='Numero de veces que '+usuario[0][2].title() + " "+usuario[0][3].title() + " " + "se ha quitado el tapabocas", bg='white',
                  font='Arial 10').grid(column=0, row=3, pady=5, padx=5)
        else:
            Label(self.ventana_dos, text='Numero de veces que todos los usuarios se han quitado el tapabocas', bg='white',
                  font='Arial 10').grid(column=0, row=3, pady=5, padx=5)

        # FRAME_DASBOARD
        """ fechas = ['2021-05-12', '2021-05-13',
                  '2021-05-15', '2021-06-3', '2021-06-5']
        colores = ['blue', 'red', 'green', 'magenta', 'black']
        tamaño = [10, 15, 20, 13, 30]

        fig, axs = plt.subplots(1, 2, dpi=65, figsize=(13, 4), sharey=True)

        fig.suptitle('Graficas usuarios sin tapabocas')

        axs[0].bar(fechas, tamaño, color=colores)
        axs[1].scatter(fechas, tamaño, color=colores)
        canvas = FigureCanvasTkAgg(fig, master=self.frame_dasboard)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=4, rowspan=5) """
        self.tablaTapabocas = ttk.Treeview(self.frame_dasboard, columns=(
            'col1', 'col2', 'col3', 'col4'))
        self.tablaTapabocas.column("#0", width=100, anchor=CENTER)
        self.tablaTapabocas.column("col1", width=170, anchor=CENTER)
        self.tablaTapabocas.column("col2", width=100, anchor=CENTER)
        self.tablaTapabocas.column("col3", width=50, anchor=CENTER)
        self.tablaTapabocas.column("col4", width=150, anchor=CENTER)

        self.tablaTapabocas.heading("#0", text="Cedula", anchor=CENTER)
        self.tablaTapabocas.heading("col1", text="Nombres", anchor=CENTER)
        self.tablaTapabocas.heading(
            "col2", text="Estado Tapabocas", anchor=CENTER)
        self.tablaTapabocas.heading("col3", text="#", anchor=CENTER)
        self.tablaTapabocas.heading("col4", text="Fecha", anchor=CENTER)

        self.tablaTapabocas.pack(side=LEFT, pady=10, padx=10)

        sb = Scrollbar(self.frame_dasboard, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.tablaTapabocas.config(yscrollcommand=sb.set)
        sb.config(command=self.tablaTapabocas.yview)

        """ Button(self.frame_dasboard, text='actualizar ', width=10, font=('Comic Sans MS', 9, 'bold'),
               bg='#ee3a1f', command=self.limpiarMostrarTapabocas, relief="raised", bd=10).pack()
        Button(self.frame_dasboard, text='mostrar ', width=10, font=('Comic Sans MS', 9, 'bold'),
               bg='#ee3a1f', command=self.mostrarTodosTapabocas, relief="raised", bd=10).pack() """

    def widgetsPerfil(self):
        global x
        x = self.buscaUsuarioPerfil()
        print("aqui wiget")
        print(x[0][2])
        self.labelFrame = LabelFrame(self.ventana_Perfil, text='PERFIL ',
                                     bg='white', font=('Arial', 40, 'bold'))
        self.labelFrame.pack(fill="both", padx=25)
        self.label1 = Label(self.labelFrame, text='espacio en blanco ', fg="white",
                            font='Arial 15', bg='white').pack(side=LEFT, fill="both")

        self.label2 = Label(self.labelFrame, text='espacio en blanco ', fg="white",
                            font='Arial 15', bg='white').pack(side=RIGHT, fill="both")

        self.label3 = Label(self.labelFrame, text='Detalles de la cuenta :',
                            font='Arial 15', bg='#cccccc', anchor="nw", relief="ridge", borderwidth=2).pack(pady=15, fill="both")

        self.label4 = Label(self.labelFrame, text='Cedula :  \t                                         '+x[0][1],
                            font='Arial 15', bg='white', anchor="nw", relief="ridge", borderwidth=2).pack(pady=5, padx=150, fill="both")

        self.label5 = Label(self.labelFrame, text='Nombres : \t                          '+x[0][2].title(),
                            font='Arial 15', bg='#cccccc', anchor="nw", relief="ridge", borderwidth=2).pack(pady=5, padx=150, fill="x")

        self.label6 = Label(self.labelFrame, text='Apellidos : \t                          '+x[0][3].title(),
                            font='Arial 15', bg='white', anchor="nw", relief="ridge", borderwidth=2).pack(pady=5, padx=150, fill="both")

        self.label7 = Label(self.labelFrame, text='Correo : \t                                         '+x[0][4],
                            font='Arial 15', bg='#cccccc', anchor="nw", relief="ridge", borderwidth=2).pack(pady=5, padx=150, fill="both")

        self.label8 = Label(self.labelFrame, text='Nombre de usuario : \t            '+x[0][5],
                            font='Arial 15', bg='white', anchor="nw", relief="ridge", borderwidth=2).pack(pady=5, padx=150, fill="both")

        self.btn1 = Button(self.labelFrame, text='actualizar datos',  command=self.irEditarPerfilPerfil,
                           activebackground='magenta', bg='#D64E40', font=('Arial', 12, 'bold')).pack(pady=15)

        self.btn2 = Button(self.labelFrame, text='Cerrar ventana',  command=self.irInicioPerfil,
                           activebackground='magenta', bg='#D64E40', font=('Arial', 12, 'bold')).pack(pady=15)

    def widgetsEditarPerfil(self):
        self.labelFrameEditarPerfil = LabelFrame(self.ventana_Editar_Perfil, text='Editar Perfil ',
                                                 font='Arial 40', bg='white', relief="groove", borderwidth=10)
        self.labelFrameEditarPerfil.pack(pady=20, padx=20, fill="both")

        Label(self.labelFrameEditarPerfil, text="Cedula").pack()
        self.cedulaEntryPerfil = Entry(self.labelFrameEditarPerfil)
        self.cedulaEntryPerfil.pack()

        Label(self.labelFrameEditarPerfil, text="Nombres").pack()
        self.nombresEntryPerfil = Entry(self.labelFrameEditarPerfil)
        self.nombresEntryPerfil.pack()

        Label(self.labelFrameEditarPerfil, text="Apellidos").pack()
        self.apellidosEntryPerfil = Entry(self.labelFrameEditarPerfil)
        self.apellidosEntryPerfil.pack()

        Label(self.labelFrameEditarPerfil, text="Correo").pack()
        self.correoEntryPerfil = Entry(self.labelFrameEditarPerfil)
        self.correoEntryPerfil.pack()

        Label(self.labelFrameEditarPerfil, text="Usuario").pack()
        self.usuarioEntryPerfil = Entry(
            self.labelFrameEditarPerfil, state='disabled')
        self.usuarioEntryPerfil.pack()

        Label(self.labelFrameEditarPerfil, text="Contraseña").pack()
        self.contraseñaEntryPerfil = Entry(self.labelFrameEditarPerfil)
        self.contraseñaEntryPerfil.pack()

        self.btnGuardarPerfil = Button(
            self.labelFrameEditarPerfil, text="Guardar", command=self.editarPerdil)
        self.btnGuardarPerfil.pack(side='left',  padx=200, pady=20)

        self.btnCancelarPerfil = Button(
            self.labelFrameEditarPerfil, text="Perfil", command=self.irPerfilEditarPerfil)
        self.btnCancelarPerfil.pack(side='right', padx=200, pady=20)

    def widgetsConsultaUsuarios(self):
        cand = self.datos.consultaActivosInactivos()
        candAE = self.datos.consultaAdministradoresEstudiantes()
        candT = self.datos.consultaUsuariosTotales()
        print(type(cand))
        print(len(cand))
        print(cand)

        Label(self.ventana_consultaUsuarios, text='Consultar Usuarios ',
              font='Arial 40', bg='white', relief="raised", borderwidth=10).pack(pady=20)

        frame1 = Frame(self.ventana_consultaUsuarios, bg="#bfdaff")

        frame1.place(x=0, y=130, width=150, height=359)

        self.btnNuevo = Button(frame1, text="Nuevo Usuario",
                               command=self.nuevoUsuario, bg='#95c799', font=('Arial', 10, 'bold'))
        self.btnNuevo.pack(pady=30)

        self.btnEditar = Button(
            frame1, text="Editar Usuario", command=self.modificarDatosUsuario, bg='#458bc6', font=('Arial', 10, 'bold'))
        self.btnEditar.pack(pady=30)

        self.btnActivar = Button(
            frame1, text="Activar Usuario", command=self.activarUsuario, bg='#a0a0a0', font=('Arial', 10, 'bold'))
        self.btnActivar.pack(pady=30)

        self.btnDesactivar = Button(
            frame1, text="Desactivar Usuario", command=self.desactivarUsuario, bg='#f24437', font=('Arial', 10, 'bold'))
        self.btnDesactivar.pack(pady=30)

        #--------------------------------------------------------------------------------------#

        frame2 = Frame(self.ventana_consultaUsuarios, bg="#d3dde3")
        frame2.place(x=155, y=130, width=165, height=359)

        Label(frame2, text="Cedula").pack()
        self.cedulaEntry = Entry(frame2)
        self.cedulaEntry.pack()

        Label(frame2, text="Nombres").pack()
        self.nombresEntry = Entry(frame2)
        self.nombresEntry.pack()

        Label(frame2, text="Apellidos").pack()
        self.apellidosEntry = Entry(frame2)
        self.apellidosEntry.pack()

        Label(frame2, text="Correo").pack()
        self.correoEntry = Entry(frame2)
        self.correoEntry.pack()

        Label(frame2, text="Usuario").pack()
        self.usuarioEntry = Entry(frame2)
        self.usuarioEntry.pack()

        Label(frame2, text="Contraseña").pack()
        self.contraseñaEntry = Entry(frame2)
        self.contraseñaEntry.pack()

        Label(frame2, text="Rol").pack()
        opciones = ["Estudiante", "Administrador"]
        self.rolEntry = ttk.Combobox(frame2, value=opciones)
        self.rolEntry.pack()

        self.btnGuardar = Button(
            frame2, text="Guardar", command=self.guardarEditar)
        self.btnGuardar.pack(side=LEFT, pady=15, padx=13)

        self.btnCancelar_ = Button(
            frame2, text="Cancelar", command=self.btnCancelar)
        self.btnCancelar_.pack(side=LEFT, pady=15, padx=15)
        #--------------------------------------------------------------------------------------#

        frameTabla = Frame(self.ventana_consultaUsuarios)
        frameTabla.place(x=325, y=130, width=890, height=359)

        self.tabla = ttk.Treeview(frameTabla, columns=(
            'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        self.tabla.column("#0", width=60, anchor=CENTER)
        self.tabla.column("col1", width=100, anchor=CENTER)
        self.tabla.column("col2", width=100, anchor=CENTER)
        self.tabla.column("col3", width=100, anchor=CENTER)
        self.tabla.column("col4", width=150, anchor=CENTER)
        self.tabla.column("col5", width=100, anchor=CENTER)
        self.tabla.column("col6", width=100, anchor=CENTER)
        self.tabla.column("col7", width=100, anchor=CENTER)

        self.tabla.heading("#0", text="Id", anchor=CENTER)
        self.tabla.heading("col1", text="Cedula", anchor=CENTER)
        self.tabla.heading("col2", text="Nombres", anchor=CENTER)
        self.tabla.heading("col3", text="Apellidos", anchor=CENTER)
        self.tabla.heading("col4", text="Correo", anchor=CENTER)
        self.tabla.heading("col5", text="Usuario", anchor=CENTER)
        self.tabla.heading("col6", text="Tipo de usuario", anchor=CENTER)
        self.tabla.heading("col7", text="Estado", anchor=CENTER)

        self.tabla.pack(side=LEFT, pady=10, padx=10)

        sb = Scrollbar(frameTabla, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.tabla.config(yscrollcommand=sb.set)
        sb.config(command=self.tabla.yview)

        self.tabla['selectmode'] = 'browse'
        self.habilitarCajas("disabled")
        self.habilitarBtnGuardarCancelar("disabled")

        frame3 = Frame(self.ventana_consultaUsuarios)
        frame3.place(x=600, y=445, width=150, height=30)
        self.btnCerrar = Button(frame3, text='Cerrar ventana',  command=self.irInicioConsultaUsuarios,
                                activebackground='magenta', bg='#D64E40', font=('Arial', 12, 'bold'))
        self.btnCerrar.pack()

        frame4 = Frame(self.ventana_consultaUsuarios)
        frame4.place(x=325, y=130, width=850, height=56)
        Label(frame4, text='Usuarios Totales : '+" " +
              str(candT[0][0]), relief="groove", borderwidth=5).pack(side=LEFT, padx=9, ipady=5, ipadx=5)
        Label(frame4, text='Usuarios Administradores : ' +
              " "+str(candAE[0][0]), relief="groove", borderwidth=5).pack(side=LEFT, padx=9, ipady=5, ipadx=5)
        Label(frame4, text='Usuarios Estudiantes : '+" " +
              str(candAE[1][0]), relief="groove", borderwidth=5).pack(side=LEFT, padx=9, ipady=5, ipadx=5)
        Label(frame4, text='Usuarios Activos : '+" " +
              str(cand[0][0]), relief="groove", borderwidth=5).pack(side=LEFT, padx=9, ipady=5, ipadx=5)
        Label(frame4, text='Usuarios Inactivos : '+" " +
              str(cand[1][0]), relief="groove", borderwidth=5).pack(side=LEFT, padx=9, ipady=5, ipadx=5)

    def nuevoUsuario(self):
        self.habilitarCajas("normal")
        self.habilitarBtnOperaciones("disabled")
        self.habilitarBtnGuardarCancelar("normal")
        self.limpiarCajas()
        self.cedulaEntry.focus()

    def activarUsuario(self):

        selected = self.tabla.focus()
        clave = self.tabla.item(selected, 'text')

        if clave == '':
            messagebox.showwarning(
                "Activar", "Debes seleccionar un usuario de la tabla para activar")
        else:
            valores = self.tabla.item(selected, 'values')
            data = str(clave)+" , "+valores[1]+" "+valores[2]
            r = messagebox.askquestion(
                "Activar", "Estas seguro que deseas activar el usuario seleccionado\n"+data)

            if r == messagebox.YES:
                n = self.datos.activarUsuario(clave)
                if n == 1:
                    messagebox.showwarning(
                        "Activar", 'Usuario activado correctamente')
                    self.limpiarTabla()
                    self.mostrarTodosUsuarios()
                    self.actualizarCand()
                else:
                    messagebox.showwarning(
                        "Activar", 'No fue posible activar el usuario, ya se encuentra activo')

    def desactivarUsuario(self):

        selected = self.tabla.focus()
        clave = self.tabla.item(selected, 'text')

        if clave == '':
            messagebox.showwarning(
                "Eliminar", "Debes seleccionar un usuario de la tabla para eliminar")
        else:
            valores = self.tabla.item(selected, 'values')
            data = str(clave)+" , "+valores[1]+" "+valores[2]
            r = messagebox.askquestion(
                "Elimniar", "Estas seguro que deseas eliminar el usuario seleccionado\n"+data)

            if r == messagebox.YES:
                n = self.datos.desactivarUsuario(clave)
                if n == 1:
                    messagebox.showwarning(
                        "Eliminar", 'Usuario eliminado correctamente')
                    self.limpiarTabla()
                    self.mostrarTodosUsuarios()
                    self.actualizarCand()
                else:
                    messagebox.showwarning(
                        "Eliminar", 'No fue posible eliminar el usuario, ya se encuentra desactivado')

    def limpiarCajas(self):
        self.cedulaEntry.delete(0, END)
        self.nombresEntry.delete(0, END)
        self.apellidosEntry.delete(0, END)
        self.correoEntry.delete(0, END)
        self.usuarioEntry.delete(0, END)
        self.contraseñaEntry.delete(0, END)
        self.rolEntry.delete(0, END)

    def modificarDatosUsuario(self):
        selected = self.tabla.focus()
        clave = self.tabla.item(selected, 'text')

        if clave == '':
            messagebox.showwarning(
                "Modificar", "Debes seleccionar un usuario de la tabla para editar")
        else:

            self.id = clave
            self.habilitarCajas("normal")
            valores = self.tabla.item(selected, 'values')
            print(valores)
            self.limpiarCajas()

            self.cedulaEntry.insert(0, valores[0])
            self.nombresEntry.insert(0, valores[1])
            self.apellidosEntry.insert(0, valores[2])
            self.correoEntry.insert(0, valores[3])
            self.rolEntry.insert(0, valores[5])
            self.usuarioEntry.insert(0, valores[4])
            """ self.estadoEntry.insert(0, valores[6]) """
            self.habilitarBtnOperaciones("disabled")
            self.habilitarBtnGuardarCancelar("normal")
            self.cedulaEntry.focus()

    def mostrarModificarDatosPerfil(self):
        self.cedulaEntryPerfil.insert(0, x[0][1])
        self.nombresEntryPerfil.insert(0, x[0][2])
        self.apellidosEntryPerfil.insert(0, x[0][3])
        self.correoEntryPerfil.insert(0, x[0][4])
        self.usuarioEntryPerfil.insert(0, x[0][5])
        self.contraseñaEntryPerfil.insert(0, x[0][6])

    def guardarEditar(self):
        if self.id == -1:

            u = self.cedulaEntry.get()
            print(u)
            self.datos.agregarNuevoUsuario(self.cedulaEntry.get(), self.nombresEntry.get(), self.apellidosEntry.get(
            ), self.correoEntry.get(), self.usuarioEntry.get(), self.contraseñaEntry.get(), self.rolEntry.get())
            messagebox.showinfo(
                "Agregar", 'Usuario creado correctamente')
        else:
            self.datos.EditarUsuarioCreado(self.cedulaEntry.get(), self.nombresEntry.get(), self.apellidosEntry.get(
            ), self.correoEntry.get(), self.usuarioEntry.get(), self.rolEntry.get(), str(self.id))
            messagebox.showinfo("Editar", "Usuario editado correctamente")
            self.id = -1

        self.limpiarTabla()
        self.mostrarTodosUsuarios()
        self.actualizarCand()
        self.limpiarCajas()
        self.habilitarBtnGuardarCancelar("disabled")
        self.habilitarBtnOperaciones("normal")
        self.habilitarCajas("disabled")

    def editarPerdil(self):
        id = x[0][0]
        self.datos.editarPerfil(self.cedulaEntryPerfil.get(), self.nombresEntryPerfil.get(), self.apellidosEntryPerfil.get(
        ), self.correoEntryPerfil.get(), self.contraseñaEntryPerfil.get(), str(id))
        messagebox.showinfo("Editar Perfil", "Datos editados correctamente")
        self.ventana_Editar_Perfil.destroy()
        self.salir2()

    def btnCancelar(self):
        r = messagebox.askquestion(
            "Cancelar", "¿Esta seguro que desea cancelar la operación actual?")
        if r == messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnGuardarCancelar("disabled")
            self.habilitarBtnOperaciones("normal")
            self.habilitarCajas("disabled")

    def habilitarCajas(self, estado):
        self.cedulaEntry.configure(state=estado)
        self.nombresEntry.configure(state=estado)
        self.apellidosEntry.configure(state=estado)
        self.correoEntry.configure(state=estado)
        self.rolEntry.configure(state=estado)
        self.usuarioEntry.configure(state=estado)
        self.contraseñaEntry.configure(state=estado)

    def habilitarBtnOperaciones(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnEditar.configure(state=estado)
        self.btnActivar.configure(state=estado)
        self.btnDesactivar.configure(state=estado)

    def habilitarBtnGuardarCancelar(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar_.configure(state=estado)


""" if __name__ == "__main__":
    ventana = Tk()
    ventana.config(bg='white')
    ventana.geometry('350x630+500+50')
    ventana.overrideredirect(1)
    ventana.resizable(0, 0)
    app = Login(ventana)
    app.mainloop() """
