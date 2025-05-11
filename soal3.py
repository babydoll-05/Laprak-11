def ubah_nama_file(file):
    with open(file, 'r') as f:
        kata = f.readlines()
        print(kata)

        print('===================ISI BERITA================')
        print(kata)
        print('===============Kata Unik pada berita=========')
        for line in kata:
            list = line.strip().split()
            print(list)

namafile = "laprak\news.txt"
ubah_nama_file(namafile)