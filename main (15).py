def hitung_total(daftar_angka, pemisah):
    total = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            total += angka
    return total

daftar_angka1 = [28, 11, 4, 20, 15, 13, 23, 25, 75, 82, 12, 18]
pemisah1 = 2
total1 = hitung_total(daftar_angka1, pemisah1)
print("Total angka dalam", daftar_angka1, "yang bisa dibagi habis oleh", pemisah1, "yaitu", total1)

daftar_angka2 = [60, 65, 70, 75, 80, 85, 90]
pemisah2 = 5
total2 = hitung_total(daftar_angka2, pemisah2)
print("Total angka dalam", daftar_angka2, "yang bisa dibagi habis oleh", pemisah2, "yaitu", total2)
