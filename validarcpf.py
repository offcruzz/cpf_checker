while True:
    cpf = input('Digite um CPF: ')
    cpfnovo = cpf[:-2]              
    reverso = 10                       
    total = 0

    for index in range(19):
        if index > 8:                 
            index -= 9                  

        total += int(cpfnovo[index]) * reverso  

        reverso -= 1                   
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                 
                d = 0
            total = 0                  
            cpfnovo += str(d)         

    sequencia = cpfnovo == str(cpfnovo[0]) * len(cpf)

    if cpf == cpfnovo and not sequencia:
        print('CPF Válido')
    else:
        print('CPF Inválido')
