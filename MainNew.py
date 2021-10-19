import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib
from tkinter import *
from PIL import ImageTk, Image
from GAfuncs import *
from Prob import *

global hyper
hyper = [0.01, 0.2]
Npop=50
MaxIter=1000

# CREATE WINDOW
root= Tk()
root.title('Qiqi\'s Optimization Tool')
root.iconbitmap("qiqiICON.ico")
#root.geometry("400x200")

def Hyper():
    # CREATE WINDOW
    Param= Tk()
    Param.title('Qiqi\'s Optimization Tool')
    Param.iconbitmap("qiqiICON.ico")
    e = Entry(Param,width=20, borderwidth=2)
    e.insert(0,str(hyper[0])) # place a default text inside the box
    e.grid(row=1,column=1,columnspan=1,padx=5,pady=5)
    m = Entry(Param,width=20, borderwidth=2)
    m.insert(0,str(hyper[1])) # place a default text inside the box
    m.grid(row=2,column=1,rowspan=2,padx=5,pady=5)

    # Labels
    GA_label = Label(Param, text="GA Hyperparameters", font=("Helvatica",15))
    GA_label.grid(row=0, column=0, columnspan=3, padx=20)
    elit_label=Label(Param, text="Elitism:")
    elit_label.grid(row=1, column=0, padx=20)
    mut_label=Label(Param, text="Mutation:")
    mut_label.grid(row=2, column=0, padx=20, pady=5)

    def SavePARA(x,y):
        global hyper
        # Elitism and Mutation
        hyper = [float(x), float(y)]
        Hyperframe = LabelFrame(root, text="hyperparameters", padx=10, pady=10)
        if AlgoOp.get() == "GA":
            Para1=Label(Hyperframe, text="elitism:  \t " + str(hyper[0]) + "\nmutation: " + str(hyper[1]),justify="left").pack()
        Hyperframe.grid(row=2, column=3, rowspan=3, padx=10, pady=10, sticky="w")
        Param.destroy()

    SavePara = Button(Param, text="Save", command=lambda: SavePARA(e.get(),m.get()))
    SavePara.grid(row=1, column=2, rowspan=2, pady=5,padx=20)



def RunOpti():
    global Npop,MaxIter
    Npop = int(NpopIn.get())
    MaxIter = int(MaxIterIn.get())
    lb,ub,dim = DefBounds()
    bestval, bestsol, vals = GAopti(ub, lb, dim, Npop, MaxIter, hyper)
    print('best value is:',bestval)
    print('best solution is:',bestsol)
    # Print Results here
    ResultFrame = LabelFrame(root, text="Results", padx=5, pady=3)
    ResultFrame.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky="w")
    Results = Label(ResultFrame, text="best value is: " + str("{:.2e}".format(bestval)) + "\nbest solution is: " +
                                     str(bestsol),justify="left").pack()
    def showplot():
        fig, ax = plt.subplots()
        ax.plot(vals)
        ax.set_xlabel('iteration')
        ax.set_ylabel('fitness')
        ax.grid(True)
        plt.title('Convergence')
        plt.show()

    ShowRes = Button(ResultFrame, text="Convergence Plot", command=showplot).pack()
    #ShowRes.grid(row=1, column=0, padx=10, pady=10)



# Options for Algorithm
AlgorithmOptions=["GA","PSO"]
CostFuncOptions=["sphere","UC"]
AlgoOp=StringVar()
AlgoOp.set(AlgorithmOptions[0])
CostOp=StringVar()
CostOp.set(CostFuncOptions[0])
dropAlgo=OptionMenu(root,AlgoOp,*AlgorithmOptions)
dropAlgo.grid(row=1,column=1,sticky="w")
dropCost=OptionMenu(root,CostOp,*CostFuncOptions)
dropCost.grid(row=2,column=1,sticky="w")

# CREATE AN ENTRY WIDGET
NpopIn = Entry(root,width=15, borderwidth=2)
NpopIn.insert(0,int(Npop)) # place a default text inside the box
NpopIn.grid(row=3,column=1,columnspan=1,padx=5,pady=5)
MaxIterIn = Entry(root,width=15, borderwidth=2)
MaxIterIn.insert(0,int(MaxIter)) # place a default text inside the box
MaxIterIn.grid(row=4,column=1,columnspan=1,padx=5,pady=5)


# Labels
Main_label=Label(root, text="Optimization Tool", font=("Helvetica",15))
Main_label.grid(row=0, column=0, columnspan=2, padx=20)
Algo_label=Label(root, text="Algorithm:")
Algo_label.grid(row=1, column=0,padx=10, sticky="e")
Cost_label=Label(root, text="Problem:")
Cost_label.grid(row=2, column=0, padx=10, sticky="e")
Npop_label=Label(root, text="Population:")
Npop_label.grid(row=3, column=0, padx=10, sticky="e")
MaxIter_label=Label(root, text="Maximum Iteration:")
MaxIter_label.grid(row=4, column=0, padx=10, sticky="e")

# Print Hyperparameters here
Hyperframe = LabelFrame(root, text="hyperparameters",padx=10, pady=10)
if AlgoOp.get()=="GA":
    Para1=Label(Hyperframe, text="elitism:\t\t" + str(hyper[0]) + "\nmutation: \t" + str(hyper[1]),justify="left").pack()
Hyperframe.grid(row=2, column=3, rowspan=3, padx=10, pady=10)

ParaEd=Button(root, text="Edit Parameters", command=Hyper)
ParaEd.grid(row=1, column=3, padx=10, ipadx=20, columnspan=1)
RUNalgo=Button(root, text="Run", command=RunOpti)
RUNalgo.grid(row=5, column=0, padx=40, pady=10, columnspan=1)


# loop window
mainloop()