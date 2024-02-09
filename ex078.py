valores = []
maior = 0
menor = 0
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
                menor = valores[c]
print(f'Você digitou os números {valores} num total de {len(valores)} valores')    
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') 
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')    
       

    