# Il est important de faire des commentairesS
# exercise 1
print("Hello word\nHello word\nHello word\nHello word")

# exercise 2
a= 99*99*99*8
print(a)

''' exercise 3
>>> 5 < 3
False
>>> 3 == 3
True
>>> 3 == "3"
False
>>> "3" > 3
False
>>> "Hello" == "hello"
False'''

# exercise 4
computer_brand = "HP"
print(f"I have a {computer_brand} computer")

# exercise 5
name = "SAWADOGO Thomas"
age  = "22 ans"
shoe_size = 41
info = f"moi {name} âgé de {age} et de pointure {shoe_size}, mon inspiration c'est devenir un super developper full stack"
print(info)

# exercise 6
a = float(input("entrer un nombre:"))
b = float(input("entrer un deuxieme nombre:"))
if a > b:
    print("Hello word")
elif a != b:
    print("rien à afficher")

# exercise 7
a = int(input("entrer un nombre:"))
if a%2 == 0:
    print(f"{a} est pair")
elif a%2 != 0:
    print(f"{a} est impair")

# exercise 8
MonNom = "SaWADOGO Thomas"
TonNom = input("entrer ton nom")
if TonNom == MonNom:
    print(f"{TonNom};tu seras developper full stack comme moi")
elif TonNom != MonNom:
    print(f"{TonNom};tu seras vigile")

# exercise 9
Taille = int(input(" entrer votre taille en pouces"))
Taille = Taille* 2.54
if Taille == 145:
    print(f"Avec ta taille de {Taille} cm, tu es prêt pour rouler")
elif Taille > 145:
    print(f"ta taille de {Taille} cm est assez grand pour rouler")
elif Taille < 145:
    print(f" Avec ta taille de {Taille} cm, tu dois grandir un peu plus pour rouler")
