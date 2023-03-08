import json

with open('C:/Users/chris/Downloads/dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
4

# Inicializando as variáveis de menor e maior valor de faturamento com o valor do primeiro dia
menor_valor = dados[0]['valor']
maior_valor = dados[0]['valor']

# Inicializando a variável de soma dos valores de faturamento com o valor do primeiro dia
soma_faturamento = dados[0]['valor']

# Inicializando a variável de quantidade de dias com faturamento acima da média como zero
dias_acima_media = 0

# Loop para percorrer todos os dias do mês
for dia in dados:
    # Verificando se o faturamento do dia atual é menor do que o menor valor já registrado
    if dia['valor'] < menor_valor:
        menor_valor = dia['valor']
    
    # Verificando se o faturamento do dia atual é maior do que o maior valor já registrado
    if dia['valor'] > maior_valor:
        maior_valor = dia['valor']
    
    # Verificando se o dia atual teve faturamento acima da média mensal
    if dia['valor'] > (soma_faturamento / len(dados)):
        dias_acima_media += 1
    
    # Adicionando o valor do faturamento do dia atual à soma total
    soma_faturamento += dia['valor']

# Calculando a média mensal de faturamento, ignorando os dias sem faturamento
media_mensal = soma_faturamento / len([dia for dia in dados if dia['valor'] > 0])

# Imprimindo os resultados

print(f"Menor valor de faturamento: {menor_valor:.2f}")

print(f"Maior valor de faturamento: {maior_valor:.2f}")

print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")
