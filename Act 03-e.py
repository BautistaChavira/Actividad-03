def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

limite = int(input("Ingrese el limite del ciclo para la sumatoria en el calculo del numero e\n"))
n = 0
e = 0
while n < limite:
    e = e + (1/factorial(n))
    n = n + 1
print("El numero resultante es: ", e)