def notas(*n, sit=False):
    """---> Função para analisar notas e situações de vários alunos.

    Args:
        sit (bool, optional): valor opcional se deve ou não adicionar a situação. Defaults to False.
        n: uma ou mais notas dos alunos

    Returns:
        [type]: dicionário com váris informações dos alunos
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = len(n)
    r['menor'] = len(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5, 2.5, 8.5, sit=True)    
