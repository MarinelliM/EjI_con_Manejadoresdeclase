from Materias import Materia
import csv
from datetime import datetime, date
from ManejadorAlumnos import ManejadorAlumnos
class ManejadorMaterias:
    __lista: list
    def __init__(self) -> None:
        self.__lista = []
        pass
  
    def agregarmateria(self,materia):
        self.__lista.append(materia)

    def buscarpromedio(self,dni):
        i = 0
        a = 0
        b = 0
        promsinap = 0
        promconap = 0
        while i < len(self.__lista):
            if self.__lista[i].getdni() == dni:
                if self.__lista[i].getnota() > 3:
                    promsinap += self.__lista[i].getnota() 
                    a += 1
                    b += 1
                    promconap += self.__lista[i].getnota()
                    i += 1
                else: 
                    promconap += self.__lista[i].getnota()
                    b += 1
                    i += 1
            else: i += 1
        print('Promedio sin aplazos: %.2f' % (promsinap/a))
        print('Promedio con aplazos: %.2f' % (promconap/b))

    def buscarmaterias(self,materia, MA):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getnombre() == materia:
                if self.__lista[i].getaprobacion() == 'P' and self.__lista[i].getnota() > 6:
                    print('DNI\t\tApellido y nombre\t\tFecha\t\tNota\t\tAño que cursa')
                    print('{}\t{}\t\t{}\t{}\t\t{}'.format(self.__lista[i].getdni(),MA.getnombrecompleto(i),self.__lista[i].getfecha(),self.__lista[i].getnota(),MA.getaño(i)))
            i += 1
  
    def initmm(self):
        archivo = open('materiasAprobadas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            dni = int(fila[0])
            nombre_materia = fila[1]
            #fecha = date(fila[2])
            fecha = datetime.strptime(fila[2], '%d/%m/%Y').date()
            nota = int(fila[3])
            aprobacion = fila[4]
            mat = Materia(dni,nombre_materia,fecha,nota,aprobacion)
            self.agregarmateria(mat)
    
    def test(self):
        for e in range(len(self.__lista)):
            self.__lista[e].mostrar()