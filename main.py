def int_to_binary(number):
    """
    Converte um número inteiro para sua representação binária.

    Args:
        number (int): Número inteiro a ser convertido.

    Returns:
        str: Representação binária do número.
    """
    if not isinstance(number, int):
        raise ValueError("O valor fornecido deve ser um número inteiro.")
    return bin(number)[2:]

# Exemplo de uso
if __name__ == "__main__":
    num = int(input("Digite um número inteiro: "))
    print(f"Representação binária: {int_to_binary(num)}")