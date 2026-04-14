# Reto: El Restaurante

print("Bienvenido al Restaurante. Elige una categoría:")
print("1. Pizza")
print("2. Hamburguesa")
print("3. Ensalada")

categoria = input("Escribe tu elección: ").lower()

if categoria == "pizza":
    tipo = input("¿La quieres 'Familiar' o 'Individual'?: ").lower()
    print(f"Preparando una Pizza {tipo}.")

elif categoria == "hamburguesa":
    queso = input("¿La prefieres 'Con Queso' o 'Sin Queso'?: ").lower()
    if queso == "con queso":
        print("Preparando una deliciosa Hamburguesa con queso fundido.")
    else:
        print("Preparando una Hamburguesa clásica sin queso.")

elif categoria == "ensalada":
    print("Preparando ensalada fresca.")

else:
    print("Opción no válida. Por favor, elige entre Pizza, Hamburguesa o Ensalada.")