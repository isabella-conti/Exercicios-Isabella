# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
caminho_json = 'Exercicio3.json'


with open(caminho_json, 'r') as arquivo:
    dados = json.load(arquivo)

dias_com_faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_valor = min(dias_com_faturamento)
maior_valor = max(dias_com_faturamento)


media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)


dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

print(f"Menor valor de faturamento no mês: {menor_valor}")
print(f"Maior valor de faturamento no mês: {maior_valor}")
print(f"Número de dias no mês com faturamento acima da média mensal: {dias_acima_da_media}")

