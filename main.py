import csv
import json
from datetime import datetime
import sys


def formatar_data(data):
    if data.lower() == 'date':
        return data
    else:
        data_formatada = datetime.strptime(data, '%Y-%m-%d %H:%M:%S%z').strftime('%d/%m/%Y')
        return data_formatada


def tratar_linha(linha):
    del linha[1:3]
    linha[0] = formatar_data(linha[0])
    linha[1] = linha[1].replace('\n', "")
    return linha


def tratar_dados(importar, exportar):
    with open(importar, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        lista = list(map(tratar_linha, leitor_csv))
    with open(exportar, 'w', encoding='utf-8', newline='') as arquivo:
        escrever_csv = csv.writer(arquivo)
        escrever_csv.writerows(lista)
        lista.clear()
    return exportar


def criar_filtro(opcao, tema):
    opcoes_buscar = {'data': 0, 'termo': 1, 'assunto': 2}
    indice_tema = opcoes_buscar[opcao]

    def filtro(linha):
        return tema in linha[indice_tema]
    return filtro


def buscar(opcao, prompt, tweets_tratados, salvar=False):
    filtro = criar_filtro(opcao, prompt)
    with open(tweets_tratados, 'r', encoding='utf-8') as tweets:
        leitor_tweets = csv.reader(tweets)
        resultados = list(filter(filtro, leitor_tweets))
    if salvar:
        agora = datetime.now()
        data_hora_formatada = agora.strftime("%d%m%Y_%H%M%S")
        nome_arquivo = f"Busca_por_{opcao}_{data_hora_formatada}.json"
        with open(nome_arquivo, 'w', encoding='utf-8') as json_novo:
            resultados_json = [{"Data": linha[0], "Conteudo": linha[1], "Assunto": linha[2]} for linha in resultados]
            json_novo.write(json.dumps(resultados_json, ensure_ascii=False))
            resultados_json.clear()
        print('\033[92m\n[Pesquisa salva com sucesso]\n\033[0m')
    else:
        print(f'Data | Conteúdo | Assunto')
        for linha in resultados:
            print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        return True


def main():
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
        if resposta in ['1', '2', '3']:
            opcoes = {'1': 'data', '2': 'termo', '3': 'assunto'}
            opcao = opcoes[resposta]
            if opcao == 'assunto':
                while True:
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
            try:
                if resultado:
                    resultado = buscar(opcao, prompt, tweets_tratados, True)
            except:
                print('\033[91m\n[Nenhuma busca para salvar]\n\033[0m')
        elif resposta == '5':
            print(f'\nObrigado pela consulta, volte sempre!')
            break

        else:
            print('Desculpe, não entendi sua resposta, digite novamente.')


if __name__ == "__main__":
    try:
        tweets_tratados = tratar_dados(sys.argv[1], sys.argv[2])
        main()
    except IndexError:
        print("É necessário fonrnecer os nomes de entrada e saída dos arquivos")
