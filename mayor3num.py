num1 = int(input("ingrese un numero:"))
num2 = int(input("ingrese otro numero:"))
num3 = int(input("ingrese otro numero: "))
if num1>num2 and num1>num3:
    mayor=num1
    if num2>num3:
        menor=num3
        medio=num2
    else:
        menor=num2
        medio=num3
elif num2>num1 and num2>num3:
    mayor=num2
    if num1>num3:
        menor=num3
        medio=num1
    else:
        menor=num1
        medio=num3
elif num3>num1 and num3>num2:
    mayor=num3
    if num2>num1:
        menor=num1
        medio=num2
    else:
        menor=num2
        medio=num1    
elif num1==num2:
    print(f"{num1} y {num2} son iguales")
    print(f"{num3} queda sin puesto")
elif num1==num3:
    print(f"{num1} y {num3} son iguales")
    print(f"{num3} queda sin puesto")
else:
    print("error de credenciales")

print(f"el numero mayor es {mayor}")
print(f"el numero medio es {medio}")
print(f"el numero menor es {menor}")