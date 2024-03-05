import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},{
                 'nome': 'Pizza Suprema','categoria':'Italiana',
                 'ativo':True}]

def exibir__nome__do__programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir__opçoes():
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurante')
    print ('3. Alternar estado do Restaurante')
    print ('4. Sair\n')


#função
def finalizar_app():
   exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpar as opções
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_novo_restaurante():
    #Docstrings - ajuda a compreender o código no futuro
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    inputs:
    -Nome do restaurante 
    -Categoria

    Output:
    -Adiciona um novo restaurante na lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')    
    #para cada restaurante na lista restaurantes: 
        #nome 
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que seja alternar o estado: ')
    #criação de variavel para saber se foi encontrado ou não.
    restaurante_encontrado = False
    #Para cada restaurante em restaurante(lista)/ Se o nome digitado for igual ao restaurante na chave nome, o restaurante encontrado é encontrado (true)
    # O restaurante = not (inversão do valor que tem) então ele inverte o estado. verdadeiro em falso e falso em verdadeiro.
   
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

#Caso o restaurante não for encontrado:
    if not restaurante_encontrado:
      print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
     try:
        opcao_escolhida = int(input ('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
         opcao_invalida()
     except: 
        opcao_invalida()
def main():
    os.system('cls')
    exibir__nome__do__programa()
    exibir__opçoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
