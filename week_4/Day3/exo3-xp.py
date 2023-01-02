# exertcise 1
def ConvertListe(a):
    iterable = iter(a)
    dct_construit = dict(zip(iterable ,iterable))
    return dct_construit
l1 = ['Ten', 'Twenty', 'Thirty']
l2 = [10, 20, 30]
l1.insert(1,l2[0])
l1.insert(3,l2[1])
l1.insert(5,l2[2])
print(ConvertListe(l1))

# exercice 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
PrixParMembre = 0
CoutTotalFilm = 0
for NomMembre, AgeMembre in family.items():
    if AgeMembre < 3:
        print(f"{NomMembre} paie 0 $")
        PrixParMembre = PrixParMembre + 0
    elif 3<AgeMembre<=12:
        print(f"{NomMembre} paie 10 $")
        PrixParMembre = PrixParMembre + 10
    else:
        print(f"{NomMembre} paie 15 $")
        PrixParMembre = PrixParMembre + 15
print(f"CoutTotalFilm = {CoutTotalFilm+PrixParMembre}")
family = {}
choix = "suivant"
while choix == "suivant":
    Nom = input("quel est ton nom:")
    Age = int(input("quel est ton age:"))
    family[Nom]=Age
    choix = input("entrer suivant pour continuer et top pour arreter:")   
print(family)

# exercise 3
brand = {"name": "Zara", 
"creation_date": 1975, 
'creator_name': "Amancio Ortega Gaona",
"type_of_clothes": "men, women, children, home", 
"international_competitors": "Gap, H&M, Benetton", 
"number_stores": 7000,
"major_color":{"France": "blue", "Spain": "red", "US": "pink, green"} }
brand["number_stores"]=2
client = (brand["type_of_clothes"])
print(f"{client} sont les clients de zara")
brand["country_creation"]="Spain"
print(brand["international_competitors"])
brand["international_competitors"] = "Gap, H&M, Benetton, Desigual"
brand.pop("creation_date")
concurent = brand["international_competitors"]
l=(list(concurent.split()))
print(f"le dernier concurent est le magasin {l[-1]}")
coul_usa = (brand["major_color"]["US"])
print(f"les principales couleurs de vêtements aus États-Unis sont {coul_usa}")
print(f"la longueur du dictionnaire est {len(brand)}")
print(brand.keys())
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print(brand["number_stores"])

# exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
'''1 >>> print(disney_users_A)
  {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
ce resultat est un dictionnaire dont les keys sont les valeurs de users et dont chaque
keys a pour valeur son idex dans la liste users
2 >>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
un dictionnaire dont chaque valeur a pour key l'index qui l'indique dans la liste users
3 >>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
un dictionnaire qui a pour keys les valeurs de la liste users dont chaque key contient comme valeur son index l'indiquant dans la liste users ou l'index d'un autre element dans la liste'''
i = 0
disney_users_A = {}
disney_users_B = {}
disney_users_C = {}
for elem in users:
    disney_users_A[elem]=i
    i = i+1
print(disney_users_A)
j = 0
for value in users:
    disney_users_B[j]=value
    j = j+1
print(disney_users_B)
users.sort()
k = 0
for element in users:
    disney_users_C[element]=k
    k = k+1
print(disney_users_C)
v = 0
t = 0
while v < len(users):
    q = users[v]
    v =v+1
while t < len(q):
    if q(t)!= "i":
        users.remove(q)

    
