# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0]
# Embedded file name: irgendwas.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess, random, os, time, speech_recognition as sr, threading, hashlib, sys
CORRECT_PASSWORD_HASH = hashlib.sha256("Ben2013".encode()).hexdigest()
balu_wake_counter = 0
pass_counter = 0
import subprocess, os

def start_keyboard():
    tap_tip_path = "C:\\Program Files\\Common Files\\microsoft shared\\ink\\TabTip.exe"
    osk_path = "C:\\Windows\\System32\\osk.exe"
    if os.path.exists(tap_tip_path):
        subprocess.Popen(f'start "" "{tap_tip_path}"', shell=True)
    else:
        if os.path.exists(osk_path):
            subprocess.Popen(f'start "" "{osk_path}"', shell=True)
        else:
            print("Keine Bildschirmtastatur gefunden.")


start_keyboard()

def angry_Balu():
    """Funktion, die ausgeführt wird, wenn Balu wütend wird."""
    global current_random_number
    output = "Balu has bited you mow the number will be choisen by Balu."
    text_output.insert(tk.END, f"{output}\n")
    current_random_number = random.randint(1, 100)


def kill_game(process_name):
    """Beendet einen Prozess mit dem angegebenen Namen."""
    try:
        subprocess.run(f"taskkill /IM {process_name} /F", shell=True, check=True)
        print(f"Prozess {process_name} erfolgreich beendet.")
    except subprocess.CalledProcessError as e:
        try:
            print(f"Fehler beim Beenden des Prozesses {process_name}: {e}")
        finally:
            e = None
            del e


def initialize_game():
    """Initialize or restart the game."""
    global current_random_number
    current_random_number = random.randint(1, 100)
    messagebox.showinfo("Game Started", "Guess the random number between 1 and 100!")
    text_output.delete("1.0", tk.END)


def run_commandParse error at or near `COME_FROM' instruction at offset 414_0


def start_game():
    global entry
    global game_window
    global text_output
    game_window = tk.Toplevel(root)
    game_window.title("Mr.X Game")
    game_window.configure(bg="#FFFFFF")
    game_window.geometry("600x400")
    game_window.iconbitmap("icon.ico")
    btn_game.config(state=(tk.DISABLED))
    game_window.protocol("WM_DELETE_WINDOW", lambda: (game_window.destroy(), btn_game.config(state=(tk.NORMAL))))
    text_output = tk.Text(game_window,
      height=15, width=70, bg="#FFFFFF", fg="#000000", insertbackground="#FFFFFF",
      font=('', 12))
    text_output.pack(pady=10)
    entry = tk.Entry(game_window, width=60, bg="#ffffff", fg="#000000", font=('Segoe UI',
                                                                              12))
    entry.pack()
    entry.bind("<Return>", lambda event: run_command())
    button_exec = tk.Button(game_window,
      text="Guess", command=run_command, bg="#ffffff",
      fg="#000000",
      font=('Segoe UI', 10))
    button_exec.pack(pady=10)
    initialize_game()


root = tk.Tk()
root.title("Main Menü")
root.geometry("350x200")
root.configure(bg="#FFFFFF")
root.resizable(False, False)
root.iconbitmap("icon.ico")
label = tk.Label(root, text="Welcome! Choose an option:", font=('Segoe UI', 12), bg="#FFFFFF", fg="#000000")
label.pack(pady=20)
btn_game = tk.Button(root, text="🎮  Start MR.X", command=start_game, font=('Segoe UI',
                                                                           11),
  bg="white",
  fg="#000000",
  width=25)
btn_game.pack(pady=5)
root.mainloop()
# global balu_wake_counter ## Warning: Unused global
# global pass_counter ## Warning: Unused global