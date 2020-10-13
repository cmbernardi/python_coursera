def computador_escolhe_jogada(n, m):
	if m >= n:
		return n
	else:
		restantes = n % (m + 1)
		if restantes > 0:
			return restantes
		else:
			return m	


def usuario_escolhe_jogada(n, m):
	jogada = int(input("\nQuantas peças você vai tirar? "))
	while jogada > m or jogada > n or jogada < 1:
		print("\nOops! Jogada inválida! Tente de novo.\n")
		jogada = int(input("Quantas peças você vai tirar? ")) 
	return jogada	 	

	
def partida():

			#definir jogo
	n = int(input("Quantas peças? "))
	while n < 1:
		n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while m < 1 and m >= n:
		m = int(input("Limite de peças por jogada? "))
			
			#definir quem começa 
	comp_start = True	
	if n % (m + 1) == 0:
		comp_start = False
		print("\nVocê começa!")
	else:
		print("\nComputador começa!\n")
	
			#jogadas e peças restantes
	while n > 0:
		if comp_start:
			jogada = computador_escolhe_jogada(n, m)
			comp_start = False
			if jogada == 1:
				print("O computador tirou {} peça.".format(jogada))	
			else:
				print("O computador tirou {} peças.".format(jogada))
			n = n - jogada 
			if n > 0:
				print("Agora restam {} peças no tabuleiro.".format(n))
			else:
				print("Fim do jogo! O computador ganhou!")
		else:
			jogada = usuario_escolhe_jogada(n, m)
			comp_start = True
			if jogada == 1:
				print("Você tirou {} peça.".format(jogada))
			else:
				print("Você tirou {} peças.".format(jogada))
			n = n - jogada
			if n > 0: 
				print("Agora restam {} peças no tabuleiro.\n".format(n))
			else:
				print("Fim do jogo! O computador ganhou!\n")	

def campeonato():
	partidas = 1
	while partidas < 4:
		print("\n**** Rodada {} ****\n".format(partidas))	
		partidas = partidas + 1	
		partida()
	print("\n**** Final do campeonato! ****\n")
	print("Placar: Você 0 X 3 computador")	

def jogo():
			#escolha do tipo de jogo
	print("\nBem-vindo ao jogo do NIM! Escolha:\n")
	tipo_jogo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")) 
	if tipo_jogo == 1:
		print("\nVocê escolheu uma partida isolada!\n")
		return partida()

	if tipo_jogo == 2:
		print("\nVocê escolheu um campeonato!")
		return campeonato() 
			
jogo()