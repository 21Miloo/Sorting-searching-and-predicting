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
 
    indexStudent = students.index(id) # Ubicamos el indice del estudiante

    # Ubicamos las notas correspondientes a el estudiante y dentro de esas notas buscamos la mas alta y ubicamos su indice

    notesStudent = notes[indexStudent] # < contiene las notas del estudiante

    # Agrupamos las notas por curso
    notesByCourse = []

    for i in range(len(notesStudent)):
        note = notesStudent[i]
        course = courses[i]

        notesByCourse.append((note, course)) # < tupla con la nota y el curso

    # Validamos que la lista no este vacia
    if not notesByCourse:
        return None

    notesByCourse.sort()

    maxNote = notesByCourse[-1]
    maxNoteCourse = maxNote[1]

    print(maxNote)
    print(maxNoteCourse)

    return maxNote, maxNoteCourse


def sortStudentsByAverage(students: list, notes: list):


    

    pass