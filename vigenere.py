def chiffrement(mdp : str, liste : list) -> str:
    mot_de_passe_cryptée=""
    i = 0
    cle = 0
    while i != len(mdp):
        o = 0
        emplacement_lettre = liste.index(mdp[i])
        cle = emplacement_lettre
        while o != cle:
            if emplacement_lettre == liste.index(liste[-1]):
                emplacement_lettre = liste.index(liste[0])
            else:
                emplacement_lettre = emplacement_lettre + 1
            o = o + 1

        mot_de_passe_cryptée = mot_de_passe_cryptée + liste[emplacement_lettre]
        i = i + 1
    return mot_de_passe_cryptée


mot_de_passe = input("entrez votre mot de_passe\n") 
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(chiffrement(mot_de_passe, liste))