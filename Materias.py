#from datetime import date
import datetime

class Materia:
    __dni: int
    __nombre_materia: str
    __fecha: datetime.date
    __nota: int
    __aprobacion: str

    def __init__(self, dni, nombremat, fecha, nota, aprobacion) -> None:
        self.__dni = dni
        self.__nombre_materia = nombremat
        self.__fecha = datetime.datetime.strptime(fecha.strftime('%d/%m/%Y'), '%d/%m/%Y').date()
        self.__nota = nota
        self.__aprobacion = aprobacion
        pass

    def mostrar(self):
        return print('Dni del alumno: {}. Materia: {}. Fecha que curso: {}. Nota: {}. Aprobacion: {}' .format(self.__dni, self.__nombre_materia,self.__fecha,self.__nota,self.__aprobacion))
    
    def __eq__(self,otro):
        return self.getdni() == otro
    
    def getdni(self):
        return self.__dni
    
    def getnota(self):
        return self.__nota
    
    def getnombre(self):
        return self.__nombre_materia
    
    def getaprobacion(self):
        return self.__aprobacion
    
    def getfecha(self):
        return self.__fecha

    def __gt__(self, otro):
        return self.getnota() > otro
