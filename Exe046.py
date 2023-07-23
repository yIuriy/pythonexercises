import emoji
from time import sleep
print('Contagem Regressiva para os fogos:')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks::fireworks::fireworks:', language='alias'))
