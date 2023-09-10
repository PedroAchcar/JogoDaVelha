from random import randint


POSICOES = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}


def menu():
    print('Bem vindo ao Jogo da Velha!')
    print('Quer jogar com dois jogadores ou contra o computador?')
    print('1 - Dois jogadores')
    print('2 - Contra o computador facil')
    print('3 - Contra o computador impossivel')

    try:
        op = int(input("Escolha uma opcao:\n> "))

        if op == 1 or op == 2 or op == 3:
            return op

        else:
            print("Opcao inexistente")
            return menu()

    except ValueError:
        print("Nao eh um numero valido")
        return menu()


def mostra_tabuleiro(tabuleiro: list[list[str]]):
    '''Mostra na tela o tabuleiro atual'''
    for linha in tabuleiro:
        print(' | '.join(linha))


def verifica_vitoria(tabuleiro: list[list[str]], atual: str):
    '''Verifica se o jogador atual venceu a partida'''
    # Verifica linhas
    for i in range(3):
        linha = tabuleiro[i]
        if linha.count(atual) == 3:
            return True

    # Verifica colunas
    for i in range(3):
        coluna = [tabuleiro[j][i] for j in range(3)]
        if coluna.count(atual) == 3:
            return True

    # Verifica diagonais
    diagonal = [tabuleiro[i][i] for i in range(3)]
    diagonal_sec = [tabuleiro[i][2-i] for i in range(3)]
    if diagonal.count(atual) == 3 or diagonal_sec.count(atual) == 3:
        return True

    return False


def verifica_empate(tabuleiro: list[list[str]]):
    '''Verifica se aconteceu um empate'''
    for linha in tabuleiro:
        if '-' in linha:
            return False

    return True


def jogada(tabuleiro: list[list[str]], atual: str):
    '''Faz a jogada desejada usando o parametro "atual" para saber de quem eh a vez'''
    print(f'Vez do jogador {atual}')

    try:
        pos = int(input("Escolha uma posicao disponível\n> "))

        if 1 <= pos <= 9:
            linha, coluna = POSICOES[pos]

            if tabuleiro[linha][coluna] == '-':
                tabuleiro[linha][coluna] = atual
                return tabuleiro

            else:
                print("Posicao ocupada")
                return jogada(tabuleiro, atual)

        else:
            print("Posicao fora do intervalo")
            return jogada(tabuleiro, atual)

    except ValueError:
        print("Nao eh um numero valido")
        return jogada(tabuleiro, atual)


def jogada_comp_facil(tabuleiro: list[list[str]], atual: str):
    '''Faz a jogada do computador nivel facil'''

    linha, coluna = randint(0, 2), randint(0, 2)

    if tabuleiro[linha][coluna] == '-':
        tabuleiro[linha][coluna] = atual
        return tabuleiro

    else:
        return jogada_comp_facil(tabuleiro, atual)


def jogador_contra_jogador(tabuleiro: list[list[str]], atual: str):
    '''Jogo entre dois jogadores'''
    mostra_tabuleiro(tabuleiro)

    while True:
        tabuleiro = jogada(tabuleiro, atual)
        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, atual):
            print('Jogo finalizado!')
            print(f'O jogador {atual} venceu a partida!')
            break

        if verifica_empate(tabuleiro):
            print('Jogo finalizado!')
            print('Deu velha!')
            break

        atual = 'O' if atual == 'X' else 'X'


def jogador_contra_computador_facil(tabuleiro: list[list[str]], atual: str):
    '''Jogo entre um jogador e o nivel facil do computador'''
    mostra_tabuleiro(tabuleiro)

    while True:
        tabuleiro = jogada(tabuleiro, 'X')
        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, atual):
            print('Jogo finalizado!')
            print(f'O jogador {atual} venceu a partida!')
            break

        if verifica_empate(tabuleiro):
            print('Jogo finalizado!')
            print('Deu velha!')
            break

        print(f'Vez do computador')
        tabuleiro = jogada_comp_facil(tabuleiro, 'O')
        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, 'O'):
            print('Jogo finalizado!')
            print(f'O computador nivel facil venceu a partida!')
            break

        if verifica_empate(tabuleiro):
            print('Jogo finalizado!')
            print('Deu velha!')
            break

        # atual = 'O' if atual == 'X' else 'X'


def main():
    '''Funcao principal do programa, controla a chamada de outras funcoes'''
    atual = 'X'
    tabuleiro = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]

    op = menu()

    match op:
        case 1:
            jogador_contra_jogador(tabuleiro, atual)

        case 2:
            jogador_contra_computador_facil(tabuleiro, atual)


if __name__ == '__main__':
    main()
