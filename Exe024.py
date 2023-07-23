city = str(input('Pense em alguma cidade:')).strip()  # Pergunta nome da cidade e retira espaços
city2 = city.upper()  # Joga pra mais, não importando o jeito de escrever Santo
city3 = city2[:6]  # Define até a letra que é pra procurar
print('Essa cidade tem a palavra Santo no início?')  # Pergunta pra complementar
print('SANTO' in city3)  # Pergunta se tem Santo na var que eu define até o 6
