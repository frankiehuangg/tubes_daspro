# Program MagicConchShell
# Mengeluarkan output random menggunakan module time

import functions.basic as basic
import time

def kerangajaib():
    # Mengeluarkan jawaban acak dengan module time dan LGC

    # KAMUS LOKAL
    # start, finish : integer
    # array_length : integer
    # jawaban : array [0...array_length-1] of string
    # seed, random_int : integer

    start = int(time.time()*1000)                                           # Mulai perhitungan waktu (dalam milidetik)

    input("Apa pertanyaanmu? ")
    jawaban = ["Ya", "Tidak", "Bisa Jadi", "Mungkin", "Tentunya", "Tidak Mungkin", "Ada kemungkinan", "Jika Tuhan berkehendak", "Tanya dirimu sendiri", "Entahlah", "Mungkin Saja", "Pertanyaannya aneh", "Besok tanyain aja lagi", "Maaf, sedang sibuk"]
    array_length = basic.length(jawaban)

    finish = int(time.time()*1000)                                          # Hentikan perhitungan

    seed = finish-start                                                     # Hitung waktu antara mulai hingga selesai

    random_int = ((214013*seed + 2531011) % 10**9 + 7) % array_length       # Hasilkan angka random (0-13)

    print(jawaban[random_int])