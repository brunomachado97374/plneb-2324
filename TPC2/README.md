### TPC2

Esta ficha tinha como objetivo iniciar a familiarização com as expressões regulares e como aplicá-las. Destaque-se dois exercícios onde foi necessário realizar um procura de conceitos novos para resolver os mesmos. Esses exercícios, o raciocínio neles aplicados e os conceitos novos aprendidos são descritos de seguida.

#### Exercicio 8

Neste exercício procedeu-se à criação da função "inteiros" que tem como objetivo devolver todos os números inteiros presentes numa string. Tal como dito no enunciado, um número inteiro pode conter um ou mais dígitos e pode ser positivo ou negativo. Além disso foi necessário ter em atenção a problemática de números decimais que podem estar representados utilizando o caracter "," ou ".". Deste modo, foi implementado no pattern um raciocínio que permitisse verificar a existência de esses caracteres antes ou após um digito. Salienta-se também uma verificação necessária que consiste na filtragem de números que não são antecedidos por ponto, no entanto, compõem a  parte decimal do número. No ficheiro TPC2.ipynb após a solução correta é possível verificar um caso onde os segundos algarismos decimais são filtrados como números inteiros, o que não está correto.

Para a realização deste exercicio, foram utilizados os raciocínios "lookbehind" e "lookahead" ambos negativos no sentido de verificar se a correspondência não é precedida por um ponto ou vírgula "[.,]" garantindo que o número inteiro não seja parte de um número decimal("lookbehind") e se a correspondência não é seguida por um ponto ou vírgula"[,.]" seguido por dígitos "\d", garantindo que o número inteiro não seja seguido por uma parte decimal ("lookahead").

Para a resolução deste exercício foi utilizada a seguinte bibliografia:

1. https://stackoverflow.com/questions/26594073/integer-pattern-python-regex
2. https://docs.python.org/3/library/re.html



#### Exercício 10

Na realização deste exercício, surgiu alguma dificuldade no momento de obter a separação dos códigos postais após realizar o match. Após uma pequena pesquisa na literacia do Python (link: https://docs.python.org/3/howto/regex.html#grouping ), foi possível verificar que o re.match() não realiza o retorno da string para a qual está a fazer a comparação.

Contudo, é possível perguntar ao objeto match informação sobre a string. Assim, verificou-se a existência do método group() que retorna as sub-strings presentes na string que se realizou o match. Assim, aplicou-se este método neste exercício, para a função retornar uma lista de tuplos compostos por dois elementos, sendo eles a primeira e segunda parte do código postal. 