# Este programa pide al usuario su nombre y lo saluda.

def main():
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Hola, {nombre}! Bienvenido al programa.")
    print("¡Hasta luego!")

if __name__ == "__main__":
    print("Este programa no debe ser importado.")
    main()