import tkinter as tk
from tkinter import ttk

# Список монет, которые покажем в выпадающем списке
coins = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana",
    "Dogecoin": "dogecoin",
    "Cardano": "cardano",
    "Ripple": "ripple",
}

def show_price():
    # Пока только проверяем, что кнопка работает
    coin_name = combo.get()
    result_label.config(text="Выбрано: " + coin_name)

# ------------ Окно ------------
window = tk.Tk()
window.title("Курсы криптовалют")
window.geometry("350x250")
window.configure(bg="#f0f0f0")

# Фикс для macOS, чтобы не было белого текста на белом фоне
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