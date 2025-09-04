import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Generador de vectores
# -------------------------
def generar_vectores():
    """Genera 10 vectores de 100 enteros aleatorios (1-100)."""
    return [np.random.randint(1, 101, size=100) for _ in range(10)]

# -------------------------
# Algoritmos con contadores
# -------------------------
def burbuja(vectores):
    ordenados = []
    intercambios = []
    for v in vectores:
        arr = v.tolist()
        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    count += 1
        ordenados.append(arr)
        intercambios.append(count)
    return ordenados, intercambios

def insercion(vectores):
    ordenados = []
    intercambios = []
    for v in vectores:
        arr = v.tolist()
        count = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                count += 1
                j -= 1
            arr[j+1] = key
        ordenados.append(arr)
        intercambios.append(count)
    return ordenados, intercambios

def seleccion(vectores):
    ordenados = []
    intercambios = []
    for v in vectores:
        arr = v.tolist()
        count = 0
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                count += 1
        ordenados.append(arr)
        intercambios.append(count)
    return ordenados, intercambios

# -------------------------
# Ejecución principal
# -------------------------
if __name__ == "__main__":
    vectores = generar_vectores()

    # Ordenar con los tres algoritmos
    ordenados_b, intercambios_b = burbuja(vectores)
    ordenados_i, intercambios_i = insercion(vectores)
    ordenados_s, intercambios_s = seleccion(vectores)

    # Mostrar algunos vectores ordenados
    print("\n===== Vectores ordenados =====")
    for idx in range(10):  # mostrar solo 3 vectores por algoritmo
        print(f"\nVector {idx+1} con Burbuja   : {ordenados_b[idx]}")
        print(f"Vector {idx+1} con Inserción : {ordenados_i[idx]}")
        print(f"Vector {idx+1} con Selección : {ordenados_s[idx]}")

    # Mostrar intercambios por vector
    print("\n===== Intercambios por vector =====")
    for i in range(10):
        print(f"Vector {i+1:02d}: Burbuja={intercambios_b[i]}, Inserción={intercambios_i[i]}, Selección={intercambios_s[i]}")

    # Calcular estadísticas
    def resumen(valores):
        return np.mean(valores), np.std(valores)

    resumen_b = resumen(intercambios_b)
    resumen_i = resumen(intercambios_i)
    resumen_s = resumen(intercambios_s)

    # Tabla de resultados
    print("\n===== Resultados de Intercambios (Promedio y Desviación Est.) =====")
    print("{:<12} {:>20} {:>20}".format("Algoritmo", "Promedio", "Desviación Est."))
    print("-"*55)
    print("{:<12} {:>20.2f} {:>20.2f}".format("Burbuja", resumen_b[0], resumen_b[1]))
    print("{:<12} {:>20.2f} {:>20.2f}".format("Inserción", resumen_i[0], resumen_i[1]))
    print("{:<12} {:>20.2f} {:>20.2f}".format("Selección", resumen_s[0], resumen_s[1]))

    # Boxplot
    datos = [intercambios_b, intercambios_i, intercambios_s]
    etiquetas = ["Burbuja", "Inserción", "Selección"]

    plt.boxplot(datos, labels=etiquetas)
    plt.title("Distribución de intercambios por algoritmo")
    plt.ylabel("Número de intercambios")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()