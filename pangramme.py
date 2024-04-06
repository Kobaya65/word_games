import string


phrases = [
    "Le vif zéphyr jubile sur les kumquats du clown gracieux.",
    "Portez ce whisky au vieux juge blond qui fume.",
    "Monsieur Jack, nous dactylographions bien mieux que notre ami Wolf.",
    # chaîne initiale, modifiée pour qu'il manque deux lettres
    # "Monsieur Jack, vous dactylographiez bien mieux que votre ami Wolf.",
    "Voulez-vous que je m’y mette, tout le week-end, à construire une phrase comportant les vingt-six lettres de l’alphabet français ?",
    "J’aime l’idée selon laquelle ce putain de chef des gangs de sex symbols new-yorkais n’était qu’un chien au foyer de Brazzaville.",
]


def building_sentence_dict(phrase):
    """Create a dictionary of all letters in phrase.
    - phrase : sentence to be analysed
    Return a dictionary of all letters in phrase."""
    dict_lettres = dict()
    for x in phrase:
        if x.lower() in string.ascii_lowercase:
            if dict_lettres.get(x.lower()):
                dict_lettres[x.lower()] += 1
            else:
                dict_lettres[x.lower()] = 1
    return dict_lettres


def pangramme():
    '''A pangram is a sentence with all the letters of the alphabet.
    '''
    for phrase in phrases:
        dict_lettres = building_sentence_dict(phrase)

        dict_lettres = sorted(dict_lettres.items(), key=lambda item: item[0])
        print(f'{phrase}')
        erreurs = ''
        for x in string.ascii_lowercase:
            erreur_flag = True
            for idx in dict_lettres:
                if idx[0] == x:
                    erreur_flag = False
                    break
                    
            if erreur_flag:
                erreurs += f'{x}, '

        if len(erreurs):
            print(f'-->  Lettres manquantes : {erreurs[:-2]}')

if __name__ == '__main__':
    pangramme()
    