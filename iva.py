producto = input("Nombre del producto: ")
precio = float(input("Precio sin IVA: "))

iva = precio * 0.19
total = precio + iva

print("--------------------------")
print("Producto:", producto)
print("Precio neto:", precio)
print("Precio con IVA:", total)
print("--------------------------")