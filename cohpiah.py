import re
import sys

def le_assinatura():
     
    '''Le os traços linguísticos do modelo e devolve uma assinatura a ser 
    comparada com os textos''' 
    print("\nBem-vindo ao detector automático de COH-PIAH.\n\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))
    print()
    return [wal, ttr, hlr, sal, sac, pal]



def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto "+ str(i) +" (aperte enter para sair): ")
        print()

    return textos


    
def separa_sentencas(texto):
    
    '''Recebe um texto e devolve uma lista das sentenças do texto'''
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
        


def separa_frases(sentenca):

    '''Recebe uma sentença e devolce ums lista de frases'''
    frases = re.split(r"[,:;]+", sentenca)
    return frases



def separa_palavras(frase):
    
    '''Recebe uma frase e devolve uma lista das palavras dentro da frase'''
    palavras = frase.split()
    return palavras



def n_palavras_unicas(lista_palavras):
    
    '''Recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas


    
def n_palavras_diferentes(lista_palavras):
    
    '''Recebe uma lista de palavras e devolve o número de palavras diferentes utilizados'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)



def n_caracteres_frases(palavra):	
    
    # Recebe uma palavra e devolve uma lista de caracteres, excluindo aqueles que dividem as frases
    n_caracteres = palavra.split()
    if n_caracteres[-1] == "," or n_caracteres[-1] == ":" or n_caracteres[-1] == ";":
        del n_caracteres[-1]
    return n_caracteres    
    


def n_caracteres_setencas(palavra):

    # Recebe uma palavra e devolve uma lista de caracteres, excluindo aqueles que dividem as sentencas
    n_caracteres = palavra.split()
    if n_caracteres[-1] == "." or n_caracteres[-1] == "!" or n_caracteres[-1] == "?":
        del n_caracteres[-1]
    return n_caracteres    



def calcula_assinatura(texto):

    '''Recebe um texto e devolve a assinatura dele'''

    wal = tamanho_medio_palavra(texto)    
    ttr = relacao_type_token(texto)   
    hlr = hapax_legomana(texto)    
    sal = tamanho_medio_sentenca(texto)  
    sac = complexidade_sentenca(texto)   
    pal = tamanho_medio_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]



def tamanho_medio_palavra(texto):

    '''
        Recebe um texto (str) e devolve o tamanho médio de palavra (float)
        {wal = soma dos tamanhos das palavras / número total de palavras}   
    '''

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []
    lista_caracteres = []
    soma = 0
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)
    for palavra in lista_palavras:
        lista_caracteres += n_caracteres_frases(palavra)
    for caractere in lista_caracteres:
        soma += len(lista_caracteres) 
    return soma / len(lista_palavras)             



def relacao_type_token(texto):

    '''
        Recebe um texto(str) e devolve a Relação Type-Token(float)
        {ttr = número de palavras diferentes / número total de palavras}
    '''
         
    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []
    soma = 0
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)
    
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)



def hapax_legomana(texto):

    '''
        Recebe um texto(str) e devolve a Razão Hapax Legomana(float)
        {hlr = número de palavras únicas / número total de palavras}
    '''

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []
    soma = 0
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)
    
    return n_palavras_unicas(lista_palavras) / len(lista_palavras)



def tamanho_medio_sentenca(texto):

    '''
        Recebe um texto(str) e devolve o tamanho médio de setença(float)
        {sal = soma dos caracteres em todas as sentenças / número total de sentenças}

        * os caracteres que separam uma sentença da outra não são contabilizados (. ! ?)
    '''  

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []
    lista_caracteres = []
    soma = 0
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)
    for palavra in lista_palavras:
        lista_caracteres += n_caracteres_setencas(palavra)
    for caractere in lista_caracteres:
        soma += len(lista_caracteres) 
    return soma / len(lista_sentencas)



def complexidade_sentenca(texto):

    '''
        Recebe um texto(str) e devolve a complexidade de sentença(float)
        {sac = número total de frases / número total de sentenças}
    ''' 

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    soma = 0
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    for frase in lista_frases:
        soma += len(lista_frases)
    return soma / len(lista_sentencas)



def tamanho_medio_frase(texto):

    '''
        Recebe um texto(str) e devolve o tamanho médio de frase(float)
        {pal = soma do número de caracteres em cada frase / número total de frases}

        * os caracteres que separam uma frase da outra não são contabilizados (, : ;)
    ''' 

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []
    lista_caracteres = []
    soma = 0
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)
    for palavra in lista_palavras:
        lista_caracteres += n_caracteres_frases(palavra)
    for caractere in lista_caracteres:
        soma += len(lista_caracteres) 
    return soma / len(lista_frases)

      

def compara_assinatura(as_a, as_b):

    '''Recebe duas assinaturas de texto e devolve o grau de similaridade'''

    grau_similaridade = 0
    for i in range(len(as_a)):
        grau_similaridade += abs(as_a[i] - as_b[i])
    grau_similaridade /= 6
    return grau_similaridade    


def avalia_textos(textos, ass_cp):
    
    '''Recebe uma lista de textos e uma assinatura ass_cp e devolve o numero (1 a n) 
       do texto com maior probabilidade de ter sido infectado'''
    
    menor_grau_similaridade = sys.maxsize
    
    for texto in range(len(textos)):
        grau_similaridade = compara_assinatura(ass_cp, calcula_assinatura(textos[texto])) 
        if grau_similaridade < menor_grau_similaridade:
            menor_grau_similaridade = grau_similaridade
            texto_infectado = texto
    return texto_infectado + 1       


            
if __name__ == "__main__":
    ass_cp = le_assinatura()
    textos = le_textos()
    print("O autor do texto {} está infectado com COH-PIAH".format(avalia_textos(textos, ass_cp)))




       
