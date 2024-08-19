import tkinter as tk
import os
import pygame as pg

root = tk.Tk()

root.title("Music Player")
root.geometry("600x400")
root.resizable(0, 0)

status = tk.StringVar()
pg.init()
pg.mixer.init()

# Btn functions

def playMusic():
    showSongName.config(state="normal")
    showSongName.delete("1.0", "end")
    showSongName.insert("1.0", playlist.get("active"))
    showSongName.config(state="disabled")
    status.set("Playing")
    pg.mixer.music.load(playlist.get("active"))
    pg.mixer.music.play()

def stopMusic():
    status.set("Stopped")
    pg.mixer.music.stop()

def resumeMusic():
    status.set("Resumed")
    pg.mixer.music.unpause()

def pauseMusic():
    status.set("Paused")
    pg.mixer.music.pause()

# Song Playlist

songFrame = tk.LabelFrame(root, text="Playlist", bg="black", fg="white", bd=5, font=("Arial",10))
songFrame.place(x = 10, y = 1, width=580, height=210)

scrollY = tk.Scrollbar(songFrame, orient="vertical")

playlist = tk.Listbox(songFrame, bg="silver", fg="black", font=("Arial", 10), selectmode="single", selectbackground="black", selectforeground="white", height="100", yscrollcommand=scrollY.set)

scrollY.pack(fill="y", side="right")
scrollY.config(command=playlist.yview)

playlist.pack(fill="both")

# Song Track

trackFrame = tk.LabelFrame(root, text="Track", bg="black", fg="white", bd=5, font=("Arial",10))
trackFrame.place(x = 10, y = 213, width=580, height=90)

showSongName = tk.Text(trackFrame, bg="white", fg="black", width=50, height=1, state="disabled")
showSongName.grid(row=0, column=0, padx=20, pady=13)

showStatus = tk.Label(trackFrame, bg="white", fg="black", width=15, textvariable=status)
showStatus.grid(row=0, column=1)

# Control Panel

ctrPanel = trackFrame = tk.LabelFrame(root, text="Control Panel", bg="black", fg="white", bd=5, font=("Arial",10), padx=15)
ctrPanel.place(x = 10, y = 305, width=580, height=90)

playBtn = tk.Button(ctrPanel, text="Play", width=15, command=playMusic)
playBtn.grid(row=0, column=0, padx=10, pady= 20)

stopBtn = tk.Button(ctrPanel, text="Stop", width=15, command=stopMusic)
stopBtn.grid(row=0, column=1, padx=10, pady= 20)

resumeBtn = tk.Button(ctrPanel, text="Resume", width=15, command=resumeMusic)
resumeBtn.grid(row=0, column=2, padx=10, pady= 20)

pauseBtn = tk.Button(ctrPanel, text="Pause", width=15, command=pauseMusic)
pauseBtn.grid(row=0, column=3, padx=10, pady= 20)

os.chdir(r"D:\Audio\AI")
myMusics = os.listdir()
for music in myMusics:
    if (".mp3" or ".flac" or ".wav" or ".ogg") in music:
        playlist.insert("end", music)

root.mainloop()