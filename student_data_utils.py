def deleteStudent(id: str, students: list, notes: list) -> bool:
    """Permite eliminar el estudiante correspondiente a un número de
    documento dado (y sus notas)"""

    indexId = students.index(id)  # Guardamos el indice del estudiante a eliminar

    students.pop(indexId)  # Eliminamos a el estudiante de la lista

    notes.pop(indexId)  # Eliminamos las notas de ese estudiante

    return bool
