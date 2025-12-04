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


# Prueba de caja negra


#Datos de prueba
estudiantes1 = ["Ana", "Carlos", "Beatriz"]
notas1 = [
    [8.5, 9.0, 7.5, 8.0, 9.5],  # Ana
    [7.0, 6.5, 7.5, 8.0, 7.0],  # Carlos
    [9.0, 9.5, 8.5, 9.0, 10.0]  # Beatriz
]
print('Prueba unitaria de sortStudentsByAverage\n')

assert sortStudentsByAverage(estudiantes1, notas1) == (['Beatriz', 'Ana', 'Carlos'], [9.2, 8.5, 7.2]), "Error en la prueba unitaria 1"
print('Prueba unitaria 1 pasada\n')

print('\n Un solo estudiante')
estudiantes2 = ["Pedro"]
notas2 = [[8.0, 8.0, 8.0, 8.0, 8.0]]
assert sortStudentsByAverage(estudiantes2, notas2) == (['Pedro'], [8.0]), "Error en la prueba 2"
print('Prueba unitaria 2 pasada\n')

print('\nOrden inverso')
estudiantes3 = ["Omar", "Esteban", "Ana"]
notas3 = [
    [5.0, 5.0, 5.0, 5.0, 5.0],  
    [7.0, 7.0, 7.0, 7.0, 7.0],  
    [9.0, 9.0, 9.0, 9.0, 9.0] 
]
assert sortStudentsByAverage(estudiantes3, notas3) == (['Ana', 'Esteban', 'Omar'], [9.0, 7.0, 5.0]), "Error en la prueba 3"
print('Prueba unitaria 3 pasada\n')


#Prueba de caja blanca

#Probaremos que la ccondicion de notas negativas funciona correctamente ya que si la nota es negativa no se debe contar para el promedio por que o no
#matriculo o cancelo la materia

print('\nPrueba 4: Filtrado de notas negativas')
estudiantes4 = ["Laura"]
notas4 = [[9.0, -1, 8.0, -1, 10.0]]  # Solo cuenta 9.0, 8.0, 10.0
assert sortStudentsByAverage(estudiantes4, notas4) == (['Laura'], [9.0]), "Error en la prueba 4"
print('Pasó')

