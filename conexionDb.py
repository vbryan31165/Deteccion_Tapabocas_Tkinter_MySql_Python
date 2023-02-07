import mysql.connector
import datetime
import numpy as np


class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='proyectomascarilla',
                                                user='root',
                                                password='')
        self.contador = 0

    def __str__(self):
        datos = self.consultaTodosUsuarios()
        aux = ""

        for row in datos:
            aux = aux+str(row)+"\n"
        return aux

    def buscaUsuario(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM USUARIOS WHERE USUARIO = %s"
        cur.execute(sql, (users,))
        usersx = cur.fetchall()

        cur.close()
        return usersx

    def buscaUsuarioPerfilb(self, users):

        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE USUARIO= %s"
        """ val = (users) """
        cur.execute(sql, (users,))
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def validarCedulaEx(self, cc):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM USUARIOS WHERE CEDULA = {}".format(cc)
        cur.execute(sql)
        cedula = cur.fetchall()
        cur.close()
        return cedula

    def buscaContraseña(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM USUARIOS WHERE CONTRASEÑA = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx

    def agregarNuevoUsuario(self, cedula, nombres, apellidos, correo, usuarios, contraseña, rol):

        if rol == "Estudiante":
            rol = "2"
        else:
            rol = "1"
        cur = self.conexion.cursor()
        sql = 'INSERT INTO USUARIOS (CEDULA,NOMBRES,APELLIDOS,CORREO,USUARIO,CONTRASEÑA,ID_ROL) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        val = (cedula, nombres, apellidos, correo, usuarios, contraseña, rol)
        cur.execute(sql, val)
        self.conexion.commit()

    def EditarUsuarioCreado(self, cedula, nombres, apellidos, correo, usuario, rol, idU):
        if rol == "Estudiante":
            rol = "2"
        else:
            rol = "1"

        cur = self.conexion.cursor()
        sql = 'UPDATE usuarios SET CEDULA=%s,NOMBRES=%s,APELLIDOS=%s,CORREO=%s,USUARIO=%s,ID_ROL=%s WHERE ID_USUARIO=%s'
        val = (cedula, nombres, apellidos, correo, usuario, rol, idU)
        cur.execute(sql, val)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def editarPerfil(self, cedula, nombres, apellidos, correo, contraseña, idu):
        cur = self.conexion.cursor()
        sql = "UPDATE usuarios SET CEDULA=%s,NOMBRES=%s,APELLIDOS=%s,CORREO=%s,CONTRASEÑA=%s WHERE ID_USUARIO=%s"
        val = (cedula, nombres, apellidos, correo, contraseña, idu)
        cur.execute(sql, val)
        self.conexion.commit()
        cur.close()

    def registrarUsuario(self, cedula, nombres, apellidos, correo, usuario, contraseña, rol):
        cur = self.conexion.cursor()
        sql = 'INSERT INTO USUARIOS (CEDULA,NOMBRES,APELLIDOS,CORREO,USUARIO,CONTRASEÑA,ID_ROL) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        val = (cedula, nombres, apellidos, correo, usuario, contraseña, rol)
        print(sql)
        cur.execute(sql, val)
        self.conexion.commit()

    def consultaTodosUsuarios(self):
        self.contador = self.contador+1
        print("CONTADOR CONSULTA USUARIOOOOO----------")
        print(self.contador)
        cur = self.conexion.cursor()
        sql = 'SELECT us.ID_USUARIO, us.CEDULA, us.NOMBRES, us.APELLIDOS, us.CORREO, us.USUARIO, rol.ROL, (CASE WHEN(us.ESTADO=1) THEN "Activo" WHEN(US.ESTADO=2) THEN "Inactivo" END)  AS NOMBRE_ESTADO FROM usuarios us INNER JOIN roles rol ON(rol.ID_ROL=us.ID_ROL) ORDER BY `us`.`ID_USUARIO` ASC'
        cur.execute(sql)
        usuarios = cur.fetchall()
        cur.close()
        return usuarios

    def consultaActivosInactivos(self):
        cur = self.conexion.cursor()
        sql = 'SELECT COUNT(1) AS Cantidad ,( CASE WHEN (ESTADO = 1 ) THEN "ACTIVO" WHEN (ESTADO = 2 ) THEN "INACTIVO" END )  AS NOMBRE_ESTADO FROM usuarios GROUP BY estado'
        cur.execute(sql)
        cantidadAI = cur.fetchall()
        cur.close()
        return cantidadAI

    def consultaAdministradoresEstudiantes(self):
        cur = self.conexion.cursor()
        sql = 'SELECT COUNT(1) AS cantidad ,( CASE WHEN (ID_ROL = 1 ) THEN "Administrador" WHEN (ID_ROL = 2 ) THEN "Estudiante" END )  AS NOMBRE_ROL FROM usuarios GROUP BY ID_ROL'
        cur.execute(sql)
        cantidadAE = cur.fetchall()
        cur.close()
        return cantidadAE

    def consultaUsuariosTotales(self):
        cur = self.conexion.cursor()
        sql = 'SELECT COUNT(1) AS cantidad FROM usuarios'
        cur.execute(sql)
        cantidadT = cur.fetchall()
        cur.close()
        return cantidadT

    def activarUsuario(self, id):
        cur = self.conexion.cursor()
        sql = 'UPDATE usuarios SET ESTADO=1 WHERE ID_USUARIO = {0}'.format(id)
        cur.execute(sql)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def desactivarUsuario(self, id):
        cur = self.conexion.cursor()
        sql = 'UPDATE usuarios SET ESTADO=2 WHERE ID_USUARIO = {0}'.format(id)
        cur.execute(sql)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def unique_rows(self, a):
        a = np.ascontiguousarray(a)
        unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
        return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

    def ordenarPorPosicionSubLista(self, lista: list, posicionOrdenar: int) -> list:
        return(sorted(lista, key=lambda elemento: elemento[posicionOrdenar-1]))

    def insetarTapabocas(self, diccionario):
        cur = self.conexion.cursor()
        """ for x in diccionario:
            # sql = 'INSERT INTO usuarios (ID_USUARIO=%s,FECHA_HORA_TAPABOCAS=%s,ESTADO_TAPABOCAS=%s) VALUES (%s,%s,%s)'

            val = (x[0][0], x[0][1], x[0][2])
            cur.execute(sql, val)
            self.conexion.commit() """
        print("diccionario antes de eliminar duplicados")
        print(len(diccionario))
        print(diccionario)
        self.ordenado = self.ordenarPorPosicionSubLista(diccionario, 2)
        print(self.ordenado)
        self.nueva = self.unique_rows(self.ordenado)

        for i in range(len(self.nueva)):

            time = datetime.datetime.now()
            """ for j in range(len(diccionario[i])): """
            sql = 'INSERT INTO tapabocas (ID_USUARIO,FECHA_HORA_TAPABOCAS,ESTADO_TAPABOCAS) VALUES (' + str(
                self.nueva[i][0]) + "," + "'" + self.nueva[i][1] + "'" + "," + str(self.nueva[i][2]) + ')'
            """ val = ()
            print(val)
            print(type(val)) """
            print(sql)
            print(cur.execute(sql))
            cur.execute(sql)
            self.conexion.commit()
            """ print(diccionario[i][j], end=' ')"""
            """ print() """

    def usuarioSinTapabocas(self):
        cur = self.conexion.cursor()
        sql = 'SELECT  us.CEDULA, CONCAT(us.Nombres, " ", us.Apellidos)AS Nombres,( CASE WHEN (tap.ESTADO_TAPABOCAS = 1 ) THEN "SIN TAPABOCAS" END )  AS ESTADO_TAPABOCAS, COUNT(*) CANTIDAD, tap.FECHA_HORA_TAPABOCAS,tap.ID_TAPABOCAS FROM usuarios  us INNER JOIN tapabocas tap ON (tap.ID_USUARIO=us.ID_USUARIO) WHERE tap.ESTADO_TAPABOCAS=1 GROUP BY us.ID_USUARIO,tap.ESTADO_TAPABOCAS, tap.FECHA_HORA_TAPABOCAS ORDER BY tap.FECHA_HORA_TAPABOCAS '
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        return data

    def usuarioUnicoSinTapabocas(self, id):

        self.contador = self.contador+1
        print("")
        print("Contador-------------------")
        print(self.contador)
        print("___________")
        print(id)
        cursor = self.conexion.cursor()
        sql = 'SELECT  us.CEDULA, CONCAT(us.NOMBRES, " ", us.APELLIDOS)AS Nombres,( CASE WHEN (tap.ESTADO_TAPABOCAS = 1 ) THEN "SIN TAPABOCAS" END )  AS ESTADO_TAPABOCAS,COUNT(*) CANTIDAD, tap.FECHA_HORA_TAPABOCAS,tap.ID_TAPABOCAS FROM usuarios  us INNER JOIN tapabocas tap ON (tap.ID_USUARIO=us.ID_USUARIO) WHERE tap.ESTADO_TAPABOCAS=1 AND tap.ID_USUARIO=%s GROUP BY us.ID_USUARIO,tap.ESTADO_TAPABOCAS,tap.FECHA_HORA_TAPABOCAS ORDER BY tap.FECHA_HORA_TAPABOCAS '
        cursor.execute(sql, (id,))
        data10 = cursor.fetchall()
        print(data10)
        cursor.close()

        return data10


"SELECT us.ID_USUARIO, us.CEDULA, us.NOMBRES, us.APELLIDOS,us.CORREO, us.USUARIO, rol.ROL FROM usuarios us INNER JOIN roles rol ON (rol.ID_ROL=us.ID_ROL) WHERE US.ESTADO=1 ORDER BY `us`.`ID_USUARIO` ASC"
