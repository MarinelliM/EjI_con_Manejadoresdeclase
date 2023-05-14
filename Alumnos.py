class Alumno:
    __dni: int
    __apellido: str
    __nombre: str
    __carrera: str
    __año_carrera: int

    def __init__(self, dni, apellido, nombre, carrera, año) -> None:
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año_carrera = año
        pass

    def __str__(self) -> str:
        return "%8d %s %s %s %4d" % (self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__año_carrera)
        pass

    def getdni(self):
        return self.__dni
    
    def getañocar(self):
        return self.__año_carrera
    
    def getapellido(self):
         return self.__apellido
    
    def getnombre(self):
         return self.__nombre
    
    def getnombreyapellido(self):
        return self.__nombre+ ' ' +self.__apellido
    
    def mostraralumno(self):
        return print('Alumno: {} {}. Dni: {}. Carrera: {}. Año de cursado: {}' .format(self.__nombre,self.__apellido,self.__dni,self.__carrera,self.__año_carrera))
    
    def __lt__(self, otro):
        if self.getañocar() < otro.getañocar():
            return True
        elif self.getañocar() == otro.getañocar():
            return (self.getapellido(), self.getnombre()) < (otro.getapellido(), otro.getnombre())
        else: return False

