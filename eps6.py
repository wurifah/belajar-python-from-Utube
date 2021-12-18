# kita belajar Casting
# mengubah dari satu tipe ke tipe lain

# ini adalah data integer
print("   =====INTEGER====    ")
data_int = 1945;
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false kalo angkanya 0
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

# data float
print("   =====FLOAT====    ")
data_float = 9.5;
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false kalo angkanya 0
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

# data boolean
print("   =====BOOLEAN====    ")
data_boolean = False;
print("data = ", data_boolean, ", type = ", type(data_boolean))

data_int = int(data_boolean) #akan dibulatkan ke bawah
data_str = str(data_boolean)
data_float = float(data_boolean) # akan false kalo angkanya 0
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_float, ", type = ", type(data_float))

# data string
print("   =====STRING====    ")
data_string = "ucup";
print("data = ", data_string, ", type = ", type(data_string))

data_int = int(data_string) # string harus angka
data_float = float(data_string) # string harus angka
data_boolean = bool(data_string) # false jika kosong
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_boolean, ", type = ", type(data_boolean))
