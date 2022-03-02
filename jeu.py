#Création des deux dict "guerrier" et "archer"
guerrier = {
    "nom" : "guerrier",
    "lvl" : 60,
    "hp" : 2000,
    "damage" : 300,
    "mana" : 1500
}

archer = {
    "nom" : "archer",
    "lvl" : 60,
    "hp" : 1400,
    "damage" : 650,
    "mana" : 700
}

#On crée les fonctions grâce à "def"
def regeneration(hp_guerrier, lvl_guerrier): #ici la fonction possède deux paramètres : hp_guerrier et lvl_guerrier
    if lvl_guerrier>50 and hp_guerrier < 500: #Pour pouvoir utiliser la fonction regeneration, on regarde si le lvl du guerrier est > 50 et si les hp du guerrier sont < 50
        guerrier["hp"] = hp_guerrier + 2000 #Si c'est le cas, la valeur de la clé "hp" du dictionnaire "guerrier" est égale à la valeur du paramètre "hp_guerrier" + 2000
        print("\nLe guerrier se régénère ! Il a maintenant", guerrier["hp"], "hp")
    elif lvl_guerrier>50 and hp_guerrier > 500: #Sinon si le lvl du guerrier est > 50 mais que les hp du guerrier sont > 500
        print("\nVous avez encore trop d'hp pour utiliser la régénération") #alors on dit à l'utilisateur que les hp du guerrier sont trop élevés
    else:
        print("\nVous n'avez pas encore le lvl suffisant pour utiliser la régénération")#Sinon on dit que le lvl du guerrier n'est pas suffisant

def attaque(nom): #Cette fonction permet à nos "guerrier" et "archer" d'attaquer. Cette fonction possède un paramètre : nom
    #Il faut bien faire la différence entre qui attaque : le guerrier ou l'archer ?
    if nom == "guerrier": #Pour dire que c'est le guerrier qui attaque, on vérifie si le paramètre "nom" de cette fonction a pour valeur "guerrier"
        return(300) #Si c'est le cas, on retourne la valeur 300 qui correspond aux dégâts que notre guerrier fera
    elif nom == "archer": #De la même manière, pour dire que c'est l'archer qui attaque, on vérifie si la valeur est "archer"
        return(650) #Si c'est le cas, on retourne la valeur 650 qui correspond aux dégâts que notre archer fera
    else: #On oublie pas de vérifier tous les autres cas avec un "else:" qui englobe toutes les autres possibilités
        return("Classe indéfinie") #Vu que pour l'instant on a que "archer" et "guerrier", si le "nom" a une autre valeur que "archer" ou "guerrier" c'est qu'on s'est trompé

#Maintenant qu'on a mis en place les fonctions et les dictionnaires, on peut s'attaquer au programme

compteur = 1 #Cette variable "compteur" me permet de faire un menu pour que l'utilisateur puisse intéragir avec le programme. 
while compteur == 1: #On dit que tant que ce compteur a pour valeur 1 (ce qui est le cas), on continue d'éxécuter le code suivant 
    print("\n1. Utiliser la compétence d'attaque de l'archer\n2. Utiliser la compétence régénération du guerrier\n3. Quitter le jeu\n") #on print notre menu
    action_user = input("Quelle action vous souhaitez faire \n") #Ici on demande à l'utilisateur quelle action il veut faire

    if action_user == "1": #Si l'utilisateur écrit 1, il veut donc faire l'action suivante : "Utiliser la compétence d'attaque de l'archer"
        guerrier["hp"] = guerrier["hp"] - attaque("archer") #attaque("archer") retourne la valeur 650 donc cette ligne est l'équivalent de "guerrier["hp"] = guerrier["hp"] - 650"
        #Vu que les hp de notre guerrier s'est affaiblit, on doit vérifier si notre guerrier a encore des hp
        if guerrier["hp"] < 0 : #Pour cela, on vérifie simplement si la valeur de la clé "hp" du dictionnaire "guerrier" est inférieur à 0
            print("\nLe guerrier a reçu un coup fatal, le combat s'arrête maintenant") #Si c'est le cas, ça veut dire que notre guerrier est mort
            compteur = 0 #Donc on peut arrêter la boucle while vu qu'il n'y a plus rien à faire. En mettant compteur = 0, on sort de la boucle while
        else: #Sinon ça veut dire que notre guerrier est encore vivant
            print("\nL'archer attaque le guerrier ! Cela enlève au guerrier 650 hp. Il lui reste donc :", guerrier["hp"]) #Donc on affiche ses hp restants

    elif action_user == "2": #Sinon si l'utilisateur écrit 2, il veut donc faire l'action suivante : Utiliser la compétence régénération du guerrier
        #Donc pour éxécuter cette fonction, il faut appeler la fonction en écrivant le nom de la fonction (dans notre cas : "regeneration")
        #Mais il faut aussi donner les paramètres de la fonction. On avait dit que pour que la régénération se lance, il fallait vérifier le lvl et les hp du guerrier
        regeneration(guerrier["hp"], guerrier["lvl"]) #Donc c'est ce qu'on fait, on donne en paramètre les hp et le lvl actuels du guerrier en paramètre
    elif action_user == "3": #Sinon si l'utilisateur écrit 3, on arrête le jeu
        print("\nFin du jeu")
        compteur = 0 #Pour arrêter le jeu, il faut donc sortir de la boucle while. Pour ce faire, on met le compteur à 0 vu que la boucle while est vraie tant que compteur = 1
    else: #Et enfin, on oublie jamais de prendre en compte toutes les autres possibilités avec un else qui englobe tout.
        print("Erreur, il n'y a que 3 choix possibles") #Si l'utilisateur écrit autre chose que 1, 2 ou 3 ça veut dire qu'il est un peu con.
