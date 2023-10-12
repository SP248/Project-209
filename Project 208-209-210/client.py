import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import time


PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
song_counter = 0
song_selected = None
infoLabel = None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    global song_counter
    global infoLabel
    global song_selected

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()
setup()


def musicWindow():
  window = Tk()
  window.title("Music Window")
  window.geometry("300x300")
  window.configure(bg = 'LightSkyBlue')
  for file in os.listdir('shared_files'):
     filename = os.fsdecode(file)
     listbox.insert(song_counter, filename)
     song_counter = song_counter + 1


  selectlabel = Label(window, text = "Select Song",bg = "LightSkyBlue", font = ("Calibri"))
  selectlabel.place(x=2,y=1)

  listbox = Listbox(window, height = 10, width = 39, activestyle='dotbox',bg = 'LightSkyBlue',borderwidth = 2, font = ("Calibri", 10))
  listbox.place(x=10,y=10)

  scrollbar = Scrollbar(listbox)
  scrollbar.place(relheight = 1, relx=1)
  scrollbar.config(command = listbox.yview)

  PlayButton = Button(window, text="Play", width = 10, bd = 1, bg = "SkyBlue", font = ("Calibri",10), command = play)
  PlayButton.place(x=30,y=200)

  Stop = Button(window, text = "Stop", bd = 1, width = 10,bg = "SkyBlue", font = ("Calibri", 10), command=stop)
  Stop.place(x=200,y=200)

  Upload = Button(window, text="Upload",width = 10,bd = 1,bg = "SkyBlue", font = ("Calibri", 10))
  Upload.place(x=30,y=250)

  Download = Button(window, text = "Download", width=10, bd=1,bg = "SkyBlue", font = ("Calibri", 10))
  Download.place(x=200,y=250)

  infoLabel = Label(window,text="", fg="blue", font = ("Calibri", 0))
  infoLabel.place(x=4,y=280)


  window.mainloop()


def play():
   global song_selected
   song_selected = Listbox.get(ANCHOR)

   pygame
   mixer.init()
   mixer.music.load('shared_files/'+song_selected)
   mixer.music.play()
   if(song_selected != ""):
      infoLabel.configure(text="Now Playing: " + song_selected)
   else:
      infoLabel.configure(text = "")

def stop():
   global song_selected
   pygame
   mixer.init()
   mixer.music.load('shared_files'+song_selected)
   mixer.music.pause()
   infoLabel.configure(text="")
