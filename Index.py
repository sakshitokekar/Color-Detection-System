from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import instructions
import sys
import os
import MlCode
import warnings
import matplotlib.pyplot as matplt
warnings.filterwarnings("ignore")

def algo():
	root.withdraw()
	win.deiconify()

def backHome():
	c.set(" ")
	win.withdraw()
	root.deiconify()

def acc():
	root.withdraw()
	page2.deiconify()

def browse():
	filename = filedialog.askopenfilename(initialdir = "/gui/images",title="Select a file",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
	algorithm = c.get()
	if(algorithm == ' '):
		showerror("Error","Please Select Algorithm")
	else:
		MlCode.set_path(filename,algorithm)

def inst():
	root.withdraw()
	instpage.deiconify()

def back_acc():
	page2.withdraw()
	root.deiconify()

root = Tk()
frame1 = Frame(root, bg="White")
root.title("Colour Detection RGS")
windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
root.geometry("{}x{}+{}+{}".format(int(windowWidth), int(windowHeight), positionRight, positionDown))
frame1 = Frame(root, bg="#1c1f1d")
frame1.place(x=0, y=0, width=int(windowWidth / 2.5), height=int(windowHeight))
frame2 = Frame(root)
frame2.place(x=int(windowWidth / 2.5), y=0)
image1 = Image.open("img/bg3.jpg")
image1 = image1.resize((int(windowWidth - (windowWidth/2.5)), int(windowHeight-(windowHeight/10.5))),Image.ANTIALIAS)

image2 = Image.open("img/bg_main.jpg")
image2 = image2.resize((int(windowWidth / 2.5), int(windowHeight)), Image.ANTIALIAS)
        
g = (windowWidth - (windowWidth / 2.5)), int(windowHeight)
image_bg = ImageTk.PhotoImage(image1, master = root)
image_bg1 = ImageTk.PhotoImage(image2, master = root)

bg_label = Label(frame2, image=image_bg)
bg_label.pack()

bg_label2 = Label(frame1, image = image_bg1)
bg_label2.place(x=0,y=0)

space_head = Label(frame1, text = """""", font=('Baskerville Old Face', 10, "bold"), bg = "#e9e7ea", fg="#221733")
space_head.grid(row = 0, column = 0, columnspan = 4, padx = 12, pady = 5)
heading =Label(frame1, text = """COLOR DETECTION SYSTEM""", font=('Baskerville Old Face', 30, "bold"), bg = "#e9e7ea", fg="#221733")
heading.grid(row = 1, column = 0, columnspan = 4, padx = 12, pady = 5)
heading2 =Label(frame1, text = """An Application that will help you to detect colors in an image.""", font=('batman forever', 15 , "bold"), bg = "#e9e7ea", fg="#221733")
heading2.grid(row = 2, column = 0, columnspan = 4, padx = 12, pady = 1)
space_head2 = Label(frame1, text = """""", font=('Baskerville Old Face', 10, "bold"), bg = "#e9e7ea", fg="#221733")
space_head2.grid(row = 4, column = 0, columnspan = 4, padx = 12, pady = 15)

upload_but = Button(frame1, text = "Select Algorithm", font = ("Times new roman", 20, "bold"), bg = "#e9e7ea",fg = "red", width = 20,command = algo)
upload_but.grid(row = 6, column=0, pady = 15, columnspan = 4)
acc_but = Button(frame1, text = "Algorithms", font = ("Times new roman", 20, "bold"), bg = "#e9e7ea",fg = "red", width = 20,command = acc)
acc_but.grid(row = 7, column=0, pady = 15, columnspan = 4)
inst_but = Button(frame1, text = "Instruction", font = ("Times new roman", 20, "bold"), bg = "#e9e7ea",fg = "red", width = 20, command = inst)
inst_but.grid(row = 8, column=0, columnspan = 4,  pady = 15)

win = Toplevel(root)
win.title("Select Algorithm")
win.geometry("500x600+150+50")

c = StringVar()
c.set(" ")
lblSelect  = Label(win  , text = 'Select Algorithm: ' , width = 25 , font = ('arial' , 30 , 'bold'),justify=LEFT)
rbKNN = Radiobutton(win,text='K-Nearest Neighbour',font=('arial',20,'bold'),variable = c,value ="KNN",width=25,justify=LEFT)
rbLogisticregression = Radiobutton(win,text='Logistic Regression',font=('arial',20,'bold'),variable = c,value ="LR",width=25,justify=LEFT)
rbSVM = Radiobutton(win,text='Support Vector Machine',font=('arial',20,'bold'),variable = c,value = "SVM",width=25,justify=LEFT)
rbDesicionTree = Radiobutton(win,text='Desicion Tree',font=('arial',20,'bold'),variable = c,value = "DT",width=25,justify=LEFT)
rbRandomForest = Radiobutton(win,text='Random Forest',font=('arial',20,'bold'),variable = c,value = "RF",width=25,justify=LEFT)
btnSelect  = Button(win, text = "Select Image", font = ("Times new roman", 20, "bold"), bg = "#e9e7ea",fg = "red", width = 25,command = browse,justify=LEFT)
btnBack  =  Button(win, text = "Back", font = ("Times new roman", 20, "bold"), bg = "#e9e7ea",fg = "black", width = 25,command =backHome,justify=LEFT)

lblSelect.pack(padx = 10,pady = 35)
rbKNN.pack( padx = 10,pady = 2)
rbLogisticregression.pack(padx = 10,pady = 2)
rbSVM.pack(padx = 10,pady = 2)
rbDesicionTree.pack( padx = 10,pady = 2)
rbRandomForest.pack(padx = 10,pady = 2)
btnSelect.pack(padx = 10,pady = 30)
btnBack.pack(padx = 10,pady = 2)

win.withdraw()


#################################################### ROHIT #########################################################################

def graph_acc(knnvar,lrvar,dtvar,svcvar,rfvar):
	'''
	algorithm_name = ['K nearest Neighbour','Logistic Regression','Decision Tree','Support Vector Classifier','Random Forests']
	algorithm_accuracy = [knnvar,lrvar,dtvar,svcvar,rfvar]
	matplt.bar(algorithm_name,algorithm_accuracy)
	matplt.xlabel("Algorithms")
	matplt.ylabel("Accuracy")
	matplt.title("Algorithm Accuracy Comparison")
	matplt.grid()
	matplt.show()
	'''
	pass

KNN_def = "A k-nearest-neighbor algorithm, often abbreviated k-nn, is an approach to data classification that estimates how likely a data point is to be a member\nof one group or the other depending on what group the data points nearest to it are in"

LogisticRegression_def = "Logistic regression is the appropriate regression analysis to conduct when the dependent variable is dichotomous(binary).  Like all regression\nanalyses, the logistic regression is a predictive analysis."


DecisionTree_def = "Decision Tree is a Supervised learning technique  that can be used for both classification and Regression problems , but mostly it is preferred for solving\nClassification problems.It is a tree-structured classifier, where internal nodes represent the features of a dataset,branches represent the decision rules and\neach leaf node represents the outcome."

RandomForest_def = "Random forest is a supervised learning algorithm used for classification as well as regression. However it is mainly used for classification problems. As\nwe know that a forest is made up of trees and more trees means more robust forest. Similarly, random forest algorithm creates decision trees\non data samples and then gets the prediction from each of them and finally selects the best solution by means of voting"

SVM_def = "A support vector machine (SVM) is a supervised machine learning model that uses classification algorithms for two-group classification problems. After\ngiving an SVM model sets of labeled training data for each category, they’re able to categorize new text."

page2 = Tk()
page2.title("Colour Detection RGS")
page2['bg']='white'
windowWidth = page2.winfo_screenwidth()
windowHeight = page2.winfo_screenheight()
positionRight = int(page2.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(page2.winfo_screenheight() / 2 - windowHeight / 2)
page2.geometry("{}x{}+{}+{}".format(int(windowWidth), int(windowHeight), positionRight, positionDown))

knnvar,lrvar,dtvar,svcvar,rfvar = MlCode.accuracy_send()

fm0_acc = Frame(page2, bg="White")
fm0_acc.place(x=0, y=0, width=int(windowWidth / 5), height=int(windowHeight))

fm1_acc = Frame(page2, bg="white")
fm1_acc.place(x=int(windowWidth / 5), y=0)
acc_image1 = Image.open("img/acc_img.jpg")
acc_image1 = acc_image1.resize((int(windowWidth), int(windowHeight-(windowHeight/10.5))),Image.ANTIALIAS)

acc_g = (windowWidth - (windowWidth/2.5), int(windowHeight))
acc_image_bg = ImageTk.PhotoImage(acc_image1, master = page2)

acc_bg_label2 = Label(fm0_acc, image = acc_image_bg)
acc_bg_label2.place(x=0,y=0)


spc3 = Label(fm1_acc, text = "----------------------------------------------------------------------------------------------------------------------", font = ("Times new roman", 10, "bold"),bg = "white", fg="white")
spc6 = Label(fm1_acc, text = "----------------------------------------------------------------------------------------------------------------------", font = ("Times new roman", 10, "bold"),bg = "white", fg="white")
spc9 = Label(fm1_acc, text = "----------------------------------------------------------------------------------------------------------------------", font = ("Times new roman", 10, "bold"),bg = "white", fg="white")
spc12 = Label(fm1_acc, text = "---------------------------------------------------------------------------------------------------------------------", font = ("Times new roman", 10, "bold"),bg = "white", fg="white")


spc3.grid(row = 5, column = 3, pady = 2, columnspan=2)
spc6.grid(row = 10, column = 3, pady = 2, columnspan=2)
spc9.grid(row = 15, column = 3, pady = 2, columnspan=2)
spc12.grid(row = 20, column = 3, pady = 2 ,columnspan=2)


headLabel = Label(fm1_acc, text = "Algorithms", font = ("Times new roman", 30, "bold"),bg = "white", fg="black")
headLabel.grid(row=0, column=2,  pady = 20,sticky = W)

knnLabel = Label(fm1_acc, text = "K Nearst Neighbour:  "+str(knnvar)+ "%" , font = ("Times new roman", 15, "bold"),bg = "white", fg="black")
knnLabel.grid(row=1, column=2, sticky = W)
defknnLabel = Label(fm1_acc, text = KNN_def, font = ("Times new roman", 15),bg = "white", fg="black")
defknnLabel.grid(row = 2, column = 2, columnspan=2,sticky = W)

lrLabel = Label(fm1_acc, text = "Logistic Regression: "+str(lrvar)+ "%", font = ("Times new roman", 15, "bold"),bg = "white", fg="black")
lrLabel.grid(row=6, column=2,  sticky = W)
deflrLabel = Label(fm1_acc, text = LogisticRegression_def, font = ("Times new roman", 15),bg = "white", fg="black")
deflrLabel.grid(row=7, column=2, columnspan=2,sticky = W)

dtLabel = Label(fm1_acc, text = "Decision Tree:  " + str(dtvar)+ "%", font = ("Times new roman", 15, "bold"),bg = "white", fg="black")
dtLabel.grid(row=11, column=2, sticky = W)
defdtLabel = Label(fm1_acc, text = DecisionTree_def , font = ("Times new roman", 15),bg = "white", fg="black")
defdtLabel.grid(row=12, column=2,  columnspan=2,sticky = W)

svcLabel = Label(fm1_acc, text = "Support Vector Classifier: "+str(svcvar) + "%", font = ("Times new roman", 15, "bold"),bg = "white", fg="black")
svcLabel.grid(row=16, column=2,sticky = W)
defsvcLabel = Label(fm1_acc, text = SVM_def , font = ("Times new roman", 15),bg = "white", fg="black")
defsvcLabel.grid(row=17, column=2, columnspan=2,sticky = W)

rfLabel = Label(fm1_acc, text = "Random Forests:  "+str(rfvar)+ "%", font = ("Times new roman", 15, "bold"),bg = "white", fg="black")
rfLabel.grid(row=21, column=2, sticky = W,pady=0)
defrfLabel = Label(fm1_acc, text = RandomForest_def, font = ("Times new roman", 15),bg = "white", fg="black")
defrfLabel.grid(row=22, column=2,  columnspan=2,sticky = W,pady=0)

'''
Graphbtn = Button(fm1_acc, text = "Histogram", font = ("Times new roman", 20, "bold"), bg = "white",fg = "red", width = 15,command = graph_acc(
knnvar,lrvar,dtvar,svcvar,rfvar))
Graphbtn.grid(row=23, column=2,pady = 50,sticky = W)
'''
Backbtn = Button(fm1_acc, text = "Back", font = ("Times new roman", 20, "bold"), bg = "white",fg = "red", width = 15,command = back_acc)
Backbtn.grid(row=23, column=3,pady = 50,sticky = W)

page2.withdraw()


#######################################################################################################################################################
global index
index = 0
def menu():
	instpage.withdraw()
	root.deiconify()
        
def nextt():
	global index
	if index == 0:
		btn_left.place(x=0, y=int((windowHeight/2)-(right.height()/2)))
	
	index = index + 1
	inst_frame.configure(image = instruction_list[index])
	inst_frame.image = instruction_list[index]
	if index == len(instruction_list)-1:
		btn_right.place_forget()

def previous():
	global index
	if index == len(instruction_list)-1:
		btn_right.place(x = int(windowWidth-right.width()), y = int((windowHeight/2)-(right.height()/2)))
	index = index - 1
	inst_frame.configure(image = instruction_list[index])
	inst_frame.image = instruction_list[index]
	
	if index == 0:
		btn_left.place_forget()

instpage = Tk()
instpage.title("Colour Detection RGS")
windowWidth = instpage.winfo_screenwidth()
windowHeight = instpage.winfo_screenheight()
positionRight = int(instpage.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(instpage.winfo_screenheight() / 2 - windowHeight / 2)
instpage.geometry(
            "{}x{}+{}+{}".format(int(windowWidth), int(windowHeight), positionRight, positionDown))
instruction1 = Image.open("img/instruction1.jpg")
instruction1 = instruction1.resize((windowWidth, windowHeight-150), Image.ANTIALIAS)
instruction1 = ImageTk.PhotoImage(instruction1, master = instpage)
instruction2 = Image.open("img/instruction2.jpg")
instruction2 = instruction2.resize((windowWidth, windowHeight), Image.ANTIALIAS)
instruction2 = ImageTk.PhotoImage(instruction2, master = instpage)
instruction3 = Image.open("img/instruction3.jpg")
instruction3 = instruction3.resize((windowWidth, windowHeight), Image.ANTIALIAS)
instruction3 = ImageTk.PhotoImage(instruction3, master = instpage)
instruction4 = Image.open("img/instruction4.jpg")
instruction4 = instruction4.resize((windowWidth, windowHeight), Image.ANTIALIAS)
instruction4 = ImageTk.PhotoImage(instruction4, master = instpage)
instruction5 = Image.open("img/instruction5.jpg")
instruction5 = instruction5.resize((windowWidth, windowHeight-100), Image.ANTIALIAS)
instruction5 = ImageTk.PhotoImage(instruction5, master = instpage)
instruction_list = [instruction1, instruction2, instruction3, instruction4,instruction5]
        
right = Image.open("img/right arrow.jpg")
right = right.resize((200,107), Image.ANTIALIAS)
right = ImageTk.PhotoImage(right, master = instpage)
left = Image.open("img/left arrow.jpg")
left =left.resize((200,107), Image.ANTIALIAS)
left = ImageTk.PhotoImage(left, master = instpage)
#index = 0

inst_frame = Label(instpage, image = instruction1, bg = "Black")
inst_frame.place(x=0, y=0, width = windowWidth, height = windowHeight)
w=int(windowWidth-right.width())
h=int((windowHeight/2)-(right.height()/2))
btn_right = Button(instpage, command = nextt, image = right, bg = "black", bd=0)
btn_right.place(x=w, y=h)
btn_left = Button(instpage, command = previous, image = left, bg = "black", bd=0)
back_btn = Button(instpage, command = menu, text="Back", font = ("Times new roman", 20, "bold"),fg = "gold", bg="black", bd = 0)
back_btn.place(x = 0, y = 0)

instpage.withdraw()

        

##################################################################################################################################################








root.mainloop()
 