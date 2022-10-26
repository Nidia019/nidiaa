import streamlit as st

class StatisticsCalculator(st):

    def __init__(self):
        st.__init__(self, title = "Statistics Calculator")

        self.addLabel(text = "Please input 10 numbers: ", row = 0, column = 0)
        self.n1Field = self.addFloatField(value = 0.0, row = 1, column = 0)
        self.n2Field = self.addFloatField(value = 0.0, row = 1, column = 1)
        self.n3Field = self.addFloatField(value = 0.0, row = 1, column = 2)
        self.n4Field = self.addFloatField(value = 0.0, row = 1, column = 3)
        self.n5Field = self.addFloatField(value = 0.0, row = 1, column = 4)
        self.n6Field = self.addFloatField(value = 0.0, row = 1, column = 5)
        self.n7Field = self.addFloatField(value = 0.0, row = 1, column = 6)
        self.n8Field = self.addFloatField(value = 0.0, row = 1, column = 7)
        self.n9Field = self.addFloatField(value = 0.0, row = 1, column = 8)
        self.n10Field = self.addFloatField(value = 0.0, row = 1, column = 9)

        self.addButton(text = "Mean", row = 2, column = 0, columnspan = 2, command = self.mean)
        self.addButton(text = "Median", row = 2, column = 4, columnspan = 2, command = self.median)
        self.addButton(text = "Mode", row = 2, column = 8, columnspan = 2, command = self.mode)

        self.finField = self.addFloatField(value = 0.0, row = 3, column = 0, state = "readonly")

    def mean(self):
        n1 = self.n1Field.getNumber()
        n2 = self.n2Field.getNumber()
        n3 = self.n3Field.getNumber()
        n4 = self.n4Field.getNumber()
        n5 = self.n5Field.getNumber()
        n6 = self.n6Field.getNumber()
        n7 = self.n7Field.getNumber()
        n8 = self.n8Field.getNumber()
        n9 = self.n9Field.getNumber()
        n10 = self.n10Field.getNumber()
        lyst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
        meanNum = sum(lyst) / len(lyst)
        self.finField.setNumber(meanNum)

    def median(self):
        n1 = self.n1Field.getNumber()
        n2 = self.n2Field.getNumber()
        n3 = self.n3Field.getNumber()
        n4 = self.n4Field.getNumber()
        n5 = self.n5Field.getNumber()
        n6 = self.n6Field.getNumber()
        n7 = self.n7Field.getNumber()
        n8 = self.n8Field.getNumber()
        n9 = self.n9Field.getNumber()
        n10 = self.n10Field.getNumber()
        lyst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
        lyst.sort()
        m1 = lyst[len(lyst) // 2]
        m2 = lyst[len(lyst) // 2 - 1]
        medianNum = (m1 + m2) / 2
        self.finField.setNumber(medianNum)

    def mode(self):
        n1 = self.n1Field.getNumber()
        n2 = self.n2Field.getNumber()
        n3 = self.n3Field.getNumber()
        n4 = self.n4Field.getNumber()
        n5 = self.n5Field.getNumber()
        n6 = self.n6Field.getNumber()
        n7 = self.n7Field.getNumber()
        n8 = self.n8Field.getNumber()
        n9 = self.n9Field.getNumber()
        n10 = self.n10Field.getNumber()
        lyst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
        frequency = {}
        for i in lyst:
            frequency.setdefault(i, 0)
            frequency[i] += 1
        frequent = max(frequency.values())
        for i, j in frequency.items():
            if j == frequent:
                modeNum = i
        self.finField.setNumber(modeNum)

def main():
    StatisticsCalculator().mainloop()

if __name__ == "__main__":
    main()
