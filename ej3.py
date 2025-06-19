edad = int(input("Ingresa tu edad: "))
es_supervisor = input("Eres supervisor: ")
autorizacion = input("Tienes autorización?: ")
if edad >= 18 and (es_supervisor == "si" or autorizacion == "si") :
    print("Acceso permitido")
else:
    print("Acceso denegado")