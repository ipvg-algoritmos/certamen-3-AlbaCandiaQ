temperatura = []
for i in range(5):
    temp =int(input("Ingresa una temperatura: "))
    temperatura.append(temp)

promedio = sum(temperatura) / len(temperatura)
maxima = max(temperatura)
check = True
for temp in temperatura:
    if temp > 15 or temp < 30 :
        check = False
        print("La temperatura está correcta")
    if temp < 10 or temp > 35 :
        print("Advertencia, verifica la temperatura de tus plantas")
        check = True
