import tkinter as tk
import pytube
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from pytube import YouTube
import os
from os import path

root=tk.Tk()
root.geometry('950x660')
root.title("YoutubeVideoDownloader")
root.config(bg="#B6A19E")
root.resizable(0,0)

def mainf():
    def sub(videos):
        try:
            n=int(user.get())
            destination=str(users.get())
            if path.exists(destination)==True:
                vid=videos[n-1]
                vid.download(destination)
                fontstyle=tkFont.Font(size=10,underline=True)
                messagebox.showinfo("Downloaded","The video has been downloaded!!")
            else:
                messagebox.showerror("Error!","Enter valid directory")
        except:
            messagebox.showerror("Error","INVALID INPUT\nPlease enter proper number/destination.\n or check your internet connection")
    global u
    try:
        frame=Frame(root)
        scroll=Scrollbar(frame)
        listbox=Listbox(frame,yscrollcommand=scroll.set,bd=3,height=8,width=140,bg="cornsilk2")
        url=u.get()
        y=YouTube(url)
        videos=y.streams.filter(progressive=True).all()
        fontstyle1=tkFont.Font(size=13,family="Arial Black")
        video=tk.Label(root,text="Videos:",font=fontstyle1,bd=0,fg="#1D2951",bg="#B6A19E")
        video.pack()
        fontstyle=tkFont.Font(size=12,underline=True,family="Arial Black")
        title=tk.Label(root,text=y.title,font=fontstyle,bd=0,fg="#1D2951",bg="#B6A19E")
        title.pack(pady=8)
        s=1
        for v in videos: 
            listbox.insert(END,"\n")
            listbox.insert(END,"  "+str(s)+".  "+str(v))
            s+=1
        frame.pack()
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=listbox.yview)
        listbox.pack()

        fontstyle=tkFont.Font(size=11,underline=True)
        choice=tk.Label(root,text="Enter your choice from above numbers: ",font=fontstyle,bg="#B6A19E")
        choice.pack(padx=5,side=tk.LEFT)    
        user=tk.Entry(root,width=4,bd=3)
        user.pack(padx=0,side=tk.LEFT)
        
        fontstyle=tkFont.Font(size=11,underline=True)
        choice=tk.Label(root,text='Enter destination(ex:"C:\\Users\\Public\\Downloads"):',font=fontstyle,bg="#B6A19E")
        choice.pack(padx=8,side=tk.LEFT)       
        users=tk.Entry(root,width=30,bd=3)
        users.pack(padx=0,side=tk.LEFT)

        fontstyle=tkFont.Font(size=12)
        submit=tk.Button(root,text="Submit",fg="black",bg="bisque",font=fontstyle,command=lambda:sub(videos))
        submit.pack(padx=10,side=tk.LEFT)
        
        e=tk.Label(root,text="\n",bg="#B6A19E")
        e.pack()
    except:
        messagebox.showerror("Error","INVALID INPUT\nPlease enter proper url\n(This video is not available for downloading).")
fontstyle=tkFont.Font(size=30,family="Arial Black")
t=tk.Label(root,text="YoutubeVideoDownloader",font=fontstyle,bg="#B6A19E")
t.pack(pady=20)

fontstyle=tkFont.Font(size=13)
r=tk.Label(root,text="Paste url here:",font=fontstyle,bg="#B6A19E")
r.pack()    

u=tk.Entry(root,width=50,bd=4)
u.pack(side=tk.TOP,pady=8)

fontstyle1=tkFont.Font(size=16,family="Times New Roman")
button=tk.Button(root,text="Download",fg="white",bg="#192841",font=fontstyle1,command=mainf)
button.pack(pady=10)

root.mainloop()
