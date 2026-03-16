import tkinter as tk
import random
from tkinter import messagebox


class NumberCipher:
    def __init__(self, root):
        self.root = root

        # Generating a random 5 digit number
        self.target = [str(random.randint(0, 9)) for _ in range(5)] #number gen
        self.attempts = 0
        self.max_attempts = 10

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady=10)

        self.labels = []  # This will hold our grid of squares

        for r in range(self.max_attempts):
            row_labels = []
            for c in range(5):
                # Create a label for each box in the 10x5 grid
                lbl = tk.Label(self.grid_frame, text="", width=4, height=2,
                               font=("Arial", 20, "bold"), bg="lightgrey", relief="groove")
                lbl.grid(row=r, column=c, padx=5, pady=5)
                row_labels.append(lbl)
            self.labels.append(row_labels)

        # Set up the Input Area
        self.input_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.input_var, font=("Arial", 16), justify="center", width=10)
        self.entry.pack(pady=10)

        # Bind the 'Enter' key to the check_guess function
        self.entry.bind("<Return>", self.check_guess)

        self.submit_btn = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=self.check_guess)
        self.submit_btn.pack(pady=5)

        # Print the answer to the terminal for testing/debugging!
        print("Psst! The target is:", "".join(self.target))

    def check_guess(self, event=None):
        guess = self.input_var.get()

        # Validate user input
        if len(guess) != 5 or not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter exactly 5 numbers.")
            return

        if self.attempts >= self.max_attempts:
            return

        # Wordle Logic Evaluation
        target_copy = self.target.copy()
        guess_list = list(guess)
        colors = ["lightgrey"] * 5  # Default all to grey

        # First pass: Check for exact matches (Green)
        for i in range(5):
            if guess_list[i] == target_copy[i]:
                colors[i] = "lightgreen"
                target_copy[i] = None  # Mark as 'used' so we don't count it again
                guess_list[i] = None

        # Second pass: Check for partial matches (Yellow)
        for i in range(5):
            if guess_list[i] is not None and guess_list[i] in target_copy:
                colors[i] = "yellow"
                # Find where it is in the target and mark it 'used' to handle duplicate numbers accurately
                target_copy[target_copy.index(guess_list[i])] = None

                # Update the UI Grid with the colors and numbers
        for i in range(5):
            lbl = self.labels[self.attempts][i]
            lbl.config(text=guess[i], bg=colors[i])

        self.attempts += 1
        self.input_var.set("")  # Clear the entry box for the next guess

        # Check for Win/Loss conditions
        if colors.count("lightgreen") == 5:
            messagebox.showinfo("You Win!", f"Awesome! You guessed it in {self.attempts} tries.")
            self.submit_btn.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)
        elif self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"Out of guesses! The number was {''.join(self.target)}.")
            self.submit_btn.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)

    # New method to reset the game state for a new game (called when going back to the menu) -Hernandez
    def reset(self):
        self.target = [str(random.randint(0, 9)) for _ in range(5)]
        self.attempts = 0
        for row in self.labels:
            for lbl in row:
                lbl.config(text="", bg="lightgrey")
        self.input_var.set("")
        self.submit_btn.config(state=tk.NORMAL)
        self.entry.config(state=tk.NORMAL)
        print("Psst! The target is:", "".join(self.target))


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberCipher(root)
    root.mainloop()