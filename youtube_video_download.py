from tkinter import *
from pytube import YouTube

class Download(object):
    #link = StringVar()
    def __init__(self,master):
        frame = Frame(master).pack()
        self.link = StringVar()    
        master.title('Download youtube videos')
        self.entry_link = Entry(frame,textvariable=self.link).pack()
        self.btn_download = Button(frame,text="Download",fg="red",command=self.download).pack()

    def download(self):
        self.video_link = self.link.get()
        youtube = YouTube(self.video_link)
        stream = youtube.streams.first()
        stream.download()


root = Tk()
root.geometry('300x150')
down = Download(root)
root.mainloop()