def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or n < 0:
        return "n harus berupa bilangan bulat nonnegatif"

    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    if not isinstance(n, int) or n < 0:
        return "n harus berupa bilangan bulat nonnegatif"

    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah bilangan 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas persegi panjang:", luas_persegi_panjang(p, l))

    elif pilihan == "2":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas segitiga:", luas_segitiga(a, t))

    elif pilihan == "3":
        n = int(input("Masukkan nilai n: "))
        print("Jumlah bilangan:", jumlah_n(n))

    elif pilihan == "4":
        n = int(input("Masukkan nilai n: "))
        print("Hasil faktorial:", faktorial(n))

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")