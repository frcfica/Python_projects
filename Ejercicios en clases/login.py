credenciales = ("admin" , "1234") # Tupla con el usuario y contraseña correctos
usuario = input("Ingrese su usuario: ").lower() #C onvierte el usuario a minúsculas para evitar problemas de mayúsculas/minúsculas
contraseña = input("Ingrese su contraseña: ") # No se convierte a minúsculas para permitir contraseñas con mayúsculas
if usuario == credenciales[0] and contraseña == credenciales[1]: # Verifica si el usuario y contraseña son correctos
    print("Bienvenido, " + usuario) # Si el usuario y contraseña son correctos, muestra un mensaje de bienvenida
while usuario != credenciales[0] or contraseña != credenciales[1]: # Si el usuario o contraseña son incorrectos, entra en un bucle para pedirlos nuevamente
    print("Usuario o contraseña incorrectos. Intente de nuevo.") # Muestra un mensaje de error
    usuario = input("Ingrese su usuario: ").lower() # Pide el usuario nuevamente y lo convierte a minúsculas
    contraseña = input("Ingrese su contraseña: ") # Pide la contraseña nuevamente sin convertirla a minúsculas