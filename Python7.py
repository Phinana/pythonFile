def devir(matris):
    sutun=[]
    bitisMatris=[]
    i=0
    j=0
    while i < len(matris[0]):
       sutun=[]
       j=0
       while j < len(matris):
            sutun.append(matris[j][i])
            j = j+1
       bitisMatris.append(sutun)
       i=i+1
    return bitisMatris

baslangicMatris = [[2, 6, 5],[5, 6,8],[769, 6,0]]

print("Verilen Matris :")
print (baslangicMatris)

print("Devrilmis hali : ")
print (devir(baslangicMatris))