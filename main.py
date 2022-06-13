filename = input("ENTER FILE NAME :- ")

with open(filename) as f:

    list = f.read().splitlines()

    print("LIST :- " ,list)

    f.close()


















