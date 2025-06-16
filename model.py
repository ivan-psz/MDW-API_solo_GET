from pydantic import BaseModel
import csv
import sys

CSV_FILE = './Base_Datos.csv'

class Estudiante(BaseModel):
    """
    Modelo de datos que representa a un estudiante.

    Atributos:
    - id: Identificador único (int).
    - matricula: Matrícula (str).
    - nombre: Nombre completo (str).
    - genero: Género del estudiante (str).
    - edad: Edad en años (int).
    - estatus: Estado de inscripción ('Activo', 'Baja temporal' o 'Baja definitiva') (str).
    - carrera: Nombre de la carrera (str).
    - semestre: Último semestre cursado (int).
    - materias_aprobadas: Número de materias aprobadas (int).
    - creditos_acumulados: Créditos totales acumulados (int).
    - porcentaje_avanzado: Porcentaje de avance curricular (int, 0-100).
    """
    id: int
    matricula: str
    nombre: str
    genero: str
    edad: int
    estatus: str
    carrera: str
    semestre: int
    materias_aprobadas: int
    creditos_acumulados: int
    porcentaje_avanzado: int
    
def load_students():
    """
    Lee el CSV de estudiantes y carga la lista de objetos Estudiante.

    Regresa:
        Una lista de instancias de Estudiante. Si ocurre un OSError,
        finaliza la ejecución.
    """
    students = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8-sig', newline='') as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                student = Estudiante(
                    id=int(row['id']),
                    matricula=row['matricula'],
                    nombre=row['nombre'],
                    genero=row['genero'],
                    edad=int(row['edad']),
                    estatus=row['estatus'],
                    carrera=row['carrera'],
                    semestre=int(row['semestre']),
                    materias_aprobadas=int(row['materias_aprobadas']),
                    creditos_acumulados=int(row['creditos_acumulados']),
                    porcentaje_avanzado=int(row['porcentaje_avanzado'])
                )
                students.append(student)
            return students
    except OSError as e:
        print(f"[ERROR {type(e)}]: No se pudo abrir/leer el archivo: {CSV_FILE}")
        sys.exit()