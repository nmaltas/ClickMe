from tkinter import *
import tkinter.font as tkFont
import random

class ClickMeApp:
    def __init__(self, win):
            
        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.configure(size=16, family = "Comic Sans MS")
        
        self.ClickMe = Button( win, text = ' Click me!! ', command = self.Relocate, bg = "#FF6600",  activebackground = "#FF6600")
        self.ClickMe.place( x = 400 - 70, y = 250 - 10 )
     
    def Relocate (self):
        XPos = random.randint( 10, 670)
        YPos = random.randint( 10, 440)
        self.ClickMe.place( x = XPos, y = YPos)
    

App=Tk()
Mpougiountri= ClickMeApp(App)
App.configure( bg = "black")
App.title('Can you click me?')
App.geometry("800x500+500+200")
App.mainloop()