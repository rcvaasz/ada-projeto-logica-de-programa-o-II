# Projeto Logica de Programacao II
 
## Sistema de Busca em Dados do Twitter

Este projeto consiste em um Sistema de Busca de Tweets que permite ao usuário realizar pesquisas em uma base de dados do Twitter. O sistema oferece funcionalidades para buscar tweets por data, por termo, por assunto e permite salvar os resultados da busca em um arquivo JSON. Abaixo estão os detalhes do projeto:

Funcionalidades

1. #### **Menu Principal**

    Ao iniciar o programa, o usuário é apresentado a um menu que oferece as seguintes opções:


    1 - Buscar tweets por data
    
    2 - Buscar tweets por termo
    
    3 - Buscar tweets por assunto
    
    4 - Salvar resultado da busca
    
    5 - Sair

1. #### **Base de Dados de Tweets**

    O sistema utiliza uma base de dados armazenada em um arquivo CSV, contendo cerca de 4 mil tweets divididos em quatro assuntos: covid-19, ciência de dados, copa do mundo e eleições. Cada tweet possui informações como data, URL, conteúdo, nomes de usuários e o assunto correspondente. Sendo eles durante a execução do programa, processados e selecionados para exibir apenas o que é relavante para o escopo proposto.

2. #### **Buscar Tweets por Data**

    Permite que o usuário digite uma data no formato dd/mm/aaaa, e o sistema imprime na tela os tweets referentes à data solicitada.

3. #### **Buscar Tweets por Termo**

    Permite que o usuário digite uma palavra ou termo, e o sistema imprime na tela os tweets que contenham a palavra informada.

4. #### Buscar Tweets por Assunto

    Permite que o usuário filtre na base de dados todos os tweets referentes a um assunto pré-determinado (_covid-19, ciência de dados, copa do mundo e eleições_).

5. #### Salvar Resultado da Busca

    Permite que o usuário salve em arquivo cada busca realizada, em formato JSON (.json), contendo a data, conteúdo e assunto de cada tweet retornado na busca.

6. #### Sair

    Permite que o usuário finalize o programa pelo menu principal quando desejar.

**Código Fonte**

O código-fonte está organizado em funções para facilitar a compreensão e manutenção. Utiliza os módulos csv e json para manipulação de arquivos e formatação dos resultados. A entrada e saída de arquivos podem ser feitas via terminal, permitindo uma interação simplificada.

**Como Executar o Programa**

O programa pode ser executado via linha de comando, fornecendo os nomes dos arquivos de entrada e saída:

`python nome_do_script.py arquivo_entrada.csv arquivo_saida.csv`

Certifique-se de ter os módulos necessários instalados para a execução correta do programa.

_Este projeto foi desenvolvido com base em conceitos aprendidos em aula, visando simplicidade e eficiência. Para eventuais dúvidas ou melhorias, sinta-se à vontade para entrar em contato._


E-mail: leonildolinck@gmail.com
Discord: leonildo




