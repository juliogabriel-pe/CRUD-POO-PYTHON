def Menu():

    print('\nBem Vindo ao CRUD')
    print('1 - Cadastro de Usuario')
    print('2 - Listar Usuario')
    print('3 - Atualizar Usuario')
    print('4 - Deletar Usuario')
    print('0 - Sair do Programa\n')

    resposta = input('Digite um valor: ')

    if resposta.isnumeric() == True:
        print('Resposta armazenada... Executando!\n')
    else:
        print('Erro! Você digitou algo diferente de numero\n')

    return resposta
