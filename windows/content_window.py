import webbrowser
from tkinter import *


class ContentWindow:

    def __init__(self, value):

        self.WIDTH = 250
        self.HEIGHT = 250

        self.value = value

        self.master = Tk()
        self.master.title('Brief')
        self.master.lift()
        self.master.attributes('-topmost', True)
        self.master.geometry('1008x600+230+130')
        self.master.resizable(0, 0)

        # The button to view the original article
        Button(self.master, text='Click Here', font='corbel 10', relief=FLAT, command=self.original_article)\
            .place(x=900, y=575)
        Label(self.master, text='To view ful article ', font='corbel 10', relief=FLAT).place(x=750, y=575)

        # A frame to hold the text box that contains the
        # description about the news

        self.description_frame = LabelFrame(self.master, text='Description', width=1006, height=575 - self.HEIGHT,
                                            bg='light green', font='corbel 12 bold')
        self.description_frame.place(x=0, y=0)

        # the text box in description
        self.desc_text_box = Text(self.description_frame, width=123, height=11, relief=SUNKEN, bd=2, wrap=WORD, font='corbel 12')
        self.desc_text_box.place(x=3, y=3)

        # The content frame to display the main news content
        self.content_frame = LabelFrame(self.master, text='Content', width=1006, height=575 - self.HEIGHT,
                                        bg='light blue', font='corbel 12 bold')
        self.content_frame.place(x=0, y=self.HEIGHT)

        # The text box in content_frame
        self.cont_text_box = Text(self.content_frame, width=123, height=15, relief=SUNKEN, bd=2, wrap=WORD, font='corbel 12')
        self.cont_text_box.place(x=3, y=3)

        # function call
        self.fill_info()
        self.master.mainloop()

    def fill_info(self):

        # Fill the description box
        self.desc_text_box.delete(0.0, END)
        self.desc_text_box.insert(0.0, self.value[1])

        # fill the content box
        # Have to beautify
        self.cont_text_box.delete(0.0, END)
        self.cont_text_box.insert(0.0, self.value[2])

    def original_article(self):
        self.master.withdraw()
        self.master.quit()
        self.master.destroy()
        url = self.value[3]
        webbrowser.open(url)


if __name__ == "__main__":
    a = ('Apple puts restrictions on coronavirus-themed apps in its App Store', 'Apple is closely evaluating apps with coronavirus focus. It says only “recognized entities such as government organizations, health-focused NGOs, companies deeply credentialed in health issues, and medical or educational institutions,” should submit such apps…', 'The company says coronavirus-themed games will not be allowed\r\nIllustration by Alex Castro / The Verge\r\nIn an effort to ensure the credibility of health and safety information in its App Store, Apple is tightening requirements for all coronavirus-focused apps… [+1028 chars]', 'https://www.theverge.com/2020/3/14/21179993/apple-restrictions-coronavirus-app-store', 'https://cdn.vox-cdn.com/thumbor/OrCEcxQRSQP5T2C0miJ8ruYHs0E=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/11477049/acastro_180604_1777_apple_wwdc_0002.jpg')

    test = ContentWindow(a)