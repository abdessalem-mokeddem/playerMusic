import tkinter as tk
import os
import fnmatch
import pygame
from pygame import mixer


music = tk.Tk()
music.title("Musique player")
music.geometry("500x500")
music.config(bg='black')

rootpath ="musicpython"
pattern ="*.mp3"

mixer.init()


box=tk.Listbox(music, fg="cyan", bg="black",width=100, font=('arial',14))
box.pack(padx=15, pady=15)


for root, dirs,files in os.walk(rootpath):
 for filename in fnmatch.filter(files,pattern):
  box.insert('end',filename) 

def select():
  font.config(text=box.get("anchor"))
  mixer.music.load(rootpath + "\\" + box.get("anchor"))
  mixer.music.play()

def stop():
    mixer.music.stop()
    box.select_clear('active')

def suv():
    suiv_song = box.curselection()
    suiv_song = suiv_song[0]+1
    suiv_song_nom =box.get(suiv_song)

    font.config(text=suiv_song_nom)

    mixer.music.load(rootpath +"\\"+ suiv_song_nom)
    mixer.music.play()
   
    box.select_clear(0,'end')
    box.activate(suiv_song)
    box.select_set(suiv_song)

def prec():
    avant_song = box.curselection()
    avant = avant_song[0] - 1
    avant_song_nom = box.get(avant)

    font.config(text=avant_song_nom)

    mixer.music.load(rootpath + "\\" + avant_song_nom)
    mixer.music.play()
  
    box.select_clear(0, 'end')
    box.activate(avant_song)
    box.select_set(avant_song)

def pause():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"

font =tk.Label(music, text="", bg='black', fg='blue', font=('arial',20))
font.pack(pady=15)

frame=tk.Frame(music,bg='blue')
frame.pack(padx=10, pady=5, anchor='center')

precButton = tk.Button(music, text="prec",command=prec)
precButton.pack(pady=15,in_=frame,side="left")
stopButton = tk.Button(music, text="stop", command=stop)
stopButton.pack(pady=15, in_=frame,side="left")
playButton = tk.Button(music, text="play", command=select)
playButton.pack(pady=15,in_=frame,side="left")
pauseButton = tk.Button(music, text="pause",command=pause)
pauseButton.pack(pady=15, in_=frame,side="left")
suvButton = tk.Button(music, text="suv",command=suv)
suvButton.pack(pady=15,in_=frame,side="left")

def update_progressbar(progressbar, value):
    progressbar["value"] = value

root = tk.Tk()
root.title("Barre de navigation")

frame = tk.Frame(root)
frame.pack(padx=15, pady=15)

for i in range(101):
    root.update()

root.mainloop()

music.mainloop()