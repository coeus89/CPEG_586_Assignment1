import numpy as np
import sys
import math
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import Frame, messagebox
import Neuron as nt

class Window(Frame):
    alpha = 0.1 #training rate
    myNeuron = nt.Neuron(alpha)
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # Create Buttons
        exitButton = Button(self, text="Exit",command=self.clickExitButton)
        trainButton = Button(self, text="Train",command=self.clickTrainButton)
        classifyButton = Button(self, text="Classify",command=self.clickClassifyButton)

        #place buttons
        trainButton.place(x=50,y=20)
        classifyButton.place(x=100,y=20)
        exitButton.place(x=170,y=20)


    def clickExitButton(self):
        exit()

    def clickTrainButton(self):
        #code for training
        try:
            #alpha = 0.01 #training rate
            #myNeuron = nt.Neuron(alpha)
            self.myNeuron.Train(10000)
            #myNeuron.Train(10000)
        except Exception as ex:
            print("an exception occurred in clickTrain method: " + str(ex))
            messagebox.showinfo("Error", "An Error Occurred in clickTrain method: " + str(ex))

    def clickClassifyButton(self):
        #code for Testing
        try:
            self.myNeuron.Classify()
            # x = int(input("Please enter a number: "))
            # messagebox.showinfo("Entered Number", "Entered Number: " + str(x))
        except Exception as ex:
            print("an exception occurred in clickClassify method " + str(ex))
            messagebox.showinfo("Error", "An Error Occurred in clickClassify method " + str(ex))
    

root = Tk()
app = Window(root)
root.wm_title("Single Neuron")
root.geometry("400x200")
root.mainloop()




