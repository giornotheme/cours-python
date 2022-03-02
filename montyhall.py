import random

def initialize_box(list_box : list[bool]) -> tuple:
    random_num = random.randint(0,2)
    i = 0
    while(i<len(list_box)):
        if i == random_num:
            list_box[i] = True
        else:
            list_box[i] = False
        i = i+1
    return list_box

def win_or_lose(condition : bool) -> bool:
    if condition == True:
        return True
    else:
        return False

box1 = bool
box2 = bool
box3 = bool
choix = True

list_box = [box1, box2, box3]

list_box_initialized = initialize_box(list_box)
print(list_box_initialized)

input_user = int(input("Quel box vous choississez\n\n"))

i=0
while(i<len(list_box_initialized)):
    if i != input_user and list_box_initialized[i] == False:
        print("la boite numéro :" , i , "est vide. Souhaitez-vous changer votre choix ? [Y/N] \n")
        break
    else:
        i = i+1

second_input_user = input()
while choix == True:
    if second_input_user == "Y":
        new_user_choice = int(input("Quel numéro de boîte voulez-vous choisir ?"))
        if new_user_choice == input_user:
            print("Veuillez choisir une boîte différente")
        elif(new_user_choice == 0 or new_user_choice == 1 or new_user_choice == 2):
            choix = False
            if list_box_initialized[new_user_choice] == True:
                print("Félicitations vous avez réussi")
            else:
                print("Dommage ! Une autre fois")
        else:
            print("Veuillez entrer un chiffre entre 0, 1 ou 2")
    elif second_input_user == "N":
        choix = False
        if list_box_initialized[input_user] == True:
            print("Félicitations vous avez réussi")
        else:
            print("Dommage ! Une autre fois")
    else:
        print("Veuillez écrire Y pour changer votre choix, ou N pour garder votre choix")

