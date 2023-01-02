# defi 1
nombre = int(input("entrer un nombre:"))
longueur = int(input("entrer un longueur"))
print(list(range(nombre,nombre*longueur+1,nombre)))

# defi 2
chaine = input("entrer une chaine:")
i = 0
j = 1
while i < len(chaine)-1:
       if chaine[i] == chaine[j]:
         chaine= chaine.replace(chaine[i]+chaine[j],chaine[j])
       j = j+1
       i = i+1
print(chaine)

