def ambil_kata_unik(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            isi = file.read()
        for tanda in ['.', ',', '!', '?', ':', ';', '(', ')', '"', "'"]:
            isi = isi.replace(tanda, '')
        kata_list = isi.lower().split()
        kata_unik = set(kata_list)
        print("Kata-kata unik dalam file:")
        for kata in sorted(kata_unik):
            print(kata)

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

nama_file = input("Masukkan nama file teks : ")
ambil_kata_unik(nama_file)