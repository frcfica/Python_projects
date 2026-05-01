# Definimos la clase que servirá como "molde" para cada cliente
class Cliente:
    def __init__(self, rut, nombre, apellido, saldo_inicial):
        # Atributos básicos que se asignan al crear el objeto
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo_inicial
        # La contraseña parte vacía (None) para identificar usuarios nuevos
        self.password = None 

# Contenedor global: un diccionario donde la llave es el RUT 
# y el valor es el objeto (instancia) del Cliente
base_datos_clientes = {}

def panel_administracion():
    print("\n--- ACCESO ADMINISTRACIÓN ---")
    admin_pass = input("Ingrese clave maestra: ")
    
    # Validación simple de acceso para el administrador
    if admin_pass != "admin123":
        print("Clave incorrecta. Regresando...")
        return

    print("\n[Registro de Nuevo Cliente]")
    rut = input("Ingrese RUT: ")
    
    # Verificamos si la llave (RUT) ya existe en el diccionario
    if rut in base_datos_clientes:
        print("Error: Este RUT ya está registrado.")
        return

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    
    # Manejo de errores por si el usuario ingresa letras en lugar de números
    try:
        monto = float(input("Monto de apertura: "))
        if monto < 0:
            print("El monto no puede ser negativo.")
            return
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")
        return

    # Creamos la instancia de la clase Cliente
    nuevo_cliente = Cliente(rut, nombre, apellido, monto)
    
    # Guardamos el objeto en el diccionario usando el RUT como identificador
    base_datos_clientes[rut] = nuevo_cliente
    print(f"Éxito: Cliente {nombre} registrado correctamente.")

def portal_cliente():
    print("\n--- PORTAL DEL CLIENTE ---")
    rut = input("Ingrese su RUT para iniciar sesión: ")

    # Buscamos si el RUT existe en nuestra base de datos (diccionario)
    if rut not in base_datos_clientes:
        print("Error: El RUT no se encuentra en el sistema.")
        return

    # Recuperamos el objeto cliente asociado a ese RUT
    cliente = base_datos_clientes[rut]

    # --- GESTIÓN DE CONTRASEÑA ---
    # Si password es None, significa que nunca ha ingresado
    if cliente.password is None:
        print("Usuario nuevo detectado. Por favor, cree su contraseña.")
        while True:
            p1 = input("Defina su contraseña: ")
            p2 = input("Confirme su contraseña: ")
            if p1 == p2 and p1 != "":
                cliente.password = p1
                print("Contraseña guardada con éxito.")
                break
            else:
                print("Las contraseñas no coinciden. Intente de nuevo.")
    else:
        # Si ya tiene contraseña, se la solicitamos para entrar
        intento = input("Ingrese su contraseña: ")
        if intento != cliente.password:
            print("Contraseña incorrecta.")
            return

    # --- MENÚ DE OPERACIONES DEL CLIENTE ---
    while True:
        print(f"\nBienvenido/a {cliente.nombre} {cliente.apellido}")
        print("1. Cambiar Contraseña")
        print("2. Ver Monto (Saldo)")
        print("3. Realizar Retiro")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            actual = input("Ingrese su clave actual: ")
            if actual == cliente.password:
                n1 = input("Nueva clave: ")
                n2 = input("Confirme nueva clave: ")
                if n1 == n2:
                    cliente.password = n1
                    print("Contraseña actualizada.")
                else:
                    print("Las claves no coinciden.")
            else:
                print("Clave actual incorrecta.")

        elif opcion == "2":
            # Accedemos al atributo 'saldo' del objeto
            print(f"Su saldo actual es: ${cliente.saldo}")

        elif opcion == "3":
            try:
                monto_r = float(input("Monto a retirar: "))
                # Validamos que tenga fondos suficientes
                if monto_r > cliente.saldo:
                    print("Fondos insuficientes.")
                elif monto_r <= 0:
                    print("Monto no válido.")
                else:
                    # Por seguridad, pedimos la clave antes de restar dinero
                    confirmar = input("Para procesar, ingrese su contraseña: ")
                    if confirmar == cliente.password:
                        cliente.saldo -= monto_r # Restamos del atributo saldo
                        print(f"Retiro exitoso por ${monto_r}")
                        print(f"Saldo restante: ${cliente.saldo}")
                    else:
                        print("Contraseña incorrecta. Operación cancelada.")
            except ValueError:
                print("Error: Ingrese un monto válido.")

        elif opcion == "4":
            print("Cerrando sesión del cliente...")
            break

def main():
    # Bucle principal que mantiene el programa corriendo
    while True:
        print("\n==============================")
        print("      SISTEMA PYBANK")
        print("==============================")
        print("1. Sistema de Administración")
        print("2. Portal del Cliente")
        print("3. Apagar Sistema")
        
        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == "1":
            panel_administracion()
        elif opcion_principal == "2":
            portal_cliente()
        elif opcion_principal == "3":
            print("Apagando PyBank... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

# Punto de entrada del script
if __name__ == "__main__":
    main()