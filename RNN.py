import numpy as np
import math

class RNN:
    def __init__(self):





class cell:

    def __int__(self,size):
        self.W=np.random.random((size,size))
        self.WU_b=np.random.random(size)
        self.V=np.random.random((size,size))
        self.V_b=np.random.random(size)
        self.U=np.random.random((size,size))
        self.h=np.random.random(size)


    def refresh_cell(self,input):
        self.h=self.tanh(np.dot(input,self.U)+np.dot(self.h,self.W)+self.WU_b)

    def tanh(self,vector):
        for i in range(len(vector)):
            vector[i]=(math.pow(math.e,vector[i])-math.pow(math.e,vector[i]))/(math.pow(math.e,vector[i])+math.pow(math.e,vector[i]))

    def output(self):
        return np.dot(self.h,self.V)+self.V_b




