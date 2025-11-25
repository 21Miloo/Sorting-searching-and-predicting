def loadData(file) -> str:
    """Permite leer el archivo database.csv y cargar las
    estructuras de datos del programa."""

    with open(file, "r") as f:
        data = f.read()

    return data


info = loadData("data/notas_estudiantes.csv")
historyEnrollment = loadData("data/hist_matriculados.csv")


def organizeInfoStudent(data) -> list:

    lines = data.split("\n")

    courses = lines[0].split(",")
    students = lines[1].split(",")

    print(courses)
    print("--------------------------------")
    print(students)
    print("--------------------------------")

    noteList = []

    for line in lines[2:]:

        if not line.strip():
            continue

        notesStr = line.split(",")  # < contiene las notas de un estudiante
        print(notesStr)

        studentsNotes = []

        for value in notesStr:
            studentsNotes.append(float(value))

        noteList.append(studentsNotes)

    print("--------------------------------")
    print(noteList)

    return courses, students, noteList


organizeInfoStudent(info)


# Abrir el archivo hist_matriculados.csv y cargar los datos en dos listas


def organizeHistoryEnrollment(data) -> list:
    """Permite leer el archivo hist_matriculados.csv y cargar las
    estructuras de datos del programa."""

    lines = data.split("\n")

    # print(lines)

    years = []
    students = []

    for line in lines[1:]:
        if not line.strip():
            continue

        value = line.split(",")
        years.append(int(value[0]))
        students.append(int(value[1]))

    print(years, "\n")
    print(students, "\n")

    return years, students


# organizeHistoryEnrollment(historyEnrollment)
