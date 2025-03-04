import tkinter as tk
from tkinter import filedialog
import os
import random
import subprocess
import platform

# Function to automatically choose default folder based on OS
def get_default_folder():
    if platform.system() == "Linux":
        # Default folder for Linux
        default_folder = os.path.expanduser("~/Videos")
    else:
        # Default folder for Windows
        default_folder = os.path.expanduser(r"C:\Users\Public\Videos")
    
    if os.path.exists(default_folder):
        return default_folder
    return None

# Function to play a random video from the folder
def play_random_video(folder):
    videos = [f for f in os.listdir(folder) if f.endswith(('.mp4', '.avi', '.mkv'))]
    if videos:
        video = random.choice(videos)
        video_path = os.path.join(folder, video)
        if platform.system() == "Linux":
            subprocess.run(['xdg-open', video_path])  # On Linux, uses default video player
        else:
            subprocess.run(['start', video_path], shell=True)  # On Windows
        
    else:
        print("No videos found in the selected folder!")

# Function to allow user to manually select a folder
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        play_random_video(folder)

# Function to play videos automatically from the default folder
def play_videos_auto():
    folder = get_default_folder()
    if folder:
        play_random_video(folder)
    else:
        print("Default folder not found! Please select a folder manually.")

# Function to draw a gradient background
def draw_gradient(canvas, color1, color2):
    width, height = canvas.winfo_width(), canvas.winfo_height()
    gradient_steps = 100  # Number of gradient steps
    for i in range(gradient_steps):
        ratio = i / gradient_steps
        r = int(color1[0] + ratio * (color2[0] - color1[0]))
        g = int(color1[1] + ratio * (color2[1] - color1[1]))
        b = int(color1[2] + ratio * (color2[2] - color1[2]))
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_rectangle(0, i * (height / gradient_steps), width, (i + 1) * (height / gradient_steps), outline="", fill=color)

# Setting up the GUI
def setup_gui():
    root = tk.Tk()
    root.title("Coffee Shop Video Player")
    root.geometry("800x600")  # Set a default window size

    # Create a canvas for the gradient background
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Update and draw the gradient after the window is rendered
    canvas.update_idletasks()
    draw_gradient(canvas, (85, 53, 34), (255, 198, 132))  # Coffee-themed colors (brown to light beige)

    # Add buttons
    select_button = tk.Button(root, text="Select Folder", command=select_folder, bg="brown", fg="white")
    select_button_window = canvas.create_window(400, 250, anchor="center", window=select_button)

    auto_button = tk.Button(root, text="Máy Test Độ Xinh Gái", command=play_videos_auto, bg="brown", fg="white")
    auto_button_window = canvas.create_window(400, 300, anchor="center", window=auto_button)

    root.mainloop()

# Run the GUI
setup_gui()
