
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

#Pruebas Unitarias

#Probaremos que la ccondicion de notas negativas funciona correctamente ya que si la nota es negativa no se debe contar para el promedio por que o no
#matriculo o cancelo la materia

print("\nPrueba unitaria Caja Negra\n")

students1 = ["Ana", "Luis", "Pedro"]
notes1 = [
    [8.0, 5.0, 7.0],         # Ana cursó 3 materias
    [9.0, -3, 6.0, 8.0],     # Luis cursó 3 materias nota -3 no cuenta
    [7.0]                    # Pedro cursó 1 materia
]

assert sortByNumberOfCourses(students1, notes1) == (
    ["Pedro", "Ana", "Luis"],   # ordenados por menor cantidad de cursos
    [1, 3, 3]
), "Error en la prueba unitaria 1"

print("Prueba unitaria 1 pasada\n")
