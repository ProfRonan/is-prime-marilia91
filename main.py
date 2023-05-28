numero = int(input('digite um número inteiro: '))

if numero <= 0:
    print('Número inválido')
elif numero == 1:
    print('Não primo')
elif numero == 2:
    print("Primo")
elif numero > 2:
    is_prime = True
    for i in range (2, int(numero**0.5) + 1):
        if numero % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Primo")
    else:
        print("Não primo")
   

            
                    
            
            
            
    
            
