import string
import unidecode

class bcolors:
    # ANSI escape codes
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ERASE_SCREEN = '\033[2J'
    CURSOR_UP_15_LINES = '\033[15A'


def main():
    lettres_manquees = set()
    clean_terminal()
    mot = input("Entrez le mot à découvrir\n(les caractères accentués seront remplacés\npar leur caractère de base) : ")
    mot_decouvert = '_' * len(mot)
    # enlever les accents qui auraient été saisis
    mot_nettoye = unidecode.unidecode(mot)
    clean_terminal()
    print(f'Mot à découvrir : {mot_decouvert}')
    # nombre d'erreurs maximum
    nb_erreurs = 6
    tour = 0
    while mot_nettoye != mot_decouvert and nb_erreurs:
        lettre = input(f'Tour {tour + 1}. Entrez une lettre (pas de caractère accentué) : ').lower()
        tour += 1
        # on regarde si la lettre saisie fait partie de l'alphabet et des voyelles accentuées
        if not lettre in string.ascii_lowercase:
            print(f'{lettre} n\'est pas une lettre.')
        else:
            if lettre in lettres_manquees or lettre in mot_decouvert:
                print(f"Lettre '{lettre}' déjà proposée.")
                tour -= 1
            else:
                trouve = False
                for idx, l in enumerate(mot_nettoye):
                    if l == lettre:
                        trouve = True
                        # recomposer mot_decouvert
                        mot_decouvert = f'{mot_decouvert[:idx]}{lettre}{mot_decouvert[idx + 1:]}'

                if not trouve:
                    # si lettre non trouvé dans mot, on l'ajoute dans le set
                    lettres_manquees.add(lettre)
                    nb_erreurs -= 1

                clean_terminal()
                if lettres_manquees:
                    lettres_proposees = ''
                    # composer la liste des lettres manquées pour affichage
                    for l in lettres_manquees:
                        lettres_proposees += f'{l}, '
                    lettres_proposees = lettres_proposees[:-2]
                    print(f'Autres lettres proposées : {lettres_proposees}')
                    
                print(f'Mot à découvrir : {mot_decouvert}')

    if mot_nettoye == mot_decouvert:
        print(f'Bravo, vous avez gagné en {tour} coup{'s' if tour > 1 else ''} !')
    else:
        print('Vous avez perdu...')
        print(f'Votre essai : {mot_decouvert}.')
        print(f'Le mot à découvrir était : {mot_nettoye}.')


def clean_terminal():
    """ Vider le terminal
    """
    print(bcolors.ERASE_SCREEN)
    print(bcolors.CURSOR_UP_15_LINES)


if __name__ == '__main__':
    main()
