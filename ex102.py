def fatorial(n, show=False):
    """Calcula o fatorial de um número
    Args:
        n: O número a ser calculdo
        show: Mostrar ou não a conta.
        Returns: O valor fatorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print('=', end='')
        f *= c
    return f
#Programa Principal
#print(fatorial(5, show=True))
help(fatorial)

