#uso de match case
opcion = input("Ingresa el nombre de la fruta:")
match opcion:
    case "manzana":
        print("roja o verde")
    case "platano":
        print("amarillo")
    case "uva":
        print("morado")
    case _:
        print("color desconocido")