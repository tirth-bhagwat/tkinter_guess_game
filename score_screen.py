import tkinter as tk
from tkinter import ttk
from constants import *


def show_002(root_002):
    def onSelectionButton_click_002(button: tk.Button):
        for btn in btnList_002:
            if btn == button:
                btn.config(bg="gray")
            else:
                btn.config(bg="white")

        difficulty = (
            button.cget("text").upper() if button.cget("text") != "All" else None
        )

        tree_002.delete(*tree_002.get_children())

        for i, row in enumerate(game_002.database_002.get_scores_002(difficulty)):
            tree_002.insert("", i, text=i + 1, values=row)
            # tree_002.insert("", i, values=(i + 1,) + row)

    def onClose_002():
        high_scores_screen_002.destroy()
        high_scores_screen_002.quit()
        root_002.deiconify()

    root_002.withdraw()

    high_scores_screen_002 = tk.Toplevel(root_002)
    high_scores_screen_002.title("High Scores")
    high_scores_screen_002.geometry("600x600")
    high_scores_screen_002.resizable(False, False)

    frame_002 = tk.Frame(high_scores_screen_002)

    frame_buttons_002 = tk.Frame(frame_002)

    btnAll_002 = tk.Button(
        frame_buttons_002,
        text="All",
        command=lambda: onSelectionButton_click_002(btnAll_002),
        bg="gray",
    )
    btnAll_002.pack(side=tk.LEFT)

    btnEasy_002 = tk.Button(
        frame_buttons_002,
        text="Easy",
        command=lambda: onSelectionButton_click_002(btnEasy_002),
        bg="#ffffff",
    )
    btnEasy_002.pack(side=tk.LEFT)

    btnMedium_002 = tk.Button(
        frame_buttons_002,
        text="Medium",
        command=lambda: onSelectionButton_click_002(btnMedium_002),
        bg="#ffffff",
    )
    btnMedium_002.pack(side=tk.LEFT)

    btnHard_002 = tk.Button(
        frame_buttons_002,
        text="Hard",
        command=lambda: onSelectionButton_click_002(btnHard_002),
        bg="#ffffff",
    )
    btnHard_002.pack(side=tk.LEFT)

    btnList_002 = [btnAll_002, btnEasy_002, btnMedium_002, btnHard_002]

    frame_buttons_002.pack(padx=10, pady=10)

    tree_002 = ttk.Treeview(
        frame_002, columns=("Name", "Difficulty", "Score", "Time(s)")
    )
    tree_002.heading("#0", text="Rank")
    tree_002.heading("Name", text="Name")
    tree_002.heading("Difficulty", text="Difficulty")
    tree_002.heading("Score", text="Score")
    tree_002.heading("Time(s)", text="Time")

    tree_002.column("#0", width=50)
    tree_002.column("Name", width=100)
    tree_002.column("Difficulty", width=100)
    tree_002.column("Score", width=100)
    tree_002.column("Time(s)", width=100)

    data_002 = game_002.database_002.get_scores_002()

    for i, row in enumerate(data_002):
        tree_002.insert("", i, text=i + 1, values=row)

    tree_002.pack(fill="y", expand=True)

    frame_002.pack(padx=10, pady=10, fill="y", expand=True)

    high_scores_screen_002.protocol("WM_DELETE_WINDOW", onClose_002)

    high_scores_screen_002.mainloop()
