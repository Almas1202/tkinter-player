from tkinter import *
from pygame import mixer
from tkinter import filedialog as fd
from os import path

def openfile():
    song = fd.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    song1 = song
    full_name = path.basename(song1)
    name = path.splitext(full_name)[0]
    song_box.insert(END, name)
    d[name] = song

def openfiles():
    songs = fd.askopenfilenames(initialdir='tracks/', title="Выберите песни!", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        full_name = path.basename(song)
        name = path.splitext(full_name)[0]
        song_box.insert(END, name)
        d[name] = song

def play():
    song = song_box.get(ACTIVE)
    mixer.music.load(d[song])
    mixer.music.play()
    song_state['text'] = "Воспроизведение"

def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Остановлено"

def pause():
    if song_state['text'] == "Воспроизведение":
        mixer.music.pause()
        song_state['text'] = "Остановлено"

    else:
        mixer.music.unpause()
        song_state['text'] = "Воспроизведение"

def next_song():
    next_s = song_box.curselection()
    next_s = next_s[0] + 1
    song = song_box.get(next_s)
    mixer.music.load(d[song])
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)
    song_state['text'] = "Воспроизведение"

def prev_song():
    next_s = song_box.curselection()
    next_s = next_s[0] - 1
    song = song_box.get(next_s)
    mixer.music.load(d[song])
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)
    song_state['text'] = "Воспроизведение"

blue = '#78DBE2'
red = '#FF033E'
green = '#4B5320'
yellow = '#FFDB58'

color = blue
color1 = '#6E5160'

d = {}

mixer.init()
root = Tk()
root.title('Плеер')

master_frame = Frame(root)
master_frame.pack()

info_frame = Frame(master_frame)
info_frame.grid(row=1, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=2, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=0)

master_frame['bg']=color
info_frame['bg']=color
controls_frame['bg']=color
file_frame['bg']=color 

#CONTROLS FRAME
back_button = Button(controls_frame, width=5, text = '<-', bg = color1, command = prev_song)
back_button.grid(row=0, column=0)

forward_button = Button(controls_frame, width=5, text = '->', bg = color1,  command = next_song)
forward_button.grid(row=0, column=4)

play_button = Button(controls_frame, width=2, text = '|>', bg = color1,  command = play)
play_button.grid(row=1, column=1)

pause_button = Button(controls_frame, width=2, text = '||', bg = color1,  command = pause)
pause_button.grid(row=1, column=2)

stop_button = Button(controls_frame, text = 'X', bg = color1,  command = stop)
stop_button.grid(row=1, column=3)
  
#FILE FRAME
openfile_button = Button(file_frame, text = 'Открыть файл', bg = color, command = openfile)
openfile_button.grid(row=0, column=0)

openfolder_button = Button(file_frame, text = 'Открыть папку', bg = color, command = openfiles)
openfolder_button.grid(row=0, column=1)

#INFO FRAME
song_state = Label(info_frame, width=35, text="Нет песен", bg = color, font="Arial 8 bold")
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=30, bg = '#B5B8B1', selectbackground="black")
song_box.grid(row=1, column=0)

space = Label(file_frame, width = 10, text = '', bg = color)
space.grid(row = 1, column = 0)

root.mainloop()