precio = float(input("Ingrese precio: "))
vip = input("¿Es miembro VIP? (Sí/No): ")

if precio >= 500:
    precio = precio * 0.9

if vip.lower() == "sí":
    precio = precio * 0.85 

print("El total es:", precio)
