# 🚀 WhatsApp Blaster via Gowa API (CSV Blast)

> 📡 Dibangun di atas [Gowa API](https://github.com/aldinokemal/gowa) by @aldinokemal
Script ini digunakan untuk melakukan **blast pesan WhatsApp otomatis** ke banyak nomor menggunakan **Gowa API**, dengan metode pengambilan data nomor & nama dari file `kontak.csv` sudah di test dengan 5000 msg tidak terblokir, gokil!

---

## 🔧 Fitur
- ✅ Login otomatis via **OTP** tanpa scan QR
- ✅ Kirim pesan ke ribuan nomor WA secara bertahap
- ✅ Pesan bisa dikustomisasi nama (personalized)
- ✅ Baca nomor dan nama dari file `.csv`
- ✅ Gunakan API Gowa (by @aldinokemal)

---
## 📦 Easy to Use
- Pastikan kamu sudah install GOWA di localhost / VPS (https://github.com/aldinokemal/go-whatsapp-web-multidevice)
- pip install requests pandas python-dotenv
- python script.py
 
## 📦 Struktur File

```bash
.
├── kontak.csv           # Daftar nomor dan nama penerima
├── script.py             # Script utama blasting
└── README.md            # Dokumentasi ini

---

## 👏 Credits

- Backend API by [Gowa](https://github.com/aldinokemal/gowa) — created by @aldinokemal
- Python integration by [@rzalvaero](https://github.com/rzalvaero)
