#Kondisi If Else
nilai = int(input("Masukkan nilai [1-10]: "))
if (nilai > 5):
    print("Lulus")
else:
    print("Tidak Lulus")
print()
#Kondisi Elif
nilai = int(input("Masukkan nilai [1-100]: "))
if (nilai >= 80):
    print("Nilai Anda : A")
elif (nilai >= 70):
    print("Nilai Anda : B")
elif (nilai >= 60):
    print("Nilai Anda : C")
elif (nilai >= 50):
    print("Nilai Anda : D")
else:
    print("Nilai Anda : E")