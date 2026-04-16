logistica = {"Norte": [], "Centro": [], "Sur": []}
for sector in logistica:
    print(f"Paquetes para {sector}:")
    item = input("Ingrese paquete (o 'fin' para terminar): ")
    while item != 'fin':
        logistica[sector].append(item)
        item = input("Ingrese paquete (o 'fin' para terminar): ")
for sector in logistica:
    if sector == "Centro":
        clave = ""
        while clave != "1234":
            clave = input("---|ZONA RESTRINGIDA|--- Ingrese clave: ")
    print(f"Paquetes en {sector}: {logistica[sector]}")