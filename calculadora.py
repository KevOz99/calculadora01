# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado_suma = sumar(num1, num2)
    resultado_resta = restar(num1, num2)
    resultado_multiplicacion = multiplicar(num1, num2)
    resultado_division = dividir(num1, num2)
    print(f"El resultado de la suma es: {resultado_suma}")
    print(f"El resultado de la resta es: {resultado_resta}")
    print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")
    print(f"El resultado de la división es: {resultado_division}")

    