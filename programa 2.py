
def calcular_superficie(lado1, lado2):
    return lado1 * lado2


lado1_rect1 = float(input("Ingrese el primer lado del primer rectángulo: "))
lado2_rect1 = float(input("Ingrese el segundo lado del primer rectángulo: "))


lado1_rect2 = float(input("Ingrese el primer lado del segundo rectángulo: "))
lado2_rect2 = float(input("Ingrese el segundo lado del segundo rectángulo: "))


superficie_rect1 = calcular_superficie(lado1_rect1, lado2_rect1)
superficie_rect2 = calcular_superficie(lado1_rect2, lado2_rect2)


if superficie_rect1 > superficie_rect2:
    print("El primer rectángulo tiene una superficie mayor.")
elif superficie_rect2 > superficie_rect1:
    print("El segundo rectángulo tiene una superficie mayor.")
else:
    print("Ambos rectángulos tienen la misma superficie.")
