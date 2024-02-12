#Fungsi pengecekan NIU
def cek_NIU():
    while True:
        niu = input("Masukkan NIU (6 digit integer): ")
        if niu.isdigit() and len(niu) == 6:
            return int(niu)
        print("NIU harus terdiri dari 6 digit integer. Coba lagi.")
#fungsi perhitungan nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_laporan, nilai_ujian):
    #Menghitung rata-rata nilai tugas dan laporan
    rata_rata = (nilai_tugas + nilai_laporan) / 2
    #Jika rata-rata kurang dari 40, maka nilai langsung K
    if rata_rata < 40:
        nilai_akhir='K'
    else:
        # Menghitung nilai akhir dengan bobot
        bobot= 0.25 * nilai_tugas + 0.25 * nilai_laporan + 0.5 * nilai_ujian
        #Menghitung bobot
        if bobot<50:
            nilai_akhir="E"
        elif 50<=bobot<60:
            nilai_akhir="D"
        elif 60<=bobot<70:
            nilai_akhir="C"
        elif 70<=bobot<80:
            nilai_akhir="B"
        else:
            nilai_akhir="A"
    return nilai_akhir

NIU=cek_NIU()
nilai_tugas=int(input("Masukan nilai tugas = "))
nilai_laporan=int(input("Masukan nilai laporan = "))
nilai_ujian=int(input("Masukan nilai ujian = "))
nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_laporan, nilai_ujian)
print("Nilai akhir = ", nilai_akhir)
