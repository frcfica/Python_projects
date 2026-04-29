productos = ["Cereal" , "Leche" , "Harina" , "Sobre de sopa" , "Azucar" , "Yogurth" , "Fideos" , "Galletas" ]
contador = 0
contador_v = [""]
for producto in productos:
    decision = input(f"Estas revisando |{producto}|, esta vencido si|no: ").lower()
    if decision == "si":
        print(f"-|ALERTA|- retirar |{producto}| del estante")
        break
    else:
        print(f"El producto es |{producto}|")