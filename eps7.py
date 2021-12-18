data = bool(int(input("Masukkan data: ")))
print("data = ", data, "type = ",type(data))

# operasi aritmatika
a = 12
b = 3
hasil = a/b
print(a,"/",b,"=",hasil) # kalo pembagian otomatis jadi float

# pangkat
a = 12
b = 2
hasil = a**b
print(a,"pangkat",b,"=",hasil) # pangkat = **

# floor division = pembulatan hasil bagi
a = 15
b = 2
hasil = a//b
print(a,"floor",b,"=",hasil) # floor = //


# modulus = sisa pembagian
a = 12
b = 2
hasil = a%b
print(a,"sisa",b,"=",hasil) # modulus = %


# prioritas operasi , dalam kurung, eksponen, perkalian, pertambahan
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print("x ** y * z + x / y - y % z // x =",hasil)
