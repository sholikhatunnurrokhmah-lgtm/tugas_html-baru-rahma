nama = input("masukan nama siswa: ")
nilai = int(input("masukan nilai siswa[1-100]: "))

if nilai >= 90:
    kategori = "sangat baik"
elif nilai >= 80:
    kategori = "baik"
elif nilai >= 70:
    kategori = "cukup"
elif nilai >= 60:
    kategori = "kurang"
else:
    kategori = "sangat kurang"

if nilai >= 0 and nilai <= 100:
    print("=== HASIL NILAI SISWA ===")
    print("kelas    : XB")
    print("nama     :", nama)
    print("nilai    :", nilai)
    print("kategori :", kategori)
else:
    print("NILAI TIDAK VALID")
