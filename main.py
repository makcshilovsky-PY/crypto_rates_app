import tkinter as tk
from tkinter import ttk
import requests

# Список монет и их ID в API CoinGecko
coins = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana",
    "Dogecoin": "dogecoin",
    "Cardano": "cardano",
    "Ripple": "ripple",
}


def get_crypto_price(coin_id):
    """Запрос курса с API CoinGecko"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if coin_id in data:
            price = data[coin_id]['usd']
            return f"${price:,.2f}"
        else:
            return "Ошибка данных"
    except Exception:
        return "Ошибка сети"


def show_price():
    selected_coin = combo.get()
    if not selected_coin:
        result_label.config(text="Выберите монету из списка!")
        return

    coin_id = coins[selected_coin]
    result_label.config(text="Загрузка...")
    window.update()

    price = get_crypto_price(coin_id)
    result_label.config(text=f"Курс {selected_coin}: {price}")


# ------------ Окно ------------
window = tk.Tk()
window.title("Курсы криптовалют")
window.geometry("350x250")
window.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use('classic')

title_label = tk.Label(window, text="Курс криптовалюты", font=("Arial", 14), bg="#f0f0f0")
title_label.pack(pady=15)

combo = ttk.Combobox(window, values=list(coins.keys()))
combo.pack(pady=5)

button = tk.Button(window, text="Получить курс", command=show_price, bg="#f0f0f0", fg="black")
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

window.mainloop()