import io
import webbrowser

import requests

from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image


class NewsApp:

    def __init__(self):

        # fetch data
        self.root = None
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&apiKey=27e7ecab2be14ddb91b8e10755c1b8fe').json()

        # print(self.data)

        print("Initializing GUI")
        # initial GUI loading
        self.load_gui()

        # Load the 1st news item
        self.load_news_item(3)

    def load_gui(self):
        self.root = Tk()
        self.root.title('News App')
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        print("Loading news item")

        # Clear the screen for the new news item
        self.clear()

        # image
        try:
            print("Inside try for index", index)

            img_url = self.data['articles'][index]['urlToImage']
            print(img_url)
            raw_data = urlopen(img_url).read()
            print("Raw data opened")
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

            label = Label(self.root, image=photo)
            label.pack()


        except:
            print("Inside except")
            img_url = 'https://www.fireebok.com/images/resource/cleanmyphone/cannotloadphotooniphone.png'
            raw_data = urlopen(img_url).read()
            print(raw_data)
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

            label = Label(self.root, image=photo)
            label.pack()

        # heading
        print("Extracted heading")
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='Black', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 50))
        heading.config(font=('verdana', 12))

        # details
        print("Extracted details")

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='Black', fg='white',
                        wraplength=350,
                        justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 10))

        # frame for buttons
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        if index != 0:
            prev = Button(frame, text="Prev", width=11, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text="Read More", width=11, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            next = Button(frame, text="Next", width=11, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        print(url)
        webbrowser.open(url)


obj = NewsApp()
