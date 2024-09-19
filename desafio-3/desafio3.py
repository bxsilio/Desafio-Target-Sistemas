import json

# Carrega dados do arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Extrai valores de faturamento, ignorando dias sem faturamento (valor 0.0)
valores = [item['valor'] for item in dados if item['valor'] > 0.0]

# Calcula o menor e o maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula a média mensal de faturament
media_mensal = sum(valores) / len(valores)

# Conta o número de dias com faturamento acima da média mensal
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
