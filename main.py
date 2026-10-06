import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

# Словарь: название монеты -> id в CoinGecko
coins = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana",
    "Dogecoin": "dogecoin",
    "Cardano": "cardano",
    "Ripple": "ripple",
}

API_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_price(crypto_id):
    # Делаем запрос к CoinGecko и возвращаем цену в USD
    params = {"ids": crypto_id, "vs_currencies": "usd"}
    response = requests.get(API_URL, params=params, timeout=10)
    # print("Запрос отправлен:", response.url)
    # print("Код ответа:", response.status_code)

    if response.status_code != 200:
        raise Exception("Сервер вернул код " + str(response.status_code))

    data = response.json()
    # print("Полученный ответ:", data)

    price = data[crypto_id]["usd"]
    # print("Цена:", price)
    return price


def show_price():
    # Что выбрал пользователь в списке
    coin_name = combo.get()
    # print("Выбрана криптовалюта:", coin_name)

    if coin_name == "":
        messagebox.showwarning("Внимание", "Сначала выберите криптовалюту!")
        return

    crypto_id = coins[coin_name]
    # print("ID для запроса:", crypto_id)

    try:
        price = get_price(crypto_id)
        result_label.config(text=coin_name + ": $" + str(price))
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Ошибка", "Нет подключения к интернету")
    except requests.exceptions.Timeout:
        messagebox.showerror("Ошибка", "Сервер долго не отвечает")
    except KeyError:
        # CoinGecko может вернуть пустой ответ при превышении лимита запросов
        messagebox.showerror("Ошибка", "API не вернуло цену. Попробуйте позже")
    except Exception as e:
        # print("Ошибка:", e)
        messagebox.showerror("Ошибка", "Что-то пошло не так: " + str(e))


# ---------- Окно ----------
window = tk.Tk()
window.title("Курсы криптовалют")
window.geometry("350x250")
window.configure(bg="#f0f0f0")

# Фикс для macOS, чтобы не было белого текста на белом фоне
style = ttk.Style()
style.theme_use('classic')

title_label = tk.Label(window, text="Курс криптовалюты к USD",
                       font=("Arial", 14), bg="#f0f0f0", fg="black")
title_label.pack(pady=15)

combo = ttk.Combobox(window, values=list(coins.keys()), state="readonly")
combo.pack(pady=5)

button = tk.Button(window, text="Получить курс", command=show_price,
                   bg="#f0f0f0", fg="black")
button.pack(pady=10)

result_label = tk.Label(window, text="Курс появится здесь",
                        font=("Arial", 16), bg="#f0f0f0", fg="black")
result_label.pack(pady=20)

window.mainloop()
