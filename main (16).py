def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b
    
def bagi(a, b):
    if b == 0:
        return "Tidak dapat dibagi oleh nol"
    return a / b

# Menyimpan fungsi-fungsi operasi dalam sebuah list
operasi = [tambah, kurang, kali, bagi]

# Menu 
while True:
    print("Pilih operasi:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    
    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")
    
    if pilihan == '5':
        print("Thank you! Kalkulator selesai digunakan.")
        break
    
    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        # Menghitung hasil operasi dengan memanggil fungsi sesuai indeks operasi
        hasil = operasi[int(pilihan) - 1](angka1, angka2)
        print("Hasil perhitungan:", hasil)
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")