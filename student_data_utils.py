def deleteStudent(id: str, students: list, notes: list) -> bool:
    """Permite eliminar el estudiante correspondiente a un número de
    documento dado (y sus notas)"""

    if id not in students:
        return False  # Si el estudiante no existe, retornamos False

    indexId = students.index(id)  # Guardamos el indice del estudiante a eliminar

    students.pop(indexId)  # Eliminamos a el estudiante de la lista

    notes.pop(indexId)  # Eliminamos las notas de ese estudiante

    return True


def getStudentMaxGrade(id: str, students: list, notes: list, courses: list):
    """Retorna la nota y el código del curso en el cual ha obtenido
    su mayor nota un estudiante dado."""

    if id not in students:
        return None

    indexStudent = students.index(id)  # Ubicamos el indice del estudiante

    # Ubicamos las notas correspondientes a el estudiante y dentro de esas notas buscamos la mas alta y ubicamos su indice

    notesStudent = notes[indexStudent]  # <- contiene las notas del estudiante

    # Agrupamos las notas por curso
    notesByCourse = []

    for i in range(len(notesStudent)):
        note = notesStudent[i]
        course = courses[i]

        notesByCourse.append((note, course))  # <- tupla con la nota y el curso

    # Validamos que la lista no este vacia
    if not notesByCourse:
        return None

    notesByCourse.sort()

    maxNote = notesByCourse[-1]
    maxNoteCourse = maxNote[1]

    print(maxNote)
    print(maxNoteCourse)

    return maxNote, maxNoteCourse


# Primero hallamos el promedio de notas y luego organizamos. EL promedio lo debemos de guardar en un array a parte

students = [
    "1033492448",
    "1032090603",
    "1002152167",
    "1028854736",
    "1014191590",
    "1024351175",
    "1036351870",
]
notas = [
    [-1.0, 1.1, 4.8, 4.2, 1.5],
    [0.4, 4.4, -1.0, 4.5, 3.3],
    [2.1, 3.1, 2.5, 1.8, 2.8],
    [3.4, 3.7, 4.2, -2.0, 3.4],
    [4.6, 4.9, 4.4, 1.6, 3.2],
    [4.0, 2.4, 2.3, 0.1, 4.1],
    [3.1, 3.7, 2.9, 3.8, 4.8],
]


def sortStudentsByAverage(students: list, notes: list) -> list:
    """Imprime por pantalla a los estudiantes ordenados
    según su promedio de notas, de mayor a menor"""

    averages = []

    # iteramos en cada nota

    for studentNotes in notes:

        validNotes = []

        for n in studentNotes:
            if n >= 0:
                validNotes.append(n)

        avgStudent = sum(validNotes) / len(
            validNotes
        )  # Lo podriamos dividir por 5 directamente, pero usamos el tamaño de la lista para descartar que hallan mas notas
        averages.append(
            avgStudent
        )  # Agregamos el promedio a la lista averages (Siguen manteniendo sus posiciones)

    print(averages)

    # Aplicamos el algoritmo burbuja  / Debemos de intercambiar tambien la posicion del estudiante cuando cambiemos la posicion de la nota

    for i in range(len(averages)):
        for j in range(len(averages) - i - 1):
            if averages[j] < averages[j + 1]:

                # Cambios en los promedios
                temp = averages[j]
                averages[j] = averages[j + 1]
                averages[j + 1] = temp

                # Cambios en los estudiantes
                tempStudent = students[j]
                students[j] = students[j + 1]
                students[j + 1] = tempStudent

    print("Promedio de estudiantes: \n")
    print("Estudiante   Promedio\n")
    for i in range(len(students)):
        print(students[i], "  ", averages[i], "\n")

    return students, averages


# sortStudentsByAverage(students, notas)


def sortByNumberOfCourses(students: list, notes: list) -> list:
    """Ordena los estudiantes según la cantidad
    de materias cursadas e imprime el resultado por la pantalla"""

    # contador manual de materias por estudiante
    quantityCoursesStudents = []

    subjectStudied = []

    for coursesStudent in notes:

        for course in coursesStudent:

            if course <= -2:
                continue
            subjectStudied.append(course)

        quantity = len(
            subjectStudied
        )  # <- Contine el numero exacto de materias del estudiante
        print(quantity)
        subjectStudied = []  # <- reiniciamos la lista para el siguiente estudiante

        quantityCoursesStudents.append(
            quantity
        )  # <- lo agregamos a una lista donde luego haremos el ordenamiento por seleccion

    # Algoritmo de ordenamiento por seleccion

    for i in range(0, len(quantityCoursesStudents)):
        min = i
        for j in range(i + 1, len(quantityCoursesStudents)):
            if quantityCoursesStudents[min] > quantityCoursesStudents[j]:
                min = j

        # Cambios en la cantidad de cursos
        temp = quantityCoursesStudents[i]
        quantityCoursesStudents[i] = quantityCoursesStudents[min]
        quantityCoursesStudents[min] = temp

        # Cambios en los estudiantes
        temp = students[i]
        students[i] = students[min]
        students[min] = temp

    print("Estudiantes por materias cursadas:\n")
    print("Estudiante\tCantidad Cursos")

    for i in range(len(quantityCoursesStudents)):
        print(students[i], "\t", quantityCoursesStudents[i])

    return students, quantityCoursesStudents


# sortByNumberOfCourses(students, notas)
