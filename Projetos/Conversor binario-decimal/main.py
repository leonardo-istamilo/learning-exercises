
def Binary_To_Decimal():
    """
    Função: Recebe um número em binario (até 8 bits) e converte para decimal.
    """
    print('-'*40)
    print('CONVERSOR BINÁRIO -> DECIMAL'.center(40))
    print('-'*40)

    num_binario = input('Número em binario (até 8 bits): ')
    len_num_binario = len(num_binario) #Guardando o comprimento da string para usos futuros

    if len_num_binario <= 8: #Verifica se o número digitado tem até 8 bits.

        cont = num_decimal = 0

        for i in range(-1, (-1 * (len_num_binario + 1)), -1): 

            if (num_binario[i] == '0') or (num_binario[i] == '1'):
                n = int(num_binario[i])
                num_decimal += n * 2 ** cont
                cont += 1
            else:
                print('Erro: Valor diferente de 0 e 1 inserido.')
                return              

        print(f"Valor em decimal: {num_decimal}")

    else:
        print('ERRO: Número digitado possui mais de 8 bits.')

Binary_To_Decimal()