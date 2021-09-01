from random import *

def legenda(habilitar):
    if habilitar==0:
        print('        Legenda \n'
              '       ╔═══╦═══╗\n'
              'Acerto ║███║░░░║ Erro\n'
              '       ╚═══╩═══╝\n')
    if habilitar==1:
        print('        Legenda \n'
              '       ╔═══╦═══╗\n'
              'Acerto ║NOM║░░░║ Erro\n'
              '       ╚═══╩═══╝\n')
def mesa_layout(mesa):
    print(f'  0   1   2   3   4   5   6   7   8   9\n'
          f'╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗\n'
          f'║{mesa[0][0][0]}│{mesa[0][1][0]}│{mesa[0][2][0]}│{mesa[0][3][0]}│{mesa[0][4][0]}│{mesa[0][5][0]}│{mesa[0][6][0]}│{mesa[0][7][0]}│{mesa[0][8][0]}│{mesa[0][9][0]}║ 0\n'
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[1][0][0]}│{mesa[1][1][0]}│{mesa[1][2][0]}│{mesa[1][3][0]}│{mesa[1][4][0]}│{mesa[1][5][0]}│{mesa[1][6][0]}│{mesa[1][7][0]}│{mesa[1][8][0]}│{mesa[1][9][0]}║ 1\n'
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[2][0][0]}│{mesa[2][1][0]}│{mesa[2][2][0]}│{mesa[2][3][0]}│{mesa[2][4][0]}│{mesa[2][5][0]}│{mesa[2][6][0]}│{mesa[2][7][0]}│{mesa[2][8][0]}│{mesa[2][9][0]}║ 2\n'
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[3][0][0]}│{mesa[3][1][0]}│{mesa[3][2][0]}│{mesa[3][3][0]}│{mesa[3][4][0]}│{mesa[3][5][0]}│{mesa[3][6][0]}│{mesa[3][7][0]}│{mesa[3][8][0]}│{mesa[3][9][0]}║ 3\n'
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[4][0][0]}│{mesa[4][1][0]}│{mesa[4][2][0]}│{mesa[4][3][0]}│{mesa[4][4][0]}│{mesa[4][5][0]}│{mesa[4][6][0]}│{mesa[4][7][0]}│{mesa[4][8][0]}│{mesa[4][9][0]}║ 4\n'    
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[5][0][0]}│{mesa[5][1][0]}│{mesa[5][2][0]}│{mesa[5][3][0]}│{mesa[5][4][0]}│{mesa[5][5][0]}│{mesa[5][6][0]}│{mesa[5][7][0]}│{mesa[5][8][0]}│{mesa[5][9][0]}║ 5\n'      
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[6][0][0]}│{mesa[6][1][0]}│{mesa[6][2][0]}│{mesa[6][3][0]}│{mesa[6][4][0]}│{mesa[6][5][0]}│{mesa[6][6][0]}│{mesa[6][7][0]}│{mesa[6][8][0]}│{mesa[6][9][0]}║ 6\n'      
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[7][0][0]}│{mesa[7][1][0]}│{mesa[7][2][0]}│{mesa[7][3][0]}│{mesa[7][4][0]}│{mesa[7][5][0]}│{mesa[7][6][0]}│{mesa[7][7][0]}│{mesa[7][8][0]}│{mesa[7][9][0]}║ 7\n'      
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[8][0][0]}│{mesa[8][1][0]}│{mesa[8][2][0]}│{mesa[8][3][0]}│{mesa[8][4][0]}│{mesa[8][5][0]}│{mesa[8][6][0]}│{mesa[8][7][0]}│{mesa[8][8][0]}│{mesa[8][9][0]}║ 8\n'      
          f'╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢\n'
          f'║{mesa[9][0][0]}│{mesa[9][1][0]}│{mesa[9][2][0]}│{mesa[9][3][0]}│{mesa[9][4][0]}│{mesa[9][5][0]}│{mesa[9][6][0]}│{mesa[9][7][0]}│{mesa[9][8][0]}│{mesa[9][9][0]}║ 9\n'      
          f'╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n')

def mesa_inicial(mesa):
    embarc=['PA1','NT1','NT2','CT1','CT2','CT3','SU1','SU2','SU3','SU4']
    taman=[5,4,4,3,3,3,2,2,2,2]
    for j in range(len(taman)):
        val=0
        while val==0:
            cont=0
            dir=randint(0,1)
            if dir==0:
                loc_col = randint(0, 4)
                loc_lin = randint(0, 9)
                for i in range(taman[j]):
                    if mesa[loc_lin][loc_col+i][0]!='   ':
                        cont=cont+1
                if cont==0:
                    for i in range(taman[j]):
                        mesa[loc_lin][loc_col+i][0] = f'{embarc[j]}'
                        val=1
            if dir==1:
                loc_col = randint(0, 9)
                loc_lin = randint(0, 4)
                for i in range(taman[j]):
                    if mesa[loc_lin+i][loc_col][0]!='   ':
                        cont=cont+1
                if cont==0:
                    for i in range(taman[j]):
                        mesa[loc_lin+i][loc_col][0] = f'{embarc[j]}'
                        val=1
    #mesa_layout(mesa)
    return mesa

