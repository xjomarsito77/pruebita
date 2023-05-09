num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
if num1 > num2:
    print(f"{num2} es el menor")
    print(f"{num1} es el mayor")
elif num2 > num1:
    print(f"{num1} es el menor")
    print(f"{num2} es el mayor")
else:
    print(f"{num1} y {num2} son iguales")

    