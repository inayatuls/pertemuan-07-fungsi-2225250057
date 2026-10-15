# Pertemuan 07 - Fungsi Python

## Identitas
 Nama: Inayatul Sholihah
 NIM: 2225250057
 Kelas: 3A 

## Deskripsi
Tugas Pertemuan 07 membahas penggunaan fungsi dalam Python, mulai dari pembuatan fungsi, parameter, nilai balik (return), perulangan, statistik sederhana, hingga ruang lingkup variabel. Pada bagian praktik, dibuat program utilitas matematika dengan beberapa pilihan menu.

## Struktur File
- `latihan/01_salam.py` : Menampilkan salam menggunakan fungsi.
- `latihan/02_luas_persegi_panjang.py` : Menghitung luas persegi panjang.
- `latihan/03_jumlah_n.py` : Menghitung jumlah bilangan dari 1 sampai n.
- `latihan/04_statistik_sederhana.py` : Menghitung nilai minimum, maksimum, dan rata-rata.
- `latihan/05_scope.py` : Mempelajari ruang lingkup variabel.
- `praktik/utilitas_matematika.py` : Program utilitas matematika berbasis menu.

## Cara Menjalankan Program
1. Buka folder tugas di Visual Studio Code.
2. Pilih file Python yang ingin dijalankan.
3. Klik kanan pada area kode.
4. Pilih **Run Python File in Terminal**.
5. Untuk program utilitas matematika, masukkan pilihan menu sesuai petunjuk di terminal.

## Hasil Pengujian

### 1. Fungsi Salam
Program menampilkan salam kepada nama yang diberikan.

### 2. Luas Persegi Panjang
- Panjang 8 dan lebar 5 menghasilkan 40.
- Panjang 2,5 dan lebar 4 menghasilkan 10.
- Panjang 0 dan lebar 7 menghasilkan 0.

### 3. Jumlah Bilangan
- n = 1 menghasilkan 1.
- n = 5 menghasilkan 15.
- n = 10 menghasilkan 55.
- n = 100 menghasilkan 5050.

### 4. Statistik Sederhana
Data: [70, 80, 65, 90, 75]
- Nilai minimum: 65.
- Nilai maksimum: 90.
- Rata-rata: 76.

### 5. Scope Variabel
Program menunjukkan bahwa variabel lokal di dalam fungsi dapat memiliki nilai berbeda dari variabel di luar fungsi.

### 6. Utilitas Matematika
- Luas persegi panjang dengan panjang 8 dan lebar 5 = 40.
- Luas segitiga dengan alas 10 dan tinggi 6 = 30.
- Jumlah bilangan dari 1 sampai 10 = 55.
- Faktorial dari 5 = 120.
- Faktorial dari 0 = 1.

## Kuis Formatif Pertemuan 07

**1. Apa fungsi kata kunci `def` dalam Python?**

Jawaban: Untuk mendefinisikan atau membuat fungsi.

**2. Apa perbedaan parameter dan argumen?**

Jawaban: Parameter ditulis pada definisi fungsi, sedangkan argumen merupakan nilai yang diberikan ketika fungsi dipanggil.

**3. Kapan fungsi sebaiknya menggunakan `return` daripada `print()`?**

Jawaban: Ketika nilai hasil fungsi perlu digunakan kembali dalam perhitungan atau disimpan ke variabel.

**4. Jika fungsi `kuadrat(x)` mengembalikan nilai `x * x`, berapakah nilai `kuadrat(4)`?**

Jawaban: 16.

**5. Mengapa variabel lokal sebaiknya tidak bergantung pada perubahan variabel di luar fungsi?**

Jawaban: Agar fungsi lebih mudah dipahami, diuji, dan perilakunya lebih terkontrol.

**6. Apa yang terjadi jika fungsi membutuhkan dua parameter tetapi hanya menerima satu argumen?**

Jawaban: Python menghasilkan `TypeError` karena jumlah argumen yang diberikan kurang.

**7. Bagaimana cara menggunakan nilai hasil fungsi untuk perhitungan berikutnya?**

Jawaban: Menyimpan nilai yang dikembalikan oleh fungsi menggunakan `return` ke dalam variabel, lalu menggunakan variabel tersebut dalam perhitungan.

**8. Apa perbedaan Step Into dan Step Over saat debugging di VS Code?**

Jawaban: Step Into masuk ke dalam fungsi yang dipanggil, sedangkan Step Over menjalankan pemanggilan fungsi tanpa masuk ke setiap baris di dalam fungsi tersebut.

**9. Apa manfaat membagi program menjadi beberapa fungsi?**

Jawaban: Program menjadi lebih terstruktur, kode dapat digunakan kembali, dan setiap bagian lebih mudah diuji serta diperbaiki.

**10. Perintah Git apa yang digunakan untuk mengirim commit lokal ke GitHub ketika remote sudah terhubung?**

Jawaban: `git push`.

## Refleksi
Melalui tugas ini, saya belajar membuat fungsi, menggunakan parameter dan `return`, melakukan perulangan, mengolah data sederhana, serta memahami ruang lingkup variabel. Saya juga belajar membuat program utilitas matematika dengan menu dan menguji hasilnya menggunakan beberapa contoh masukan.