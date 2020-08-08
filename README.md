# Real News

Real news is news software that displays important and
interesting news over a wide range of topics.

Buid completely using [__python__](https://www.python.org/) 
and [__tkinter__](https://docs.python.org/3/library/tkinter.html)

___
## Author
Adwaith Rajesh

Find me on [instagram](https://www.instagram.com/__adwaith__rajesh_/)

## Usage

If you are using this software for the first time
i would suggest running the initialize.bat in the Real_News
folder

This will use [pip](https://pip.pypa.io/en/stable/)
to install the required package for the project

After that you have to run the Real_news.py in the Real News
directory


## API included
This software contains two api

1. [open weather map api](https://openweathermap.org/api)

2. [news api](https://newsapi.org/)

## working
First the programs checks whether the system is connected
to the internet or not.

If not the main software won't run and exits showing an 
error message

If connected the program proceeds to the main_portion
where in the side bar the available topics are displayed.

Every click on the topic item will send a get request
to the api, which in turn returns the hot news.
In total we are able to click the topic items 250 times.

As 250 being the total number of requests to be send to the
API per day

when clicked on a topic the current headlines associated
with the topic will displayed on the headline box.

On clicking each headline, the software displays a dialog box
with the description and content of the news.

User can further view the original article by using, 
by clicking on a button provided on the bottom right
of the dialog box. 


## Note for the user
If you are making any changes to the current program
,remember to use your own API keys as the keys provided
in the software will change within 15 days from the date
of launching

date of launching --> 28/3/2020
___
## Drawbacks

This software can only be used 250 times a day, 250
meaning that, it is the total number of clicks in the
topic side bar in the main software

The new headlines will only updates every 15 minutes.

contents not fully available.
Need to view the original article(option included internally)

