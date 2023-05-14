from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMaterias import ManejadorMaterias
#from Alumnos import Alumno
import csv
#from Menu import menu
#import numpy as np
if __name__ == "__main__":
    a = input('Ingresa un valor:')
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

    #menu(ma,mm)

# import csv
# from Menu import menu
#
# from Alumnos import Alumno
# from Materias import Materia
# import numpy as np
# if __name__ == "__main__":
#     #alumnos = None
#     materias = []
#     with open('materiasAprobadas.csv', 'r', encoding='utf8') as archivo:
#         reader = csv.reader(archivo, delimiter=';')
#         next(reader)
#         for fila in reader:
#             materia = Materia(fila[0],fila[1],fila[2],fila[3],fila[4])
#             materias.append(materia)
#     archivo.close()
#     for i in range(len(materias)):
#         materias[i].mostrar()
#     with open('alumnos.csv', 'r', encoding='utf8') as archivo:
#         reader = csv.reader(archivo, delimiter=';')
#         next(reader)
#         #alumnos = []
# # Otra forma de cargar el archivo en el arreglo numpy es usando el metodo loadtxt: alumnos = np.loadtxt('alumnos.csv',delimiter=';')
#     #     a = 0
#     #     alumnos_np = np.empty(i, dtype=Alumno)
#     #     for fila in reader:
#     #         alumno = Alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
#     #         #alumnos.append(alumno) 
#     #         #alumnos_np = np.array(alumnos)
#     #         alumnos_np[a] = alumno
#     #         a += 1
#     # archivo.close()
#     # for i in range(len(alumnos_np)):
#     #     alumnos_np[i].mostraralumno()
#     #print(alumnos_np)
   

#         i = sum(1 for fila in reader) # contar el número de filas restantes
#         alumnos_np = np.empty(i, dtype=Alumno) # inicializar el arreglo numpy con el tamaño adecuado
#         archivo.seek(0) # volver al principio del archivo
#         next(reader) # omitir la primera fila de encabezado
#         for a, fila in enumerate(reader):
#             alumno = Alumno(fila[0], fila[1], fila[2], fila[3], fila[4])
#             alumnos_np[a] = alumno
#     archivo.close()
#     for alumno in alumnos_np:
#         alumno.mostraralumno()
#     menu(alumnos_np,materias)