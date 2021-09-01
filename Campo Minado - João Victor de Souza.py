#João Victor de Souza
from random import *
def letreiro_iniciar():
    print('░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░  ███╗░░░███╗██╗███╗░░██╗░█████╗░██████╗░░█████╗░\n'
          '██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗  ████╗░████║██║████╗░██║██╔══██╗██╔══██╗██╔══██╗\n'
          '██║░░╚═╝███████║██╔████╔██║██████╔╝██║░░██║  ██╔████╔██║██║██╔██╗██║███████║██║░░██║██║░░██║\n'
          '██║░░██╗██╔══██║██║╚██╔╝██║██╔═══╝░██║░░██║  ██║╚██╔╝██║██║██║╚████║██╔══██║██║░░██║██║░░██║\n'
          '╚█████╔╝██║░░██║██║░╚═╝░██║██║░░░░░╚█████╔╝  ██║░╚═╝░██║██║██║░╚███║██║░░██║██████╔╝╚█████╔╝\n'
          '░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░\n')

def letreiro_venceu():
    print('██╗░░░██╗░█████╗░░█████╗░███████╗  ██╗░░░██╗███████╗███╗░░██╗░█████╗░███████╗██╗░░░██╗\n'
          '██║░░░██║██╔══██╗██╔══██╗██╔════╝  ██║░░░██║██╔════╝████╗░██║██╔══██╗██╔════╝██║░░░██║\n'
          '╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░  ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░╚═╝█████╗░░██║░░░██║\n'
          '░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░  ░╚████╔╝░██╔══╝░░██║╚████║██║░░██╗██╔══╝░░██║░░░██║\n'
          '░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗  ░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝███████╗╚██████╔╝\n'
          '░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚══════╝░╚═════╝░\n')

def letreiro_perdeu():
    print('██╗░░░██╗░█████╗░░█████╗░███████╗  ██████╗░███████╗██████╗░██████╗░███████╗██╗░░░██╗\n'
          '██║░░░██║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║░░░██║\n'
          '╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░  ██████╔╝█████╗░░██████╔╝██║░░██║█████╗░░██║░░░██║\n'
          '░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░  ██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██╔══╝░░██║░░░██║\n'
          '░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗  ██║░░░░░███████╗██║░░██║██████╔╝███████╗╚██████╔╝\n'
          '░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝░╚═════╝░\n')

def mostrar_mesa(mesa):
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

def abrir_vazios(matriz,matriz_ext, i, j):
    jog_valid = (' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ')
    dimensao = len(matriz)
    game_over=0
    if matriz[i][j][0] == "░░░":
        matriz[i][j][0] = "   "
        matriz_ext[i][j][0] = "   "
        linha_inicial = i - 1
        if linha_inicial < 0:
            linha_inicial = 0
        linha_final = i + 1
        if linha_final > dimensao - 1:
            linha_final = dimensao - 1
        coluna_inicial = j - 1
        if coluna_inicial < 0:
            coluna_inicial = 0
        coluna_final = j + 1
        if coluna_final > dimensao - 1:
            coluna_final = dimensao - 1

        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                abrir_vazios(matriz,matriz_ext, l, c)
    if matriz[i][j][0] in jog_valid:
        matriz_ext[i][j][0] = matriz[i][j][0]
    if matriz[i][j][0] == ' M ':
        matriz_ext[i][j][0] = matriz[i][j][0]
        game_over=1
    return (matriz,matriz_ext,game_over)

def calcular_vizinhanca(matriz):
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(dimensao):

            if matriz[i][j][0] != " M ":

                linha_inicial = i - 1
                if linha_inicial < 0:
                    linha_inicial = 0
                linha_final = i + 1
                if linha_final > dimensao - 1:
                    linha_final = dimensao - 1
                coluna_inicial = j - 1
                if coluna_inicial < 0:
                    coluna_inicial = 0
                coluna_final = j + 1
                if coluna_final > dimensao - 1:
                    coluna_final = dimensao - 1

                valor = 0
                for l in range(linha_inicial, linha_final + 1):
                    for c in range(coluna_inicial, coluna_final + 1):
                        if matriz[l][c][0] == " M ":
                            valor = valor + 1
                if valor != 0:
                    matriz[i][j][0] = f' {valor} '
    return matriz

