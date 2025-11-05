# Lazzuardi Langga Duta Wijaya - 2501667 - 1A

# soal 1
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)


#soal 2
def volume_tabung(r, t):
    return 3.14 * r * r * t

hasil = volume_tabung(7, 10)
print("Volume tabung adalah:", hasil)


#soal 3
def hitung(angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    return total, rata_rata

def main():
    data = input("Masukkan angka (pisahkan dengan koma): ")
    angka = [int(x) for x in data.split(",")]

    total, rata_rata = hitung(angka)

    print("Total:", " + ".join(map(str, angka)), "=", total)
    print("Rata-rata =", total, "/", len(angka), "=", rata_rata)

main()




