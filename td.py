#tipe data boolean (bool)
print(True) #True = 1, False = 0

#tipe data string (str)
print("Halo semuaa") #string = karakter

#tipe data integer (int)
print(100, 200, 300, 400, 500) #integer = bilangan bulat

#tipe data float (float)
print(100.0, 200.0, 300.0, 400.0, 500.0) #float = bilangan desimal

#tipe data hexadecimal (hex)
print("hexadecimal dari 100 adalah", hex(100)) #hexadecimal = bilangan basis 16

#tipe data complex (complex)
print(1j) #complex = bilangan kompleks
print(1+2j)

#tipe data List
print([1,2,3,4,5]) #list = array atau array satu dimensi
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5)) #tuple = array atau array satu dimensi yang tidak bisa diubah
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Rakha", 'lahir tanggal':5-10-2008}) #dictionary = array atau array satu dimensi yang bisa diubah

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Rakha", 'umur':16, 'alamat':'Karawang', 'hobi':'nonton'}
print(biodata) #menampilkan isi dari variabel biodata
print(biodata['nama']) #menampilkan isi dari variabel biodata dengan kata kunci 'nama'
print(type(biodata)) #menampilkan tipe data dari variabel biodata