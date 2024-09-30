#Mendefinisikan sebuah karakter/Nama Orang
manusia1="Frasinka"
manusia2="Nasya"

#Percakapan Pertama
print(f"{manusia1} : Hai, {manusia2}haiiii, ehh kemarin aku ketemu kamu di kampus loo? ")
print(f"{manusia2} : eh Iya Halo {manusia1} iyakahh? kemarin aku galiat maaf ya buru buru ke kos soalnya")

print(f"{manusia1} : masih di gg wn kan kosnya?")
print(f"{manusia1} : iya {manusia2} kamu juga masih di wn kah ? (Udah/Belum) : ")
Jawaban=input(f"{manusia2} : ")

if Jawaban.lower() == "masih":
    print(f"{manusia2} : masih dongg, setia aku sama kamu")
else:
    print(f"{manusia2} : engga, Aku udah pindah")

print(f"{manusia1} : Lah Sama dong wkwkwk")
print(f"{manusia1} : Eh btw kamu kemarin kamu beli galon berapa?")

#Input untuk mendapatkan data harga
harga_nasya=int(input(f"{manusia2} : kemarin beli sekitar(Masukkan harga Saja) : "))
harga_frasinka=int(input(f"{manusia1} : wahh aku kemarin beli (Masukkan harga Saja) : "))

#Menghitung jumlah Perbedaan harga
Perbedaan_harga =abs(harga_frasinka - harga_nasya)

# Penyeleksian kondisi operasi logika untuk perbandingan uang
if harga_nasya>harga_frasinka:
    print(f"{manusia1} : Eh ternyata galonku aku lebih mahal {Perbedaan_harga} dari kamu")
elif harga_nasya<harga_frasinka:
    print(f"{manusia1} : Eh ternyata aku lebih murah {Perbedaan_harga}  dari kamu")
else:
    print(f"{manusia1} : wahh cuma selisih sedikit ya {harga_nasya}")
# Lanjut dengan operasi aritmatika lain
Total_harga = harga_nasya + harga_frasinka 
print(f"{manusia2} : kalau kita beli dengan hargamu dan hargaku ditambah jadi berapa ya?")
print(f"{manusia1} : emm berapa ya")
print(f"{manusia1} : hargaku kemarin {harga_frasinka} + harga kamu {harga_nasya} tahun jadi Totalnya")
print(f"{manusia1} : {Total_harga} jadi segitu sihhh")
print(f"{manusia2} : wahh hebat bgt tampa kakulator")
print(f"{manusia1} : ahhhh bisa aja")


