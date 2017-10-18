"""
A GUI web crawler program that provides information on college.
Name: University web
Version: 2.0
AUthor: Bibek Bhandari
"""

#necessary modules
from tkinter import *
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup 
import webbrowser

class Application():
    def __init__(self, master):
        #the welcome heading of the program.
        self.heading = Label(master, text="UniversityWeb", font=('arial 40 bold'), fg="steelblue")
        self.heading.grid(row=0, column=1)

        #labell -->Ask for the user input
        self.user = Label(master, text="Insert a University/College name", font=('arial 20 bold'))
        self.user.grid(row=2, column=0)

        self.btns = Button(master, text = "Find Information", width=30, height=3, command=self.find_info)
        self.btns.grid(row=3, column=0)

        #quit button
        self.wuit = Button(master, text="Exit", command=master.quit, width=30, height=3)
        self.wuit.grid(row=4, column=0)

        #entry box
        #global self.college
        self.college = StringVar()
        self.box = Entry(master, width=40, textvariable=self.college)
        self.box.grid(row=2, column=1)
        
        #textbox
        self.textbox = Text(master)
        
        self.textbox.grid(row=3, column=1)
    #function for crawiling from niche.com
    def find_info(self):
        self.main_url = self.college.get()
        self.college1 = self.main_url.replace(' ', '-')
        self.request = requests.get('https://www.niche.com/colleges/'+str(self.college1)+'/cost/')

        #<span data-reactid="350">$46,508</span> This is the average scholarship provided by our example university-Harvard

        self.content = self.request.content
        self.soup = BeautifulSoup(self.content, 'html.parser')
        
        #trying to get result from various data-reactid 
        #data react-id in moslty in range between 339-355

        try:
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "341"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                #inserting the result in text box with formatting
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "342"})
                self.data = self.element.text
                data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "343"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "344"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "345"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "346"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "347"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "348"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "349"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "350"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "351"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "352"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "353"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "354"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:  
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "340"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:  
                pass
            try:
                self.element = self.soup.find("div", {"class": "scalar__value", "data-reactid": "339"})
                self.data = self.element.text
                self.data1 = self.data[:(self.data.index('N'))]
                self.textbox.insert(0.0, ("Average Scholarship: " + str(self.data1) + " "+ str(self.main_url)+"\n"))
            except AttributeError:  
                pass
        except AttributeError:
            pass


root =Tk()
root.geometry("1200x720")
root.resizable(False, False)

b = Application(root)
root.mainloop()