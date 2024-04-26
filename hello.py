f=open("example.txt","r")
# f.write("Panda \nChilaka \nVannurSwamy Chekalaguriki \nSarvani VannurSwamy \nnviefnve neinveib nvwijgor nvvo2rgn \niowrhf2iorhg vnrirgjrijwrogj fjggjgnfk \niwrrjgorigjoirg figjgnbn nfirjfi")
for line in f:
    word=line.split()
    print(str(word))
f.close()