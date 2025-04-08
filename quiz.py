'''Gabbe och Daniela'''

import tkinter as tk
from tkinter import messagebox

fragor = { }
score = { }


def quiz(): 
    poäng = 0 
    nick = input ("\nSkriv in ditt nickname: ") 
    while nick in score.keys(): 
        nick = input ("Nickname finns redan, välj en ny: ") 
        
   
    for fraga, korrekt_svar in fragor.items(): 
        print(f"Fråga: {fraga}") 
        svar = input ("Ditt svar: ") 

        if svar.lower().strip() == korrekt_svar.lower().strip(): 
            print("rätt")                     
            poäng += 1  
            
        else: 
            print("fel")  
    
    score[nick] = poäng 
    print(f"\n{nick} du fick {poäng} poäng.\n") 


def visaScore():
    text = ""
    for nick, poäng in score.items(): 
        text += f"{nick} {poäng} poäng\n" 
    return text

def showPOP():
    poäng = visaScore()
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo("Scores:", poäng)
    root.quit()


def visaFragor():
    if fragor: 
        for fråga in fragor.keys(): 
            print(f"Fråga: {fråga}") 
    else:
        print("Finns inga frågor.")
        
        

def visaFragorSvar():
    if fragor:
        for fråga, svar in fragor.items():
            print(f"Fråga: {fråga}\t svar: {svar}") 
    else:
        print("Finns inga frågor.")

def laggTill():
    while True: 
        fråga = input("\nSkriv in din fråga: ") 
        svar = input("Skriv in ditt svar: ") 
        fragor[fråga] = svar  

        print("Din fråga har lagts till.\n")

        print("Vill du lägga till fler frågor?")
        while True:
            try:
                val = int(input("1.Ja/2.Nej "))  
                if val == 1:  
                    break 
                elif val == 2: 
                    return   
                else: 
                    (print("Välj 1 eller 2."))
            except ValueError: 
                print("Du måste skriva in en siffra.")

    
    

class main():
    while True:
        print("\nMeny")
        print("1. Starta Quiz") 
        print("2. Se scores")
        print("3. Lägg till fråga")
        print("4. Visa frågor")
        print("5. Visa frågor och svar")
        print("6. Avsluta")

        try:
            val = int(input("Skriv in ditt val: "))
            if val == 1:
                quiz()
                    
            elif val == 2:
                showPOP()
                                   
            elif val == 3:
                laggTill()
                print("Din fråga har lagts till.\n")

            elif val ==4:
                visaFragor()

            elif val==5:
                visaFragorSvar()
                            
            elif val ==6:
                print("\nQuiz avslutad")
                break    
            else:
                print("Alternativ finns inte. Gör ett val mellan 1-6.")
        except ValueError:
            print("\nDu måste skriva in en siffra. Gör ett val mellan 1-6.")

        except Exception as e:
            print(f"okänt fel: {e}")

main()

