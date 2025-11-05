# Lazzuardi Langga Duta Wijaya - 2501667 - 1A

def login():
    password_benar = "Latihan"
    kesempatan = 3

    print("=== Menu Login Admin ===")
    input("Masukkan username: ")

    for i in range(kesempatan):
        password = input("Masukkan password: ")

        if password == password_benar:
            print("Login berhasil! Selamat datang, Admin.")
            return True 
        else:
            sisa = kesempatan - (i + 1)
            print("Password salah!", end=" ")
            if sisa > 0:
                print("Kesempatan tersisa:", sisa)
            else:
                print("\nKesempatan habis. Akses ditolak!")
                return False  


def main():
    hasil_login = login()

    if hasil_login:
        print("Akses diberikan.")
    else:
        print("Akses ditolak.")


main()
