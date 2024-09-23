# Ecrire une fonction qui prend en entrée une liste d'entiers
# et qui renvoie une liste de même longueur qui contient
# True ou False selon que l'entier testé est pair ou impair.
# Exemple: [2, 3, 6, 18] la fonction renvoie [True, False, True, True]
import main


print(main.liste([78,12,45,69,48,2,5631,75]))
# Ecrire une fonction q01ui renvoie la liste des N premiers
# entiers multiples de n, entre 1 et N.
# Exemple: si N = 17 et n = 3, la fonction renvoie
# il y a 5 multiples de 3 entre 0 et 17

def liste_multiples(N, n):
    multiples = 0
    l1 = []
    for i in range (1, N):
        if i % n == 0:
            multiples+=1
            l1.append(i)
    return f"Il y a {multiples} multiples de {n} entre 0 et {N}, qui sont {l1}"

print(liste_multiples(100, 4))

# Ecrire un programme python qui permet de compter et d'afficher
# le nombre d'éléments d'une liste d'entiers v, qui sont multiples
# Exemple: [3, 5, 2] et [18, 12, 35] la fonction renvoie
# La valeur 3 possède 2 multiples
# La valeur 5 possède 1 multiple
# La valeur 2 possède 2 multiples

const_v1 = [3, 5, 2]
const_v2 = [18, 12, 35, 9, 56, 63]

def is_multiple(m, n):
    return m % n == 0
def count_multiples_in_list(n, v):
    m = 0
    for e in v: 
        if is_multiple(e, n):
            m+=1
    return m


def count_multiples(v, v2):
    mults = []
    for n in v:
        m = count_multiples_in_list(n, v2)
        mults.append(m)
        
    return mults

def pretty_print(v1, v2):
    mults = count_multiples(v1, v2)
    for i in range(len(v1)):
        texte = f"La valeur {v1[i]} possède {mults[i]} multiples"
        print(texte)

pretty_print(const_v1, const_v2)
assert count_multiples(const_v1, const_v2) == [4, 1, 3]




# Ecrire un programme python qui prend en entrée un entier n,
# et renvoie la liste des diviseurs de n.
def is_divider(n, d):
    return n % d == 0

def dividers_list(n):
    div = []
    for i in range(n, 0, -1):
        if is_divider(n, i):
            div.append(i)
    return div

print(dividers_list(78 ))

# Ecrire un programme python qui prend en entrée
# une chaine de caractères, et renvoie une chaine où
# les caractères auront été inversés.
# Exemple : pour "rivière" la fonction renvoie "erèivir"

def invert(c):
    e = c[::-1]
    return e

def is_palindrome(c):
    if invert(c) == c:
        return True
    else:
        return False
    
print(invert("baobab"))
print(is_palindrome("baobab"))

# Ecrire un programme python qui fait la somme des nombres entiers
# pairs qui sont inférieurs à un certain nombre entier n donné.
# vous prendrez soin de vous appuyer sur des fonctions secondaires et
# d'afficher un texte pour présenter le résultat.

def sum_of_evens(n):
    s = 0
    for i in range(n):
        if main.is_even(i):
            s+=i
    return s

def cool_print(n):
    texte = f"La somme des entiers pairs inférieur à {n} est égale à {sum_of_evens(n)}"
    print(texte)

cool_print(110)

