suhu=float(input("Masukan suhu ruangan sekarang = "))
if suhu<0:
    print("Membeku")
elif suhu<10:
    print("Sangat Dingin")
elif suhu<20:
    print("Sejuk")
elif suhu<30:
    print("hangat")
elif suhu<40:
    print("Panas")
else:
    print("Sangat Panas")