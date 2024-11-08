try:
    n1 = int(input("digite o número que será dividido"))
    n2 = int(input("digite o número que você quer dividir"))

    res = n1/n2
    print(res)

except:
    print("deu algum erro")
except ZeroDivisionError:
    print("Você dividiu por zero")