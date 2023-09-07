""" Refaça o desafio 051 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão usan-
do a estrutura while.
"""
# TODO exercício atualizado v2
print('\033[032m<>\033[32m' * 10)
print('   \033[031mGerador de PA\033[031m')
print('\033[032m<>\033[32;0m' * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('\033[33m {}\033[33;0m -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM!')
