from tkinter import *
from tkinter import ttk
from from_decimal import decimalToAnyBase
from to_decimal import anyBaseToDecimal

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

    # Aquí sucede la magia...
    def convertNumber(self):
        # Obtenemos las entradas de nuestra app
        base = self.getNumberBase()
        number = self.input.get()
        baseResult = self.getNumberBaseResult()
        x = False

        # Si la base a la que queremos convertir es 10,
        # solo ocuparemos una función
        if baseResult == 10:
            x = anyBaseToDecimal(number, base)
        # en caso de que sea al revés, que nuestro numero
        # inicial sea base 10, se usará una función diferente

        elif base == 10:
            x = decimalToAnyBase(number, baseResult)
        
        # Si las bases son diferentes a 10, se usarán las 
        # 2 funciones, para convertir el numero a decimal
        # y el resultado a la base deseada
        else:
            xDecimal = anyBaseToDecimal(number, base)
            # este if existe porque la primera funcion puede fallar,
            # así evitamos seguir arrastrando errores
            if xDecimal is not False:
                x = decimalToAnyBase(xDecimal, baseResult)
        
        # Como nuestra x solo puede tener, ya sea nuestro numero o
        # la sentencia False, unicamente la ponemos sin ninguna condicional
        # pues Python puede dar como verdaro la sentencia si nuestra 
        # variable tiene valor
        if x:
            self.result.configure(text="Your result is: " + str(x))
        else:
            self.result.configure(text="Invalid input")

root = Tk()
app = Application(master=root)
app.master.title("Conversor de bases")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()