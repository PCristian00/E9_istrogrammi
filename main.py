def istogrammi(lista):
    for num in lista:
        print("*" * num)


print("Inserire numeri separati da spazi")
print("INVIO per confermare")
a = [int(x) for x in input().split()]

istogrammi(a)
