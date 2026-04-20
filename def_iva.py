# Definimos la función
def calcular_iva(): #Función para calcular el IVA de un producto
    print("=|Bienvenido a la calculadora de IVA (19%)|=") #Mensaje de bienvenida
    nombre = input("Ingre el nombre del producto: ") #Solicitamos el nombre del producto
    precio_neto = float(input("Precio: ")) #Precio sin IVA
    iva = precio_neto * 0.19 #Valor del IVA en Chile
    total = precio_neto + iva #Precio total con IVA incluido
    print("==========|CALCULADORA DE IVA|==========") #Encabezado para mostrar el resultado
    print(f"Resultado para: {nombre}") #Mostramos el nombre del producto
    print(f"Neto: {precio_neto}") #Mostramos el precio sin IVA
    print(f"Total con IVA: {total}") #Mostramos el precio total con IVA incluido
    print("="*40) #Línea de separación para mejorar la presentación del resultado
# Llamamos a la función
calcular_iva() 