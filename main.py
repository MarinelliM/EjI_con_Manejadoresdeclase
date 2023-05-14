from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMaterias import ManejadorMaterias
import csv
if __name__ == "__main__":
    mm = ManejadorMaterias()
    mm.initmm()
    mm.test()
    dni = int(input('Ingrese dni a buscar:'))
    mm.buscarpromedio(dni)
    ma = ManejadorAlumnos(3,10)
    ma.testManejadorAlumnos()
    with open('alumnos.csv', 'r', encoding='utf8') as archivo:
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        i = sum(1 for fila in reader) # contar el número de filas restantes
        archivo.seek(0) # volver al principio del archivo
        next(reader)
    ma = ManejadorAlumnos(i,i*2)
    ma.initman()
    materia = str(input('Ingrese el nombre de la materia a buscar:'))
    mm.buscarmaterias(materia,ma)
    ma.crearorden()
