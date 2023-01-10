liste1 = [[7,"i",3],["T","s","i"],["h","%","x"],["i","","#"],["s","M",""],["$","a",""],["#","t","%"],["^","r","!"]]
mot = ""
for i in range(len(liste1)):
    if type(liste1[i][0]) == str:
        mot = mot + liste1[i][0]
for i in range(len(liste1)):
    if type(liste1[i][1]) == str:
        mot = mot + liste1[i][1]
for i in range(len(liste1)):
    if type(liste1[i][2]) == str:
        mot = mot + liste1[i][2]
new_mot = mot.replace("$#^"," ")
new_mot = new_mot.replace("%"," ")
new_mot = new_mot.replace("# !"," ")
print(new_mot)
