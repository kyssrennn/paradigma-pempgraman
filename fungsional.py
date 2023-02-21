def input_alas_dan_tingi():
    alas = float (input('masukkan alas :'))
    tinggi = float(input('masukkan tinggi: '))

    return alas, tinggi

def hitung_luas(alas,tinggi):
    return 0.5 * alas * tinggi

print(hitung_luas(5, 10))

alas, tinggi = input_alas_dan_tingi()
print(hitung_luas(alas,tinggi))