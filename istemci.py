import tkinter as tk

def calculate_interest():
    gold = float(gold_entry.get())
    army_size = int(army_entry.get())
    interest = (gold * army_size) * 0.05
    interest_label.config(text="Interest: {:.2f}".format(interest))

root = tk.Tk()
root.title("Micro Cheat")

# Arayüz bileşenlerinin oluşturulması
title_label = tk.Label(root, text="Micro Cheat", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

option_frame = tk.Frame(root)
option_frame.pack(pady=10)

average_button = tk.Button(option_frame, text="Average Micro")
average_button.pack(side=tk.LEFT, padx=5)

god_button = tk.Button(option_frame, text="God Micro")
god_button.pack(side=tk.LEFT, padx=5)

bot_frame = tk.Frame(root)
bot_frame.pack(pady=10)

bot_label = tk.Label(bot_frame, text="Saldırılan Bot:")
bot_label.pack(side=tk.LEFT)

bot_entry = tk.Entry(bot_frame)
bot_entry.pack(side=tk.LEFT)

gold_frame = tk.Frame(root)
gold_frame.pack(pady=10)

gold_label = tk.Label(gold_frame, text="Altın:")
gold_label.pack(side=tk.LEFT)

gold_entry = tk.Entry(gold_frame)
gold_entry.pack(side=tk.LEFT)

army_frame = tk.Frame(root)
army_frame.pack(pady=10)

army_label = tk.Label(army_frame, text="Asker Sayısı:")
army_label.pack(side=tk.LEFT)

army_entry = tk.Entry(army_frame)
army_entry.pack(side=tk.LEFT)

calculate_button = tk.Button(root, text="Hesapla", command=calculate_interest)
calculate_button.pack(pady=10)

interest_label = tk.Label(root, text="Interest: ")
interest_label.pack()

version_label = tk.Label(root, text="Sürüm 0.8.12, Yapımcı: Shellbee")
version_label.pack(pady=10)

root.mainloop()
