#Soal1

def inputan(kalimat):
    kalimat = input("Masukkan sebuah kalimat: ")
    a = [ ]
    
    for j in kalimat:
        a.append(j)

    return kalimat
    
    for i in range(len(kalimat)):
        if a > 200:
            print("Batas karakter maksimal hanya 200")
        elif a == 0:
            print("Masukkan sebuah inputan")
        else:
            print("* {} *".format(a))
        
    







