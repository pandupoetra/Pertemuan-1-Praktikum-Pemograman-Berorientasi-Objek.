import math
a=int(input("Masukan panjanga jari-jari lingkaran = "))
luas=math.pi*a**2
luas_baru="{:.2f}".format(luas)
Keliling=2*math.pi*a
Keliling_baru="{:.2f}".format(luas)
print("Keliling lingkaran adalah =", Keliling_baru)
print ("Luas lingkaran adalah =", luas_baru)