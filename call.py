def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian Tidak Bisa Menggunakan 0"

print("\n+----------Kalkulator Sederhana-----------+")
print("|=========================================|\n")

while True:
    print("Pilih Operasi\n--------------------")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[0] Exit")

    pilihan = input("Masukkan Pilihan Anda: ")

    if pilihan == '0':
        print("Anda keluar dari Operator Aritmatika\n")
        break

    op_1 = float(input('Masukkan Angka ke-1: '))
    op_2 = float(input('Masukkan Angka ke-2: '))
    
    if pilihan == '1':
        hasil = penjumlahan(op_1, op_2)
        print("Hasil Penjumlahan: ", hasil)
    elif pilihan == '2':
        hasil = pengurangan(op_1, op_2)
        print("Hasil Pengurangan: ", hasil)
    elif pilihan == '3':
        hasil = perkalian(op_1, op_2)
        print("Hasil Perkalian: ", hasil)
    elif pilihan == '4':
        hasil = pembagian(op_1, op_2)
        print("Hasil Pembagian: ", hasil)
    else:
        print("Pilihan tidak valid, silakan coba lagi")
