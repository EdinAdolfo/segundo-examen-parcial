
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))


resultado = calcular_promedio(num1, num2, num3)


print(f"El promedio de {num1}, {num2} y {num3} es: {resultado}")
