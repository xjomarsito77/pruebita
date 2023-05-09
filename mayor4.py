num1=int(input("ingresa un numero: "))
num2=int(input("ingresa un numero: "))
num3=int(input("ingresa un numero: "))
num4=int(input("ingresa un numero: "))
if num1>num2 and num3 and num4:
    print(f"{num1} es el mayor de {num2},{num3} y {num4}")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} es el mayor de {num3},{num4} y {num1}")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} es el mayor de {num4},{num1} y {num2}")
elif num4>num1 and num4>num2 and num4>num3:
    print(f"{num4} es el mayor de {num1},{num2} y {num3}")
elif num1==num2 and num1!=num3 and num1!=num4:
    print(f"{num1} y {num2} son iguales, a diferencia que {num3} y {num4} son distintos")
elif num2==num3 and num2!=num1 and num2!=num4:
    print(f"{num2} y {num3} son iguales, a diferencia que {num1} y {num4} son distintos")
elif num3==num4 and num3!=num1 and num3!=num2:
    print(f"{num3} y {num4} son iguales, a diferencia que {num1} y {num2} son distintos")
elif num1==num3 and num1!=num2 and num1!=num4:
    print(f"{num1} y {num3} son iguales, a diferencia que {num2} y {num4} son distintos")
elif num2==num4 and num2!=num1 and num2!=num3:
    print(f"{num2} y {num4} son iguales, a diferencia que {num1} y {num3} son distintos")
else:
    print("todos son iguales")

