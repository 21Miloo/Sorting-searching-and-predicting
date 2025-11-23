def deleteStudent(id: str, students: list, notes: list) -> bool:
    """Permite eliminar el estudiante correspondiente a un número de
    documento dado (y sus notas)"""

    if id not in students:
        return False  # Si el estudiante no existe, retornamos False

    indexId = students.index(id)  # Guardamos el indice del estudiante a eliminar

    students.pop(indexId)  # Eliminamos a el estudiante de la lista

    notes.pop(indexId)  # Eliminamos las notas de ese estudiante

    return True


def getStudentMaxGrade(id: str, students: list, notes):
    """Retorna la nota y el código del curso en el cual ha obtenido
    su mayor nota un estudiante dado."""

    indexStudent = students.index(id) 

    # Ubicamos las notas correspondientes a el estudiante y dentro de esas notas buscamos la mas alta y ubicamos su indice


    notesStudent = notes[indexStudent]

    #Buscamos el numero mas alto en la lista

    count = 0
    for note in notes:
        if note > count:
            count = note
    
    print(count) # Debe de imprimir la nota mayor


    pass
