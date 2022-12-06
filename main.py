import tkinter as tk
from tkinter import ttk

import gamescreen
import score_screen
from game import *
from constants import *


diff_dict_002 = {
    "EASY": EASY,
    "MEDIUM": MEDIUM,
    "HARD": HARD,
}


def btnSinglePlayer_click_002(root_002):
    game_002.start_002(difficulty=diff_dict_002[comboDifficulty_002.get()])
    gamescreen.show_002(
        root_002, diff_dict_002[comboDifficulty_002.get()], game_type_002="single"
    )


def btnMultiPlayer_click_002(root_002):
    ret_list = []
    gamescreen.show_002(
        root_002, diff_dict_002[comboDifficulty_002.get()], 1, ret_list, "multi"
    )
    if len(ret_list) > 0:
        game_002.start_002(diff_dict_002[comboDifficulty_002.get()], ret_list[0])
        gamescreen.show_002(
            root_002, diff_dict_002[comboDifficulty_002.get()], 2, game_type_002="multi"
        )
    else:
        root_002.deiconify()


def btnHighScores_click_002(root_002):
    root_002.withdraw()
    score_screen.show_002(root_002)


root_002 = tk.Tk()
root_002.title("Mainscreen")
root_002.configure(bg=BGCOLOR_002)
root_002.geometry("400x600")

frame_002 = tk.Frame(root_002)
frame_002.config(bg=BGCOLOR_002)

comboDifficulty_002 = tk.ttk.Combobox(
    frame_002,
    values=["EASY", "MEDIUM", "HARD"],
    font=(FONTFACE_002, 15),
    state="readonly",
)
comboDifficulty_002.current(0)
comboDifficulty_002.grid(row=1, column=0, pady=10)

btnSinglePlayer_002 = tk.Button(
    frame_002,
    text="Single Player",
    font=(FONTFACE_002, 15),
    bg=BGCOLOR_002,
    fg=FGCOLOR_002,
    command=lambda: btnSinglePlayer_click_002(root_002),
)
btnSinglePlayer_002.grid(row=2, column=0, pady=10)

btnTwoPlayer_002 = tk.Button(
    frame_002,
    text="Multi Player",
    font=(FONTFACE_002, 15),
    bg=BGCOLOR_002,
    fg=FGCOLOR_002,
    command=lambda: btnMultiPlayer_click_002(root_002),
)
btnTwoPlayer_002.grid(row=3, column=0, pady=10)

btnScores_002 = tk.Button(
    frame_002,
    text="Scores",
    font=(FONTFACE_002, 15),
    bg=BGCOLOR_002,
    fg=FGCOLOR_002,
    command=lambda: btnHighScores_click_002(root_002),
)
btnScores_002.grid(row=4, column=0, pady=10)

frame_002.pack(expand=True)

root_002.mainloop()
