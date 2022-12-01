#! python3
""" 
	Esse programa gera tabelas de boletim de nota de um aluno!
"""

import datetime,openpyxl,escola,boletim

aviso = "(ou digite q para sair do programa)"

while True:
	dados = {}
	
	#Recebe o nome do aluno do usuário
	dados['aluno']=input("Digite o Nome do aluno " +aviso+ ": ")
		
	#verifica se o usuário digitou "q" para sair do programa
	if(dados["aluno"] == "q"):
		print("Muito obrigado")
		break;
		
	#Recebe a classe do aluno do usuário
	dados['classe']=input("Digite a classe do aluno(Em número inteiro) " +aviso+ ": ")
		
	#verifica se o usuário digitou "q" para sair do programa
	if(dados["classe"] == "q"):
		print("Muito obrigado")
		break;
		
	#recebe o trimestre do usuário
	dados['trimestre']= input("Digite o trimeste (em número inteiro)"+aviso+": ")
	
	#verifica se o usuário digitou "q" para sair do programa
	if(dados["trimestre"] == "q"):
		print("Muito obrigado")
		break;
		
	#recebe o Ano lectivo do usuário
	dados['ano_lectivo']= input("Digite o ano_lectivo "+aviso+": ")
	
	#verifica se o usuário digitou "q" para sair do programa
	if(dados["ano_lectivo"] == "q"):
		print("Muito obrigado")
		break;

				
	print("Ok, Agora forneça as disciplinas e as respectivas notas")
	dados["caderneta"] = []
	while True:
		resposta = {}
		resposta['disciplina'] = input("Digite a disciplina "
			+" (digite q se já não há nenhuma): "
		)
		if(resposta['disciplina']=="q"):
			print("Muito obrigado!")
			break;
				
		resposta['nota'] = input("Digite a nota para a disciplina"
			+ " de " + resposta['disciplina']+": "
		)
		if not resposta['nota'].isdecimal():
			print("A nota deve ser inteiro")
			continue;
		else:
			dados['caderneta'].append(resposta)
			
			
	if len(dados['caderneta'])==0:
		print("Nenhuma nota, nem disciplina")
		break;
	
	notas = []
	for caderneta in dados['caderneta']:
		notas.append(int(caderneta["nota"]))
	
	media = escola.media(notas)
	dados['media']=media
	
	dados['situacao'] = escola.situacao(int(dados['media']))
	
	boletim.criarBoletim(dados)
	user = input("Pretende gerar mais um boletim?(s/n)")
	if user == "s":
		continue;
	else: 
		break;

	
	
