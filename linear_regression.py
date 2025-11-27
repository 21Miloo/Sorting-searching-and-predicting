import matplotlib.pyplot as plt
from plots import plot_data

# A representa la pendiente de la recta (representa el cambio anual en estudiantes. En la práctica, suele estar entre –50 y +50)
# B representa la intersección con el eje Y ( número de estudiantes cuando X=0 puede ser * un número muy grande * un número negativo *un valor que no tiene sentido interpretativo)

X = 0  # Año

Y = 0  # Cantidad de estudiantes matriculados

# Ecuacion lineal:
#
# Y = aX + b

# Pedir año al usuario
# # Retornar cantidad de estudiantes que estima estarán matriculados ese año así como el
# error del modelo. También deberá generar un archivo que contenga una gráfica cómo la
# mostrada en esta guía, donde aparezcan los datos históricos, la regresión lineal y el punto
# específico que fue estimado de acuerdo a la solicitud del usuario.


def linearRegressionPredict(years: list, a: float, b: float):
    """Calcula los valores estimados de estudiantes matriculados para cada año en la lista de años"""

    estimatedStudents = []

    for year in years:

        y = (a * year) + b

        estimatedStudents.append(y)

    return estimatedStudents


def calculateMAE(students: list, estimatedStudents: list):
    """Calcula el Error Absoluto Medio (MAE) entre los valores reales y los estimados."""

    totalError = 0

    for i in range(len(students)):

        error = abs(students[i] - estimatedStudents[i])

        totalError += error

    mae = totalError / len(students)

    return mae


def pedrictOneYear(year: int, students: list, a: float, b: float):
    """Predice la cantidad de estudiantes para un único año futuro."""

    # Calcular el valor estimado para el año futuro
    estimatedStudents = (a * year) + b

    return estimatedStudents


def predictFutureStudents(years: list, students: list, a: float, b: float):

    # 1. Calcular valores estimados para todos los años históricos
    estimatedStudents = linearRegressionPredict(years, a, b)

    # 2. Calcular el MAE del modelo
    mae = calculateMAE(students, estimatedStudents)

    # 3. Pedir año futuro
    futureYear = int(input("Ingrese un año futuro para predecir: "))

    # 4. Calcular la predicción para ese año
    futurePrediction = pedrictOneYear(futureYear, students, a, b)

    print("\n-------------------------------------")
    print("Año futuro:", futureYear)
    print("Estudiantes estimados:", futurePrediction)
    print("Error MAE del modelo:", mae)
    print("-------------------------------------\n")

    # 5. Preparar datos para pasarlos a la funcion de graficar
    data = []
    for i in range(len(years)):
        data.append([years[i], students[i]])

    # Graficamos los datos históricos y la regresión
    plot_data(data, estimatedStudents, years)

    # Dibujamos EL PUNTO FUTURO ENCIMA DE LA GRÁFICA
    plt.plot(
        futureYear, futurePrediction, "go", markersize=12
    )  # punto específico que fue estimado de acuerdo a la solicitud del usuario (go: green y circulo, markersize: tamaño del punto)
    plt.show()

    return estimatedStudents, mae, futureYear, futurePrediction
