filename = "C:/Users/bruno/OneDrive/Ambiente de Trabalho/UNI/Uni_4ano/2Semestre/PLN/Material_Aula/plneb-2324/data/CIH Bilingual Medical Glossary English-Spanish.txt"

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Remover pontuação

text.replace("."," ")
text.replace(","," ")
text.replace("-"," ")
text.replace(":"," ")
text.replace("/"," ")
text.replace("'"," ")
text.replace("("," ")
text.replace(")"," ")


text = text.lower()

#Dividir o texto
tokens = text.split()

# Função que verifica se duas palavras são anagramas
def Anagrama(palavra1,palavra2):
    return sorted(palavra1) == sorted(palavra2)

# Função que verifica os anagramas existentes no documento
def VerificaAnagrama(string):
    PalavrasVerificadas = set()
    Anagramas = {}
    
    for i in range(len(tokens)):
        for j in range(i+1, len(tokens)):
            if tokens[i] not in PalavrasVerificadas and Anagrama(tokens[i], tokens[j]):
                palavra = ''.join(sorted(tokens[i]))
                if palavra not in Anagramas:
                    Anagramas[palavra] = [tokens[i]]
                else:
                    Anagramas[palavra].append(tokens[i])
                PalavrasVerificadas.add(tokens[i])

    return Anagramas
    
resultado = VerificaAnagrama(tokens)
for chave, valores in resultado.items():
    print(f'{chave}: {valores}')
