def sumar(a ,b):
    return a+b
while True:
    try:
        n1 = int(input("Ingrese valor: "))
        n2 = int(input("Ingrese valor: "))
        break
    except:
        print("Ingrese solo numeros!")

print(sumar(n1, n2))