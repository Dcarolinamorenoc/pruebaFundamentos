Voltaje1=float(input("Querido usuario ingresa el valor del primer voltaje: "))
Voltaje2=float(input("Querido usuario ingresa el valor del segundo voltaje: "))
Voltaje3=float(input("Querido usuario ingresa el valor del tercer voltaje: "))
Voltaje4=float(input("Querido usuario ingresa el valor del cuarto voltaje: "))
Voltaje5=float(input("Querido usuario ingresa el valor del quinto voltaje: "))

promediovol= (Voltaje1+Voltaje2+Voltaje3+Voltaje4+Voltaje5)/5

if promediovol >=220:
    print(f"{promediovol} Este voltaje es ALTO")
else:
    print(f"{promediovol} Este voltaje es CORRECTO")
    


