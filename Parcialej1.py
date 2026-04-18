precio = float(input("Ingrese precio del videojuego: "))
vip = input("¿Es miembro VIP? (Sí/No): ")

if precio >= 500:
    precio = precio * 0.9   # descuento del 10%

if vip.lower() == "sí":
    precio = precio * 0.85  # descuento adicional del 15%

print("El precio final es:", precio)
