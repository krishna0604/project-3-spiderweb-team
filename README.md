<h1><b> PROJECT DATA ENGINEER BY SPIDERWEB TEAM </b></h1> 
<hr>
<h2> Kelompok 5 FTDE-01 Digital Skola </h2> 
Selamat datang, kami sudah menyelesaikan berbagai problem bisnis berupa mini project dari Bootcamp data Engineer, Digital Skola. Kami telah menyelesaikan tahap Airflow, Bigquery, dan Docker dengan best practicenya. 
<br>
Teman - teman bisa mengakses full langkah demi langkah tahap pengerjaan project dengan mengakses file "Step by step Project 3 by Spiderweb team.pdf" yang tertera dalam repositori ini
<br>
Teman - teman bisa mengakses requirement project melalui link : https://gitlab.com/farhansmg/dskola_nosql_project3. 
<hr>

<h2> Nama anggota Kelompok : ( Nama lengkap - username github - email ) </h2>

1. I Gusti Agung Krishna Dwipayana - krishna0604 - agungkrishna04@gmail.com
2. Hafidha Harfiana Dewi - HafidhaHD - harfiana.hafidha@gmail.com
3. hermawan Adi Prasetyo - adiprasetyohermawan - adiprasetyohermawan00@gmail.com
4. Humairoh - humairoh22 - humairohhumay@yahoo.co.id
5. I Putu Ferry Wistika - putuwistika - 12820001@mahasiswa.itb.ac.id
6. Fenny Inriana - Fennyinriana
<hr>

<h2> Tahap Pengerjaan : </h2>  
1. <b>Tahap Pertama</b> : Project 3 ini merupakan lanjutan dari projectc 2, namun menggunakan airflow. Database kami sudah tersedia di postgre
<br>
2. <b>Tahap Kedua</b> : MMenginstal library yang diperlukan menggunakan !pip di google colab
<br>
3. <b>Tahap Ketiga</b> : Lalu kami memasukkan informasi koneksi ke postgreSQL ( password dirahasikan untuk membuat dokumen ini ) yang bisa diakses pada file "/postgre_to_bigquery_project_3.py"
<br>
4. <b>Tahap Keempat</b> : Lalu membaca setiap tabel  menggunakaan kode python yang bisa diakses pada file "/postgre_to_bigquery_project_3.py"
<br>
5. <b>Tahap Kelima</b> : Lalu menggunggah dataframe ke bigquery dengan ‘google-cloud-bigquery’ menggunakan kode python yang bisa diakses pada file "/postgre_to_bigquery_project_3.py"
<br>
6. <b>Tahap Keenam</b> : Kode sukses dijalankan dan data sudah tampil di Google Bigquery. Kini kami sudah bisa melihat schema, details, dan preview dari masing-masing tabel.
<br>
7. <b>Tahap Ketujuh</b> : Pada git bash, kami membuat direktori baru dan pindah ke direktori tersebut. direktori ini bernama “airflow_docker”.
<br>
8. <b>Tahap Kedelapan</b> : Kami membuka VSCode dan memastikan bahwa folder direktori sudah terbuka untuk membuat file ocker-compose.yaml, namun sebelum itu kami mendefiniskan fernet key dan webserver secret key di git bash
<br>
9. <b>Tahap Kesembilan</b> : Kami memasukkan unci fernet dan secret key webserver tersebut ke file docker-compose.yaml
<br>
10. <b>Tahap Kesepuluh</b> : Kami membuat file dag di dalam direktori dan memasukkan file example_day.py
<br>
11. <b>Tahap Kesebelas</b> : Kami menjalankan airflow dengan menggunakan $ docker-compose up
<br>
12. <b>Tahap Keduabelas</b> : Kami mengecek airflow apakah running healthy menggunakan $ docker-compose ps
<br>
13. <b>Tahap Ketigabelas</b> : Kami mengakses airflow WEB UI dengan local host 8080:8080
<br>
14. <b>Tahap Keempatbelas</b> : Lalu kami akan membuat DAG baru untuk mengotomatiskan proses ekstraksi data 
<br>
15. <b>Tahap Kelimabelas</b> : Kami refresh airflow. lalu mengaktifkan postgres_to_biquery_dag dan sudah memastikan task task berjalan dengan sukses
16. <b>Tahap Keenambelas</b> : kami menggunakan kode python dag untuk menylesaikan task requirements dari mentor dan mendapatkan hasil yang sesuai dengan yang diharapkan

