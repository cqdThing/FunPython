import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")

        pygame.mixer.init()

        self.is_playing = False
        self.current_song = None

        # Create buttons
        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=10)

        self.skip_button = tk.Button(root, text="Skip", command=self.skip_song)
        self.skip_button.pack(pady=10)

        self.load_button = tk.Button(root, text="Load", command=self.load_song)
        self.load_button.pack(pady=10)

        self.song_list = []

    def load_song(self):
        song_path = filedialog.askopenfilename(title="Select a song", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if song_path:
            self.song_list.append(song_path)
            self.current_song = song_path
            print(f"Loaded song: {os.path.basename(song_path)}")

    def play_song(self):
        if self.current_song:
            if not self.is_playing:
                pygame.mixer.music.load(self.current_song)
                pygame.mixer.music.play()
                self.is_playing = True
                print(f"Playing: {os.path.basename(self.current_song)}")

    def pause_song(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            print("Paused")

    def skip_song(self):
        if self.song_list:
            if self.is_playing:
                pygame.mixer.music.stop()
            current_index = self.song_list.index(self.current_song)
            next_index = (current_index + 1) % len(self.song_list)
            self.current_song = self.song_list[next_index]
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.is_playing = True
            print(f"Skipped to: {os.path.basename(self.current_song)}")

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()