# Pertemuan 05 Perulangan Python

Nama: Rijal Munawarudin
NIM: 2225250151
Kelas: 3F

## Tujuan

Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif.

## Cara Menjalankan

```bash
python latihan/01_tabel_perkalian.py
python latihan/02_jumlah_bilangan.py
python latihan/03_validasi_input.py
python latihan/04_hitung_genap.py
python kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

1. Meminta pengguna memasukkan suku pertama `a`.
2. Meminta pengguna memasukkan beda `d`.
3. Meminta pengguna memasukkan banyak suku `n`.
4. Melakukan perulangan sebanyak `n` kali.
5. Menghitung setiap suku deret aritmetika menggunakan suku pertama dan beda.
6. Menampilkan setiap suku yang diperoleh.
7. Menjumlahkan semua suku selama proses perulangan.
8. Menampilkan jumlah seluruh suku setelah perulangan selesai.

Rumus suku ke-n:

`Un = a + (n - 1) × d`

## Hasil Pengujian

### Kuis 2 - Deret Aritmetika

| No | Input                   | Keluaran yang Diharapkan           | Keluaran Aktual                    | Status   |
| -- | ----------------------- | ---------------------------------- | ---------------------------------- | -------- |
| 1  | a = 2, d = 3, n = 5     | 2, 5, 8, 11, 14 dan jumlah = 40.00 | 2, 5, 8, 11, 14 dan jumlah = 40.00 | Berhasil |
| 2  | a = 10, d = -2, n = 4   | 10, 8, 6, 4 dan jumlah = 28.00     | 10, 8, 6, 4 dan jumlah = 28.00     | Berhasil |
| 3  | a = 1.5, d = 0.5, n = 3 | 1.5, 2, 2.5 dan jumlah = 6.00      | 1.5, 2, 2.5 dan jumlah = 6.00      | Berhasil |

### Program Latihan

| No | Program                 | Input       | Keluaran Aktual                     | Status   |
| -- | ----------------------- | ----------- | ----------------------------------- | -------- |
| 1  | `01_tabel_perkalian.py` | 4           | Tabel perkalian 4 dari 1 sampai 10  | Berhasil |
| 2  | `01_tabel_perkalian.py` | -3          | Tabel perkalian -3 dari 1 sampai 10 | Berhasil |
| 3  | `02_jumlah_bilangan.py` | 1           | Jumlah = 1                          | Berhasil |
| 4  | `02_jumlah_bilangan.py` | 5           | Jumlah = 15                         | Berhasil |
| 5  | `02_jumlah_bilangan.py` | 10          | Jumlah = 55                         | Berhasil |
| 6  | `03_validasi_input.py`  | 120, -5, 75 | 120 dan -5 ditolak, 75 diterima     | Berhasil |
| 7  | `04_hitung_genap.py`    | 1           | Banyak bilangan genap = 0           | Berhasil |
| 8  | `04_hitung_genap.py`    | 2           | Banyak bilangan genap = 1           | Berhasil |
| 9  | `04_hitung_genap.py`    | 5           | Banyak bilangan genap = 2           | Berhasil |
| 10 | `04_hitung_genap.py`    | 10          | Banyak bilangan genap = 5           | Berhasil |

## Refleksi

Kesalahan perulangan yang perlu diperhatikan adalah menentukan batas perulangan agar jumlah suku yang ditampilkan sesuai dengan nilai `n`.

Cara memperbaikinya adalah memastikan perulangan dilakukan sebanyak `n` kali. Dengan demikian, jumlah suku yang ditampilkan sesuai dengan input dan semua suku dapat dijumlahkan dengan benar.

Berdasarkan hasil pengujian menggunakan beda positif, beda negatif, dan bilangan desimal, program Kuis 2 dapat berjalan dengan baik.