import pandas as pd
import numpy as np
from apyori import apriori

baseMercado = pd.read_csv('mercado.csv', header=None)

transacoes = baseMercado.applymap(str).values.tolist()

#print(transacoes)

#Gerar regras de associação usando apriori

regras = apriori(transacoes, min_suport=0.3, min_confidence=0.8, min_leaft=2)

#Converter resultado para lista
resultados = list(regras)

print('Resultado das regras')
#print(resultados)

A = [] #SE - regra
B = [] #ENTÃO - regra
suporte = []
confianca = []
lift = []

for resultado in resultados:

    s = resultado[1] #suporte 
    print('S', s)
    result_rules = resultado[2] #regras
    print('Rules', result_rules)
    
    for result_rule in result_rules:
        a = list(result_rule[0]) #SE - regra
        b = list(result_rule[1]) #ENTÃO - regra
        c = result_rule[2] #Confiança
        l =  result_rule[3] #lift
        print(f'{a}->{b}(Suporte: {s}, Confiança: {c}, Lift: {l})')

        A.append(a)
        B.append(b)
        suporte.append(s)
        confianca.append(c)
        lift.append(l)

# Criação do novo df
rules_df = pd.DataFrame({
    'A': A,
    'B': B,
    'Suporte': suporte,
    'Confianca': confianca,
    'Lift': lift
})        

print('Ordenando df por lift')

print(rules_df.sort_values(by='Lift', ascending=False))