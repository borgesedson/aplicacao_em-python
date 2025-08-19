import sys

import os
restaurantes = [
    {'nome': 'YVá', 'Categoria': 'Italiana', 'ativo': True},
    {'nome':'Pizza Suprema', 'Categoria': 'Moçambicana', 'ativo': False},
    {'nome': 'Sushi', 'Categoria': 'Japonesa', 'ativo': False}
]


def exibir_nome_do_programa() :
 
    
    print("""
    
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████───██████████████─████████████████──────────────────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────────────────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────────────────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────────────────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██───██████████████─██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████───██████████████─██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────────────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────────────────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────────────────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─████████████████─██████████████─██████──██████████────────────────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────  \n """)

restaurantes = [
    {'nome': 'YVá', 'Categoria': 'Italiana', 'ativo': True},
    {'nome': 'Pizza Suprema', 'Categoria': 'Moçambicana', 'ativo': False},
    {'nome': 'Sushi', 'Categoria': 'Japonesa', 'ativo': False}
]

# Funções de exibição
def exibir_nome_do_programa():
    print("=== Sistema de Restaurantes ===\n")

def exibir_opcao():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar estado de restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system('cls') 
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()



def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu...")
    os.system('cls')

# Funções principais
def finalizar_app():
    exibir_subtitulo("Finalizando o app...")
    voltar_ao_menu_principal ()

def opcao_invalida():
    print("Opção inválida.")
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    ''' Esta função é responsável por cadastrar novos restaurantes 
    '''
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante= input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante '{nome}': ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'Categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"✅ Restaurante '{nome_do_restaurante}' cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes")
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(22)} | Status')

    for restaurante in restaurantes:
        nome_restaurante= restaurante['nome']
        categoria = restaurante['Categoria']
        ativo = "Ativo" if restaurante['ativo'] else "Inativo"
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(22)} | {ativo} ')

    voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    exibir_subtitulo("Alterar estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar: ")
    restaurante_encontrado = False # false porque ainda não encontrou

    for restaurante in restaurantes:
       if nome_restaurante ==restaurante['nome'] :
        restaurante_encontrado = True
        restaurante['ativo'] = not restaurante['ativo']
        mensagem = f'O restaurante {nome_restaurante.ljust}| foi ativado com sucesso' if restaurante['ativo'] else f' O restaurante foi desativado com sucesso'
        print(mensagem)
        
        # ativo ='ativado' if restaurante['ativo'] else 'desativado
        # print(f'-{nome_restaurante.ljust(20)}| {categoria.ljust(20)} | {'ativo'}')
            
    if not restaurante_encontrado :
       print('O restaurante não encontrado.')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alterar_estado_do_restaurante()
        elif opcao == 4:
            finalizar_app()
    except:
        opcao_invalida()

def main():
    while True:
        exibir_nome_do_programa()
        exibir_opcao()
        escolher_opcao()

if __name__ == '__main__':
    main()
