from tkinter import *
import random
import time
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System By Hasaan AHmad")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)


# ========================================================================
#                  CALCULATOR
# ========================================================================
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(f2, font=('arail', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue",
                   justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="7", bg="powder blue",
              command=lambda: btnclick(7))
btn7.grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="8", bg="powder blue",
              command=lambda: btnclick(8))
btn8.grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="9", bg="powder blue",
              command=lambda: btnclick(9))
btn9.grid(row=2, column=2)
Addition = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="+", bg="powder blue",
                  command=lambda: btnclick("+"))
Addition.grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="4", bg="powder blue",
              command=lambda: btnclick(4))
btn4.grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="5", bg="powder blue",
              command=lambda: btnclick(5))
btn5.grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="6", bg="powder blue",
              command=lambda: btnclick(6))
btn6.grid(row=3, column=2)
Subtraction = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="-", bg="powder blue",
                     command=lambda: btnclick("-"))
Subtraction.grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="1", bg="powder blue",
              command=lambda: btnclick(1))
btn1.grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="2", bg="powder blue",
              command=lambda: btnclick(2))
btn2.grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="3", bg="powder blue",
              command=lambda: btnclick(3))
btn3.grid(row=4, column=2)
Multiply = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="*", bg="powder blue",
                  command=lambda: btnclick("*"))
Multiply.grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="0", bg="powder blue",
              command=lambda: btnclick(0))
btn0.grid(row=5, column=0)
btnClear = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="C", bg="powder blue",
                  command=btnClearDisplay)
btnClear.grid(row=5, column=1)
btnEquals = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="=", bg="powder blue",
                   command=btnEqualsInput)
btnEquals.grid(row=5, column=2)
Division = Button(f2, padx=16, pady=16, fg="black", font=('arail', 20, 'bold'), text="/", bg="powder blue",
                  command=lambda: btnclick("/"))
Division.grid(row=5, column=3)

# ========================================================================
#                  TIME AND HEADING NAME
# ========================================================================

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text=" Comsats Sasta Restaurant ", fg="DARKSLATEBLUE", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="DARKSLATEBLUE", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)


# ========================================================================
#                  PROGRAM
# ========================================================================

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    if (AndyWalaBurger.get() == ""):
        CoAndyWalaBurger = 0
    else:
        CoAndyWalaBurger = float(AndyWalaBurger.get())

    if (Biryani.get() == ""):
        CoBiryani = 0
    else:
        CoBiryani = float(Biryani.get())

    if (IceCream.get() == ""):
        CoIceCream = 0
    else:
        CoIceCream = float(IceCream.get())

    if (Pulav.get() == ""):
        CoPulav = 0
    else:
        CoPulav = float(Pulav.get())

    if (Tea.get() == ""):
        CoTea = 0
    else:
        CoTea = float(Tea.get())

    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())

    CostofAndyWalaBurger = CoAndyWalaBurger * 25
    CostofDrinks = CoD * 20
    CostofBiryani = CoBiryani * 25
    CostofIceCream = CoIceCream * 30
    CostPulav = CoPulav * 50
    CostTea = CoTea * 5

    Central_GST = (((CostofAndyWalaBurger + CostofDrinks + CostofBiryani + CostofIceCream + CostPulav + CostTea) * 2.5) / 100)

    State_GST = (((CostofAndyWalaBurger + CostofDrinks + CostofBiryani + CostofIceCream + CostPulav + CostTea) * 2.5) / 100)

    Total_cost = (CostofAndyWalaBurger + CostofDrinks + CostofBiryani + CostofIceCream + CostPulav + CostTea)

    CostofMeal = "Rs", str('%.2f' % (CostofAndyWalaBurger + CostofDrinks + CostofBiryani + CostofIceCream + CostPulav + CostTea))
    C_gst = "Rs", str('%.2f' % Central_GST)
    S_gst = "Rs", str('%.2f' % State_GST)
    OverAllCost = "Rs", str('%.2f' % (Total_cost + Central_GST + State_GST))

    UniversityKaTax.set(S_gst)
    Cost.set(CostofMeal)
    TaxNikal.set(C_gst)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    Tea.set("")
    AndyWalaBurger.set("")
    Biryani.set("")
    IceCream.set("")
    Pulav.set("")
    Drinks.set("")

    rand.set("")

    Total.set("")
    UniversityKaTax.set("")
    TaxNikal.set("")
    Cost.set("")


