import re, json

# ficheiros utilizados 

filename = "C:/Users/bruno/OneDrive/Ambiente de Trabalho/UNI/Uni_4ano/2Semestre/PLN/plneb-2324/TPC5/conceitos.json"
filename2 = "C:/Users/bruno/OneDrive/Ambiente de Trabalho/UNI/Uni_4ano/2Semestre/PLN/plneb-2324/TPC5/livrinho.txt"
filename3= "C:/Users/bruno/OneDrive/Ambiente de Trabalho/UNI/Uni_4ano/2Semestre/PLN/plneb-2324/TPC5/termos_traduzidos.txt"

with open(filename, 'r', encoding='utf-8') as file:
    conceitos = json.load(file)

with open(filename2, 'r', encoding='utf-8') as file:
    texto = file.read()
    
with open(filename3, 'r', encoding='utf-8') as file:
    termos = file.read()
    
    
#  padrões para detetar padrões específicos
    
blacklist= ["e","de","para","pelo","os","são","este"]
conceitos_min = { chave.lower(): conceitos[chave] for chave in conceitos}

padrao = r'(.+?) @ (.+)'

dic_termos = {}
for match in re.finditer(padrao, termos):
    portugues = match.group(1).lower()
    ingles = match.group(2).lower()
    dic_termos[portugues] = ingles

def etiquetador(matched): 
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    if (palavra in conceitos_min) and (palavra not in blacklist) and (palavra in dic_termos.keys()):
        descricao = "en: " + str(dic_termos[palavra]) +"\n"
        descricao += str(conceitos_min[palavra])
        descricao = re.sub(r"<br>\s*",r" ",descricao) #remove os <br> das descricoes
        etiqueta = f'<a href="" title = "{descricao}">{original}</a>' #meter o original para que a palavra apareça escrita como tava antes em vez de ficar em minusculas
        return etiqueta
    else:
        return original


# HTML
expressao =r"[\wáàéíçõâúãóê]+"
texto = re.sub(r"\n",r"<br> ",texto)
texto = re.sub(r"\f",r"<hr>",texto) 
texto = re.sub(expressao,etiquetador,texto, flags=re.IGNORECASE)

with open("livro.html", "w", encoding='utf-8') as file_out:
    print(texto, file=file_out)

