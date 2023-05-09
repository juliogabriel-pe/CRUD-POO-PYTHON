def Cadastrar(cursor):

    cursor
    nome = input('Digite seu Nome: ')
    nome = nome.upper()
    sobrenome = input('Digite seu Sobrenome: ')
    sobrenome = sobrenome.upper()
    email = input('Digite seu Email: ')
    email = email.upper()
    senha = input('Digite sua senha: ')
    senha = senha.upper()

    comandoInsert = f'INSERT INTO usuario (nome,sobrenome,senha,email) VALUES ("{nome}","{sobrenome}","{senha}","{email}")'

    return comandoInsert


def Listar(cursor):

    cursor
    ComandoListar = f'SELECT * FROM usuario'
    if not ComandoListar:
        ComandoListar = print('Vazio! Usuarios nao cadastrados!')

    return ComandoListar


def Atualizar(cursor):

    cursor
    ContaAtualizar = input('Digite o email da conta para atualizar: ')
    ComandoAtualizar = f'DELETE FROM usuario WHERE email = "{ContaAtualizar}"'

    nome = input('Digite seu Nome: ')
    nome = nome.upper()
    sobrenome = input('Digite seu Sobrenome: ')
    sobrenome = sobrenome.upper()
    email = input('Digite seu Email: ')
    email = email.upper()
    senha = input('Digite sua senha: ')
    senha = senha.upper()

    ComandoInsert = f'INSERT INTO usuario (nome,sobrenome,senha,email) VALUES ("{nome}","{sobrenome}","{senha}","{email}")'

    return ComandoAtualizar, ComandoInsert


def Deletar(cursor):

    cursor
    ContaDeletar = input('Digite o email da conta para deletar: ')
    ComandoDeletar = f'DELETE FROM usuario WHERE email = "{ContaDeletar}"'
    print('Conta deletada com sucesso')

    return ComandoDeletar
