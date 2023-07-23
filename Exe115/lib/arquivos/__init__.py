dados = {}  # Variável global para armazenar os dados dos cadastrados

def escrevedormenu(txt='Teste', tam=0):
    print('=' * tam)
    print(txt.center(tam))
    print('=' * tam)


def leiaintmenu(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número válido\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[33mO usuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return n


def menu():
    escrevedormenu('MENU PRINCIPAL', 40)
    print("""\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m\n\033[33m2\033[m - \033[34mCadastrar novas Pessoa\033[m
\033[33m3\033[m - \033[34mSair do Sistema\033[m""")
    opcao = leiaintmenu("\033[32mSua opção:\033[m ")
    if opcao == 1:
        return vercadastrados()
    elif opcao == 2:
        return cadastrarnovo()
    elif opcao == 3:
        escrevedormenu('Saindo do sistema... Até logo', 50)


def vercadastrados():
    escrevedormenu('PESSOAS CADASTRADAS', 40)
    for pessoa in dados.values():
        nome = pessoa["nome"]
        idade = pessoa["idade"]
        print(f'Nome: {nome}, Idade: {idade}')
    return menu()


def cadastrarnovo():
    escrevedormenu('NOVO CADASTRO', 40)
    nome = str(input('Nome: '))
    idade = leiaintmenu('Idade: ')
    dados[len(dados) + 1] = {"nome": nome, "idade": idade}
    print(f'Novo registro de {nome} adicionado.')
    return menu()