import tkinter as tk
from tkinter import PhotoImage

# Initialize the main application window
parent = tk.Tk()
parent.title("Image in Button Example")

# Load the image
image = PhotoImage(file="muah.png")

# Create the Button widget and set the image
button = tk.Button(parent, image=image)
button.pack(pady=20)

# Keep a reference to the image 
# to prevent garbage collection
button.image = image

# Run the application
parent.mainloop()import tkinter as tk
from tkinter import PhotoImage

# Initialize the main application window
parent = tk.Tk()
parent.title("Image in Button Example")

# Load the image
image = PhotoImage(file="muah.png")

# Create the Button widget and set the image
button = tk.Button(parent, image=image)
button.pack(pady=20)

# Keep a reference to the image 
# to prevent garbage collection
button.image = image

# Run the application
parent.mainloop()