from cgitb import text
from platform import python_branch
from sqlite3 import Row
import tkinter as tk
import clipboard
from colorama import Fore
import pyautogui
import webbrowser
import time


my_w = tk.Tk()
my_w.geometry("350x350")
my_w.title("atalho de suporte")
global data

telefone = ('44999624068')


def teste_select():
    global data
    pyautogui.hotkey('win')
    pyautogui.typewrite('bloco de notas')
    time.sleep(3)
    pyautogui.typewrite('https://wa.me/', telefone)


b1 = tk.Button(my_w, text='Selecionar', command=lambda: teste_select(),
               font=20, bg='lightyellow')
b1.grid(row=1, column=1, padx=2, pady=5)
