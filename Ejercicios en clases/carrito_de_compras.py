carrito = {}
continuar = True
print("---|Bienvenido al Carrito de compras|---")
while continuar:
    item = input("Ingrese un artículo: ")
    precio = float(input("Ingrese el precio de " + item + ": "))
    carrito[item] = precio
    continuar = input("¿Quieres añadir articulos a la lista (Si/No)? ").lower() == "si"
coste = 0
print("\n---|Carrito de compras|---")
for item, precio in carrito.items():
    print(item, '\t' , precio)
    coste += precio
    print("Costo total: ", coste)