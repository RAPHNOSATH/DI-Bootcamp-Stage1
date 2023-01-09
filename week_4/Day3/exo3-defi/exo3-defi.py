import re
mot = input("entrer un mot:")
dic_mot = {}
form = re.compile("[a-zA-Z]",re.IGNORECASE)
m = form.match(mot)
if m:
    for caract in mot:
        p = []
        t =0
        while t<len(mot):
            if caract == mot[t]:
                p.append(t)
        t+=1
    dic_mot.update({caract:p})
    print(dic_mot)
else:
    print("le format de mot n'est pas respecté")

items_purchase = {
  "Water": 600,
  "Bread": 350,
  "TV": 1000,
  "Fertilizer": 2000,
  "Apple": 400,
  "Honey": 350,
  "Fan": 125,
  "Bananas": 4000,
  "Pan": 100,
  "Spoon": 265.78,
  "Phone": 999,
  "Speakers": 300,
  "Laptop": 5000,
  "PC": 1200
}
p = []
wallet = float(input("donner la somme se trouvant dans votre portefeuille:"))
for produit in items_purchase.items():
    if produit[1] < wallet:
        p.append(produit[0])
p.sort()
print(p)