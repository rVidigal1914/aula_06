
while True:

    try:

        numeros = input ("DIGITE UMA LISTA DE NUMEROS SEPARDOS POR VIRGULA. Ex: 1,4,6")

        lista_de_num = numeros.split(",")

        lista_num_inteiros = []

        for numero in lista_de_num:
        
            lista_num_inteiros.append(int(numero))
            print(lista_num_inteiros)
        break
    except:
        print("Você digitou número errado")
