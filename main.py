while True:
    
    try:

        nome = input("Digite seu nome")

        if not nome.isalpha():
            raise ValueError("VOCÊ NÃO DIGITOU UM NOME VÁLIDO!!")


        nome_maiusculo = nome.upper()

        print(nome_maiusculo)
        break

    except ValueError as e:
            print(e)



