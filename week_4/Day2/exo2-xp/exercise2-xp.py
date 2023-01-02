# exercise 1
my_fav_numbers = {77655841,62354292,64161307}
my_fav_numbers.add(60501209)
my_fav_numbers.add(66496261)
my_fav_numbers.remove(64161307)
friend_fav_numbers = {66813432,71931772,62848622}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

'''exercicse 2
 on ne peut pas modifier un tuple existant donc on ne peut pas ajouter des elements'''
# exercise 3
fruit = ["Banana","Apples","Oranges","Blueberries"]
fruit.remove("Banana")
fruit.pop(2)
fruit.append("Kiwi")
fruit.insert(0,"Apples")
a = fruit.count("Apples")
print(a)
fruit.clear()
print(fruit)

'''exercice 4
1-un float est un type de donnée en python qui represente les nombres decimales
la difference: une variable flottant accepte les entiers et qui les affiche sous forme de flottant
or les variables entiers n'acceptent pas les nombres flottants
2-oui en convertissant une sequence d'entier en float'''
liste = [1.5,2,2.5,3,3.5,4,4.5,5]

# exercise 5
for i in range(1,21):
    print(i)
a = list(range(1,21))
for i in a:
    if i%2==0 and i< len(a):
        print(a[i])
# exercise 6
MonNom = "SAWADOGO"
NomUtilisateur = input("entrer votre nom:")
while NomUtilisateur!=MonNom:
    NomUtilisateur = input("entrer votre nom:")
# EXERCISE 7
fruit = input("entrer votre ou vos fruits préféré(s):")
ListeFruit = ((fruit.split()))
NomFruit = input("entrer un nom de n'importe quel fruit:")
i = 0
while i<len(ListeFruit):
    one_fruit = ListeFruit[i]
    i = i+1
if one_fruit==NomFruit:
    print("Vous avez choisi l'un de vos fruits préférés! Profitez-en!")
elif one_fruit!=NomFruit:
    print("Vous avez choisi un nouveau fruit. J'espère que vous appréciez!")
 
# EXERCISE 8
ListeGarniture = []
choix = "quitter"
p = ""
while p!= choix:
    NomGarniture = input("enter une garniture de pizza:")
    print(f"{NomGarniture}:j'ajoute cette garniture à votre pizza")
    ListeGarniture.append(NomGarniture)
    p = input("entrer quitter pour arreter et ajouter pour ajouter de garniture:")
print(ListeGarniture)
PrixUnitaireGarniture = 10+2.5
PrixTotalGarniture = PrixUnitaireGarniture*len(ListeGarniture)
print(PrixTotalGarniture)

# EXERCISE 9
PrixMoins3Ans = 0
Prix3_12Ans = 0
PrixPlus12Ans = 0
i = 0
NombrePersonne = int(input("entrer le nombre de personne voulant un billet dans la famille:"))
while i < NombrePersonne:
    AgePersonne = int(input("quel est ton age:"))
    if AgePersonne < 3:
        PrixMoins3Ans = PrixMoins3Ans+ 0
    elif 3<AgePersonne<=12:
        Prix3_12Ans = Prix3_12Ans + 10
    else:
        PrixPlus12Ans = PrixPlus12Ans + 15
    i = i+1
PrixTotalBillet = Prix3_12Ans + PrixPlus12Ans
print(f" le prix total des billets est {PrixTotalBillet} $")
ListeAdolescent = ["thomas","pierre","seyni","simeon","clement","prisca","marcel"]
i = 0
while i < len(ListeAdolescent):
    AgeAdolescent = int(input(f"{ListeAdolescent[i]}, quel est ton age?:"))
    if 21<=AgeAdolescent<16:
        del ListeAdolescent[i]
    i = i+1
print(ListeAdolescent)

# exercise 10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
for sandwich_finis in finished_sandwiches:
    print(f"I made your {sandwich_finis}")

# exercise 11
sandwich_orders.append(("Pastrami sandwich"))
sandwich_orders.append(("Pastrami sandwich"))
print("la charcuterie est à cours de pastrami")
i = len(sandwich_orders)-3
while i < len(sandwich_orders):
    sandwich_orders.pop(i)
print(sandwich_orders)
finished_sandwiches.pop(-1)
print(finished_sandwiches)





