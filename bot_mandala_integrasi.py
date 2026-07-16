import requests
import time

TOKEN = "8541971105:AAGP-k9lS5eVoav6WEfBpul216cN8nalBHU"
CHAT_ID = "7957705843"
URL_BASE = f"https://api.telegram.org/bot{TOKEN}"

def kirim_pesan(text):
    requests.post(f"{URL_BASE}/sendMessage", json={"chat_id": CHAT_ID, "text": text})

def cek_pesan():
    try:
        res = requests.get(f"{URL_BASE}/getUpdates?offset=-1")
        data = res.json()
        # Nambahkeun saringan: lamun 'result' teu aya, balikkeun list kosong
        return data.get('result', [])
    except:
        return []

print("=== BOT MANDALA V26 AKTIF: Siap ngalatih logika ===")
last_id = 0

while True:
    results = cek_pesan()
    if results:
        pesan_anyar = results[-1]
        if pesan_anyar['update_id'] != last_id:
            teks = pesan_anyar['message'].get('text', '')
            jawaban = f"Mandala V26 narima paréntah: {teks}. (Sistem siap diproses)"
            kirim_pesan(jawaban)
            last_id = pesan_anyar['update_id']
    time.sleep(2)
