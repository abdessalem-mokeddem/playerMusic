import tkinter as tk
import os
import fnmatch
from pygame import mixer
from tkinter import filedialog

def ouverture():
    fichier_nom = filedialog.askopenfilename(initialdir="/",
                                            title="Selectionne un fichier",
                                            filetypes=(("Fichier text",
                                            "*.txt*"),
                                            ("Toutes les fichiers",
                                            "*.*")))


def volume(event):
    mixer.music.set_volume(volume_musique.get())


def lecture():
    label.config(text=liste.get("anchor"))
    mixer.music.load(rootpath + "\\" + liste.get("anchor"))
    mixer.music.play()


def boucle():
    label.config(text=liste.get("anchor"))
    mixer.music.load(rootpath + "\\" + liste.get("anchor"))
    mixer.music.play(loops=-1)


canvas = tk.Tk()
canvas.title("Musique player")
canvas.geometry("600x600")
canvas.config(bg='black')

rootpath = "musicpython"
pattern = "*.mp3"


mixer.init()

liste = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('arial', 14))
liste.pack(padx=15, pady=15)

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        liste.insert('end', filename)  

def select():
    label.config(text=liste.get("anchor"))
    mixer.music.load(rootpath + "\\" + liste.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    liste.select_clear('active')


def suv():
    son = liste.curselection()
    son = son[0] + 1
    suiv_song_nom = liste.get(son)

    label.config(text=suiv_song_nom)

    mixer.music.load(rootpath + "\\" + suiv_song_nom)
    mixer.music.play()
    liste.select_clear(0, 'end')
    liste.activate(son)
    liste.select_set(son)


def prec():
    avant_song = liste.curselection()
    avant_song_song = avant_song[0] - 1
    nom_son = liste.get(avant_song_song)

    label.config(text=nom_son)

    mixer.music.load(rootpath + "\\" + nom_son)
    mixer.music.play()
    
    liste.select_clear(0, 'end')
    liste.activate(avant_song)
    liste.select_set(avant_song)

def pause():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"

#
volume_musique = tk.Scale(canvas, from_=0, to_=1.0, orient="horizontal", resolution=0.1,showvalue=0, command=volume)
volume_musique.set(0.8)
volume_musique.pack()

label = tk.Label(canvas, text="", bg='black', fg='blue', font=('arial', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg='blue')
top.pack(padx=10, pady=5, anchor='center')

precButton = tk.Button(canvas, text="prec", command=prec)
precButton.pack(pady=15, in_=top, side="left")
stopButton = tk.Button(canvas, text="stop", command=stop)
stopButton.pack(pady=15, in_=top, side="left")
playButton = tk.Button(canvas, text="play", command=select)
playButton.pack(pady=15, in_=top, side="left")
pauseButton = tk.Button(canvas, text="pause", command=pause)
pauseButton.pack(pady=15, in_=top, side="left")
suvButton = tk.Button(canvas, text="suv", command=suv)
suvButton.pack(pady=15, in_=top, side="left")
bclButton = tk.Button(canvas, text="Réécouter", command=boucle)
bclButton.pack(ipady=15, in_=top, side="left")
ouv_btn = tk.Button(canvas, text="Ajouter", command=ouverture)
ouv_btn.pack(pady=15, in_=top, side="left")

canvas.mainloop()
