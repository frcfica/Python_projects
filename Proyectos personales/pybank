# ==========================================================
# EXPLICACIÓN DEL [import sys]
# ==========================================================
""" En el código unificado, usamos sys.exit(). Esta función le dice a Python: "Cierra el programa completamente y deja de ejecutar cualquier línea de código ahora mismo".
Es la forma más "limpia" y profesional de terminar un programa desde adentro de una función o un bucle infinito (while True). """

import sys

# ==========================================================
# PAREJA 1: EL MODELO (CLASE CLIENTE)
# ==========================================================
class Cliente:
    def __init__(self, rut, nombre, apellido, saldo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo
        self.password = None # Comienza vacío según la instrucción

# DICCIONARIO GLOBAL (Donde se guarda todo)
db = {}

# ==========================================================
# PAREJA 2: PANEL DE ADMINISTRACIÓN
# ==========================================================
def panel_admin():
    print("\n--- ADMIN ---")
    clave = input("Contraseña maestra: ")
    if clave != "admin123":
        print("Clave incorrecta")
        return

    rut = input("RUT: ")
    if rut in db:
        print("El RUT ya existe")
    else:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        monto = float(input("Monto inicial: "))
        # Guardamos el objeto en el diccionario usando el RUT como llave
        db[rut] = Cliente(rut, nombre, apellido, monto)
        print("Registrado con éxito")

# ==========================================================
# PAREJA 3: AUTENTICACIÓN (LOGIN)
# ==========================================================
def login():
    rut = input("Ingrese su RUT: ")
    if rut not in db:
        print("RUT no registrado")
        return None

    usuario = db[rut]

    # Si no tiene clave, debe crear una
    if usuario.password is None:
        print("Usuario nuevo, cree su clave")
        p1 = input("Clave nueva: ")
        p2 = input("Repita clave: ")
        if p1 == p2:
            usuario.password = p1
            print("Clave guardada")
        else:
            print("No coinciden")
            return None

    # Pedir clave para entrar
    intento = input("Contraseña: ")
    if intento == usuario.password:
        return usuario
    else:
        print("Clave errónea")
        return None

# ==========================================================
# PAREJA 4: OPERACIONES (RETIRO)
# ==========================================================
def retirar(usuario):
    monto = float(input("Monto a retirar: "))
    if monto > usuario.saldo:
        print("Saldo insuficiente")
    else:
        confirmar = input("Confirme su clave para retirar: ")
        if confirmar == usuario.password:
            usuario.saldo -= monto
            print(f"Retiro exitoso. Saldo: {usuario.saldo}")
        else:
            print("Clave incorrecta")

# ==========================================================
# PAREJA 5: MENÚS Y UNIÓN
# ==========================================================
def menu_cliente(usuario):
    while True:
        print(f"\n--- HOLA {usuario.nombre} ---")
        print("1. Ver Saldo / 2. Retirar / 3. Salir")
        op = input("Opción: ")
        if op == "1":
            print(f"Saldo: {usuario.saldo}")
        elif op == "2":
            retirar(usuario)
        elif op == "3":
            break

def main():
    while True:
        print("\n--- PYBANK ---")
        print("1. Admin / 2. Cliente / 3. Salir")
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            panel_admin()
        elif opcion == "2":
            user = login()
            if user:
                menu_cliente(user)
        elif opcion == "3":
            sys.exit()

main()
