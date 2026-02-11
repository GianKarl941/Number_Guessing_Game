import tkinter as tk
from tkinter import font as tkfont


def display_credits(self):
    credits_text = """
    Developed by:
    •  Hernandez, Gian Karl
    •  Recuenco, Allen Xavier
    •  Sagisi, Janelle
    •  Andan, Sean Regnauld
    """
    credits_label = tk.Label(self, text=credits_text, font=tkfont.Font(family='Helvetica', size=12))
    credits_label.pack(pady=10)