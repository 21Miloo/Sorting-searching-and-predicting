import matplotlib
import os
import subprocess

# Intentar seleccionar un backend GUI disponible en macOS.
# Debe hacerse antes de importar `pyplot`, pero si ya hay un backend
# establecido por la variable de entorno, intentamos no romperlo.
for _backend in ("macosx", "TkAgg", "Qt5Agg"):
    try:
        matplotlib.use(_backend)
        break
    except Exception:
        # si no está disponible, intentamos el siguiente
        continue

import matplotlib.pyplot as plt


def predictStudents(years: list, students: list, yearToPredict: int):
    """
    Predice estudiantes usando rectas por tramos (como pidió el profesor),
    calcula el MAE, y genera la gráfica con:
        - Datos reales
        - Rectas por tramos
        - Punto predicho
    """

    # -----------------------------
    # 1. ORDENAR LOS DATOS
    # -----------------------------
    data = sorted(zip(years, students), key=lambda x: x[0])
    years_sorted = [d[0] for d in data]
    students_sorted = [d[1] for d in data]

    # -----------------------------
    # 2. FUNCIÓN AUXILIAR: obtener predicción por segmento
    # -----------------------------
    def predict_from_segments(x):
        # Si x está antes del primer punto → extrapolar
        if x <= years_sorted[0]:
            x1, y1 = years_sorted[0], students_sorted[0]
            x2, y2 = years_sorted[1], students_sorted[1]

        # Si x está después del último punto
        elif x >= years_sorted[-1]:
            x1, y1 = years_sorted[-2], students_sorted[-2]
            x2, y2 = years_sorted[-1], students_sorted[-1]

        # Si x está en medio → buscar el tramo correspondiente
        else:
            for i in range(len(years_sorted) - 1):
                x1, x2 = years_sorted[i], years_sorted[i+1]
                if x1 <= x <= x2:
                    y1 = students_sorted[i]
                    y2 = students_sorted[i+1]
                    break

        # calcular pendiente y recta
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        return m * x + b

    # -----------------------------
    # 3. CALCULAR MAE
    # -----------------------------
    predicted_all = [predict_from_segments(x) for x in years_sorted]

    mae = sum(abs(students_sorted[i] - predicted_all[i]) for i in range(len(years_sorted)))
    mae /= len(years_sorted)

    # -----------------------------
    # 4. PREDICCIÓN FINAL
    # -----------------------------
    predicted_year = predict_from_segments(yearToPredict)

    # -----------------------------
    # 5. GRAFICAR
    # -----------------------------
    plt.figure(figsize=(12, 6))

    # Datos reales
    plt.scatter(years_sorted, students_sorted, color="blue", label="Datos reales")

    # Dibujar rectas por tramos
    for i in range(len(years_sorted)-1):
        x1, x2 = years_sorted[i], years_sorted[i+1]
        y1, y2 = students_sorted[i], students_sorted[i+1]

        # pendiente y recta
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        xs = [x1, x2]
        ys = [m*x1 + b, m*x2 + b]

        plt.plot(xs, ys, color="orange")

    # Punto predicho
    plt.scatter(yearToPredict, predicted_year, color="green", s=120, label=f"Predicción {yearToPredict}")

    plt.title("Modelo de predicción por tramos lineales")
    plt.xlabel("Año")
    plt.ylabel("Estudiantes matriculados")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # Guardar una copia de la figura para diagnóstico
    try:
        plt.savefig('last_prediction.png')
    except Exception:
        pass

    # Intentar mostrar la ventana con bloqueo. Si el backend es no-interactivo
    # (por ejemplo 'Agg') o `plt.show()` falla, abrir la imagen guardada con el
    # visor por defecto de macOS para garantizar que el usuario vea la gráfica.
    backend = matplotlib.get_backend().lower()
    try:
        if 'agg' in backend:
            # backend no interactivo: abrir la imagen guardada
            if os.path.exists('last_prediction.png'):
                subprocess.run(['open', 'last_prediction.png'])
        else:
            plt.show(block=True)
    except Exception:
        if os.path.exists('last_prediction.png'):
            try:
                subprocess.run(['open', 'last_prediction.png'])
            except Exception:
                # último recurso: imprimir ruta al archivo
                print('Gráfica guardada en:', os.path.abspath('last_prediction.png'))

    # -----------------------------
    # 6. RETORNAR VALORES
    # -----------------------------
    return predicted_year, mae
