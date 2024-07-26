import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False}, {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo':True},
{'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('Finalizar o app')

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção Inválida')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    #Docstring
    '''
    Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Add um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    #Criar um dicionário com essas informações
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    
    #append é para colocar os dados na lista de restaurantes
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(18)} | {'Status'}')
#para cada restaurante na lista de restaurantes:
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo =  'Ativado' if restaurante ['ativo'] else 'Desativado'
# .ljust é para dar um determinado espacamento entre as palavras
        print(f'- {nome_restaurante.ljust(18)} | {categoria.ljust(18)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    #variavel que tem o valor de false ate que o restaurante escolhido pelo usuário seja encontrado
    restaurante_encontrado = False

    #Para cada restaurante em restaurantes, preciso fazer um loop para saber se eu tenho o restaurante q a pessoa digitou com aquele nome
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # o not na frente inverte o tipo de boleano da variavel, caso seja true, fica false e vice versa
            restaurante['ativo'] = not restaurante['ativo']
            # ESTRUTURA TERNÁRIO
            mensagem = f' O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f' O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
# o not foi colocado pq pra entrar nessa condição, precisa ser verdadeiro
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')      
    voltar_ao_menu_principal()

def escolher_opcao():
  #try p tentar fazer essa conversao do numero q o usuario colocar, caso ele nao consiga, usamos o except(caso o usuario digite uma letra por ex)  
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

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
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()