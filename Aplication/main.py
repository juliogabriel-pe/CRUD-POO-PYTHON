from menu import Menu
from functions import *
from conexaoMYSQL import *
import time

while True:

    flag = Menu()
    cursor = conexao.cursor()
    time.sleep(1)

    if flag == '1':

        try:
            comandoInsert = Cadastrar(cursor)
            cursor.execute(comandoInsert)
            conexao.commit()
            cursor.close()
            print('Adicionado Perfeitamente')
            time.sleep(1)
        except mysql.connector.errors.IntegrityError as e:
            print(
                f'Ocorreu um erro de integridade: {e}')
        time.sleep(1)

    elif flag == '2':

        ComandoListar = Listar(cursor)
        cursor.execute(ComandoListar)
        resultado = cursor.fetchall()
        print(resultado)
        cursor.close()
        time.sleep(1.5)

    elif flag == '3':

        ComandoAtualizar, ComandoInsert = Atualizar(cursor)
        cursor.execute(ComandoAtualizar)
        conexao.commit()
        cursor.execute(ComandoInsert)
        conexao.commit()
        cursor.close()
        print('Alteração concluida')
        time.sleep(1)

    elif flag == '4':

        ComandoDeletar = Deletar(cursor)
        cursor.execute(ComandoDeletar)
        conexao.commit()
        cursor.close()
        time.sleep(0.5)

    elif flag == '0':
        # tela de bye
        cursor.close()
        conexao.close()
        time.sleep(0.5)
        print("Conexão fechada com sucesso")
        break
