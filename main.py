# Importação dos múdulos utilizados, buscando utilizar somente o conteúdo visto em aula.
import csv  # módulo csv para processamento de arquivos csv.
import json  # módulo json para processamento do arquivo json para exportação.
from datetime import datetime  # módulo datetime para formatação da data e geração do nome do arquivo JSON.
import sys  # módulo sys, que permite importar o arquivo csv via terminal, sem a necessidade de configurar o código.


def formatar_data(data):
    """
        Descrição:
            Formata a string conforme solicitado.

        Parâmetros:
            data (str) : Recebe a string oriunda do csv para ser formatada.

        Retorno:
            data_formatada : Retorna a string formatada no padrão dd/mm/aaaa
    """
    # Exclui o cabeçalho da formatação
    if data.lower() == 'date':
        return data
    else:
        # Utilização da biblioteca datetime para formatar a data, sendo melhor e mais legível do que tratar os índices.
        data_formatada = datetime.strptime(
            data, '%Y-%m-%d %H:%M:%S%z').strftime('%d/%m/%Y'
                                                  )
        return data_formatada


def tratar_linha(linha):
    """
        Descrição:
            Formata as linhas do csv, retirando colunas que não serão utilizadas,
            trocando a datas e removendo tabulações.

        Parâmetros:
            linha (list) : Recebe uma lista com 5 strings para serem formatadas

        Retorno:
            linha (list) : Retorna a lista formatada no padrão 'Data, Conteúdo e Assunto'.

    """
    del linha[1:3]
    linha[0] = formatar_data(linha[0])
    linha[1] = linha[1].replace('\n', "")
    return linha


