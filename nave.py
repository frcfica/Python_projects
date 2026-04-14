energia_total = 0
while energia_total < 100:
    energia_sumada = int(input("Ingrese una cantidad de energia al cohete: "))
    if energia_sumada <= 0:
        print("Error: no puedes quitar energia o la cantidad es erronea.")
    elif energia_sumada == 100:
        energia_total += energia_sumada
    elif energia_sumada > 0 and energia_sumada <= 100:
        energia_total += energia_sumada
        print(f"Has cargado {energia_sumada} % -->|hay {energia_total} % hasta ahora|<--")
    else:
        print("Has puesto mas de la energia solicitada para despegar.")
print(f"Has llegado a | {energia_total} % | preparate para el despegue...")
contador = 3
while contador >= 1:
    print(f"      | {contador} |")
    contador -= 1
print("---> DESPEGUE <---")
