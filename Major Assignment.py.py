from tkinter import *
window = Tk()
window.title("Calculator")

def mean():
    lyst = [eval(N1.get()), eval(N2.get()), eval(N3.get()), eval(N4.get()), eval(N5.get()), eval(N6.get()), eval(N7.get()), eval(N8.get()), eval(N9.get()), eval(N10.get())]
    meanNum = sum(lyst) / len(lyst)
    FinNumber.set("Mean: " + str(meanNum))

def median():
    lyst = [eval(N1.get()), eval(N2.get()), eval(N3.get()), eval(N4.get()), eval(N5.get()), eval(N6.get()), eval(N7.get()), eval(N8.get()), eval(N9.get()), eval(N10.get())]
    lyst.sort()
    m1 = lyst[len(lyst) // 2]
    m2 = lyst[len(lyst) // 2 - 1]
    medianNum = (m1 + m2) / 2
    FinNumber.set("Median: " + str(medianNum))

def mode():
    lyst = [eval(N1.get()), eval(N2.get()), eval(N3.get()), eval(N4.get()), eval(N5.get()), eval(N6.get()), eval(N7.get()), eval(N8.get()), eval(N9.get()), eval(N10.get())]
    frequency = {}
    for i in lyst:
        frequency.setdefault(i, 0)
        frequency[i] += 1
    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            modeNum = i
    FinNumber.set("Mode: " + str(modeNum))

NumLabel = Label(window, text = "Please input 10 numbers:")
NumLabel.grid(row = 0, column = 0)

N1 = StringVar()
Entry1 = Entry(window, width = 3, textvariable = N1)
Entry1.grid(row = 1, column = 0, padx = 2)
N2 = StringVar()
Entry2 = Entry(window, width = 3, textvariable = N2)
Entry2.grid(row = 1, column = 1, padx = 2)
N3 = StringVar()
Entry3 = Entry(window, width = 3, textvariable = N3)
Entry3.grid(row = 1, column = 2, padx = 2)
N4 = StringVar()
Entry4 = Entry(window, width = 3, textvariable = N4)
Entry4.grid(row = 1, column = 3, padx = 2)
N5 = StringVar()
Entry5 = Entry(window, width = 3, textvariable = N5)
Entry5.grid(row = 1, column = 4, padx = 2)
N6 = StringVar()
Entry6 = Entry(window, width = 3, textvariable = N6)
Entry6.grid(row = 1, column = 5, padx = 2)
N7 = StringVar()
Entry7 = Entry(window, width = 3, textvariable = N7)
Entry7.grid(row = 1, column = 6, padx = 2)
N8 = StringVar()
Entry8 = Entry(window, width = 3, textvariable = N8)
Entry8.grid(row = 1, column = 7, padx = 2)
N9 = StringVar()
Entry9 = Entry(window, width = 3, textvariable = N9)
Entry9.grid(row = 1, column = 8, padx = 2)
N10 = StringVar()
Entry10 = Entry(window, width = 3, textvariable = N10)
Entry10.grid(row = 1, column = 9, padx = 2)


btnMean = Button(window, text = "Mean", width = 10, command = mean)
btnMean.grid(row = 2, column = 0, padx = 15)

btnMedian = Button(window, text = "Median", width = 10, command = median)
btnMedian.grid(row = 2, column = 4, padx = 15)

btnMode = Button(window, text = "Mode", width = 10, command = mode)
btnMode.grid(row = 2, column = 8, padx = 15)

FinNumber = StringVar()
FinEntry = Entry(window, state = "readonly", width = 40, textvariable = FinNumber)
FinEntry.grid(row = 3, column = 0, columnspan = 9, padx = 40, pady = 5)
