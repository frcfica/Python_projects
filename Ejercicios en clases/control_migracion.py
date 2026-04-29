pasaporte = input("¿Tu pasarporte está vigente? (Si/No): ").lower().strip()
if pasaporte == "no":
    print("No puedes ingresar al país. Tienes que dirigirte a la oficina de tramites.")
elif pasaporte == "si":
    print("\nMotivos de viaje:|Turismo|Trabajo|Estudio|Otro|.")
    motivo = input("¿Cuál es el motivo de su viaje?: ").lower().strip()
    if motivo == "turismo":
        print("Permiso autorizado por 90 días.")
    elif motivo == "trabajo":
        print("Debe presentar su contrato laboral en el módulo 5.")
    elif motivo == "estudio":
        print ("Debe presentar su comprobante de matrícula.")
    else:
        print("Por favor, espere a un oficial de migración.")
else:
    print("Respuesta no válida. Por favor, reinicie el proceso y responda 'Si' o 'No'.")