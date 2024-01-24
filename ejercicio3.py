Voltaje1=float(input("Querido usuario ingresa el valor del primer voltaje: "))
Voltaje2=float(input("Querido usuario ingresa el valor del segundo voltaje: "))
Voltaje3=float(input("Querido usuario ingresa el valor del tercer voltaje: "))

promediovol= (Voltaje1+Voltaje2+Voltaje3)/3

if promediovol <115:
    print(f"{promediovol} Este voltaje es CORRECTO")
else:
    if promediovol >115:
        if promediovol<220:
            print(f"{promediovol} Este voltaje es ALTO")
        else:
            if promediovol>220:
                print(f"{promediovol} Este voltaje es PELIGROSO")
    