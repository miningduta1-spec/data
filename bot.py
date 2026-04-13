import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = "API_TOKEN_BOTMU"
CHAT_ID = "CHAT_ID_TELEGRAMMU"

def ambil_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # Sesuaikan dengan struktur webmu
    sinyal = soup.find(id="sinyal").text
    profit = soup.find(id="profit").text
    return sinyal, profit

def kirim_laporan():
    sinyal, profit = ambil_data("https://mstdjohan.github.io/datacenter/simulasi.html")
    bot = Bot(token=TOKEN)
    pesan = f"📊 Laporan Trading\nSinyal: {sinyal}\nProsentase Keuntungan: {profit}"
    bot.send_message(chat_id=CHAT_ID, text=pesan)

if __name__ == "__main__":
    kirim_laporan()
