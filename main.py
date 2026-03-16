# Number Guessing Game 
# A Group project by:
# Hernandez, Gian Karl
# Recuenco, Allen Xavier
# Sagisi, Janelle
# Andan, Sean Regnauld

# Importing necessary libraries (Pyhton 3.12.12 standard libraries)
from logging import root
import os
import tkinter as tk
from tkinter import font as tkfont
from tkinter import PhotoImage
import pygame
from pygame import mixer
from NumGuessGame_Python_logic_kinterfied import NumberCipher
# Menu class to create the main menu of the game
class GameApp(tk.Tk):
    """Main menu class for the number guessing game"""
    # these arguments allow for flexibility when creating instances for every class
    def __init__ (self, *args, **kwargs): 

        # no need to set the size of the window since it will adjust based on the content, but you can set a minimum size if desired
        tk.Tk.__init__(self, *args, **kwargs)
        # Make the window 1280x720 and allow resizing
        self.geometry("1280x720")
        self.resizable(width=True, height=True)
        # Set the title of the window
        self.title("Number Guessing Game! 👀")
        # Set the font for the title
        self.title_font = tkfont.Font(family='Comic Sans MS', size=42, weight="bold")

        # Default background color for the whole app
        self.bg_color = "#fff4ad"
        self.configure(bg=self.bg_color)

        # Container to hold the different frames (pages) of the game
        container = tk.Frame(self, bg=self.bg_color)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GamePage, CreditsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Place all frames in the same location; the one on the top of the stacking order will be visible
            frame.grid(row=0, column=0, sticky="nsew")
        # Apply background color to all created widgets/frames
        self.apply_bg_recursive(container)

        self.show_frame("StartPage")

    # Function to apply background color to all widgets recursively
    def apply_bg_recursive(self, widget):
        """Recursively set the background color for supported widgets."""
        bg = self.bg_color
        try:
            if isinstance(widget, (tk.Frame, tk.Label, tk.Entry, tk.Text, tk.Radiobutton, tk.Checkbutton, tk.Listbox, tk.Canvas)):
                widget.configure(bg=bg)
            if isinstance(widget, tk.Button):
                widget.configure(bg=bg, activebackground=bg)
        except tk.TclError:
            pass
        for child in widget.winfo_children():
            self.apply_bg_recursive(child)
    
    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    """Start page of the game where the user can start the game"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Number Ciphher™️", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # background handled by the app's global `bg_color`

        start_button = tk.Button(self, text="Start Game", command=lambda: controller.show_frame("GamePage"))
        start_button.pack()

        credits_button = tk.Button(self, text="Credits", command=lambda: controller.show_frame("CreditsPage"))
        credits_button.pack()
    
class GamePage(tk.Frame):
    """Game page where the user can play the game"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # background handled by the app's global `bg_color`

        # Instantiate the NumberCipher game
        self.game = NumberCipher(self)

        game_back_button = tk.Button(self, text="Back to Menu", command=lambda: [self.game.reset(), controller.show_frame("StartPage")])
        game_back_button.pack()

class CreditsPage(tk.Frame):
    """Credits page to displa
    y the credits of the game"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Credits Page", font=controller.title_font)
        label.pack(pady=20)

        # background handled by the app's global `bg_color`

        #Credits of the game
        import credits
        credits.display_credits(self) # Call the display_credits function from the credits module to

        credits_back_button = tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("StartPage"))
        credits_back_button.pack()
        # Add widgets to display results here (e.g., labels for correct/incorrect guesses, play again button, etc.)

if __name__ == "__main__":
    # Initialize pygame mixer before starting the app
    try:
        pygame.mixer.init()
        # Get the absolute path to the audio file relative to this script
        audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bg_music_5.wav")
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    except Exception as e:
        print(f"Audio playback error: {e}")
    app = GameApp()  # Create an instance of the GameApp class
    app.mainloop()  # Start the main event loop to run the application
