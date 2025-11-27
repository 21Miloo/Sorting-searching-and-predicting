# comando pip install matplotlib
from utils import organizeInfoStudent, organizeHistoryEnrollment, loadData
from student_data_utils import deleteStudent, getStudentMaxGrade, sortStudentsByAverage, sortByNumberOfCourses
from linear_regression import predictFutureStudents



info = loadData("data/notas_estudiantes.csv")
historyEnrollment = loadData("data/hist_matriculados.csv")

# Cargamos la información de los estudiantes
courses, students, notes = organizeInfoStudent(info)

# Cargar la información histórica
yearsHistory, studentsHistory = organizeHistoryEnrollment(historyEnrollment)

while True:
    print("\n----- MENÚ PRINCIPAL -----")
    print("1. Eliminar estudiante")
    print("2. Nota más alta de un estudiante")
    print("3. Promedio de estudiantes")
    print("4. Ordenar por cantidad de cursos")
    print("5. Predecir matrícula futura")
    print("6. Salir\n")

    option = input("Seleccione opción: ")

    if option == '1':
        id = input("Ingrese el documento del estudiante: ")
        deleteStudent(id, students, notes)

    elif option == '2':
        id = input("Ingrese el documento del estudiante: ")
        getStudentMaxGrade(id, students, notes, courses)

    elif option == '3':
        sortStudentsByAverage(students, notes)

    elif option == '4':
        sortByNumberOfCourses(students, notes)

    elif option == '5':
        a = float(input("Ingrese valor de a: "))
        b = float(input("Ingrese valor de b: "))
        predictFutureStudents(yearsHistory, studentsHistory, a, b)

    elif option == '6':
        print("Saliendo...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
