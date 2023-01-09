def display_message():
    print(f"j'apprends:\nles langages de balisage comme: html et css\nles langages de programmation comme:JavaScript et python")
display_message()

def favorite_book(title):
    a = f"One of my favorite books is {title}"
    print(a)
favorite_book("programmation")

def describe_city(city,country = "Burkina Faso"):
    describe = f"{city} is in {country}"
    print(describe)
describe_city("")

def generateur_nombre(n):
    import random
    valeur = random.randint(1,100)
    if n == valeur:
        print(f"{valeur} est bonne")
    else:
        print(f"{valeur} est mauvaise")   
    print(f"nombre_généré={valeur}\nnombre_entré={n}")
n = int(input("entrer un nombre compris entre 1 et 100:"))
if 1 < n <= 100:
    generateur_nombre(n)
else:
    print(f"{n} n'est pas entre 1 à 100")


def make_shirt(size="XXL",text="J'aime Python"):
    print(f"the size of the shirt is {size} and the text is {text}")
make_shirt()
make_shirt("L")
make_shirt("XL","J'aime coder")
make_shirt(size="XXL",text="J'aime Python")
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print(name)
show_magicians(magician_names )
p =[]
def make_great():
    for element in magician_names:
       element = ' '.join([element,'the great']) 
       p.append(element)
    print(p)
make_great()
show_magicians(p)

# exercise 7
def get_random_temp():
    import random
    n = random.randint(-10,40)
    return n
print(get_random_temp())
def main():
    temp = get_random_temp()
    print(f"la temperature actuelle est de {temp} degrés Celsius")
    if temp < 0:
        print(f"Brrr,c'est glacial! Poortez des couches supplémentaires aujourd'huit")
    elif 0 < temp < 16:
        print(f"Assez froid! N'oublie pas ton manteau")
    elif 16 < temp <= 23:
        print(f"légerement froid! portez vos souliers")
    elif 23 <= temp < 32:
        print(f"legerement chaud! portez vos vestes et vos souliers")
    elif 32 < temp <= 40:
        print(f"il fait chaud! Portez des t-shirt et des pantalons à tissus simple")
main() 
def get_random_temp(season):
    import random
    if season == "hiver":
        n = random.randint(-10,16)
    elif season == "printemps":
        n = random.randint(17,23)
    elif season == "automne":
        n = random.randint(24,32)
    elif season == "été":
        n = random.randint(33,40)
    return n
def main():
    season = input("taper une saison: soit hiver,soit été,soit printemps,soit automne: \n")
    print(f"la temperature de la saison {season} est {get_random_temp(season)} degrés celsius")
main()
def get_random_temp(season):
    import random
    if season == "hiver":
        n = random.uniform(-10,16)
    elif season == "printemps":
        n = random.uniform(17,23)
    elif season == "automne":
        n = random.uniform(24,32)
    elif season == "été":
        n = random.uniform(33,40)
    return n
def main():
    season = input("taper une saison: soit hiver,soit été,soit printemps,soit automne: \n")
    print(f"la temperature de la saison {season} est de {get_random_temp(season)} degrés celsius")
main()
#liste_mois = {1:"Janvier",2:"Fevrier",3:"Mars",4:"Avril",5:"Mai",6:"juin",7:"Juillet",8:"Août",9:"Septembre",10:"Octobre",11:"Novembre",12:"Décembre"}
def get_random_temp(mois):
    if mois == 1 or mois == 2 or mois == 12:
        print("nous sommes en periode d'hiver")
    elif mois == 3 or mois == 4 or mois == 5:
        print("nous somme en periode de printemps")
    elif mois == 6 or mois == 7 or mois == 8:
        print("nous somme en periode de l'été")
    elif mois == 9 or mois == 10 or mois == 11:
        print("nous somme en periode de l'automne")
def main():
    mois = int(input("donner un entier compris entre 1 à 12: \n"))
    if 1<mois<=12:
        get_random_temp(mois)
    else:
        print(" la saison est indéterminée")
main()