# ========================================================================
#                  RESTAURANT MENU
# ========================================================================
Tea = StringVar()
AndyWalaBurger = StringVar()
Biryani = StringVar()
IceCream = StringVar()
Pulav = StringVar()
Drinks = StringVar()
rand = StringVar()
Cost = StringVar()
UniversityKaTax = StringVar()
TaxNikal = StringVar()
Total = StringVar()

lblTea = Label(f1, font=('arial', 16, 'bold'), text="Tea", bd=16, anchor="w")
lblTea.grid(row=0, column=0)
lblTea = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tea, bd=10, insertwidth=4, bg="white", justify='right')
lblTea.grid(row=0, column=1)

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=1, column=0)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="white",
                  justify='right')
txtDrinks.grid(row=1, column=1)

lblIceCream = Label(f1, font=('arial', 16, 'bold'), text="Ice-Cream", bd=16, anchor="w")
lblIceCream.grid(row=2, column=0)
lblIceCream = Entry(f1, font=('arial', 16, 'bold'), textvariable=IceCream, bd=10, insertwidth=4, bg="white",
                    justify='right')
lblIceCream.grid(row=2, column=1)

lblAndyWalaBurger = Label(f1, font=('arial', 16, 'bold'), text="AndyWalaBurger", bd=16, anchor="w")
lblAndyWalaBurger.grid(row=3, column=0)
txtAndyWalaBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=AndyWalaBurger, bd=10, insertwidth=4, bg="white", justify='right')
txtAndyWalaBurger.grid(row=3, column=1)

lblBiryani = Label(f1, font=('arial', 16, 'bold'), text="Biryani", bd=16, anchor="w")
lblBiryani.grid(row=4, column=0)
txtBiryani = Entry(f1, font=('arial', 16, 'bold'), textvariable=Biryani, bd=10, insertwidth=4, bg="white", justify='right')
txtBiryani.grid(row=4, column=1)

lblPulav = Label(f1, font=('arial', 16, 'bold'), text="Rice-Plate", bd=16, anchor="w")
lblPulav.grid(row=5, column=0)
txtPulav = Entry(f1, font=('arial', 16, 'bold'), textvariable=Pulav, bd=10, insertwidth=4, bg="white", justify='right')
txtPulav.grid(row=5, column=1)

# ========================================================================
#                  RESTAURANT BILL INFO
# ========================================================================

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=2)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="IVORY",
                     justify='right')
txtReference.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="IVORY", justify='right')
txtCost.grid(row=1, column=3)

lblUniversityKaTax = Label(f1, font=('arial', 16, 'bold'), text="UniversityKaTax", bd=16, anchor="w")
lblUniversityKaTax.grid(row=2, column=2)
txtUniversityKaTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=UniversityKaTax, bd=10, insertwidth=4, bg="IVORY", justify='right')
txtUniversityKaTax.grid(row=2, column=3)

lblTaxNikal = Label(f1, font=('arial', 16, 'bold'), text="TaxNikal", bd=16, anchor="w")
lblTaxNikal.grid(row=3, column=2)
txtTaxNikal = Entry(f1, font=('arial', 16, 'bold'), textvariable=TaxNikal, bd=10, insertwidth=4, bg="IVORY", justify='right')
txtTaxNikal.grid(row=3, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=4, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="IVORY",
                     justify='right')
txtTotalCost.grid(row=4, column=3)

# ========================================================================
#                  BUTTONS
# ========================================================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="IVORY", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="IVORY", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit", bg="IVORY",
                 command=qExit).grid(row=7, column=3)

root.mainloop()

