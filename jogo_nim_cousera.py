'''funçao computador_escolhe_jogada recebe N e M e retorna um int correspondente
   a proxima jogada do computador, ou seja, qts peças o computador deve retirar do tabuleiro '''
def computador_escolhe_jogada(n,m):
    
    if n%(m+1)!=0:
        
        return n%(m+1)
        
    else:
        
        return m
        
'''funçao usuario_escolhe_jogada que recebe N e M, solicita que o jogador informe
    a jogada e verifica se o valor informado é valido. Se valido a funçao retorna
    os valores caso contrario pede novos valores de N e M'''
def usuario_escolhe_jogada(n,m):

    valido=int(input("Quantas peças serao retiradas? "))

    #verificar se VALOR é valido
    while valido > m or valido > n or valido <1:
        print(" Oops! Jogada inválida! Tente de novo.")
        valido=int(input("Quantas peças serao retiradas? "))
    else:
        
        return valido

'''funçao partida nao recebe nenhum parametro, solicita os valores de N e M ao usuario
   e inicia o jogo alternando as jogadas entre o usuario e computador. A jogada inicial
   deve ser feita de acordo com a estrategia vencedora, a cada jogada é impresso na tela
   o estado do jogo, qtd de peças removidas na jogada e qtd restante de peças, quando a ultima
   peça é retirada a funçao imprime quem ganhou na tela.
   "O computador ganhou!" ou "Você ganhou!" '''

def partida():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças retiradas por jogada?"))
   
    turno = True    #controle de quem é a vez de jogar
   
    #Verificar se N é multiplo de M+1
    if n%(m+1)== 0 :
          
        print("\nVocê começa!")
        
    else:
        print("\nComputador começa!")
        turno = False
        
    while n>0:
            if turno:
                
                retirada=usuario_escolhe_jogada(n,m)
                n=n-retirada
                print("Você tirou",retirada,"peça(s).\n")
                print("Agora restam ",n, " peças no tabuleiro.\n")
                turno = False
            else:
                
                retirada=computador_escolhe_jogada(n,m)
                n-=retirada
                print("O computador tirou",retirada,"peça(s).\n")
                print("Agora restam ",n, " peças no tabuleiro.\n")
                turno = True

    if turno:
            print ("Fim do jogo! O computador ganhou!\n\n")
            return 0
    else:
            print ("Fim do jogo!Voce ganhou!\n\n")
            return 1

''' funçao campeonato realiza tres partidas seguidas do jogo e no final mostra o placar
    e indica o vencedor do campeonato.
    Placar: Você X  Computador '''

def campeonato():
    print("\nVocê escolheu um campeonato\n")
    n_partida = 1 #contador de partidas jogadas
    computador = usuario = 0    #contador de vitorias

    while n_partida < 4:
        print("### Rodada", n_partida,"###\n")
        resultado = partida()
        n_partida+=1
        if resultado == 0:
            computador += 1
        else:
            usuario += 1

    print(" ### Final do campeonato! ###")    
    print("Placar: Voce ",usuario,"X",computador,"Computador\n\n")

''' N= numero de peças inicial e M numero maximo de peças que pode ser retirada em uma jogada
    ESTRATEGIA VENCEDORA:
    - Se N é multiplo de (m+1) o usuario começa caso contrario, o computador começa'''

def main():
    print ("Bem vindo ao jogo do NIM \n")
    print ("1- para jogar uma partida isolada")
    print ("2- para jogar um campeonato")
    escolha = int(input("Escolha: "))

    while escolha != 1 and escolha !=2:
        print ("Opção inválida!\n")
        print ("1- para jogar uma partida isolada")
        print ("2- para jogar um campeonato")
        escolha = int(input("Escolha: "))

    if escolha == 1:
         
         partida()
    else:
         campeonato()
    
#=============================================#

main()            
    
