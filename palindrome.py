
def est_palindrome(phrase: str) -> str:
    """Check if phrase is a palindrome.
    - phrase : sentence to test
    Return OK/NOK followed by the phrase, or a dedicated message if phrase < 2 characters
    """
    if len(phrase) < 2:
        res = f'\n{phrase} : entrer au minimum 2 lettres.\n'
    else:
        unwanted_letters = 'àâäéèêëìïîòôöóùûÀÄÂÃÈÉÊËÌÍÎÏÇçñùûü'
        replace_by = 'aaaeeeeiiioooouuaaaaeeeeiiiiccnuuu'
        exclude = " !.?,;:'-_+/¤*^¨¤~&#{[|`\\@}]°"
        # création d'un dictionnaire 
        my_dict = str.maketrans(unwanted_letters, replace_by, exclude)
        # modification des caractères non désirés et suppression des caractères à exclure
        phrase_nettoyee = phrase.translate(my_dict).lower()
        # on créé la phare renversée
        phrase_renverse = ''.join(reversed(phrase_nettoyee))

        if phrase_nettoyee == phrase_renverse:
            res = f"OK  {phrase}"
        else:
            res = f"NOK {phrase}"

    return res


# liste de palindromes
palindromes = [
    "Engage le jeu que je le gagne",
    "Oh ! cela te perd, répéta l'écho",
    "Ce satrape repart à sec",
    "Noir, ô hélas, Isis a le horion",
    "Émile nu a une lime",
    "Eh, ce lac né en calèche",
    "Etc... art tracté",
    "Lieur à Rueil",
    "Rions noir",
    "z",
    "Tu l'as trop été, Port-salut",
    "Un soleil du sud lie l'os nu",
    "Tu l'as trop écrasé César ce Port-Salut",
    "Ésope reste ici et se repose",
    "Éric notre valet alla te laver ton ciré",
    "Léon a sucé ses écus à Noël",
    "Élu par cette crapule",
    "Léon, émir cornu, d'un roc rime Noël",
    "L'âme soeur, elle, rue, ose mal",
    "Et si l'arôme des bottes révèle madame, le verset t'obsède, moraliste",
    "Zozo",
    "Caserne, genre sac",
    "Élucide l'édicule",
    "Éros s'essore",
    "Et curé gorgé de grog éructe",
    "Rose utérus, à ma masure, tu es or",
    "Nue, j'aime demi à jeun",
    "Sa lèvre cervelas",
    "Sévère mal à l'âme, rêves",
    "Ta fesse n'a le désir irisé de l'ânesse, fat",
    "Un socialiste, et si laïc, os nu",
    "Un ému a son os au menu",
    "À Laval, elle l'avala",
    "Et Luc colporte trop l'occulte",
    "L'âme des uns n'use de mal",
    "Ce repère, Perec",
    "Ce reptile lit Perec",
    "Ce reptile relit Perec",
    "La mère Gide digère mal",
    "À l'étape, épate-la",
    "Eh ! ça va la vache",
    "Ève, leste lia l'ail et se lève",
    "L'âme sûre ruse mal",
    "L'ami naturel ? Le rut animal",
    "Lune de ma dame d'été, été de ma dame de nul",
    "Suce ses écus",
    "La mariée ira mal",
    "Et la marine va, papa, venir à Malte",
    "Et la marine va venir à Malte",
    "Noël à León",
    "Sa lèvre écervelée",
    "aa"
]

# trie des palidromes
palindromes_tries = sorted(palindromes)
print(str(palindromes_tries) + "\n\n")
# palindromes triés
for phrase in palindromes_tries:
    print(phrase)
print("\n")
# test des palindromes
for phrase in palindromes:
    print(est_palindrome(phrase))
