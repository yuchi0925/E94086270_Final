#!/usr/bin/env python
# coding: utf-8

# In[231]:


import librosa
import matplotlib.pyplot as plt
import librosa.display
import soundfile
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import pygame
import playsound


# In[232]:


import string
import random

# Randomly generated filename
def random_word():
    number_of_strings = 1
    length_of_string = 6
    for x in range(number_of_strings):
        word = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    return word        


# In[233]:


# set the speed of mixing music
def set_speed(speed):
    speed = str(speed)
    sr = sr_mix
    if speed=='0':
        sr = 22050
    elif speed=='1':
        sr = 26460
    elif speed=='2':
        sr = 30870    
    elif speed=='3':
        sr = 35280
    elif speed=='4':
        sr = 39690    
    elif speed=='-1':
        sr = 17640
    elif speed=='-2':
        sr = 13230
    elif speed=='-3':
        sr = 8820
    elif speed=='-4':
        sr = 4410     
    if flag_click==False or flag_click8==False:    
        file_name = random_word()
        soundfile.write(f'{file_name}.wav',y_mix,sr)
        name = f'{file_name}.wav'
        pygame.mixer.music.load(name)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.pause()


# In[234]:


win = tk.Tk()
win.title('My Audio Mixer')
win.geometry('600x450')
win.configure(bg='dimgray')


# pygame initialize
pygame.init()
pygame.mixer.init()


# labelframe
labelframe1 = tk.LabelFrame(win, text=" choose music ", height=130, width=580, bg='dimgray', font=('Times New Romen',15,'bold'), fg='white')
labelframe1.place(x=10, y=5)

labelframe2 = tk.LabelFrame(win, text=" mixing ", height=130, width=285, bg='dimgray', font=('Times New Romen',15,'bold'), fg='gold')
labelframe2.place(x=10, y=150)

labelframe3 = tk.LabelFrame(win, text=" random mixing ", height=130, width=580, bg='dimgray', font=('Times New Romen',15,'bold'), fg='gold')
labelframe3.place(x=10, y=295)

labelframe3 = tk.LabelFrame(win, text=" mix control ", height=130, width=285, bg='dimgray', font=('Times New Romen',15,'bold'), fg='white')
labelframe3.place(x=305, y=150)

# 音頻疊加
name = random_word()
y_mix = 0
sr_mix = 0
def music_mix(song1, song2):
    global name, y_mix, sr_mix
    y, sr = librosa.load(song1)
    y2, sr2 = librosa.load(song2)
    len_max = max(len(y), len(y2))
    len_min = min(len(y), len(y2))
    mix = np.zeros(len_max)
    for i in range(len_max):
        if (i<len_min):
            mix[i] = y[i]+y2[i]
        else:
            if (len(y)>=len(y2)):
                mix[i] = y[i]
            else:
                mix[i] = y2[i]    
    soundfile.write(f'{name}.wav', mix, sr)
    y_mix, sr_mix = librosa.load(f'{name}.wav')

    
# the function used in button
def play_music():
    music_mix(f'{menu1.get()}.wav', f'{menu2.get()}.wav')
    pygame.mixer.music.load(f'{name}.wav')
    pygame.mixer.music.play()
    
def pause_music():
    pygame.mixer.music.pause()
    
def unpause_music():
    pygame.mixer.music.unpause()  
    
def stop_music():
    global count, name, count8, speed, flag_click
    pygame.mixer.music.stop()      
    count = 0
    count8 = 0
    name = random_word()
    button3['image']=photo1
    flag_click=True
    speed.set(0)

def random_stop_music():
    global count, name, count8, flag_click8
    pygame.mixer.music.stop()      
    count = 0
    count8 = 0
    name = random_word() 
    label3.config(text='')
    label4.config(text='')
    button8['image']=photo1
    flag_click8=True
    speed.set(0)

    
# button
# bt1 -- stop music
button1 = tk.Button(win, text='Reset', width=10, height=2, font=('Times New Romen',12,'bold'), command=stop_music, bg='dimgray', fg='white')  
# button1.grid(row=3, column=1, padx=10, pady=10, columnspan=1, ipady=0, sticky='w')
button1.place(x=120, y=195)

