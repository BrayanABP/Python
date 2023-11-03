pn = float(input("primera nota: "))
ps =float(input("segunda nota: "))
pt = float (input("tercera nota: "))
ef = float (input("nota del examen final: "))
tf = float (input("nota del trabajo final: "))
nd = (pn+ps+pt)/3
final = nd*0.55+ef*0.30+tf*0.15
print("La nota final es ",round(final,1))