def exportar_csv(importar, exportar):
    """
        Descrição:
            Recebe um arquivo csv no terminal e retorna um arquivo csv pronto para ser utilizado nas pesquisas.

        Parâmetros:
            importar (file) : Recebe o arquivo sem tratamento.
            exportar (str) : Recebe o nome (str) do arquivo que será salvo.

        Retorno:
            exportar (file) : retorna arquivo que será salvo.
    """
    # Uso da função with que permite ler e escrever arquivos sem a necessidade de fechá-los manualmente.
    with open(importar, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        # Uso do comando map para simplificar a criação das linhas.
        lista = list(map(tratar_linha, leitor_csv))
    # Uso da função with que permite ler e escrever arquivos sem a necessidade de fechá-los manualmente.
    with open(exportar, 'w', encoding='utf-8', newline='') as arquivo:
        escrever_csv = csv.writer(arquivo)
        escrever_csv.writerows(lista)
        # Limpando a lista após o uso para otimizar espaço em memória.
        lista.clear()
    return exportar


def criar_filtro(opcao, prompt):
    """
        Descrição:
            Função enclausurada simples que cria um dicionário e atribui a opção do menu a uma string.

        Parâmetros:
            opcao (str) : Recebe a opção (str) oriunda do menu principal e repassada pela função buscar().
            prompt (str) : Recebe o prompt (str) oriunda do menu principal e repassada pela função buscar().

        Retorno:
            filtro (str) : retorna a variável filtro que será utilizada na busca.
    """
    opcoes_buscar = {'data': 0, 'termo': 1, 'assunto': 2}
    indice_tema = opcoes_buscar[opcao]

    def filtro(linha):
        return prompt in linha[indice_tema]

    return filtro


def buscar(opcao, prompt, tweets, salvar=False):
    """
        Descrição:
            A principal função do programa, ela recebe o arquivo csv e os parâmetros de busca, e aplica
            independente da opção selecionada (data, termo ou assunto). Ela recebe, processa, imprime na tela e salva
            em '.JSON'.


        Parâmetros:
            opcao (str) : Recebe a opção (str) oriunda do menu principal e repassa para a função criar_filtro().
            prompt (str) : Recebe o prompt (str) oriunda do menu principal e repassa para a função criar_filtro().
            tweets (csv) : Recebe o arquivo csv tratado anteriormente e utiliza para filtragem de dados.
            salvar (bool) : Caso seja True, a função não imprime e salva o resultado impresso anteriormente.

        Retorno:
            return True : Retorna verdadeira, caso tenha uma pesquisa a ser salva.
            return False : Retorna Falso, caso não tenha nenhuma pesquisa anterior para ser salva, e reseta após salvar.
    """
    # A função filtro sendo chamada
    filtro = criar_filtro(opcao, prompt)
    # Abrindo o arquivo csv para consulta
    with open(tweets, 'r', encoding='utf-8') as tweets:
        leitor_tweets = csv.reader(tweets)
        # Filtrando os resultados conforme as definições recebidas pela função filtra_busca().
        resultados = list(filter(filtro, leitor_tweets))
    # Se salvar = True, ele executa a rotina para salvar.
    if salvar:
        agora = datetime.now()
        # A função datetime está sendo utilizada para gerar o nome do arquivo JSON exportado, auxiliando no
        # armazenamento.
        data_hora_formatada = agora.strftime("%d%m%Y_%H%M%S")
        nome_arquivo = f"Busca_por_{opcao}_{data_hora_formatada}.json"
        with open(nome_arquivo, 'w', encoding='utf-8') as json_novo:
            resultados_json = [{"Data": linha[0], "Conteudo": linha[1], "Assunto": linha[2]} for linha in resultados]
            json_novo.write(json.dumps(resultados_json, ensure_ascii=False))
            resultados_json.clear()
        print('\033[92m\n[Pesquisa salva com sucesso]\n\033[0m')
        return False
    # Se salvar = False, ele apenas imprime a consulta na tela.
    else:
        print(f'Data | Conteúdo | Assunto')
        for linha in resultados:
            print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        return True


def main():
    """
        Descrição:
            É a função menu, onde são apresentadas as opções do programa sendo recebidos os inputs do usuário.

        Parâmetros:
            Não possui parâmetros de entrada.

        Retorno:
            Não possui parâmetros de saída.
    """
    while True:
        print('-' * 30)
        print('Boas vindas ao nosso sistema:')
        print('1 - Buscar tweets por data')
        print('2 - Buscar tweets por termo')
        print('3 - Buscar tweets por assunto')
        print('4 - Salvar resultado da busca')
        print('5 - Sair')
        print('-' * 30)
        resposta = input(f'Selecione uma opção: ')
        # lista criada para simplificar as opções do menu
        if resposta in ['1', '2', '3']:
            opcoes = {'1': 'data', '2': 'termo', '3': 'assunto'}
            # atribuição da seleção do menu a um par de valor, chave.
            opcao = opcoes[resposta]
            if opcao == 'data':
                while True:
                    data_prompt = input('Digite a data no formato dd/mm/aaaa: ')
                    # função datetime para formatar a hora e o bloco try, except para controlar as entradas corretas.
                    try:
                        prompt = datetime.strptime(data_prompt, '%d/%m/%Y').strftime('%d/%m/%Y')
                    except ValueError:
                        print('Data inválida. Por favor, digite uma data válida no formato correto.')
                        continue
                    resultado = buscar(opcao, prompt, tweets_tratados, False)
                    break
            elif opcao == 'assunto':
                while True:
                    # submenu assunto, apenas com os assuntos pré selecionados.
                    print('\tAssuntos disponíveis:\n'
                          '\t1. Copa do Mundo\n'
                          '\t2. Eleições\n'
                          '\t3. Ciência de Dados\n'
                          '\t4. Covid-19')
                    prompt = input(f'\tDigite uma opção para a busca em {opcao}: ')
                    if prompt in ['1', '2', '3', '4']:
                        assuntos = {'1': 'copa do mundo', '2': 'eleições', '3': 'ciência de dados', '4': 'covid-19'}
                        prompt = assuntos[prompt]
                        resultado = buscar(opcao, prompt, tweets_tratados, False)
                        break
                    else:
                        print('Digite uma opção válida.')
            else:
                prompt = input(f'Digite uma opção para a busca em {opcao}: ')
                resultado = buscar(opcao, prompt, tweets_tratados, False)

        elif resposta == '4':
            # uso do try para controlar se existe uma pesquisa anterior para ser salva, controlando a exceção
            # gerada pela falta de variáveis.
            try:
                if resultado:
                    resultado = buscar(opcao, prompt, tweets_tratados, True)
            except UnboundLocalError:
                print('\033[91m\n[Nenhuma busca para salvar]\n\033[0m')
        elif resposta == '5':
            print(f'\nObrigado pela consulta, volte sempre!')
            break

        else:
            print('Desculpe, não entendi sua resposta, digite novamente.')


if __name__ == "__main__":
    try:
        tweets_tratados = exportar_csv(sys.argv[1], sys.argv[2])
        main()
    except IndexError:
        print("É necessário fonrnecer os nomes de entrada e saída dos arquivos")
