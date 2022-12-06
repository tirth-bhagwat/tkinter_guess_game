import tkinter as tk
from tkinter import messagebox, simpledialog
from constants import *


def show_002(
    root_002, difficulty, player_num_002=2, ret_list_002=None, game_type_002="single"
):
    def btnNumber_click(number_002):

        if player_num_002 == 1:
            ret_list_002.append(number_002)
            game_screen_002.destroy()
            game_screen_002.quit()
            return

        result_002 = game_002.guess_002(number_002)

        lblLife_002.config(
            text=("♥ " * game_002.attemptsRemaining_002)
            + ("♡ " * (3 - game_002.attemptsRemaining_002))
        )
        if result_002 == 0:
            lblHint_002.config(text="Correct!", fg=FGCOLOR_002)
        elif result_002 == -1:
            lblHint_002.config(text="Too low!", fg=HINTCOLOR_002)
        elif result_002 == 1:
            lblHint_002.config(text="Too high!", fg=HINTCOLOR_002)

        if game_002.gameResult_002 == False:
            messagebox.showinfo("Game Over", "You lose!")
            game_screen_002.destroy()
            root_002.deiconify()

        if game_002.gameResult_002 == True:
            messagebox.showinfo("Game Over", "You win!")

            if game_type_002 == "single":
                username = simpledialog.askstring(
                    "Username",
                    "Please enter your username to save your score. \n If you don't want to save your score, just leave it blank.",
                )

                if username is not None and username.strip() != "":
                    game_002.database_002.insert_score_002(
                        username=username.strip(),
                        difficulty=game_002.difficulty,
                        score=game_002.score_002["score"],
                        time_taken=game_002.score_002["time"],
                    )

            game_screen_002.destroy()
            root_002.deiconify()

    def onWindowClose_002():
        root_002.deiconify()
        game_screen_002.destroy()
        game_002.stop_002()
        game_screen_002.quit()

    root_002.withdraw()

    if player_num_002 == 1:
        instruction_002 = "Select a number to be guessed by your opponent."
    else:
        instruction_002 = "A number has been generated between 1 and 10. \n Try to guess the number in as few attempts as possible.\n Max attempts: 3"

    game_screen_002 = tk.Toplevel(root_002)
    game_screen_002.title("Guessing Game")
    game_screen_002.geometry("800x600")
    game_screen_002.configure(bg=BGCOLOR_002)
    game_screen_002.resizable(False, False)

    frame_002 = tk.Frame(game_screen_002)
    frame_002.config(bg=BGCOLOR_002)

    lblTitle_002 = tk.Label(
        frame_002,
        text="Guessing Game",
        font=(FONTFACE_002, 20),
        bg=BGCOLOR_002,
        fg=FGCOLOR_002,
    )
    lblTitle_002.grid(row=0, column=0, pady=10)

    lblInstruction_002 = tk.Label(
        frame_002,
        text=instruction_002,
        font=(FONTFACE_002, 15),
        bg=BGCOLOR_002,
        fg=FGCOLOR_002,
    )
    lblInstruction_002.grid(row=1, column=0, pady=10)

    lblLife_002 = tk.Label(
        frame_002,
        text="♥ " * 3,
        font=(FONTFACE_002, 25),
        bg=BGCOLOR_002,
        fg="#ff0000",
    )
    if player_num_002 != 1:
        lblLife_002.grid(row=2, column=0, pady=10)

    frame_buttons_002 = tk.Frame(frame_002)
    frame_buttons_002.config(bg=BGCOLOR_002)

    buttons_002 = []
    for i in range(difficulty):
        buttons_002.append(
            tk.Button(
                frame_buttons_002,
                text=i + 1,
                font=(FONTFACE_002, 15),
                bg=BGCOLOR_002,
                fg=FGCOLOR_002,
                command=lambda i=i: btnNumber_click(i + 1),
            )
        )
        buttons_002[-1].grid(row=i // 5, column=i % 5, padx=10, pady=10)

    frame_buttons_002.grid(row=3, column=0, pady=10)

    lblHint_002 = tk.Label(
        frame_002,
        text="",
        font=(FONTFACE_002, 15),
        bg=BGCOLOR_002,
        fg=FGCOLOR_002,
    )
    lblHint_002.grid(row=4, column=0, pady=10)

    frame_002.pack(expand=True)

    game_screen_002.protocol("WM_DELETE_WINDOW", onWindowClose_002)

    game_screen_002.mainloop()
