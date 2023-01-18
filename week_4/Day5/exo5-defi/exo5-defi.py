def sequence(mots = "without,hello,bag,world"):
    new_mots = mots.split(',')
    new_mots.sort()
    p = new_mots[0]
    i = 1
    while i < len(new_mots):
        p = p + "," + new_mots[i]
        i += 1
    print(p)
sequence()
sequence("thomas,marcel,prisca,siméon,moussa")