def main():
    while True:
        try:
            _cTokens = int(input("Cantidad de tokens (1-3): "))
            if _cTokens < 1 or _cTokens > 3:
                print("Número inválido. Debe ser entre 1 y 3.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        tokens = [input(f"Token {i + 1}: ") for i in range(_cTokens)]
        palabras = input("Ingrese una oración: ").split()

        print("\n----------------------------------------------")
        for palabra in palabras:
            print(f"{palabra} : palabra reservada" if palabra in tokens else palabra)

        if input("¿Otra oración? (s/n): ").strip().lower() != 's':
            break


if __name__ == "__main__":
    main()
