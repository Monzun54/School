'''Gabbe och Micke'''

import random


ordlista = ["rasha", "programmering", "lektion", "tunnelbana", "spel", "hangman", "utveckling"]


ord = random.choice(ordlista)
ord_dolt = ["_"] * len(ord) 
                   

max_gissningar = 6
fel_gissningar = 0
gissade_bokstäver = [] 


def skriv_ut_ord():                                   
    print("Ord: " + " ".join(ord_dolt)) 
    print(f"Gissade bokstäver: {', '.join(gissade_bokstäver)}")
    print(f"Felaktiga gissningar: {fel_gissningar}/{max_gissningar}")


while fel_gissningar < max_gissningar:
    skriv_ut_ord()
    gissning = input("Gissa en bokstav: ")

    if gissning in gissade_bokstäver:
        print("Du har redan gissat den bokstaven!")
        continue
                                        
    if len(gissning) != 1 or not gissning.isalpha(): 
        print("Var god och gissa en bokstav!")
        continue

    gissade_bokstäver.append(gissning)

    if gissning in ord:      
        print(f"Bra gissning! {gissning} finns i ordet.") 
        for i in range(len(ord)):
            if ord[i] == gissning:
                ord_dolt[i] = gissning
    else:
        print(f"Tyvärr, {gissning} finns inte i ordet.")
        fel_gissningar += 1

    if "_" not in ord_dolt: # varje rätt gissning ersätter "_" med bokstäver. När alla "_" är borta printas texten
        skriv_ut_ord()
        print("Grattis! Du har gissat rätt ord!")
        break

if fel_gissningar == max_gissningar: 
    print(f"Spelet slut! Du har förlorat. Ordet var: {ord}")
    