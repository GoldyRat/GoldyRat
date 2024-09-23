# Ecrire une fonction qui prend en entrée une liste d'entiers
# et qui renvoie une liste de même longueur qui contient
# True ou False selon que l'entier testé est pair ou impair.
# Exemple: [2, 3, 6, 18] la fonction renvoie [True, False, True, True] 

def is_even (n):
    return n % 2 == 0

def integers_to_booleans (v):
    w = []
    for n in v:
        if is_even (n): #si n est pair:
            w.append (True)
        else:  #sinon:
            w.append (False)
    return w

assert integers_to_booleans ([2, 3, 6, 18]) == [True, False, True, True]

# Ecrire une fonction qui renvoie la liste des N premiers
# entiers multiples de n.
# Exemple: si N = 17 et n = 3, la fonction renvoie
#          il y a 5 multiples de 3 entre 0 et 17


# Ecrire un programme python qui prend en entrées deux listes d'entiers
# v1 et v2, et qui compte, pour chaque élément de v1, le nombre de multiples
# présents dans la liste v2.
# Exemple: pour v1 = [3, 5, 2] et v2 = [18, 12, 35] la fonction renvoie
# La valeur 3 possède 2 multiples
# La valeur 5 possède 1 multiple
# La valeur 2 possède 2 

def is_multiple (d, m):
    return m % d == 0

def count_multiples_in_liste (n, v):
    cpt = 0
    for e in v:
        if is_multiple (n, e):  # si e est un multiple de n:
            cpt = cpt + 1  # cpt += 1   cpt -= 3 veut dire cpt = cpt - 3
    return cpt

def count_multiples (v1, v2):
    mults = []
    for n in v1:  # pour chaque elmt de V1:
         m = count_multiples_in_liste (n, v2) #compter le nombre de multiples dans v2
         mults.append (m)  # ajouter dans mults
    return mults

def pretty_print (v1, v2):
    # for e in v1:
    #     texte = f"La valeur {e} possède {count_multiples_in_liste (e, v2)} multiples"
    #     print (texte)

    mults = count_multiples (v1, v2)
    print (mults)  
    for i in range (len (v1)):
        texte = f"La valeur {v1 [i]} possède {mults [i]} multiples"
        print (texte)


v1 = [3, 5, 2]
v2 = [18, 12, 35, 9, 56, 63]
pretty_print (v1, v2)
assert count_multiples ([3, 5, 2], [18, 12, 35, 9, 56, 63]) == [4, 1, 3]



# Ecrire un programme python qui prend en entrée un entier n,
# et renvoie la liste des diviseurs.

def get_dividers (n):
    dividers = []
    for i in range (n, 0, -1):
        if n % i == 0:
            dividers.append (i)
    return dividers

assert get_dividers (7) == [7, 1]
assert get_dividers (12) == [12, 6, 4, 3, 2, 1]
print ("\n\n" + str (get_dividers (12)))

# Ecrire un programme python qui prend en entrée 
# une chaine de caractères, et renvoie une chaine où 
# les caractères auront été inversés.
# Exemple : pour "rivière" la fonction renvoie "erèivir"

def reverse_chain (chain):
    reversed_chain = ""
    for c in chain:
        reversed_chain = c + reversed_chain
    return reversed_chain

print (reverse_chain ("rivière"))

assert reverse_chain ("rivière") == "erèivir"
assert reverse_chain ("blablabla pouki") == "ikuop albalbalb"

# Ecrire un programme python qui fait la somme des nombres entiers
# pairs qui sont inférieurs à un certain nombre entier n donné.
# vous prendrez soin de vous appuyer sur des fonctions secondaires et
# d'afficher un texte pour présenter le résultat.

def make_sum_of_lower_evens (n):
    # version avec la boucle FOR
    # sum_of_lower_evens = 0
    # for i in range (0, n + 1, 2):
    #     sum_of_lower_evens = sum_of_lower_evens + i
    # return sum_of_lower_evens

    # Version "Pythonnerie"
    # return sum (list (range (0, n + 1, 2)))

    # Version avec la boucle WHILE
    sum_of_lower_evens = 0
    while n >= 0:
        if n % 2 == 0:
            sum_of_lower_evens += n
        n -= 1   # n = n - 2
    return sum_of_lower_evens


assert make_sum_of_lower_evens (7) == 12
assert make_sum_of_lower_evens (8) == 20

n = 8
print (f"\n Sum of evens for {n} est: {make_sum_of_lower_evens (n)}")

# Ecrire une fonction python qui prend en arguments une liste de nom valeurs
# un entier de nom n. La fonction doit renvoyer le couple formé de la liste comprenant
# les n premiers éléments de valeurs (situés à gauche) et de la liste comprenant
# les éléments restants (situés à droite).
