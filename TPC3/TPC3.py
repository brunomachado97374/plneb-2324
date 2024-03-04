# 1. Analisar Doc
# 2. Extrair Termos:
#       - data cleaning
#       - pattern matching:  1. Identificar o que temos de extrair e colocar um caracter especial antes que não esteja presente no documento   
# 3. Guardar Termos - estrutura: dicionário{"palavra": "significado", ....}
# 4. Gerar Termos

import re

filename = "Material_Aula\plneb-2324\data\dicionario_medico.txt"

with open(filename,'r', encoding= 'utf-8') as f:
    texto = f.read()

# data cleaning

texto = re.sub(r'(\w+)\n{2,}\f([A-ZÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ])',r"\1\n\2", texto)  # \f está entre a designação e a descrição
texto = re.sub(r'(\w+)\n{2,}\f([a-záéíóúàèìòùâêîôûãõç])',r"\1 \2", texto) # \f está no meio da descrição
texto = re.sub(r'\f',"", texto) # \f esta no inicio da página

# marcar designações

texto = re.sub(r'\n\n(.+)', r'\n\n@\1', texto)  # colocar um @ antes de cada designação para identificação 
texto = re.sub(r'@(.+)\n\n@', r'@\1\n', texto)  # devido a quebra de página, algumas designações estavam separadas da explicação, sendo colocado erradamente um @


# Extrair termos

termos = []
#termos = re.findall(r'@(.+)\n([^@]+)', texto) # capta os dois grupos tanto a designação como como a descrição. é gerada uma lista de tuplos [(designação, descrição)]

termos = re.findall(r'@([^@\n]+)\n([\s\S]+?)\n+@', texto)


# Gerar HTML


# barra colorida no topo da página
barra_superior = "<div class='barra-superior'><h1>Dicionário Médico</h1></div>"

texto_int = "<p>Este é um dicionário médico desenvolvido na disciplina de Linguística de Processamento Natural (LPN EB). Ele contém uma lista abrangente de termos e suas definições relacionadas ao campo da medicina e da saúde. Use este recurso como uma referência útil para entender e explorar o vocabulário técnico e especializado usado por profissionais da saúde.</p>"

body = "<body>"


html = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dicionário Médico</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
{barra_superior}
{texto_int}
{body}
<div class="container">
"""
# Adicionar termos agrupados alfabeticamente ao HTML
for designacao, descricao in termos:
    designacao_format = f"<span class='caractere-especial'>&#9679;</span>{designacao}"
    html += f"<h5 class='designacao'>{designacao_format}</h5>"
    html += f"<p>{descricao}</p>"
    html += "<hr/>"

html += """ 


</html>
"""

# Defina o caminho completo para o arquivo HTML
caminho_html = "C:/Users/bruno/OneDrive/Ambiente de Trabalho/UNI/Uni_4ano/2Semestre/PLN/Aulas/aula3_2.html"

# Abra o arquivo HTML para escrita
with open(caminho_html, "w", encoding="utf-8") as file_out:
    file_out.write(html)