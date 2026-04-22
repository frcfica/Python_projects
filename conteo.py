candidatos = ("A" , "B" , "C")
votos = [0, 0, 0]
while votos[0] + votos[1] + votos[2] < 10:
    voto = input("Ingrese su voto (A, B o C): ").upper()
    if voto in candidatos:
        suma = candidatos.index(voto)
        votos[suma] += 1
    else:
        print("Voto inválido. Intente de nuevo.")   
print ("Fin de la votación:")
for i in range(len(candidatos)):
    print(candidatos[i] + ": " + str(votos[i]) + " votos")