import random

#Fonction pour initialiser quels box vont être false et quel box va être true
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

#Fonction pour lancer la partie
def jouer(number_of_play : int):
    box1 = bool
    box2 = bool
    box3 = bool
    win_count = 0
    lose_count = 0
    i=0
    IA_behavior = input("1. IA change tout le temps de choix\n2. IA ne change jamais de choix\n")

    if IA_behavior == "1":
        while(i < number_of_play):
            list_box = [box1, box2, box3]
            list_box_initialized = initialize_box(list_box) #Initialisation de notre liste de box
            choices = [0, 1, 2] #Création d'une liste où l'IA va piocher son choix
            IA_choice = random.choice(choices)
            choices.remove(IA_choice)
            IA_choice_wrong_box = random.choice(choices)

            while list_box_initialized[IA_choice_wrong_box] == True:
                IA_choice_wrong_box = random.choice(choices)
            choices.remove(IA_choice_wrong_box)

            new_IA_choice = random.choice(choices)

            if list_box_initialized[new_IA_choice] == True:
                win_count = win_count + 1
            else:
                lose_count = lose_count + 1
            
            i = i + 1

        print("Nombre de parties jouées :", number_of_play)
        print("Nombre de parties gagnées :", win_count)
        print("Nombre de parties perdues :", lose_count)

        print("Pourcentage victoire :", round((win_count/number_of_play)*100),"%")
        print("Pourcentage défaite :", round((lose_count/number_of_play)*100),"%")

    elif IA_behavior == "2":
        while(i < number_of_play):
            list_box = [box1, box2, box3]
            list_box_initialized = initialize_box(list_box)
            IA_choice = random.randint(0,2)

            if list_box_initialized[IA_choice] == True:
                win_count = win_count + 1
            else:
                lose_count = lose_count + 1
            
            i = i + 1

        print("Nombre de parties jouées :", number_of_play)
        print("Nombre de parties gagnées :", win_count)
        print("Nombre de parties perdues :", lose_count)

        print("Pourcentage victoire :", round((win_count/number_of_play)*100),"%")
        print("Pourcentage défaite :", round((lose_count/number_of_play)*100),"%")


number_of_play = int(input("cb de parties ? "))
jouer(number_of_play)