import requests

valor = float(input("Digite o valor a ser convertido: "))
de = input("Digite a moeda que deseja converter: ").upper()
para = input("Digite a moeda de destino: ").upper()

url = requests.get(f'https://economia.awesomeapi.com.br/json/last/{de}-{para}')
cotacao = url.json()

moeda_selecionada = f'{de}{para}'

nome_moeda_conversao = str(cotacao[moeda_selecionada]['name'])
valor_antes_da_barra = nome_moeda_conversao.split('/')[0]
valor_depois_da_barra = nome_moeda_conversao.split('/')[-1]

valor_bid = float(cotacao[moeda_selecionada]['bid'])
valor_calculado = valor * valor_bid

print(f"Essa é a cotação atual do {valor_antes_da_barra}({de}):", valor_bid)
print(f"O valor de '{valor} {de}' convertido para {valor_depois_da_barra}({para}):",valor_calculado)

print(f'\n {cotacao}')