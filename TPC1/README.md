### TPC1

O código presente no ficheiro anagramas.py serve para identificar os diversos anagramas presentes no documento e posteriormente agrupá-los. São realizas as seguintes operações:

1. Abre o arquivo de texto localizado em filename e lê o seu conteúdo.
2. Remove a pontuação do texto, substituindo os caracteres específicos (como ".", ",", "-", ":" etc) por espaços.
3. Converte todo o texto para minúsculas.
4. Divide o texto em palavras individuais.
5. Define uma função Anagrama que verifica se duas palavras são anagramas.
6. Define uma função VerificaAnagrama que verifica e retorna um dicionário de anagramas encontrados no texto.
7. Executa a função VerificaAnagrama no texto dividido em tokens e imprime os resultados.

Detelhando mais ao pormenor a função VerificaAnagrama, esta percorre todas as palavras no texto e verifica se existem anagramas para cada uma delas. Para isso, ela compara cada palavra com todas as palavras subsequentes no texto. Se uma palavra tem um anagrama, então essa palavra é adicionada a um dicionário de anagramas.

O dicionário de anagramas é estruturado de forma que as chaves são os anagramas em si, isto é, as letras da palavra ordenadas alfabeticamente, e os valores associados a essas chaves são listas das palavras originais que são anagramas entre si.
