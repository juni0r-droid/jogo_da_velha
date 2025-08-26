jogar_novamente = True # jogar de novo

while jogar_novamente:
    j1 = ''
    j2 = ''
    print('Escolha sua jogada, jogador 1:')
    print('X')
    print('O')

    while j1 == '' or j2 == '':
        escolha = input('Digite a sua escolha (X ou O): ')

        if escolha == 'X' or escolha == 'x':
            print('Jogador 1 escolheu X')
            print('Jogador 2 será O')
            j1 = 'X'
            j2 = 'O'

        elif escolha == 'O' or escolha == 'o':
            print('Jogador 1 escolheu O')
            print('Jogador 2 será X')
            j1 = 'O'
            j2 = 'X'

        else:
            print('Símbolo inválido. Escolha apenas X ou O :)')

    tabuleiro = [[' ', ' ', ' '], #matriz tabuleiro
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

    print('\nINSTRUÇÕES:')
    print('Use números de 0 a 2 para linha e coluna, como no xadrez!\n')

    jogador_atual = j1
    rodadas = 0
    vencedor = 'ninguem'
    fim_jogo = True

    while fim_jogo: # laço para o jogo continuar
        print('\nTabuleiro:')
        
        print('    0    1    2')
        print('0', tabuleiro[0])
        print('1', tabuleiro[1])
        print('2', tabuleiro[2])

        print('\nVez do jogador', jogador_atual)

        jogada_valida = True
        while jogada_valida:
            linha = int(input('Escolha a linha (0 a 2): '))
            coluna = int(input('Escolha a coluna (0 a 2): '))
            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
                if tabuleiro[linha][coluna] == ' ':
                    tabuleiro[linha][coluna] = jogador_atual
                    jogada_valida = False
                else:
                    print('Posição ocupada')
            else:
                print('Coordenada inválida')

        rodadas = rodadas + 1
        #verificação de vitória:
        #linhas e colunas
        for posição in range(3):
            if tabuleiro[posição][0] == tabuleiro[posição][1] == tabuleiro[posição][2] != ' ':
                vencedor = jogador_atual
            if tabuleiro[0][posição] == tabuleiro[1][posição] == tabuleiro[2][posição] != ' ':
                vencedor = jogador_atual

        #diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
            vencedor = jogador_atual
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
            vencedor = jogador_atual

        #término e troca de jogadores:
        if vencedor != 'ninguem' or rodadas == 9:
            fim_jogo = False
        else:
            if jogador_atual == j1: #se o jogador atual foi o j1, logo após a jogada dele será o j2:
                jogador_atual = j2
            else:
                jogador_atual = j1
    #resultado final
    print('\nTabuleiro final:')
    
    print('    0    1    2')
    print('0', tabuleiro[0])
    print('1', tabuleiro[1])
    print('2', tabuleiro[2])

    if vencedor != 'ninguem':
        print('\nParabéns! O jogador', vencedor, 'venceu!')
    else:
        print('\nDeu empate!')

    #jogar novamente
    resposta = input('\nDeseja jogar novamente? (s para sim): ')
    if resposta == 's' or resposta == 'S':
         jogar_novamente = True
    else:
        jogar_novamente = False
print('\nObrigado por jogar :D')

       