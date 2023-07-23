def notas(*num, sit=False):
    """=. Função que recebe várias notas e situações de alunos, analisando-as.
    :param num: uma ou mais notas(aceita várias)
    :param sit: valor opcional, TRUE para mostrar a situação, FALSE para não mostrar
    :return: dicionário com várias informações sobre a situação da turma."""
    resp = {'total': len(num),
            'maior': max(num),
            'menor': min(num),
            'média': sum(num) / len(num)}
    if sit:
        if resp["média"] >= 7:
            resp['situação'] = 'BOA'
        elif 5 <= resp["média"] < 7:
            resp['situação'] = 'RAZOÁVEL'
        elif resp["média"] < 5:
            resp['situação'] = 'RUIM'
    return resp


# Programa principal
resp = notas(6.5, 7.8, 5.6, sit=True)
print(resp)
