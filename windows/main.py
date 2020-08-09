"""
    author --> Adwaith Rajesh
    follow me on ig @adwaith__rajesh
"""


try:
    from window_logic import *
    from content_window import *
except ImportError:
    from .window_logic import *
    from .content_window import *

finally:
    from tkinter import *
    from datetime import date
    import calendar


class MainWindow:

    def __init__(self):

        self.display = Display()
        self.in_class_news = {}

        self.master = Tk()
        self.master.geometry('1440x880+0+0')
        self.master.resizable(1, 1)
        self.master.title('Real News')

        # App topics
        self.topics = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

        # The top frame
        # The top frame displays the date and time info, temp m and place
        self.top_frame = Frame(self.master, width=1428, height=25, bg='cyan')
        self.top_frame.place(x=0, y=0)

        self.cloud_temp = Label(self.top_frame, text="", bg='cyan', font='corbel 13', width=20)
        self.cloud_temp.place(x=1180, y=0)

        # Label to display date
        self.date_day = Label(self.top_frame, text="", bg='cyan', font='corbel 13', width=20)
        self.date_day.place(x=930, y=0)

        # The side bar frame
        # The side ar frame will contain all the news topics, like national, international, sports , etc
        self.side_bar_frame = LabelFrame(self.master, text='Topics', width=250, height=840, bg='light green', font='Corbel 12 bold')
        self.side_bar_frame.place(x=0, y=25)

        # The main frame
        # The main frame will contain all the headlines of news
        # depending on the topic selection on the side bar frame
        self.main_frame = LabelFrame(self.master, text='Head Lines', height=840, width=1180, bg='light blue', font='Corbel 12 bold')
        self.main_frame.place(x=250, y=25)

        # A list box to display the topics
        self.side_box = Listbox(self.side_bar_frame, width=37, height=50, font='Corbel 14')
        self.side_box.place(x=10, y=10)

        # Bind double click and enter to the list elements
        self.side_box.bind('<Double-Button-1>', self.func_side_box_event)
        self.side_box.bind('<Return>', self.func_side_box_event)

        # A list box to insert all the headlines
        self.main_box = Listbox(self.main_frame, width=192, height=50, font='Corbel 15')
        self.main_box.place(x=10, y=10)
        # Bind double click and enter to the list elements
        self.main_box.bind('<Double-Button-1>', self.func_main_box_event)
        self.main_box.bind('<Return>', self.func_main_box_event)

        self._topics()

        self.master.mainloop()

    def func_side_box_event(self, e):
        self.in_class_news.clear()

        # Get the current selection from the side box
        selection = self.side_box.curselection()[0]
        self.master.title(self.topics[selection])

        news_ = self.display.show_info(selection)
        self.in_class_news = news_.copy()  # Change the class variable

        self.main_box.delete(0, END)
        for info in news_.values():
            self.main_box.insert(END, info[0])

    def func_main_box_event(self, e):
        # Get the current selection from the main box
        selection = self.main_box.curselection()[0]
        value = self.in_class_news.get(selection)

        content_window = ContentWindow(value)

    # Fill all the topics into the side box or the topic box
    def _topics(self):
        for topic in self.topics:
            self.side_box.insert(END, topic)

        self.add_weather_date()

    def add_weather_date(self):
        weather = self.display.weather()
        self.cloud_temp.config(text=str(weather[0]) + "   " + str(weather[1]) + '°C')

        today = date.today()
        week = calendar.day_name[today.weekday()]
        self.date_day.config(text=f'{today}   {week}')


if __name__ == "__main__":
    test = MainWindow()
