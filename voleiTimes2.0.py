# libraries importadas
import random
from time import sleep

# ornamentos (detalhes visuáis)
ornamentos = {'ornamento_1': '\033[36m-=\033[m'}

# banco de dados com os participantes
participantes = ['Nivea', 'Daniel', 'Murillo', 'Raissa', 'Ester', 'Matheus', 'Luiz Felipe', 'Erick', 'Wesley', 'Alexandre', 'Maycon',
                 'Gre.Nathan', 'Havila', 'Maria', 'Zeus', 'João Pedro Peix.', 'Isaque', 'Igor', 'Lucas Aq.', 'Lucas Soa.',
                 'Raniel', 'Lucas', 'Samella', 'Arthur']

# banco de dados com os possíveis times
times = ['\033[33mTime A', '\033[32mTime B', '\033[31mTime C', '\033[34mTime D']

# código para randomizar o banco de dados
selecao = random.sample(participantes, len(participantes))

# Menu do programa (detalhe visual)
print(ornamentos['ornamento_1']*20)
print('\033[35mGerador de times automático\033[m')
print(ornamentos['ornamento_1']*20)
sleep(2)
print('\033[35mGerando\033[m', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(1)
print('')

# Laço principal de repetição
for c in range(0, 4):
    print('')
    print(times[c])
    if c < 4:
        print('='*10)
    for c2 in range(0, 6):
        if len(selecao) <= 6:
            # Laço que separa os componentes da lista
            for integrantes in selecao:
                print(integrantes)

            break
        else:
            print(selecao[c2])
            # Código para separar os jogadores que já foram selecionados do banco de dados principal
            selecionados = selecao.pop(c2)
    print('='*10)
