velocidad = float(input("Ingresa la velocidad del coche: ")) 
if velocidad < 20:
    print("Muy lento")
elif 20 <= velocidad <= 60:
    print("Velocidad moderada")
elif 61 <= velocidad <= 120:
    print("Velocidad alta")
else:
    print("¡Multa por exceso de velocidad!")