""" Questão 18, Nível 3: Um site exige que os usuários insiram nome de usuário e senha para se registrar. Escreva um programa para verificar a validade da senha digitada pelos usuários. A seguir estão os critérios para verificar a senha:

Pelo menos 1 letra entre [a-z] #
Pelo menos 1 número entre [0-9] #
Pelo menos 1 letra entre [A-Z] #
Pelo menos 1 caractere de [$#@] #
Comprimento mínimo da senha de transação: 6 #
Comprimento máximo da senha da transação: 12 Seu programa deverá aceitar uma sequência de senhas separadas por vírgulas e irá verificá-las de acordo com os critérios acima. As senhas que atendem aos critérios devem ser impressas, cada uma separada por vírgula. Exemplo Se as seguintes senhas forem fornecidas como entrada para o programa: ABd1234@1,aF1#,2w3E*,2We3345 Então, a saída do programa deverá ser: ABd1234@1
Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

senhas = input('Senhas: ').split(',')

senhas_validas = []

for senha in senhas:
    verificador = set()  # Criando um conjunto

    if 6 <= len((senha).strip()) <= 12:  # Verificar a quantidade de caracteres
        verificador.add('Tamanho')

        for caractere in senha:
            if caractere.isnumeric():  # Se houver um número
                verificador.add('Numero')

            elif caractere.isalpha():  # Se houver uma letra
                if caractere.isupper():  # Se a letra for maiúscula
                    verificador.add('maiúscula')

                else:  # Se a letra for minuscula
                    verificador.add('minúscula')

            else:  # Se houver caracter especial
                verificador.add('caracter')

        if len(verificador) == 5:  # Salvar senhas válidas em uma lista
            senhas_validas.append(senha)

# Mostrar senhas válidas:
print(', '.join(senhas_validas))
