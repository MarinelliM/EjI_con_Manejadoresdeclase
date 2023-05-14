import numpy as np
from Alumnos import Alumno
import csv
class ManejadorAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento = 5) -> None:
        self.__alumnos = np.empty(dimension, dtype = Alumno)
        self.__dimension = dimension
        self.__cantidad = 0
        pass
    
    def agregaralumno(self, alum):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]=alum
        self.__cantidad+=1

    def getalumno(self, alum):
        return self.__alumnos[alum]
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__alumnos[i].mostraralumno())
    
    def getnombrecompleto(self,indice):
        return self.__alumnos[indice].getnombreyapellido()
    
    def getaño(self,indice):
        return self.__alumnos[indice].getañocar()
    
    def testManejadorAlumnos(self):
        a1 = Alumno(43839127,'Marinelli','Mauricio','POO',2023)
        a2 = Alumno(43839128,'Nicolas','Lloveras','POO',2023)
        a3 = Alumno(43839129,'Matias','Alvarez','PyE',2022)
        self.agregaralumno(a1)
        self.agregaralumno(a2)
        self.agregaralumno(a3)
        self.mostrar()
    
    def crearorden(self):
        listaordenada = sorted(self.__alumnos,reverse=False)
        for i in range(len(listaordenada)):
            listaordenada[i].mostraralumno()

    def initman(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            dni = fila[0]
            apellido = fila[1]
            nombre = fila[2]
            carrera = fila[3]
            añocar = fila[4]
            al = Alumno(dni,apellido,nombre,carrera,añocar)
            self.agregaralumno(al)

