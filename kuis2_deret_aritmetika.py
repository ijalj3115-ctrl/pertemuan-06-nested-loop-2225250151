print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Lengkapi validasi n dengan while.
while n <= 0:
    n = int(input("Banyak suku n: "))

# Lengkapi for untuk menampilkan suku dan menghitung total.
total = 0
suku_list = []

for i in range(n):
    suku = a + i * d
    total += suku
    
    # Menyesuaikan format tampilan suku agar pas dengan test case (bilangan bulat tanpa .0)
    if suku.is_integer():
        suku_list.append(str(int(suku)))
    else:
        suku_list.append(str(suku))

# Menampilkan deret suku sesuai test case
print(", ".join(suku_list))

# Tampilkan jumlah akhir dengan dua angka di belakang koma
print(f"Jumlah = {total:.2f}")