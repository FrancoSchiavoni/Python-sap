import sys
import time

def show_iteration_bar(iteration, total):
    try:
        # Calculamos el progreso como un porcentaje
        progress = (iteration + 1) / total
        # Calculamos el número de caracteres "#" para representar el progreso
        num_caracteres = int(50 * progress)
        # Creamos la cadena que representa el progreso
        progress_bar = "[" + "#" * num_caracteres + " " * (50 - num_caracteres) + "]"
        # Imprimimos el progreso en la primera línea de la consola
        sys.stdout.write(f"\rProgreso: {progress_bar} {progress * 100:.2f}%")
        sys.stdout.flush()  # Limpiamos el buffer de la salida estándar
        time.sleep(0.1)
    except Exception as e:
        # Si ocurre un error, lo mostramos en la segunda línea de la consola
        sys.stderr.write(f"\nError al mostrar el progreso: {e}\n")


def show_error(e):
        sys.stderr.write(f"\nError al mostrar el progreso: {e}\n")
        sys.stdout.flush()  # Limpiamos el buffer de la salida estándar
        time.sleep(0.1)