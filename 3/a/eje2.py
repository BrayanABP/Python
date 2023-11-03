f1 = input ("Ingrese la frase 1:")
f2 = input ("Ingrese la frase 2:")
lista_final = []

longitud_frase_corta = min (len(f1), len(f2))
for indice in range (longitud_frase_corta):
  if f1[indice] == f2 [indice]:
      lista_final.append(f1[indice])

print (lista_final)