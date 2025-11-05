# Lazzuardi Langga Duta Wijaya - 2501667 - 1A

def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai,
                         jam_selesai, menit_selesai, detik_selesai):
    total_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

    selisih = total_selesai - total_mulai

    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60

    return jam, menit, detik


def main():
    print("=== Input waktu mulai ===")
    jam_mulai = int(input("Jam: "))
    menit_mulai = int(input("Menit: "))
    detik_mulai = int(input("Detik: "))

    print("\n=== Input waktu selesai ===")
    jam_selesai = int(input("Jam: "))
    menit_selesai = int(input("Menit: "))
    detik_selesai = int(input("Detik: "))

    jam, menit, detik = hitung_selisih_waktu(
        jam_mulai, menit_mulai, detik_mulai,
        jam_selesai, menit_selesai, detik_selesai
    )

    print("\nSelisih waktu:")
    print(f"{jam} jam - {menit} menit - {detik} detik")


main()
