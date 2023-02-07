class validar_contraseña():
    error = []

    def validar_longitud_contraseña(self, contraseña):
        if len(contraseña) < 8:
            self.error.append("La contraseña debe tener al menos 8 caracteres")
            return False

        else:
            return True

    def espacio_blanco(self, contraseña):
        if contraseña.count(" ") > 0:
            self.error.append("La contraseña no debe tener espacios en blanco")
            return False
        else:
            return True

    def minuscula(self, contraseña):
        caracter_minuscula = False

        for letra in contraseña:
            if letra.islower() == True:
                caracter_minuscula = True
        if not caracter_minuscula:
            self.error.append(
                "La contraseña debe tener al menos un caracter en minuscula")
            return False
        else:
            return True

    def mayuscula(self, contraseña):
        caracter_mayuscula = False

        for letra in contraseña:
            if letra.isupper() == True:
                caracter_mayuscula = True
        if not caracter_mayuscula:
            self.error.append(
                "La contraseña debe tener al menos un caracter en Mayuscula")
            return False
        else:
            return True

    def numero(self, contraseña):
        num = False
        for letra in contraseña:
            if letra.isdigit() == True:
                num = True
        if not num:
            self.error.append("La contraseña debe tener al menos un numero")
            return False
        else:
            return True

    def no_alfanumerico(self, contraseña):
        if contraseña.isalnum() == True:
            self.error.append(
                "La contraseña debe tener al menos un caracter No Alfanumerico")
            return False
        else:
            return True

    def contraseña_ok(self, contraseña):
        ok = self.validar_longitud_contraseña(contraseña) and self.espacio_blanco(contraseña) and self.mayuscula(
            contraseña) and self.minuscula(contraseña) and self.numero(contraseña) and self.no_alfanumerico(contraseña)
        return ok
