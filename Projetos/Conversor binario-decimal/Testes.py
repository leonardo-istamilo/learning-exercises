def binario_para_decimal():
    """
    Função: Converte um número binário (até 8 bits) para decimal.
    """
    num_binario = input('Digite um número binário (até 8 bits): ')

    if not num_binario or not num_binario.isdigit() or any(digito not in {'0', '1'} for digito in num_binario):
        print('Erro: Por favor, digite um número binário válido.')
        return

    len_num_binario = len(num_binario)
    num_decimal = 0

    for i in range(len_num_binario):
        n = int(num_binario[i])
        num_decimal += n * 2 ** (len_num_binario - i - 1)

    print(f"Equivalente decimal: {num_decimal}")


binario_para_decimal()