# Pertemuan 03 Seleksi Python

Nama: Muhammad Fatih Ammar
NIM: 2225250135
Kelas: 3E

## Tujuan

Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan

Jalankan program menggunakan Python 3 melalui terminal VS Code.

Contoh:

python tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

1. Baca koefisien a, b, dan c sebagai float.
2. Periksa apakah a sama dengan 0.
3. Jika a sama dengan 0, tampilkan bahwa input bukan persamaan kuadrat.
4. Jika a tidak sama dengan 0, hitung diskriminan D = b² - 4ac.
5. Jika D lebih besar dari 0, hitung dan tampilkan dua akar real berbeda.
6. Jika D sama dengan 0, hitung dan tampilkan satu akar real kembar.
7. Jika D kurang dari 0, tampilkan bahwa tidak ada akar real.
8. Tampilkan nilai numerik dengan dua angka di belakang koma.

## Hasil Pengujian

| Input (a, b, c) | Hasil yang Diharapkan | Status |
|---|---|---|
| (1, -5, 6) | Dua akar real: 3 dan 2 | Berhasil |
| (1, 2, 1) | Akar real kembar: -1 | Berhasil |
| (1, 0, 1) | Tidak ada akar real | Berhasil |
| (0, 2, 3) | Bukan persamaan kuadrat | Berhasil |

## Refleksi

Kesalahan logika yang perlu diperhatikan adalah penggunaan kondisi pada diskriminan. Program harus membedakan kondisi D > 0, D = 0, dan D < 0 dengan tepat. Kesalahan tersebut diperbaiki dengan menggunakan nested if sehingga setiap kemungkinan diskriminan memiliki cabang yang sesuai.
