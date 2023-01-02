mot = input("entre un mot:")
dic_mot = {}
i = 0
j = 1
while j < len(mot):
    if mot[i]==mot[j]:
        dic_mot[mot[i]] = [i,j]
    else:
        dic_mot[mot[i]] = [i]
    j = j+1
print(dic_mot)