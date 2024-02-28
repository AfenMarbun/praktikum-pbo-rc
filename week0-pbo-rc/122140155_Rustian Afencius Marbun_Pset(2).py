jumlah_siswa = int(input("Masukan jumlah siswa : "))
nilai_siswa = {}

for i in range (jumlah_siswa):
    nama = input("Masukan nama siswa " + str(i + 1) + " : ")
    nilai = int(input("Masukan nilai " + nama + " : "))

    nilai_siswa[nama] = nilai


print("\nDaftar Nilai siswa : ")
for nama, nilai in nilai_siswa.items():
    # print(f"{nama} : {nilai}")
    print(nama + " : " + str(nilai))