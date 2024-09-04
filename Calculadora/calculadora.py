BANNERS = [
    r"""
   _____      _            _           _                 
  / ____|    | |          | |         | |                
 | |     __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _ 
 | |    / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |
 | |___| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
  \_____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|
                                                         
    Made with LOVE by @ivaeiro
    """
]

def imprimir_banner():
    for banner in BANNERS:
        print(banner)

imprimir_banner()

#funciones operaciones

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def division(num1, num2):
    return num1 / num2

while True:
    print("""
    Indica la operacion:
    
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir
    """)

    opcion = input("Selecciona una opcion: ")

    if opcion == '1':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el primer numero: "))
        print(f"El resultado de la suma es: {suma(num1, num2)}")
    elif opcion == '2':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el primer numero: "))
        print(f"El resultado de la resta es: {resta(num1, num2)}")
    elif opcion == '3':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el primer numero: "))
        print(f"El resultado de la multiplicacion es: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el primer numero: "))
        print(f"El resultado de la division es: {division(num1, num2)}")
    else:
        print("Saliento de la calculadora...")
        break