
descuentos = {(1, True): 0.2, (1, False): 0.15, (2, True): 0.1, (2, False): 0.05}
tot_recaudo = tot_descuento = nro_personas = 0
while True:
    valor_boleta = int(input("Ingrese el valor de la boleta..."))
    if valor_boleta <= 0:
        break
    estrato = int(input("Estrato....."))
    edad = int(input("Edad........"))
    descuento = descuentos.get((estrato, edad < 18), 0)
    if descuento == 0:
            print("No tiene descuento, el estrato es mayor o igual a 3")
    pagar = valor_boleta - valor_boleta * descuento
    tot_recaudo += pagar
    tot_descuento += valor_boleta * descuento
    nro_personas += 1
    print("Valor descontado....", valor_boleta * descuento)
    print("Valor a pagar.......", pagar)
    print("")
    print("")
    print ("Número de personas ingresadas...", nro_personas)
    print ("Total valor recaudado...........", tot_recaudo)
    print ("Total valor descontado..........", tot_descuento)