def jogada(mesa_int,mesa_ext,tent,dificuldade,visor):
    embarc = ['PA1', 'NT1', 'NT2', 'CT1', 'CT2', 'CT3', 'SU1', 'SU2', 'SU3', 'SU4']
    valida=0
    while valida==0:
        jogadas_validas=['0','1','2','3','4','5','6','7','8','9']
        linha = input('Linha Desejada: ')
        coluna = input('Coluna Desejada: ')
        if coluna in jogadas_validas and linha in jogadas_validas:
            linha=int(linha)
            coluna=int(coluna)
            if mesa_int[linha][coluna][0] == 'JOG':
                print('Jogada Invalida!\nTente Novamente!')
            if mesa_int[linha][coluna][0] != 'JOG':
                valida=1
                if mesa_int[linha][coluna][0] == '   ':
                    if visor==1:
                        mesa_ext[linha][coluna][0]='░░░'
                    if visor==0:
                        mesa_ext[linha][coluna][0]='░░░'
                    mesa_int[linha][coluna][0]='JOG'
                if mesa_int[linha][coluna][0] in embarc:
                    jogadas.append(mesa_int[linha][coluna][0])
                    if visor==1:
                        mesa_ext[linha][coluna][0]=mesa_int[linha][coluna][0]
                    if visor==0:
                        mesa_ext[linha][coluna][0]='███'
                    if dificuldade==0 or dificuldade==1:
                        tent=tent-1
                    mesa_int[linha][coluna][0] = 'JOG'
        else:
            print('Jogada Invalida!\nTente Novamente!')
    return (mesa_int,mesa_ext,jogadas,tent)
def fim_de_jogo(jogadas):
    endgame = 0
    embarc = ['PA1', 'NT1', 'NT2', 'CT1', 'CT2', 'CT3', 'SU1', 'SU2', 'SU3', 'SU4']
    taman = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]
    for j in range(len(embarc)):
        if jogadas.count(embarc[j]) == taman[j]:
            endgame = 1
    return endgame

def escolher_dificuldade():
    valido=0
    while valido==0:
        print('Configurações: ')
        possiveis_dificuldades=['0','1','2']
        possiveis_mostrar=['0','1']
        dificuldade_escolhida=input('0 = Fácil (5 Tentativas, Acertar embarcações não gasta Tentativas.)\n'
                                        '1 = Médio (3 Tentativas, Acertar embarcações não gasta Tentativas.)\n'
                                        '2 = Dificil (5 Tentativas, Acertar embarcações GASTA Tentativas.)\n'
                                        'Digite o Codigo da Dificuldade Escolhida: ')
        print('')
        escolha_mostrar=input('0 = NÃO Mostrar o que está nos locais Atingidos\n'
                              '1 = Mostrar o que está nos locais Atingidos\n'
                              'Digite o Codigo Escolhido: ')
        print('')
        if dificuldade_escolhida in possiveis_dificuldades and escolha_mostrar in possiveis_mostrar:
            valido=1
            dificuldade_escolhida=int(dificuldade_escolhida)
            escolha_mostrar=int(escolha_mostrar)
            if dificuldade_escolhida==0:
                quantidades_tentativas_escolhida=5
            if dificuldade_escolhida==1:
                quantidades_tentativas_escolhida=3
            if dificuldade_escolhida==2:
                quantidades_tentativas_escolhida=5
        else:
            print('Escolha Invalida\n')
    return (dificuldade_escolhida,quantidades_tentativas_escolhida,escolha_mostrar)





mesa_externa=[      [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#1
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#2
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#3
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#4
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#5
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#6
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#7
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#8
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#9
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#10
              ]
mesa_interna=[      [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#1
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#2
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#3
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#4
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#5
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#6
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#7
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#8
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#9
                    [['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   '],['   ']],#10
              ]
jogadas=[]
dificuldade,tentativas_max,mostrar = escolher_dificuldade()
endgame=0
tentativas=0
mesa_interna=mesa_inicial(mesa_interna)
while endgame==0 and tentativas != tentativas_max:
    mesa_layout(mesa_externa)
    legenda(mostrar)
    print(f'Tentativas restantes: {tentativas_max-tentativas} ')
    mesa_interna,mesa_externa,jogadas,tentativas=jogada(mesa_interna,mesa_externa,tentativas,dificuldade,mostrar)
    endgame=fim_de_jogo(jogadas)
    tentativas+=1
if endgame==1:
    mesa_layout(mesa_externa)
    print('PARABÉNS! Você Ganhou!!')
if endgame==0:
    mesa_layout(mesa_externa)
    print('Infelizmente, Você Perdeu, Tente Novamente outra Vez.')