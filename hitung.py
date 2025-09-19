# hitung.py

def luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga"""
    return 0.5 * alas * tinggi

def luas_persegi(sisi):
    """Menghitung luas persegi"""
    return sisi * sisi

def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran"""
    phi = 3.14159
    return phi * (jari_jari ** 2)

def main():
    print("=== Program Perhitungan Luas Bangun Datar ===")
    print("1. Segitiga")
    print("2. Persegi")
    print("3. Lingkaran")
    
    pilihan = input("Pilih bangun datar (1/2/3): ")

    try:
        if pilihan == "1":
            alas = float(input("Masukkan panjang alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            print(f"Luas segitiga = {luas_segitiga(alas, tinggi)}")
        elif pilihan == "2":
            sisi = float(input("Masukkan panjang sisi: "))
            print(f"Luas persegi = {luas_persegi(sisi)}")
        elif pilihan == "3":
            r = float(input("Masukkan jari-jari: "))
            print(f"Luas lingkaran = {luas_lingkaran(r)}")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

if __name__ == "__main__":
    main()
