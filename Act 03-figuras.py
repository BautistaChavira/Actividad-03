import math

def areaCuadrado():
    input1 = input("Ingrese la medida de los lados del cuadrado\n")
    cuadrado = int(input1)**2
    print("El area del cuadrado es ", cuadrado)

def areaTriangulo():
    input1 = input("Ingrese la medida de la base\n")
    input2 = input("Ingrese la medida de la altura\n")
    triangulo = int(input1) * int(input2) / 2
    print("El area del triangulo es ", triangulo)

def areaCirculo():
    input1 = input("Ingrese el radio\n")
    circulo = math.pi * (int(input1)**2)
    print(f"El area del circulo es {circulo:.2f}")

opcion = int(input("Elija la figura del area que desea calcular\n[1]Cuadrado\n[2]Triangulo\n[3]Circulo\n"))
if opcion == 1:
    areaCuadrado()
else:
    if opcion == 2:
        areaTriangulo()
    else:
        if opcion == 3:
            areaCirculo()
