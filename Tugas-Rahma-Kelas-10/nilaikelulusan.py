print("=== SISTEM PENILAIAN SISWA ===")

nama = input("Nama siswa : ")
kelas = input("Kelas      : ")
nilai = int(input("Nilai ujian: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")

else:
    if nilai >= 90:
        predikat = "A - Sangat Baik"
    elif nilai >= 80:
        predikat = "B - Baik"
    elif nilai >= 70:
        predikat = "C - Cukup"
    elif nilai >= 60:
        predikat = "D - Kurang"
    else:
        predikat = "E - Sangat Kurang"

    if nilai >= 75:
        status = "Lulus"
    else:
        status = "Belum Lulus"

    print("\n=== HASIL PENILAIAN ===")
    print("Nama     :", nama)
    print("Kelas    :", kelas)
    print("Nilai    :", nilai)
    print("Predikat :", predikat)
    print("Status   :", status)