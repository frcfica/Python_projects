supermercado = {
    "lacteos": {"leche": 1100, "yogurt": 450, "queso": 2500, "mantequilla": 1200},
    "verduras":{"tomate": 1500, "lechuga": 900, "papas": 1200, "cebolla": 1000},
    "carnes": {"pollo": 5000, "vacuno": 9500, "cerdo": 4500, "hamburguesa": 800},
    "articulos_aseo": {"cloro": 1300, "detergente": 7500, "lavaloza": 2200}
}
carrito = []
total_general = 0

print("Bienvenido al supermercado")
while True:
    print("\n ===| PASILLOS DISPONIBLES |===")
    print("1. Lacteos\n2. Verduras\n3. Carnes\n4. Articulos de aseo\n5. Salir y pagar")

    opcion = input("Seleccione un pasilo (1-4), para salir digite la  opcion 5 o 'salir': ").lower()

    if opcion == "5" or opcion == "salir":
        break
    if opcion == "1": opcion = "lacteos"
    elif opcion == "2": opcion = "verduras"
    elif opcion == "3": opcion = "carnes"
    elif opcion == "4": opcion = "articulos de aseo"