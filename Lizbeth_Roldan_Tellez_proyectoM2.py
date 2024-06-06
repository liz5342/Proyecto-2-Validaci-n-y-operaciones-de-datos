def verificar_longitud_palabra():
    palabra = input("Ingrese una palabra: ")
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

def encontrar_cuadrante():
    try:
        x = float(input("Ingrese X: "))
        y = float(input("Ingrese Y: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return
    
    if x == 0 or y == 0:
        print("Ninguna coordenada debe ser 0.")
        return
    
    if x > 0 and y > 0:
        cuadrante = "I"
    elif x < 0 and y > 0:
        cuadrante = "II"
    elif x < 0 and y < 0:
        cuadrante = "III"
    elif x > 0 and y < 0:
        cuadrante = "IV"
    
    print(f"El punto se encuentra en el cuadrante {cuadrante}")

# Llamadas a las funciones
verificar_longitud_palabra()
encontrar_cuadrante()
