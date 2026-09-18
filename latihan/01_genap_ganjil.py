# Input: satu bilangan bulat
# Proses: menentukan bilangan genap atau ganjil
# Output: keterangan genap atau ganjil

bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")