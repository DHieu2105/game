import tkinter as tk

# ================== TẠO WINDOW ==================
root = tk.Tk()
root.title("Ô Ăn Quan")
root.geometry("800x500")
root.configure(bg="#d9d9d9")

# ================== FRAME ==================
start_frame = tk.Frame(root, bg="#d9d9d9")
mode_frame = tk.Frame(root, bg="#d9d9d9")

start_frame.pack(fill="both", expand=True)


# ================== HÀM CHUYỂN MÀN ==================
def show_mode():
    start_frame.pack_forget()
    mode_frame.pack(fill="both", expand=True)


def back_to_start():
    mode_frame.pack_forget()
    start_frame.pack(fill="both", expand=True)


# ================== MÀN HÌNH 1 ==================
title = tk.Label(
    start_frame,
    text="Game Ô Ăn Quan",
    font=("Arial", 24),
    bg="#d9d9d9"
)
title.pack(pady=100)

start_btn = tk.Button(
    start_frame,
    text="START",
    font=("Arial", 18),
    bg="#4a7bdc",
    fg="white",
    width=15,
    height=2,
    command=show_mode
)
start_btn.pack()


# ================== MÀN HÌNH 2 ==================
title2 = tk.Label(
    mode_frame,
    text="Chọn chế độ chơi",
    font=("Arial", 22),
    bg="#d9d9d9"
)
title2.pack(pady=80)


# ===== Nút PvP =====
btn_pvp = tk.Button(
    mode_frame,
    text="👤 VS 👤",
    font=("Arial", 18),
    bg="#4a7bdc",
    fg="white",
    width=15,
    height=2,
    command=lambda: print("PvP")
)
btn_pvp.pack(pady=10)


# ===== Nút PvAI =====
btn_pvai = tk.Button(
    mode_frame,
    text="👤 VS 🤖",
    font=("Arial", 18),
    bg="#4a7bdc",
    fg="white",
    width=15,
    height=2,
    command=lambda: print("PvAI")
)
btn_pvai.pack(pady=10)


# Nút setting (chưa xử lý)
tk.Button(
    root,
    text="⚙",
    font=("Arial", 20)
).place(x=10, y=10)

# Nút thoát game
tk.Button(
    root,
    text="❌",
    font=("Arial", 20),
    command=root.destroy
).place(x=750, y=10)


# ================== CHẠY ==================
root.mainloop()