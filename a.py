import sys
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)  

def knapsack_top_down(berat, keuntungan, kapasitas):
    jumlah_objek = len(berat)
    memo = [[-1 for _ in range(kapasitas + 1)] for _ in range(jumlah_objek + 1)]

    def rekursif_knapsack(indeks, sisa_kapasitas):
       
        if indeks == 0  or kapasitas == 0:
            return 0

        if memo[indeks][sisa_kapasitas] != -1:
            return memo[indeks][sisa_kapasitas]

        tidak_berobjek = rekursif_knapsack(indeks - 1, sisa_kapasitas)

        masuk = 0
        if berat[indeks - 1] <= sisa_kapasitas:
            masuk = keuntungan[indeks - 1] + rekursif_knapsack(indeks - 1, sisa_kapasitas - berat[indeks - 1])

        memo[indeks][sisa_kapasitas] = max(tidak_berobjek, masuk)
        return memo[indeks][sisa_kapasitas]

    return rekursif_knapsack(jumlah_objek, kapasitas)

def knapsack_bottom_up(berat, keuntungan, kapasitas):
    jumlah_objek = len(berat)
    tabel_dp = [[0 for _ in range(kapasitas + 1)] for _ in range(jumlah_objek + 1)]

    for i in range(1, jumlah_objek + 1):
        for batas_kapasitas in range(1, kapasitas + 1):
            if berat[i - 1] <= batas_kapasitas:
                tabel_dp[i][batas_kapasitas] = max(
                    tabel_dp[i - 1][batas_kapasitas],
                    keuntungan[i - 1] + tabel_dp[i - 1][batas_kapasitas - berat[i - 1]]
                )
            else:
                tabel_dp[i][batas_kapasitas] = tabel_dp[i - 1][batas_kapasitas]

    return tabel_dp[jumlah_objek][kapasitas]

def data_knapsack(jumlah_objek, mod_berat, mod_keuntungan, kapasitas):
    berat = [(i % mod_berat + 1) for i in range(jumlah_objek)]
    keuntungan = [(i % mod_keuntungan + 5) for i in range(jumlah_objek)]
    return berat, keuntungan, kapasitas

datasets = [
    data_knapsack(5, 7, 10, 10), # DataSet 1
    data_knapsack(10, 10, 15, 20), # DataSet 2
    data_knapsack(20, 7, 10, 35),   # DataSet 3
    data_knapsack(50, 10, 15, 70),  # DataSet 4
    data_knapsack(100, 15, 20, 150), # DataSet 5
    data_knapsack(200, 20, 25, 300), # DataSet 6
    data_knapsack(500, 35, 40, 1200), # DataSet 7
    data_knapsack(1000, 1000, 1500, 2000) #DataSet 8
]

def ukur_waktu(knapsack, datasets, label):
    waktu_eksekusi = []
    print(f"\nHasil Waktu Eksekusi untuk {label}:")
    for idx, (berat, keuntungan, kapasitas) in enumerate(datasets):
        waktu_mulai = time.time()
        knapsack(berat, keuntungan, kapasitas)
        waktu_selesai = time.time()
        durasi = waktu_selesai - waktu_mulai
        waktu_eksekusi.append(durasi)
        print(f"Dataset {idx + 1} (Jumlah Objek: {len(berat)}): {durasi:.6f} detik")
    return waktu_eksekusi

waktu_top_down = ukur_waktu(knapsack_top_down, datasets, "Top-Down")  
waktu_bottom_up = ukur_waktu(knapsack_bottom_up, datasets, "Bottom-Up")  

jumlah_objek = [5, 10, 20, 50, 100, 200, 500, 1000]
plt.figure(figsize=(12, 6))
plt.plot(jumlah_objek, waktu_top_down, label='Top-Down', marker='o', color='blue')
plt.plot(jumlah_objek, waktu_bottom_up, label='Bottom-Up', marker='o', color='orange')
plt.xlabel('Jumlah Objek')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Perbandingan Waktu Eksekusi Top-Down vs Bottom-Up')
plt.legend()
plt.grid()
plt.show()
