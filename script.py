import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import time

# Konfigurasi Gowa API
API_URL = "https://localhost:3000" #MASUKIN URL GOWA ALDIKEMAL
USERNAME = "XXX" #USERNAME FOR CREDENTIAL
PASSWORD = "XXX" #PASSWORD FOR CREDENTIAL

# Baca CSV
# df = pd.read_csv("kontak.csv")
df = pd.read_csv("kontak.csv", encoding="latin1")

# Optional konfigurasi
REPLY_MESSAGE_ID = "3EB089B9D6ADD58153C561"
IS_FORWARDED = False
DURATION = 3600

# Kirim pesan personalisasi
for index, row in df.iterrows():
    nomor = f"{row['phone']}@s.whatsapp.net"
    nama = row['nama']
    pesan_template = row['pesan']
    pesan_final = pesan_template.format(nama=nama)

    payload = {
        "phone": nomor,
        "message": pesan_final,
        "reply_message_id": REPLY_MESSAGE_ID,
        "is_forwarded": IS_FORWARDED,
        "duration": DURATION
    }

    try:
        response = requests.post(
            API_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            print(f"[✓] Pesan ke {nama} ({row['phone']}) sukses")
        else:
            print(f"[✗] Gagal ke {nama}: {response.text}")

    except Exception as e:
        print(f"[!] Error kirim ke {nama}: {e}")

    time.sleep(1)
