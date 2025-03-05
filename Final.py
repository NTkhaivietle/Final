import tkinter as tk
import os
import random
import subprocess
import platform

# Function to automatically choose the default folder based on OS
def get_default_folder():
    if platform.system() == "Linux":
        # Default folder for Linux
        return os.path.expanduser("~/Videos")
    else:
        # Default folder for Windows
        return os.path.expanduser(r"C:\Users\Public\Videos")

# Function to play a random video from the folder and show a text tab afterward
def play_random_video(folder):
    videos = [f for f in os.listdir(folder) if f.endswith(('.mp4', '.avi', '.mkv'))]
    if videos:
        video = random.choice(videos)
        video_path = os.path.join(folder, video)
        print(f"Playing video: {video_path}")
        try:
            if platform.system() == "Linux":
                # Use `mpv` as it supports fullscreen natively and exits after playback
                subprocess.run(['mpv', '--fs', video_path])  # Fullscreen flag for mpv
            elif platform.system() == "Windows":
                # Use `start` to open the default media player in fullscreen
                # Note: Some media players on Windows may not support direct fullscreen
                os.system(f'"" "{video_path}" /fullscreen')
            else:
                print("Unsupported operating system for this function.")
        except Exception as e:
            print(f"Error playing video: {e}")
    else:
        print("No videos found in the selected folder!")

# Function to display a new tab with some text
def show_text_tab():
    text_tab = tk.Toplevel()  # Create a new top-level window (tab)
    text_tab.title("Information")
    text_tab.geometry("400x300")  # Set the size of the tab

    label = tk.Label(text_tab, text="The video has finished playing!", font=("Arial", 14))
    label.pack(pady=50)

    # Add a button to close the tab
    close_button = tk.Button(text_tab, text="Close", command=text_tab.destroy, bg="brown", fg="white")
    close_button.pack(pady=20)

# Function to automatically play videos from the default folder
def play_videos_auto():
    folder = get_default_folder()
    if folder and os.path.exists(folder):
        play_random_video(folder)
    else:
        print("Default folder not found or doesn't exist!")

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

    # Add a button to automatically play videos
    auto_button = tk.Button(root, text="Play Random Video", command=play_videos_auto, bg="brown", fg="white")
    canvas.create_window(400, 300, anchor="center", window=auto_button)

    root.mainloop()

# Run the GUI
setup_gui()
