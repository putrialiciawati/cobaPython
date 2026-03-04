#KOMENTAR
#KOMENTAR


'''doctsring'''
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

def main():
    print("=== Kalkulator Sederhana Python ===")
    print("Pilih Operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali   (*)")
    print("4. Bagi   (/)")

    try:
        pilihan = input("\nMasukkan pilihan (1/2/3/4): ")
        
        if pilihan in ['1', '2', '3', '4']:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
            elif pilihan == '2':
                print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
            elif pilihan == '3':
                print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
            elif pilihan == '4':
                print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid.")
            
    except ValueError:
        print("Input salah! Harap masukkan angka.")

if __name__ == "__main__":
    main()
