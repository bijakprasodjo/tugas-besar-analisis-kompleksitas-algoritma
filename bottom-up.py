def ransel_bottom_up(bobot, keuntungan, kapasitas):
    jumlah_objek = len(bobot)
    tabel_dp = [[0 for _ in range(kapasitas + 1)] for _ in range(jumlah_objek + 1)]

    for i in range(1, jumlah_objek + 1):
        for batas_kapasitas in range(1, kapasitas + 1):
            if bobot[i - 1] <= batas_kapasitas:
                tabel_dp[i][batas_kapasitas] = max(
                    tabel_dp[i - 1][batas_kapasitas],
                    keuntungan[i - 1] + tabel_dp[i - 1][batas_kapasitas - bobot[i - 1]]
                )
            else:
                tabel_dp[i][batas_kapasitas] = tabel_dp[i - 1][batas_kapasitas]

    objek_terpilih = []
    sisa_kapasitas = kapasitas
    for i in range(jumlah_objek, 0, -1):
        if tabel_dp[i][sisa_kapasitas] != tabel_dp[i - 1][sisa_kapasitas]:
            objek_terpilih.append(i)
            sisa_kapasitas -= bobot[i - 1]

    objek_terpilih.sort()
    return tabel_dp[jumlah_objek][kapasitas], objek_terpilih

def input_manual_bottom_up():
    n = int(input("Masukkan jumlah objek: "))
    bobot = []
    keuntungan = []
    for i in range(n):
        w = int(input(f"Masukkan berat untuk objek {i + 1}: "))
        p = int(input(f"Masukkan keuntungan untuk objek {i + 1}: "))
        bobot.append(w)
        keuntungan.append(p)
    kapasitas = int(input("Masukkan kapasitas ransel: "))

    keuntungan_maksimal, objek_terpilih = ransel_bottom_up(bobot, keuntungan, kapasitas)
    print(f"Maksimum keuntungan yang dapat diperoleh adalah: {keuntungan_maksimal}")
    print(f"Objek yang terpilih: {objek_terpilih}")

input_manual_bottom_up()
