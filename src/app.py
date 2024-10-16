from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def main():
    while True:
        print("\nIngrese su fecha de nacimiento:")
        dia = int(input("Día (DD): "))
        mes = int(input("Mes (MM): "))
        año = int(input("Año (YYYY): "))

        try:
            fecha_nacimiento = datetime(año, mes, dia)
            edad = calcular_edad(fecha_nacimiento)
            print(f"Tienes {edad} años.")
        except ValueError:
            print("La fecha ingresada no es válida. Por favor, inténtelo de nuevo.")

        continuar = input("\n¿Deseas calcular otra edad? (s/n): ").lower()
        if continuar != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
