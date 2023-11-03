import random
lanza = 0
while lanza < 10:
    input("Enter para su lanzamiento!!")
    x = random.randint(1,6)
    print(f"Resultado: {x}")
    lanza += 1
    if x == 1:
        print("Pierde el juego! Sacaste 1!")
        break
if lanza == 10:
  print("Ganaste el juego! No sacaste el número 1!!")
