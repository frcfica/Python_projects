mascota = {
    "nombre": "Thomas",
    "especie": "Perro",
    "edad": 5,
    "raza": "Labrador",
    "vacunas": ["Antirrábica", "Distemper", "Parvovirus"]
}
nueva_vacuna = "Hepatitis"
mascota["vacunas"].append(nueva_vacuna)
cantidad_vacunas = len(mascota["vacunas"])
print(f"---|Ficha de la mascota|---")
print(f"Nombre: {mascota['nombre']}")
print(f"Especie: {mascota['especie']}")
print(f"Vacunas registradas: {', '.join(mascota['vacunas'])}") #.join() para mostrar las vacunas en una sola línea separadas por comas.
print(f"-------------------------------")
print(f"Total de vacunas: {cantidad_vacunas}")