def tiga_terbaik(data):
    urut = sorted(data, reverse=True)
    nilai_terbaik = urut[:3]

    return nilai_terbaik

data = [99,98,97,70,65,78]
print(tiga_terbaik(data))