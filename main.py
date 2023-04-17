numero = int(input('digite um número inteiro: '))

if numero <= 0:
    print('Número inválido')
elif numero == 1:
    print('Não primo')
elif numero == 2 or numero == 3 or numero == 5: 
    print('Primo')
else:
    for i in range(2, numero):
        if numero % i == 0:
            print('Não primo')
            break
        elif numero % 3 == 0:
            print('Não primo')
            break
        elif numero % 5 == 0:
            print('Não primo')
            break
        else: 
            print('Primo')
            break
            
                    
            
            
            
    
            
