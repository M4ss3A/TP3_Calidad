def sumar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def calcular_total(precio, cantidad):
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
    return precio * cantidad
