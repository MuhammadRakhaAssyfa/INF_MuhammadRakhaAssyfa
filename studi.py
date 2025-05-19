a = 80
b = 20

print("Pilihan Operasi Matematika")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
itung = input("Pilih operasi (1/2/3/4) : ")
if itung == '1':
    print("Hasil : ", a+b)
elif itung == '2':
    print("Hasil : ", a-b)
elif itung == '3':
    print("Hasil : ", a*b)
elif itung == '4':
    print("Hasil : ", a/b)
else:
    print("Pilihan tidak ada.")