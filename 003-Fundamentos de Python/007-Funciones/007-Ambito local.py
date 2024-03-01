email = "info@josevicentecarratala.com"

def dimeHola(nombre,edad):
    global email
    email = "uno@dos.com"
    return f"Yo te digo hola, {nombre}, y que sepas que tienes {edad} años, y tu email es {email}"

print(dimeHola("Jose Vicente",45))
print(dimeHola("Juan",40))
print(dimeHola("Jorge",50))

print(email)
