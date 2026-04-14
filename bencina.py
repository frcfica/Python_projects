print("--|Bienvenido a la estación de servicio [Santo Tomas]|--")
for bomba in range(1, 4):
    print(f"\n--|Revisando Bomba {bomba}|--")
    respuesta = input(f"Bomba {bomba}: ¿Desea cargar combustible? (si/no): ").lower()
    if respuesta == "si":
        monto = float(input("Ingrese el monto a cargar: "))
        while monto <= 0:
            monto = float(input("Error, ingrese un monto válido: "))
        print(f"Bomba {bomba} cargada con ${monto}")
    else:
        print(f"Saltando Bomba {bomba}...")
        continue
print("\n--|Proceso de carga de bombas finalizado|--")
