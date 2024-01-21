import random

print("Privet, dobro pozhalovat v igru kamen, nozhnitsi, bumaga!")
skolkoraz = int(input("Skolko raz ti hochesh sigrat'?\n"))

user_total_score = 0
rand_total_score = 0

for _ in range(skolkoraz):
    tvoibal = 0
    compbal = 0

    while True:
        try:
            vibor = input("Viberi chislo '1-kamen' '2-nozhnitsi' '3-bumaga'\n")
            list_play = ['1', '2', '3']
            if vibor in list_play:
                break
            else:
                print("Napishi chislo 1, 2 ili 3")
        except ValueError:
            print("Ne slovo, a chislo")

    for _ in range(1): 
        rand = random.choice(list_play)
        print(rand)
        if rand == '1' and vibor == '2':
            compbal += 1
        elif rand == '1' and vibor == '3':
            tvoibal += 1
        elif rand == '2' and vibor == '1':
            tvoibal += 1
        elif rand == '2' and vibor == '3':
            compbal += 1
        elif rand == '3' and vibor == '2':
            tvoibal += 1
        elif rand == '3' and vibor == '1':
            compbal += 1

    user_total_score += tvoibal
    rand_total_score += compbal

    if tvoibal > compbal:
        print("Pobeda!")
    elif tvoibal < compbal:
        print("Porazhenie!")
    else:
        print("Nichia!")

print(f"Obshi schet: Tvoi - {user_total_score}, Kompyutera - {rand_total_score}")

       
        
        
        


        

      

        
