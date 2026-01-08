# Menu Recommendation Engine (Rule-Based)

## Deskripsi
Aplikasi ini adalah **menu recommendation system berbasis aturan (rule-based)** yang berjalan di command line (CLI).
Sistem memberikan **Top 3 rekomendasi menu** berdasarkan preferensi pengguna seperti:
- waktu makan
- preferensi rasa
- budget

Pendekatan rule-based dipilih untuk menjaga **transparansi keputusan**, kemudahan pengujian, dan kemudahan pengembangan.

---

## Fitur Utama
- Input user tervalidasi (tidak menerima input ilegal)
- Sistem scoring eksplisit untuk setiap menu
- Ranking Top 3 menu terbaik
- Menampilkan alasan di balik setiap rekomendasi

---

## Struktur Project
menu_recommendation_engine/
│
├── main.py # Entry point & CLI
├── menu_data.py # Data menu
├── recommender.py # Logic & scoring engine
└── README.md

## Cara Menjalankan
Pastikan Python sudah terinstall.

## Contoh Input
python main.py

Waktu makan      : siang
Preferensi rasa : sedang
Budget          : medium

## Contoh Output 
1 Nasi Goreng Ayam
Skor   : 9
Alasan :
- Cocok untuk waktu makan
- Sesuai preferensi rasa
- Sesuai budget
- Menu populer
