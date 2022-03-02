def add_user(nom, prenom, tel): #fonction pour ajouter des utilisateurs
    person = {
        "nom" : nom,
        "prenom" : prenom,
        "tel" : tel
    }
    return person

def export_agenda(agenda): #fonction pour retourner l'agenda
    return agenda

def import_agenda(agenda, imported_agenda): #fonction pour importer un agenda
    agenda = imported_agenda
    return agenda

agenda = [] # au début on initialise une liste vide (cette liste est notre agenda)
compteur = 1

while(compteur == 1): #menu
    action_user = input("\n1. Importer un annuaire\n2. Chercher un utilisateur et afficher ses informations\n3. Ajouter un utilisateur\n4. Exporter l'annuaire\n0. Quitter\n")
    match action_user:
        case "1":
            #création deux personnes en tant qu'exemple pour l'import
            example_person={
                "nom" : "Dupont",
                "prenom" : "Jean",
                "tel" : 123456789
            }
            example_person2={
                "nom" : "Dupont",
                "prenom" : "Jeanne",
                "tel" : 987654321
            }
            example_agenda = [example_person, example_person2]#création d'une variable qui est un exemple d'agenda à importer
            agenda = import_agenda(agenda, example_agenda)
            print(agenda)

        case "2":
            compteur2 = 1
            while compteur2 == 1:#menu
                action_user2 = input("\n1. Chercher par nom\n2. Chercher par prénom\n3. Chercher par téléphone\n0. Annuler\n")
                match action_user2:
                    case "1":#recherche par nom
                        nom = input("\nNom de la personne\n")
                        i = 0
                        if i == len(agenda):#vérification de l'agenda si il est vide
                            print("L'agenda est vide. Veuillez enregistrer des personnes dans l'agenda")
                        else:
                            while i<len(agenda):
                                actual_person = agenda[i]
                                if actual_person["nom"] == nom:
                                    print("Nom : ", actual_person["nom"], "\nPrénom :", actual_person["prenom"], "\nTéléphone :", actual_person["tel"])
                                    i = i+1
                                else:
                                    i = i+1
                    case "2":#recherche par prénom
                        prenom = input("\nPrénom de la personne\n")
                        i = 0
                        if i == len(agenda):
                            print("L'agenda est vide. Veuillez enregistrer des personnes dans l'agenda")
                        else:
                            while i<len(agenda):
                                actual_person = agenda[i]
                                if actual_person["prenom"] == prenom:
                                    print("Nom : ", actual_person["nom"], "\nPrénom :", actual_person["prenom"], "\nTéléphone :", actual_person["tel"])
                                    i = i+1
                                else:
                                    print(prenom, "n'est pas répertorié dans l'agenda")
                                    i = i+1
                    case "3":#recherche par tel
                        tel = input("\nTéléphone de la personne\n")
                        i = 0
                        if i == len(agenda):
                            print("L'agenda est vide. Veuillez enregistrer des personnes dans l'agenda")
                        else:
                            while i<len(agenda):
                                actual_person = agenda[i]
                                if actual_person["tel"] == tel:
                                    print("Nom : ", actual_person["nom"], "\nPrénom :", actual_person["prenom"], "\nTéléphone :", actual_person["tel"])
                                    i = i+1
                                else:
                                    print(tel, "n'est pas répertorié dans l'agenda")
                                    i = i+1
                    case "0":
                        compteur2 = 0

        case "3":
            #variables pour l'ajout d'une nouvelle personne
            nom = input("\nNom de la personne\n")
            prenom =input("\nPrénom de la personne\n")
            tel =input("\nTéléphone de la personne\n")

            check_if_user_already_exist = False #variable boolean qui permet de savoir si la personne existe déjà dans l'agenda
            i = 0
            while(i<len(agenda)):
                actual_person = agenda[i]
                if actual_person["nom"] == nom and actual_person["prenom"] == prenom and actual_person["tel"] == tel:
                    check_if_user_already_exist = True #si la personna existe, on met le bool à true
                    compteur3 = 1
                    while(compteur3 == 1):
                        action_user3 = input("Cette personne existe déjà dans votre agenda. Souhaitez vous changez son numéro de téléphone ? [Y/N]\n")
                        if action_user3 == "Y":
                            new_tel = input("Saisissez le nouveau numéro de téléphone\n")
                            actual_person["tel"] = new_tel
                            break
                        elif action_user3 == "N":
                            print("Les données n'ont pas été modifiées")
                            break
                        else:
                            print("Saisie incorrecte.")
                    break
                else:
                    i = i+1

            if check_if_user_already_exist == False: #si on a trouvé personne identique dans l'agenda alors on ajouter la personne dans l'agenda
                new_person = add_user(nom, prenom, tel)
                agenda.append(new_person)
                print(agenda)
            
        case "4":
            print(export_agenda(agenda)) #on retourne l'agenda

        case "0":
            compteur=0
