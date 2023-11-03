listado=[]

numero=int(input("Ingrese cuantos elementos desea tener en la lista"))

for x in range(numero):
  listado.append(input("ingrese el primer elemento a la lista:"))
print(listado)
listado.reverse()
print(listado[1])