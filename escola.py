def media(notas):
	soma = 0
	media=0
	for nota in notas:
		soma+=int(nota)
	
	media = soma/len(notas)
	
	return media;
	

def situacao(media):
	if media>=10:
		return "Aprovado";
	else:
		return "Reprovado";

res = media([19,12,11,20,20])
print(res)
