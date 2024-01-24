import math

longitud1=float(input("Querido usuario ingresa el valor de un lado de su triangulo equilatero: "))

raiz= math.sqrt (3)/4
areatri= raiz*(longitud1*longitud1)

if areatri>1000:
    print(f"El area de de este triangulo equiltaero es: {areatri}  y Los DATOS NO SON VALIDOS debido a que el area es mayor a 1000")
else:
    print(f"El area de de este triangulo equiltaero es: {areatri} y Los DATOS SON VALIDOS debido a que el area no es mayor a 1000")

