def ransel_top_down(berat, profit, kapasitas):
    jumlah_objek = len(berat)
    memo = [[-1 for _ in range(kapasitas + 1)] for _ in range(jumlah_objek + 1)]

    def knapsack_rekursif(indeks, sisa_kapasitas):
        if indeks == 0 or sisa_kapasitas == 0:
            return 0
        
        if memo[indeks][sisa_kapasitas] != -1:
            return memo[indeks][sisa_kapasitas]
        tanpa_objek_terkini = knapsack_rekursif(indeks - 1, sisa_kapasitas)

        pakai_objek_terkini = 0
        if berat[indeks - 1] <= sisa_kapasitas:
            pakai_objek_terkini = profit[indeks - 1] + knapsack_rekursif(indeks - 1, sisa_kapasitas - berat[indeks - 1])

        memo[indeks][sisa_kapasitas] = max(tanpa_objek_terkini, pakai_objek_terkini)
        return memo[indeks][sisa_kapasitas]

    profit_maksimal = knapsack_rekursif(jumlah_objek, kapasitas)

    objek_terpilih = []
    kapasitas_tersisa = kapasitas
    for i in range(jumlah_objek, 0, -1):
        if memo[i][kapasitas_tersisa] != memo[i - 1][kapasitas_tersisa]:
            objek_terpilih.append(i)  
            kapasitas_tersisa -= berat[i - 1]

    objek_terpilih.sort()
    return profit_maksimal, objek_terpilih

def input_manual_top_down():
    n = int(input("Masukkan jumlah objek: "))
    berat = []
    profit = []
    for i in range(n):
        w = int(input(f"Masukkan berat untuk objek {i + 1}: "))
        p = int(input(f"Masukkan profit (profit) untuk objek {i + 1}: "))
        berat.append(w)
        profit.append(p)
    kapasitas = int(input("Masukkan kapasitas ransel: "))

    profit_maksimal, objek_terpilih = ransel_top_down(berat, profit, kapasitas)
    print(f"Maksimum profit yang dapat diperoleh adalah: {profit_maksimal}")
    print(f"Objek yang terpilih: {objek_terpilih}")

input_manual_top_down()
