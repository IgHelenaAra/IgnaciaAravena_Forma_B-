
compradores = []

# 1 - 2 - 3
def validar_letras_numeros_codigo(alfaveto_numeros_codigo):
    """Verifica que el codigo tenga al menos 1 letra mayúscula, al menos 1 número y no espacio en blanco"""
    caracteres_permitidos = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789")
    for caracter in alfaveto_numeros_codigo:
        if caracter not in caracteres_permitidos:
            return False
    return True

def validar_nombre(nombre):
    """Verifica que nombres no esten repetidos"""
    for comprador in compradores:
        if comprador['nombre'].lower() == nombre.lower():
            return False
    return True

def validar_tipo_entrada(tipo_entrada):
    """Verificamos que el tipo de entrada sea G (General) o  V (Vip)"""
    return tipo_entrada.upper() in ['G','V']

def validar_codigo_vericador(codigo_verificador):
    """Verificamos que el codigo: mínimo de 6 caracteres, al menos 1 letra mayúscula, al menos 1 número y no espacio en blanco"""
    if len(codigo_verificador) != 6:
        return False
    if not validar_letras_numeros_codigo(codigo_verificador):
        return False 
    for comprador in compradores:
        if comprador['codigo_verificador'].upper() == codigo_verificador.upper():
            return False
    return True

# Paso 1
def registro_de_compradores():
    """Registramos compradores"""
    print("°° Registro compradores °°")
    comprador = {}

    while True:
        nombre = input("Nombre del comprador: ")
        if validar_nombre(nombre):
            comprador['nombre'] = nombre
            break
        print("Error: El nombre que ingreso ya esta registrado o es invalido.")
    while True:
        tipo_entrada = input("El tipo de entrada seleccionada es(G - v):").strip().upper()
        if validar_tipo_entrada(tipo_entrada):
            break
        print("Error: El tipo de entrada debe ser G (General) o V (Vip).")
    while True:
        codigo_verificador = input("Ingrese un codigo de minimo 6 digitos(letras(una mayus) - Numeros): ")
        if validar_codigo_vericador(codigo_verificador):
            compradores['codigo_verificador'] = codigo_verificador.upper()
            break
        print("Error: el codigo debe tener mínimo de 6 caracteres, al menos 1 letra mayúscula, al menos 1 número y no espacios en blanco.")
    
    compradores.append(comprador)
    print("¡Compra exitosa!")

# Paso 2
def buscar_comprador():
    """Buscamos mediante su nombre"""
    print("°° Buscamos comprador °°")
    if not compradores:
        print("El comprador no se encuentra.")
        return

    busqueda_comprador = input(" Ingrese el nombre del comprador: ").strip()
    compradores_encontrados = []
    for comprador in compradores:
        if busqueda_comprador.lower() in comprador['nombre'].lower(): 
            compradores_encontrados.append(comprador)

    if not compradores_encontrados:
        print("El comprador no se encuentra.")
        return
    
    print("Resultados de la busqueda: ")
    for i, comprador in enumerate(compradores_encontrados, 1):
        print(f"Busqueda {i}: ")
        print(f"Codigo Verificador: {comprador['codigo_verificador']}")
        print(f"Nombre comprador: {comprador['nombre']}")
        print(f"Tipo de Entrada: {comprador['tipo_entrada']}")

# Paso 3
def cancelar_compra():
    """Cancelamos o Eliminamos la compra"""
    print("°° Cancelamos compra °°")
    if not compradores:
        print("No se pudo cancelar la compra.")
        return
    nombre = input("Ingrese el nombre del comprador a cancelar la compra:").strip().upper()
    for i, comprador in enumerate(compradores):
        if comprador['nombre'].upper() == nombre.upper():
            confirmacion = input(f"Seguro quieres cancelar la compra de {comprador['nombre']}?? [Si(S) / No(N)]:").strip().upper()
            if confirmacion == 'S':
                print("¡Compra cancelada!")
            else:
                print("No se pudo cancelar la compra.")
            return
    print("No se pudo cancelar la compra.")

def main():
    while True:
        print("Concierto de Trap con el 'Conejo Simpático'")
        print("__ Menú Web __")
        print("1 - Comprar entrada.")
        print("2 - Consultar entrada.")
        print("3 - Cancelar entrada.")
        print("4 - Salir.")

        opcion = input("Seleccione una opcion(1 a 4): ").strip()

        if opcion == "1":
            registro_de_compradores()  
        elif opcion == "2":
            buscar_comprador()
        elif opcion == "3":
            cancelar_compra()  
        elif opcion == "4":
            # Salir
            print("Saliendo del programa....")
            break
        else:
            print("Error: Ingrese una opcion correspondiente(1 - 2 - 3 - 4).")

if __name__ == "__main__":
    main()