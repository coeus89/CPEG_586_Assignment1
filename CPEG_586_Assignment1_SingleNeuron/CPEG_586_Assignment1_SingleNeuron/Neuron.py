import numpy as np
import sys
import math
from tkinter import *
from tkinter import messagebox

class Neuron():
    alpha = 0.0
    w1 = 0
    w2 = 0
    b = 0
    def __init__(self, learningRate:float = 0.01):
        self.alpha = learningRate
    
    def Train(self,iterations:int):
        #messagebox.showinfo("Training", "Number: " + str(x))
        self.w1 = np.random.rand()
        self.w2 = np.random.rand()
        self.b = np.random.rand()
        # w1 = 0.5
        # w2 = 2.2
        # b = 1.0
        x = 0
        trainingData = [
            [0.0,2.1], 
            [0.0,1.9],
            [1.0,2.2],
            [1.0,2.4],
            [2.0,2.61],
            [2.0,2.59],
            [3.2,2.94],
            [3.2,2.84],
            [4.0,3.19],
            [4.0,3.22],
            [5.0,3.49],
            [5.0,3.51],
            [6.0,3.79],
            [6.0,3.81],
            [7.0,4.05],
            [7.0,4.15],
            [8.0,4.5],
            [8.0,4.3],
            [9.0,4.66],
            [9.0,4.74],
            [10.0,5.1],
            [10.0,4.9]
        ]

        for i in range(0,iterations):
            x = i
            x1 = trainingData[i%(len(trainingData))][0]
            x2 = trainingData[i%(len(trainingData))][1]
            #get expected
            y = self.getY(self.w1,self.w2)
            #Find new weights
            newWeights = self.newWeight(x1,x2,self.w1,self.w2,self.b)
            self.w1 = newWeights[0]
            self.w2 = newWeights[1]
            self.b = self.newBias(x1,x2,self.w1,self.w2,self.b)
            # print(i)
        
        messagebox.showinfo("Weights", "W1: " + str(self.w1) + "\nW2: " + str(self.w2) + "\nb: " + str(self.b))

            
    def getY(self, x1:float, x2:float):
        res = 0.3 * x1 + 2.0
        y = 0.0
        if x2 > res:
            y = 1.0
        return y

    def newWeight(self, x1:float, x2:float, w1:float, w2:float, b:float):
        exponent = -1.0*(x1*w1 + x2*w2 + 1.0*b)
        a = (1.0/(1.0 + (math.e)**exponent)) #Sigmoid
        y = self.getY(x1,x2)
        gradw1 = -1.0*(y - a) * x1
        newW1 = w1 - self.alpha * gradw1
        gradw2 = -1.0*(y - a) * x2
        newW2 = w2 - self.alpha * gradw2
        res = []
        res.append(newW1)
        res.append(newW2)
        return res

    def newBias(self, x1:float, x2:float, w1:float, w2:float, b:float):
        exponent = -1.0*(x1*w1 + x2*w2 + 1.0*b)
        a = (1.0/(1.0 + math.e**exponent)) #Sigmoid
        y = self.getY(w1,w2)
        gradb = -1.0*(y - a) * 1.0
        newB = b - self.alpha * gradb
        return newB

    def Classify(self):
        testData = [
            [0.0,1.0], #0
            [0.0,2.4],
            [1.0,5.9],
            [1.0,0.3],
            [2.0,4.4],
            [2.0,4.0],
            [3.2,2.89],
            [3.2,2.91],
            [4.0,3.4],
            [4.0,20.0],
            [5.0,3.9],
            [5.0,3.51],
            [6.0,3.79],
            [6.0,1.4],
            [7.0,4.3],
            [7.0,3.44],
            [8.0,7.7],
            [8.0,1.3],
            [9.0,4.8],
            [9.0,6.1],
            [10.0,5.04],
            [10.0,6.9]
        ]
        resMsg = ""
        for i in range(0,len(testData)):
            x1 = testData[i][0]
            x2 = testData[i][1]
            y = self.getY(x1,x2)
            exponent = -1.0*(x1*self.w1 + x2*self.w2 + 1.0*self.b)
            a = (1.0/(1.0 + math.e**exponent)) #Sigmoid
            res = 0
            if a > 0.6:
                res = 1
                print("For the values x1=" + str(x1) + " x2=" + str(x2) + " the Expected Value was " + str(y) + ". The actual classification was " + str(res) + "\n")
            elif a < 0.4:
                res = 0
                print("For the values x1=" + str(x1) + " x2=" + str(x2) + " the Expected Value was " + str(y) + ". The actual classification was " + str(res) + "\n")
            else:
                res = 2
                print("For the values x1=" + str(x1) + " x2=" + str(x2) + " the Expected Value was " + str(y) + ". The actual classification was " + str(res) + "\n")
            
            
