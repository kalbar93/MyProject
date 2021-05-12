from tkinter import*
import requests
from bs4 import BeautifulSoup


def takeURL():
    global page, soup
    page = requests.get(poleAdres.get())
    soup = BeautifulSoup(page.content, 'html.parser')


def preview():
    global page,soup
    print(page)

def takeA():
    global page,soup
    soup = soup.find("a")

def takeAllA():
    global page, soup
    soup = soup.find_all("a")

def takeP():
    global page, soup
    soup = soup.find("p")

def takeAllP():
    global page, soup
    soup = soup.find_all("p")

def takeDiv():
    global page, soup
    soup = soup.find("div")

def takeAllDiv():
    global page, soup
    soup = soup.find_all("div")

def takeClass():
    global page, soup
    soup = soup.find("class")

def takeAllCLASS():

    global page, soup
    soup = soup.find_all("class")


def writeTXT():
    pass



root = Tk()

root.title(" SWS - Simply Web Scrapper")
root.geometry("550x400")
root.resizable(width=None , height=None)

TopFrame = Frame(root,bg = "#c2c2d6")
ButtonFrame = Frame(root, bg = "#c2c2d6")
PreviewFrame = Frame(root, bg = "#c2c2d6")
TopFrame.grid()
ButtonFrame.grid()
PreviewFrame.grid()

#TOP

labelAdres = Label(TopFrame , text= "Wprowadz adres URL",bg = "#c2c2d6")
labelAdres.grid()

poleAdres = Entry(TopFrame,justify = LEFT , width = 30, command = takeURL())
poleAdres.grid(row=1, column= 0)


#BUTTON

labelPrzyciski = Label(ButtonFrame, text = "Wybierz opcję:",bg = "#c2c2d6")
labelPrzyciski.grid(row =0 ,column=0, columnspan = 3, pady = 5 )

btFindP = Button(ButtonFrame, text = "Find <p>",bg = "#c2c2d6", command = takeP())
btFindP.grid(row= 1,column= 0,pady=5,padx=3)

btFindA = Button(ButtonFrame, text = "Find <a>",bg = "#c2c2d6", command = takeA())
btFindA.grid(row =1 , column= 1,pady=5,padx=3)

btFindALLp = Button(ButtonFrame , text = "Find all<p>",bg = "#c2c2d6",command = takeAllP() )
btFindALLp.grid(row = 2, column=0 ,pady=5,padx=3)

btFindALLa = Button(ButtonFrame , text = "Find all<a>",bg = "#c2c2d6",command = takeAllA())
btFindALLa.grid(row = 2, column=1,pady=5,padx=3 )

btFindDiv = Button(ButtonFrame , text = "Find <div>",bg = "#c2c2d6", command = takeDiv())
btFindDiv.grid(row=3 ,column = 0,pady =5 , padx=3)

btFindDiv = Button(ButtonFrame , text = "Find all<div>",bg = "#c2c2d6", command = takeAllDiv())
btFindDiv.grid(row=3 ,column = 1,pady =5 , padx=3)

labelKlasa1 = Label(ButtonFrame, text= "Wpisz nazwe klasy:",bg = "#c2c2d6")
labelKlasa1.grid(row = 4 , column=0, columnspan =3  )

entryKlasa1= Entry(ButtonFrame, width =10)
entryKlasa1.grid(row = 5 , column=0,columnspan= 3)

btAccent1 = Button(ButtonFrame , text= "Single class",bg = "#c2c2d6", command = takeClass() )
btAccent1.grid(row =6 , column = 0,pady =5 , padx=3)

btAccent2 = Button(ButtonFrame,text= "All class",bg = "#c2c2d6", command = takeAllCLASS())
btAccent2.grid(row =6, column = 1,pady =5 , padx=3)


#PREVIEW


labelPre = Label(PreviewFrame, text = "Preview")
labelPre.grid(row = 0, column = 0, columnspan = 3 )

textPre = Text(PreviewFrame,width = 30, height = 30,highlightbackground = "BLACK",highlightthickness= 2,wrap = WORD, command= preview())
textPre.grid(row = 1 , column = 1 ,columnspan = 3, sticky = E)


root.mainloop()