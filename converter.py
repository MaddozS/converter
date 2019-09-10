from tkinter import *
from tkinter import ttk
from from_decimal import *
from to_decimal import *

basesList = []
basesNames = []
class Bases:

    def __init__(self, name, numberBase):
        self.name = name
        self.numberBase = numberBase
        basesList.append(self)
        basesNames.append(self.name)
Bases("Binario",2)
Bases("Base 3",3)
Bases("Base 4",4)
Bases("Base 5",5)
Bases("Base 6",6)
Bases("Base 7",7)
Bases("Octal",8)
Bases("Base 9",9)
Bases("Decimal",10)
Bases("Hexadecimal",16)

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, justify=LEFT)
        self.label["text"] = "Número:"
        self.label.grid(column=0, row=0, sticky="e")

        self.input = Entry(self)
        self.input.grid(column=1, row=0, sticky="ew")
        
        self.baseValue = StringVar()
        self.baseValue.set(basesNames[0]) # default value

        self.label2 = Label(self)
        self.label2["text"] = "Base:"
        self.label2.grid(column=0, row=1, sticky="e")

        self.menuNumber = ttk.Combobox(self, textvariable=self.baseValue)
        self.menuNumber['values'] = basesNames
        self.menuNumber.grid(column=1, row=1)

        self.label2 = Label(self)
        self.label2["text"] = "Base de resultado: "
        self.label2.grid(column=0, row=2, sticky="e")

        self.baseValueResult = StringVar()
        self.baseValueResult.set(basesNames[0]) # default value

        self.menuNumberResult = ttk.Combobox(self, textvariable=self.baseValueResult)
        self.menuNumberResult['values'] = basesNames
        self.menuNumberResult.grid(column=1, row=2)

        self.convert = ttk.Button(self, text="Convertir", command=self.convertNumber)
        self.convert.grid(row = 4, columnspan=2)

        self.result = Label(self)
        self.result["text"] = "Your result is: "
        self.result.grid(row=3, columnspan=2, sticky="ew")


    def getNumberBase(self):
        baseNumber = None
        for base in basesList:
            if base.name == self.menuNumber.get():
                baseNumber = base.numberBase
        return baseNumber

    def getNumberBaseResult(self):
        baseNumber = None
        for base in basesList:
            if base.name == self.menuNumberResult.get():
                baseNumber = base.numberBase
        return baseNumber

    def convertNumber(self):
        base = self.getNumberBase()
        number = self.input.get()
        baseResult = self.getNumberBaseResult()
        x = False
        if baseResult == 10:
            x = anyBaseToDecimal(number, base)
        elif base == 10:
            x = decimalToAnyBase(number, baseResult)
        else:
            xDecimal = anyBaseToDecimal(number, base)
            if xDecimal is not False:
                x = decimalToAnyBase(xDecimal, baseResult)
        if x:
            self.result.configure(text="Your result is: " + str(x))
        else:
            self.result.configure(text="Invalid input")

root = Tk()
app = Application(master=root)
app.master.title("Conversor de bases")
app.master.maxsize(1000, 400)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()