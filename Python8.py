def checkFile(file, word):
    with open(file, 'r') as obj:
        for line in obj:
            if word in line:
                print(line)
                return True
    return False

def updateFile(file, word):
    with open(file, 'w') as obj:
                obj.write(word)
                return True
    return False

word = input("Aranacak kelimeyi giriniz : ")
w = checkFile("ipTables.log", word)
if w:
    print("Islem basarili. Aranan kelime bulundu.")
    z = updateFile("site.txt", word)
else:
    print("Aradiginiz kelime dosyada bulunmamaktadir.")