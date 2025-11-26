
X = 0 # Año

Y = 0 # Cantidad de estudiantes matriculados

# Ecuacion lineal: 
# 
# Y = aX + b

#Pedir año al usuario
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


def pedrictOneYear(year: int, a: float, b: float):

    """Predice la cantidad de estudiantes para un único año futuro."""

    estimatedStudents = (a * year) + b

    return estimatedStudents
    
    

def predictFutureStudents(years, students, a, b):
    
    estimatedStudents = linearRegressionPredict(years, a, b)