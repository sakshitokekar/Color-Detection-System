from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import Index

class Instructions:
    def __init__(self):
        # creating tkinter window
        self.root = Tk()

        # Title for window
        self.root.title("Colour Detection RGS")

        # determining size of window
        self.windowWidth = self.root.winfo_screenwidth()
        self.windowHeight = self.root.winfo_screenheight()

        # determining the position to set the window
        self.positionRight = int(self.root.winfo_screenwidth() / 2 - self.windowWidth / 2)
        self.positionDown = int(self.root.winfo_screenheight() / 2 - self.windowHeight / 2)

        # position the window at the center of the page
        self.root.geometry(
            "{}x{}+{}+{}".format(int(self.windowWidth), int(self.windowHeight), self.positionRight, self.positionDown))
        
        self.instruction1 = Image.open("img/instruction1.jpg")
        self.instruction1 = self.instruction1.resize((self.windowWidth, self.windowHeight), Image.ANTIALIAS)
        self.instruction1 = ImageTk.PhotoImage(self.instruction1, master = self.root)
        self.instruction2 = Image.open("img/instruction2.jpg")
        self.instruction2 = self.instruction2.resize((self.windowWidth, self.windowHeight), Image.ANTIALIAS)
        self.instruction2 = ImageTk.PhotoImage(self.instruction2, master = self.root)
        self.instruction3 = Image.open("img/instruction3.jpg")
        self.instruction3 = self.instruction3.resize((self.windowWidth, self.windowHeight), Image.ANTIALIAS)
        self.instruction3 = ImageTk.PhotoImage(self.instruction3, master = self.root)
        self.instruction4 = Image.open("img/instruction4.jpg")
        self.instruction4 = self.instruction4.resize((self.windowWidth, self.windowHeight), Image.ANTIALIAS)
        self.instruction4 = ImageTk.PhotoImage(self.instruction4, master = self.root)
        self.instruction_list = [self.instruction1, self.instruction2, self.instruction3, self.instruction4]
        
        self.right = Image.open("img/right arrow.jpg")
        self.right = self.right.resize((200,107), Image.ANTIALIAS)
        self.right = ImageTk.PhotoImage(self.right, master = self.root)
        self.left = Image.open("img/left arrow.jpg")
        self.left =self.left.resize((200,107), Image.ANTIALIAS)
        self.left = ImageTk.PhotoImage(self.left, master = self.root)
        self.index = 0
        
    def nextt(self):
        if self.index == 0:
            self.btn_left.place(x=0, y=int((self.windowHeight/2)-(self.right.height()/2)))
            
        self.index = self.index + 1
        self.frame.configure(image = self.instruction_list[self.index])
        self.frame.image = self.instruction_list[self.index]
        
        if self.index == len(self.instruction_list)-1:
            self.btn_right.place_forget()
        
    def previous(self):
        if self.index == len(self.instruction_list)-1:
            self.btn_right.place(x = int(self.windowWidth-self.right.width()), y = int((self.windowHeight/2)-(self.right.height()/2)))
            
        self.index = self.index - 1
        self.frame.configure(image = self.instruction_list[self.index])
        self.frame.image = self.instruction_list[self.index]
        
        if self.index == 0:
            self.btn_left.place_forget()
        
    def instructions(self):
        #creating a frame
        self.frame = Label(self.root, image = self.instruction1, bg = "Black")
        self.frame.place(x=0, y=0, width = self.windowWidth, height = self.windowHeight)
                
        w=int(self.windowWidth-self.right.width())
        h=int((self.windowHeight/2)-(self.right.height()/2))
        
        self.btn_right = Button(self.root, command = self.nextt, image = self.right, bg = "black", bd=0)
        self.btn_right.place(x=w, y=h)
        
        self.btn_left = Button(self.root, command = self.previous, image = self.left, bg = "black", bd=0)
        
        self.back_btn = Button(self.root, command = self.menu, text="Back", font = ("Times new roman", 20, "bold"), 
                               fg = "gold", bg="black", bd = 0)
        self.back_btn.place(x = 0, y = 0)
        
        self.root.mainloop()
        
    def menu(self):
        self.root.destroy()
        x = index.MainMenu()
        x.mainMenu()
    

if __name__ == "__main__":
    x = Instructions()
    x.instructions()
        
        