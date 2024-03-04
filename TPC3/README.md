### TPC 3

No âmbito do TPC 3 foram desenvolvidos dois pontos principais propsotos pelo docente:

1. Familiarização com o HTML bem como explorar funcionalidades;
2. Melhor estruturação das expressões regulares para lidar com alguns problemas identificados na aula.


Relativamente ao **ponto 1** foi gerado um arquivo HTML que servirá como uma representação visual do dicionário médico. O objetivo é criar uma página web que exiba os termos médicos e suas definições de forma organizada e estruturada.

A estrutura do HTML inclui:

- Uma barra na parte superior da página com o título "Dicionário Médico". Esta estutura é representada usando o ficheiro "syle.css" para ter uma cor de fundo específica e texto em branco.

- Uma seção introdutória que fornece uma breve descrição do dicionário médico e sua finalidade. É inserido no HTML como um parágrafo.

- Container Principal: Todo o conteúdo é envolvido em um container principal. Este passo tem como objetivo centralizar e limitar a largura máxima do conteúdo para melhor legibilidade.

- Designações e descrições: Cada termo médico e sua descrição são inseridos na página. A designação é exibida em negrito e seguida pela descrição. Antes de cada designação, é colocado um caractere especial (um círculo preenchido), que é estilizado usando o CSS para dar destaque visual.

- Estilo CSS: O arquivo CSS é vinculado ao HTML para aplicar estilos visuais à página. Isso inclui formatação de texto, cores de fundo, espaçamento e outros estilos para tornar a página mais atraente e legível.


Abordando agora o ponto 2, durante a análise do ficheiro .pdf e a sua posterior passagem para .txt identificou-se algumas situações provocadas pelo form feed, isto é as quebras de página.

- **Situação 1:** Devido à quebra de página, a designação fica separada da descrição, tendo a estrutura seguinte no ficheiro .txt:


- **Situação 2:** Devido à quebra de página, a descrição é separada em duas partes no ficheiro:


- **Situação 3:** O indicador de quebra de página aparece antes da designação (caso que não corresponde a uma exceção):


Desta forma, cada um destes casos foi tratado de forma individual, realizando uma expressão regular para cada situação. Sucintamente, Na situação 1, realiza-se a captura do grupo 1 (designação) que é seguido de dois ou mais \n e um \f e posteriormente é capturado o segundo grupo (primeira letra da descrição que é maiúscula). Entre os grupos de captura é colocado um \n.

Para a situação 2, mantêm-se um raciocínio semelhante, no entanto o segundo grupo de captura será iniciado por uma letra minúscula e entre os grupos de captura é colocado um " ".

Para a situação 3, substituiu-se o \f por uma string vazia, algo já realizado na aula.

Nota: Para a situação 2, a regex desenvolvida pode ainda não cumprir a 100% de todos os casos possíveis, nomeadamente, se a segunda frase que foi separada na descrição começar por letra maiúscula.

Por fim a expressão regular para a captação dos termos (tuplo designação, descrição) foi aprimorada para abregar mais casos. A título de exemplo:

@análise didática
Análise que todo psiquiatra candidato a psicanalista deve submeter-se para se tornar membro da sociedade psicanalítica e poder praticar a especialidade. Exigência introduzida em 1922, tem por finalidade instruir o futuro
psicanalista e corrigir, eventualm

Nesta situação, após futuro existe um \n, no entanto, a frase seguinte ainda pertence a este termo. Assim foi usado o @ da próxima designação para captar corretamente todo o texto.
