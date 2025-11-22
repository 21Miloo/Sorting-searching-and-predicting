
def loadData(file) -> str:

    '''Permite leer el archivo database.csv y cargar las
        estructuras de datos del programa.'''
    
    with open(file, 'r') as f:
        data = f.read()


    return data
    

info = loadData('data/notas_estudiantes.csv')    




def organizeInfoStudent(data) -> list:

    lines = data.split('\n')

    courses = lines[0].split(',')
    students = lines[1].split(',')

    print(courses)
    print(students)

    noteList = []

    count = 2 # Empieza desde 2 ya que la notas se encuentran a partir de la 2da posicion

    for line in lines[2:]:
      note = line.split(',')
      noteList.append(note)
      count += 1

    print(noteList)

    return courses, students, noteList


organizeInfoStudent(info)