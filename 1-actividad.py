"""
Cree un programa donde solicita al usuario que ingrese un numerador 
y un denominador para realizar una división. Si el denominador 
es cero, captura la excepción ZeroDivisionError y muestra un 
mensaje de error. Si el usuario ingresa valores no numéricos,
captura la excepción ValueError. El programa sigue solicitando la 
entrada hasta que se ingrese una entrada válida. Después de cada 
división exitosa, pregunta al usuario si desea realizar otra división.
Si el usuario ingresa 's', el programa continuará ejecutándose, 
de lo contrario, el programa finalizará.
"""

def dividir_numeros():
    while True:
        try:
            numerador = float(input("Ingrese el numerador: "))
            denominador = float(input("Ingrese el denominador: "))
            resultado = numerador / denominador
            print("El resultado de la división es:", resultado)
            break  # Sale del bucle si la división se realiza con éxito
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Ingresa solo números. Inténtalo de nuevo.")

def principal():
    while True:
        print("\n--- División de Numeros ---")
        dividir_numeros()
        
        continuar = input("\n¿Desea realizar otra división? (s/n): ")
        if continuar.lower() != 's':
            break  # Sale del bucle principal si el usuario no desea continuar


if __name__ == "__main__":
    principal()