def abrir_numeros(matriz,matriz_ext):
    invalidos=(' M ','   ')
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(dimensao):

            if matriz[i][j][0] == "   ":

                linha_inicial = i - 1
                if linha_inicial < 0:
                    linha_inicial = 0
                linha_final = i + 1
                if linha_final > dimensao - 1:
                    linha_final = dimensao - 1
                coluna_inicial = j - 1
                if coluna_inicial < 0:
                    coluna_inicial = 0
                coluna_final = j + 1
                if coluna_final > dimensao - 1:
                    coluna_final = dimensao - 1

                for l in range(linha_inicial, linha_final + 1):
                    for c in range(coluna_inicial, coluna_final + 1):
                        if not matriz[l][c][0] in invalidos:
                            matriz_ext[l][c][0] = matriz[l][c][0]
    return (matriz,matriz_ext)

def sortear_minas(matriz):
    dimensao = len(matriz)
    cont_minas = 0
    while cont_minas < dimensao:
        linha = randint(0, dimensao - 1)
        coluna = randint(0, dimensao - 1)
        if matriz[linha][coluna][0] != " M ":
            matriz[linha][coluna][0] = " M "
            cont_minas = cont_minas + 1
    return matriz

def validar_jogada(usadas):
    valid=0
    while valid==0:
        jog_valid=('0','1','2','3','4','5','6','7','8','9')
        print('Após a Escolha de Linha e Coluna você poderá escolher entre Marcar/Desmarcar bomba ou fazer Sua Jogada!')
        linha = input("Digite a Linha: ")
        coluna = input("Digite a Coluna: ")
        if linha in jog_valid and coluna in jog_valid:
            if not f'{linha}{coluna}' in usadas:
                linha = int(linha)
                coluna = int(coluna)
                valid=1
            else:
                print('Jogada já feita!\n')
        else:
            print('Jogada Invalida!\n')
    return (linha, coluna, valid)

def contar_restantes(matriz_ext):
    quant=0
    for i in range(10):
        for j in range(10):
            if matriz_ext[i][j][0]=='░░░' or matriz_ext[i][j][0]=='███':
                quant+=1
    return quant

def contar_usadas(matriz_ext,usadas):
    for i in range(10):
        for j in range(10):
            if matriz_ext[i][j][0]!='░░░':
                if matriz_ext[i][j][0]!='███':
                    if not f'{i}{j}' in usadas:
                        usadas.append(f'{i}{j}')
    return usadas
9
def escolher_jogada():
    interruptor2=0
    while interruptor2==0:
        valid=['0','1','2']
        jogada=input('\nVocê deseja Marcar/Desmarcar uma Bomba (0)\n'
                     'Fazer sua jogada (1)\n'
                     'Cancelar sua Escolha de Linha e Coluna (2) \n'
                     'Digite o Codigo escolhido: ')
        if jogada in valid:
            jogada=int(jogada)
            interruptor2=1
    return jogada

def marcar_bomba(matriz_ext,l,c):
    if matriz_ext[l][c][0] == '███':
        matriz_ext[l][c][0] = '░░░'
    else:
        matriz_ext[l][c][0] = '███'
    return matriz_ext

mesa_interna=[      [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#1
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#2
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#3
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#4
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#5
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#6
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#7
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#8
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#9
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#10
              ]
mesa_externa=[      [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#1
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#2
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#3
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#4
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#5
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#6
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#7
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#8
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#9
                    [['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░'],['░░░']],#10
              ]

mesa_interna = sortear_minas(mesa_interna)
mesa_interna=calcular_vizinhanca(mesa_interna)
jog_usadas=[]
quantidade_restantes=90
gameover=0
letreiro_iniciar()
while quantidade_restantes>10 and gameover==0:
    #mostrar_mesa(mesa_interna)
    mostrar_mesa(mesa_externa)
    linha,coluna,interruptor=validar_jogada(jog_usadas)
    liberar_jogada=escolher_jogada()
    if interruptor==1 and liberar_jogada==1:
        mesa_interna,mesa_externa,gameover=abrir_vazios(mesa_interna,mesa_externa,linha,coluna)
        mesa_interna,mesa_externa=abrir_numeros(mesa_interna,mesa_externa,)
        interruptor=0
    if liberar_jogada==0:
        mesa_externa=marcar_bomba(mesa_externa,linha,coluna)
    jog_usadas=contar_usadas(mesa_externa,jog_usadas)
    quantidade_restantes = contar_restantes(mesa_externa)
mostrar_mesa(mesa_interna)
mostrar_mesa(mesa_externa)
if gameover==1:
    letreiro_perdeu()
if gameover==0:
    letreiro_venceu()