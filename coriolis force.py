# Lintang: Utara dan Selatan
posisi_lintang = "selatan"
arah_angin_awal = "timur" 
if posisi_lintang  == "utara" and arah_angin_awal == "timur":
    print("Dibelokkan ke kiri")
else:
    print("Dibelokkan ke kanan")

    print("-" * 30)

posisi_lintang = "khatulistiwa"
arah_angin_awal = "timur" 

if posisi_lintang == "utara": 
    print("Gaya Coriolis Dibelokkan ke KANAN")
elif posisi_lintang == "selatan":
    print("Gaya Coriolis Dibelokan ke KIRI")
elif posisi_lintang == "khatulistiwa":
    print("Gaya Coriolis:  Tidak ada pembelokan")
else:
    print("Data tidak valid! Masukan utara, selatan, atau khatulistiwa")