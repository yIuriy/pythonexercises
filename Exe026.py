f1 = str(input("Pense em uma frase:")).lower().strip()  # Pergunta, joga pra minus e tira espaços
frase = f1.replace('à', 'a').replace('â', 'a').replace('ã', 'a').replace('á', 'a')  # Garante que todos os a seja vistos
print(f'A letra "A" aparece na frase {frase.count("a")} vezes.')  # Conta vezes que a aparece
print(f'A letra "A" aparece pela primeira vez na posição {frase.find("a") + 1}.')  # Primeira vez left para rigth
print(f'A letra "A" aparece pela última vez posição {frase.rfind("a") + 1}.')  # Última vez right para left
