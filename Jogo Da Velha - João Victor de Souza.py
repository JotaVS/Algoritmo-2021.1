def mesa_layout(mesa):
    print(
        f'  0   1   2 \n'
        f'╔═══╦═══╦═══╗\n'
        f'║ {mesa[0][0][0]} ║ {mesa[0][1][0]} ║ {mesa[0][2][0]} ║ 0\n'
        f'╠═══╬═══╬═══╣\n'
        f'║ {mesa[1][0][0]} ║ {mesa[1][1][0]} ║ {mesa[1][2][0]} ║ 1\n'
        f'╠═══╬═══╬═══╣\n'
        f'║ {mesa[2][0][0]} ║ {mesa[2][1][0]} ║ {mesa[2][2][0]} ║ 2\n'
        f'╚═══╩═══╩═══╝\n')

def jogo_da_velha():
    print('░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ██╗░░░██╗███████╗██╗░░░░░██╗░░██╗░█████╗░\n'
          '░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ██║░░░██║██╔════╝██║░░░░░██║░░██║██╔══██╗\n'
          '░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║███████║  ╚██╗░██╔╝█████╗░░██║░░░░░███████║███████║\n'
          '██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══██║  ░╚████╔╝░██╔══╝░░██║░░░░░██╔══██║██╔══██║\n'
          '╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░██║  ░░╚██╔╝░░███████╗███████╗██║░░██║██║░░██║\n'
          '░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝\n')
def jogadorx():
    print('░░░▒█ █▀▀█ █▀▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▀▄▒▄▀ \n'
          '░▄░▒█ █░░█ █░▀█ █▄▄█ █░░█ █░░█ █▄▄▀ 　 ░▒█░░ \n'
          '▒█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▄▀▒▀▄ \n')
def jogadoro():
    print('░░░▒█ █▀▀█ █▀▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀█ \n'
          '░▄░▒█ █░░█ █░▀█ █▄▄█ █░░█ █░░█ █▄▄▀ 　 ▒█░░▒█ \n'
          '▒█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄█\n')
def ganhou():
    print('▒█▀▀█ █▀▀█ █▀▀▄ █░░█ █▀▀█ █░░█ \n'
          '▒█░▄▄ █▄▄█ █░░█ █▀▀█ █░░█ █░░█ \n'
          '▒█▄▄█ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ░▀▀▀ \n')
def empate():
    print('▒█░▒█ █▀▀█ █░░█ ▀█░█▀ █▀▀ 　 █░░█ █▀▄▀█ 　 █▀▀ █▀▄▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ \n'
          '▒█▀▀█ █░░█ █░░█ ░█▄█░ █▀▀ 　 █░░█ █░▀░█ 　 █▀▀ █░▀░█ █░░█ █▄▄█ ░░█░░ █▀▀ \n'
          '▒█░▒█ ▀▀▀▀ ░▀▀▀ ░░▀░░ ▀▀▀ 　 ░▀▀▀ ▀░░░▀ 　 ▀▀▀ ▀░░░▀ █▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀\n')
def jogada(mesa, jogador,mesa_pontos):
    jogada_valida = 0
    while jogada_valida == 0:
        if jogador == 'X':
            jogadorx()
        if jogador == 'O':
            jogadoro()
        mesa_layout(mesa)
        linha = input("Linha: ")
        coluna = input("Coluna: ")
        print(' ')
        if linha == '0' or linha == '1' or linha == '2':
            if coluna == '0' or coluna == '1' or coluna == '2':
                linha=int(linha)
                coluna=int(coluna)
                if mesa[linha][coluna] == 'X' or mesa[linha][coluna] == 'O':
                    print('Jogada Invalida, Tente Novamente!\n')
                if mesa[linha][coluna] == [' ']:
                    if jogador == 'X':
                        mesa[linha][coluna] = ('X')
                        mesa_pontos[linha][coluna] = 1
                    if jogador == 'O':
                        mesa[linha][coluna] = ('O')
                        mesa_pontos[linha][coluna] = 2
                    jogada_valida = 1
            else:
                print('Jogada Invalida, Tente Novamente!\n')
        else:
            print('Jogada Invalida, Tente Novamente!\n')
    return (mesa,mesa_pontos)

def teste_fim_de_jogo(mesa_pontos):
    linha0=0
    linha1=0
    linha2=0
    for i in range(3):
        for j in range(3):
            if i==0:
                linha0=linha0+mesa_pontos[i][j]
            if i==1:
                linha1=linha1+mesa_pontos[i][j]
            if i==2:
                linha2=linha2+mesa_pontos[i][j]
    coluna0=0
    coluna1=0
    coluna2=0
    for i in range(3):
        for j in range(3):
            if i==0:
                coluna0=coluna0+mesa_pontos[j][i]
            if i==1:
                coluna1=coluna1+mesa_pontos[j][i]
            if i==2:
                coluna2=coluna2+mesa_pontos[j][i]
    diagonal_primaria=mesa_pontos[0][0]+mesa_pontos[1][1]+mesa_pontos[2][2]
    diagonal_secundaria=mesa_pontos[0][2]+mesa_pontos[1][1]+mesa_pontos[2][0]
    if linha0==3 or linha1==3 or linha2==3 or coluna0==3 or coluna1==3 or coluna2==3 or diagonal_primaria==3 or diagonal_secundaria==3:
        vencedor='X'
        fim_de_jogo=1
        return (vencedor,fim_de_jogo)
    if linha0==6 or linha1==6 or linha2==6 or coluna0==6 or coluna1==6 or coluna2==6 or diagonal_primaria==6 or diagonal_secundaria==6:
        vencedor='O'
        fim_de_jogo=1
        return (vencedor,fim_de_jogo)
    else:
        vencedor=''
        fim_de_jogo=0
        return (vencedor,fim_de_jogo)

mesa = [[[' '], [' '], [' ']],
        [[' '], [' '], [' ']],
        [[' '], [' '], [' ']]]
mesa_pontos =   [[10, 10, 10],
                [10, 10, 10],
                [10, 10, 10]]
fim_de_jogo = 0
jogadas=0
jogo_da_velha()
vencedor=''
while fim_de_jogo==0 and jogadas!=9:
    if fim_de_jogo==0 and jogadas!=9:
        jogador='X'
        mesa,mesa_pontos=jogada(mesa,jogador,mesa_pontos)
        vencedor,fim_de_jogo=teste_fim_de_jogo(mesa_pontos)
        jogadas+=1
    if fim_de_jogo==0 and jogadas!=9:
        jogador='O'
        mesa,mesa_pontos=jogada(mesa,jogador,mesa_pontos)
        vencedor,fim_de_jogo=teste_fim_de_jogo(mesa_pontos)
        jogadas+=1
if vencedor=='X':
    jogadorx()
    ganhou()
    mesa_layout(mesa)
if vencedor == 'O':
    jogadoro()
    ganhou()
    mesa_layout(mesa)
if vencedor!='X' and vencedor!='O':
    empate()
    mesa_layout(mesa)