# bt9 -- stop music
button9 = tk.Button(win, text='Reset', width=10, height=2, font=('Times New Romen',12,'bold'), command=random_stop_music, bg='dimgray', fg='white')  
button9.place(x=120, y=337)

# bt3 -- ordinary play
p1= Image.open('play1.png')
p1= p1.resize((50, 50),Image.ANTIALIAS)
p3= p1.resize((30, 30),Image.ANTIALIAS)
p2= Image.open('pause1.png')
p2= p2.resize((50, 50),Image.ANTIALIAS)
p4= p2.resize((30, 30),Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(p1, master=win)
photo2 = ImageTk.PhotoImage(p2, master=win)
photo3 = ImageTk.PhotoImage(p3, master=win)
photo4 = ImageTk.PhotoImage(p4, master=win)
label_img = tk.Label(win, image=photo1)


count=0
flag_click=True
def change_image(): 
    """click button to change the photo of play and pause"""
    global flag_click, count
    flag_click = not flag_click
    if flag_click:
        button3['image']=photo1
        pause_music()
    else:
        button3['image']=photo2
        if count==0:
            play_music()
            count+=1
        else:
            unpause_music() 
    win.update()
button3 = tk.Button(win, image = photo1, command=change_image, bg='dimgray')
button3.place(x=40, y=193)



values=['arcade', 'brahms', 'I remember everything', 'nutcracker', 'nostalgic','pistachio','sweetwaltz', 'vibeace']
# 隨機編曲
def random_mix():
    random1 = random.choice(values)
    random2 = random.choice(values)
    music_mix(f'{random1}.wav', f'{random2}.wav')
    pygame.mixer.music.load(f'{name}.wav')
    pygame.mixer.music.play()
    label3.config(text=f'{random1}')
    label4.config(text=f'{random2}')

count8=0
flag_click8=True
def change_image8(): 
    """click button to change the photo of play and pause"""
    global flag_click8, count8
    flag_click8 = not flag_click8
    if flag_click8:
        button8['image']=photo1
        pause_music()
    else:
        button8['image']=photo2
        if count8==0:
            random_mix()
            count8+=1
        else:
            unpause_music() 
    win.update()   
    
# bt8 -- random mix
button8 = tk.Button(win, image = photo1, command=change_image8, bg='dimgray')
button8.place(x=40, y=335)


### slider
def volume_control(volume_scale):
    volume_scale = int(volume_scale)
    pygame.mixer.music.set_volume((volume_scale+5)/10)

volume = tk.Scale(orient=tk.HORIZONTAL, label='volume', from_=-5, to=5, command=volume_control, bg='dimgray', fg='white')
volume.place(x=335, y=193)


speed = tk.Scale(orient=tk.HORIZONTAL, label='speed', from_=-4, to=4, command=set_speed, bg='dimgray', fg='white')
speed.place(x=455, y=193)



# label
label1 = tk.Label(win, text='Music1', width=10, height=1, font=('Times New Romen',12,'bold'), bg='dimgray', fg='white')#, command=getTextInput)  # Choose Music
label1.place(x=15, y=45)

label2 = tk.Label(win, text='Music2', width=10, height=2, font=('Times New Romen',12,'bold'), bg='dimgray', fg='white')#, command=getTextInput)  # Choose Picture
label2.place(x=15, y=85)

label3 = tk.Label(win, text='', width=20, height=2, font=('Times New Romen',12,'bold'), bg='dimgray', fg='white')#, command=getTextInput)  # Choose Picture
label3.place(x=340, y=320)

label4 = tk.Label(win, text='', width=20, height=2, font=('Times New Romen',12,'bold'), bg='dimgray', fg='white')#, command=getTextInput)  # Choose Picture
label4.place(x=340, y=370)

label5 = tk.Label(win, text='Music1 :', width=10, height=2, font=('Times New Romen',12,'bold'), bg='dimgray', fg='white')#, command=getTextInput)  # Choose Picture
label5.place(x=250, y=320)

label6 = tk.Label(win, text='Music2 :', width=10, height=2, font=('Times New Romen',12,'bold'), bg='dimgray', fg='white')#, command=getTextInput)  # Choose Picture
label6.place(x=250, y=370)



# choose music
# 下拉選單1
menu1 = ttk.Combobox(win, values=['arcade', 'brahms', 'I remember everything', 'nutcracker', 'nostalgic', 'pistachio','sweetwaltz', 'vibeace'], state="readonly")
menu1.place(x=120, y=46)
menu1.current(0)
def callbackFunc(event): # 下拉選單回傳函式
    print(menu1.get())
menu1.bind("<<ComboboxSelected>>", callbackFunc)

# 下拉選單2
menu2 = ttk.Combobox(win, values=['arcade', 'brahms', 'I remember everything', 'nutcracker', 'nostalgic','pistachio','sweetwaltz', 'vibeace'], state="readonly")
menu2.place(x=120, y=95)
menu2.current(0)
def callbackFunc(event): # 下拉選單回傳函式
    print(menu2.get())    
menu2.bind("<<ComboboxSelected>>", callbackFunc)



# 單一歌曲的 play buttons
count4 = 0
flag_click4 = True
def change_image4(): 
    """click button to change the photo of play and pause"""
    global flag_click4, count4
    flag_click4 = not flag_click4
    if flag_click4:
        button4['image']=photo3
        pause_music()
    else:
        button4['image']=photo4
        if count4==0:
            play_single_music4()
            count4+=1
        else:
            unpause_music()
        

count5 = 0
flag_click5 = True
def change_image5(): 
    """click button to change the photo of play and pause"""
    global flag_click5, count5
    flag_click5 = not flag_click5
    if flag_click5:
        button5['image']=photo3
        pause_music()
    else:
        button5['image']=photo4
        if count5==0:
            play_single_music5()
            count5+=1
        else:
            unpause_music()

def play_single_music4():
    global music_count
    pygame.mixer.music.load(f"{menu1.get()}.wav")    
    pygame.mixer.music.play()

def play_single_music5():
    global music_count
    pygame.mixer.music.load(f"{menu2.get()}.wav")    
    pygame.mixer.music.play()

def stop_music4():
    global count4, flag_click4
    pygame.mixer.music.stop()      
    count4 = 0   
    button4['image']=photo3
    flag_click4=True

def stop_music5():
    global count5, flag_click5
    pygame.mixer.music.stop()      
    count5 = 0
    button5['image']=photo3
    flag_click5=True
   
    
# bt4 -- play single music1    
button4 = tk.Button(win, image = photo3, command=change_image4, bg='dimgray') 
button4.place(x=300, y=40)
# bt5 -- play single music2    
button5 = tk.Button(win, image = photo3, command=change_image5, bg='dimgray')
button5.place(x=300, y=90)
# bt6 -- reset single music1   
button6 = tk.Button(win, text='Reset', command=stop_music4, bg='dimgray', font=('Times New Romen',12,'bold'), fg='white')  
button6.place(x=350, y=41)
# bt7 -- reset single music2    
button7 = tk.Button(win, text='Reset', command=stop_music5, bg='dimgray', font=('Times New Romen',12,'bold'), fg='white')    
button7.place(x=350, y=91)




###使用說明
ins= Image.open('ins2.png')
ins= ins.resize((480, 360),Image.ANTIALIAS)
tk_ins = ImageTk.PhotoImage(ins)
def createNewWindow():
    new_win = tk.Toplevel(win)
    new_win.title('instruction')
    new_win.geometry('480x360')
    new_win.configure(bg='gray')
    label1 = tk.Label(new_win, width=480, height=360, image=tk_ins, bg='dimgray')
    label1.place(x=0, y=0)
    

new_window_bt = tk.Button(win, text="instruction", command=createNewWindow, bg='dimgray', fg='gold', font=('Times New Romen',12,'bold'))
new_window_bt.place(x=480, y=41)





win.mainloop()
pygame.mixer.music.stop()


# In[ ]:





# In[ ]:





# In[ ]:




