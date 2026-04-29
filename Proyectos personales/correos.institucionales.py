dominio = "@alumnos.santotomas.cl"
print("--|Bienvenido al generador de correos|--")
nombre = input("Ingrese su nombre: ").lower().strip()
apellido = input("Ingrese su apellido: ").lower().strip()
while True:
    año = input("Ingrese solo los últimos 2 dígitos de su año de nacimiento (Ej: 98): ")
    if len(año) == 2 and año.isdigit():
        break
    else:
        print("Error: Debe ingresar exactamente 2 números.")
print(f"\nSu correo institucional es: {nombre}.{apellido}{año}{dominio}")
