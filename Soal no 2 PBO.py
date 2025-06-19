def convert_to_int(string):
    try:
        result = int(string)
        return result
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Meminta input dari pengguna
umur = input('Masukkan umur kamu: ')  # inputan yang benar adalah angka

# Mengonversi umur dan menambahkan 5 tahun
umur5tahunlagi = convert_to_int(umur)

# Memastikan umur5tahunlagi tidak None sebelum mencetak
if umur5tahunlagi is not None:
    umur5tahunlagi += 5
    print(f"Umur kamu 5 tahun lagi adalah {umur5tahunlagi}")