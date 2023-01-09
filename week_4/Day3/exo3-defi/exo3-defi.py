mot = input("entrer un mot:")
dic_mot = {}
for caract in mot:
    if mot.count(caract) == 1:
        dic_mot[caract]=[mot.index(caract)]
    else:
        dic_mot[caract]=[mot.index(caract)]
print(dic_mot)
