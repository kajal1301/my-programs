from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def clickDownload():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR", "ENTER url ")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR", "ENTER LOCATION ")
        return
    url = getURL.get()
    print(url)
    global yt
    yt = YouTube(url)
    print(yt.title)
    global videos
    videos = yt.streams.filter(mime_type='video/mp4').all()
    count = 1
    for v in videos:
        listbox.insert(END, str(count)+". "+str(v)+"\n\n")
        count += 1
    
    messagebox.showinfo("Downloading Finish", yt.title+" has been downloaded Sucessfully!!!")


root = Tk()

root.title("YouTube Video Dowloader")
root.geometry("855x500")
root.resizable(False, False)
headLabel       = Label(root,   text="YOUTUBE VIDEO DOWNLOADER",  font=("Century Gothic",25)).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)
getURL = StringVar()
getLoc = StringVar()

urlEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)


downloadButton  = Button(root, text = "DOWNLOAD",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickDownload).grid(row=4, column=1, padx=10, pady=10)

root.mainloop()