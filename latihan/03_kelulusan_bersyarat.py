# Input: nilai akhir dan persentase kehadiran
# Proses: memeriksa nilai minimal 60 dan kehadiran minimal 80%
# Output: status kelulusan

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")