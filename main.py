from fastapi import FastAPI
import model
    
# Carga inicial de datos
students = model.load_students()

app = FastAPI()

@app.get("/estudiantes")
async def get_all(carrera: str | None = None):
    """
    Primer nivel: /estudiantes

    - Si se proporciona `carrera`, filtra la lista por ese valor.
    - Si no, devuelve todos los estudiantes.

    Parámetros de consulta:
    - carrera (opcional): Nombre de la carrera a filtrar.

    Retorna:
        Lista de estudiantes.
    """
    if carrera:
        students_subset = []
        for student in students:
            if student.carrera == carrera:
                students_subset.append(student)
        if not students_subset:
            return {"Error": "La carrera ingresada no existe"}
        return (students_subset)
    return (students)

@app.get("/estudiantes/activos")
async def get_enrolled_students():
    """
    Segundo nivel: /estudiantes/activos

    - Devuelve sólo los estudiantes con estatus == 'Activo'.
    - Si no hay ninguno, retorna un mensaje informativo.

    Retorna:
        Lista de estudiantes activos o un dict con mensaje.
    """
    students_subset = []
    for student in students:
        if student.estatus == 'Activo':
            students_subset.append(student)
    if not students_subset:
        return {"No hay alumnos activos"}
    return (students_subset)

@app.get('/estudiantes/{matricula}')
async def get_student_by_school_id(matricula: str):
    """
    Primer nivel: /estudiantes/{matricula}

    Parámetro del path:
    - matricula: Matrícula del estudiante a buscar.

    Retorna:
        Instancia de Estudiante si existe, o un dict de error.
    """
    for student in students:
        if student.matricula == matricula:
            return (student)
    return {"Error": "La matrícula ingresada no existe"}

@app.get("/estudiantes/genero/{genero}")
async def get_students_by_gender(genero: str):
    """
    Segundo nivel: /estudiantes/genero/{genero}

    Parámetro de path:
    - genero: Género a filtrar ('Femenino' o 'Masculino').

    Retorna:
        Lista de estudiantes o dict de error si no hay coincidencias.
    """
    students_subset = []
    for student in students:
        if student.genero == genero:
            students_subset.append(student)
    if not students_subset:
        return {"Error": "No hay instancias relacionadas al parámetro ingresado"}
    return (students_subset)

@app.get("/estudiantes/semestre/{semestre}")
async def get_students_by_semester(semestre: int):
    """
    Segundo nivel: /estudiantes/semestre/{semestre}

    Parámetro de path:
    - semestre: Número de semestre a filtrar.

    Retorna:
        Lista de estudiantes o dict de error si no hay coincidencias.
    """
    students_subset = []
    for student in students:
        if student.semestre == semestre:
            students_subset.append(student)
    if not students_subset:
        return {"Error": "No hay instancias relacionadas al parámetro ingresado"}
    return (students_subset)

@app.get("/estudiantes/genero/{genero}/semestre/{semestre}")
async def get_students_by_gender_semester(genero: str, semestre: int):
    """
    Tercer nivel: /estudiantes/genero/{genero}/semestre/{semestre}

    Parámteros de path:
    - genero: Género.
    - semestre: Semestre.

    Retorna:
        Lista combinada o dict de error si no hay coincidencias.
    """
    students_subset = []
    for student in students:
        if student.genero == genero and student.semestre == semestre:
            students_subset.append(student)
    if not students_subset:
        return {"Error": "No hay instancias relacionadas a los parámetros ingresados"}
    return (students_subset)

@app.get("/estudiantes/semestre/{semestre}/porcentaje_min/{porcentaje_min}")
async def get_students_by_semester_percentage(semestre: int, porcentaje_min: int):
    """
    Tercer nivel: /estudiantes/semestre/{semestre}/porcentaje_min/{porcentaje_min}

    Parámetros de path:
    - semestre: Semestre.
    - porcentaje_min: Porcentaje avanzado mínimo.

    Retorna:
        Lista o dict de error si no hay coincidencias.
    """
    students_subset = []
    for student in students:
        if student.semestre == semestre and student.porcentaje_avanzado >= porcentaje_min:
            students_subset.append(student)
    if not students_subset:
        return {"Error": "No hay instancias relacionadas a los parámetros ingresados"}
    return (students_subset)

@app.get("/estudiantes/{carrera}/{materias_min}")
async def get_students_by_degree_courses(carrera: str, materias_min: int):
    """
    Tercer nivel: /estudiantes/{carrera}/{materias_min}

    Parámteros de path:
    - carrera: Nombre de la carrera.
    - materias_min: Número mínimo de materias aprobadas.

    Retorna:
        Lista de coincidencias o dict de error.
    """
    students_subset = []
    for student in students:
        if student.carrera == carrera and student.materias_aprobadas >= materias_min:
            students_subset.append(student)
    if not students_subset:
        return {"Error": "No hay instancias relacionadas a los parámetros ingresados"}
    return (students_subset)

@app.get("/estudiantes/genero/{genero}/creditos_max/{creditos_max}")
async def get_students_by_gender_credits(genero: str, creditos_max: int):
    """
    Tercer nivel: /estudiantes/genero/{genero}/creditos_max/{creditos_max}

    Parámetros de path:
    - genero: Género del estudiante.
    - creditos_max: Máximo de créditos acumulados.

    Retorna:
        Lista filtrada o dict de error.
    """
    students_subset = []
    for student in students:
        if student.genero == genero and student.creditos_acumulados <= creditos_max:
            students_subset.append(student)
    if not students_subset:
        return {"Error": "No hay instancias relacionadas a los parámetros ingresados"}
    return (students_subset)