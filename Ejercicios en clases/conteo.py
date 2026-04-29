candidatos = ("Jose Antonio Kast" , "Jeannette Jara" , "Franco Parisi")
votos = [0, 0, 0]
while True:
    voto = input("Ingrese su voto (Jose Antonio Kast, Jeannette Jara, Franco Parisi) o 'salir' para terminar: ").lower()
    if voto == "salir":
        break
    elif voto == candidatos[0].lower():
        votos[0] += 1
    elif voto == candidatos[1].lower():
        votos[1] += 1
    elif voto == candidatos[2].lower():
        votos[2] += 1
    else:
        print("Voto no válido. Intente de nuevo.")
print("Resultados de la votación:")
for i in range(len(candidatos)):
    print(f"{candidatos[i]}: {votos[i]} votos")
    print("El ganador es: " + candidatos[votos.index(max(votos))])