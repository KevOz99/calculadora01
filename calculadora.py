#calculadora.py

def sumar(a,b):
    return a+b

if __name__== "_main_":
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    resultado = sumar(num1+num2)
    print(f"EL RESULTADO DE LA SUMA ES: {resultado} ")
     