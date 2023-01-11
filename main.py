from tkinter import *
import random
import time

root = Tk()
root.geometry("1500x800+10+10")
root.resizable(0, 0)
root.title("Restorano administravimo programa")
root.iconbitmap(r'admin.ico')

Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# ------------------LAIKAS--------------

localtime = time.asctime(time.localtime(time.time()))

# -----------------INFO----------------

lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Restorano Administravimo Programa",
                fg="grey1", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20,), text=localtime, fg="grey1", anchor=W)
lblinfo.grid(row=1, column=0)

# ---------------ADMINISTRAVIMO SISTEMA------------------

text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white",
                   justify='right')
txtdisplay.grid(columnspan=4)


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")


def eqals():
    global operator
    sumup = str(eval(operator))

    text_Input.set(sumup)
    operator = ""


def ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    # rand.set(randomRef)

    cof = float(Snacks.get())
    colfries = float(Lunch.get())
    cob = float(Burger.get())
    cofi = float(Pizza.get())
    cochee = float(Dessert.get())
    codr = float(Drinks.get())

    costofsnacks = cof * 5
    costoflunch = colfries * 8
    costofburger = cob * 9
    costofpizza = cofi * 12
    costofdessert = cochee * 6
    costofdrinks = codr * 2

    costofmeal = str(
        '%.2f' % (costofsnacks + costoflunch + costofburger + costofpizza + costofdessert + costofdrinks))
    PayTax = ((costofsnacks + costoflunch + costofburger + costofpizza + costofdessert + costofdrinks) * 0.33)
    Totalcost = (costofsnacks + costoflunch + costofburger + costofpizza + costofdessert + costofdrinks)
    Ser_Charge = ((costofsnacks + costoflunch + costofburger + costofpizza + costofdessert + costofdrinks) / 99)
    Service = str('%.2f' % Ser_Charge)
    OverAllCost = str('%.2f' % (PayTax + Totalcost + Ser_Charge))
    PaidTax = str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()


def reset():
    rand.set("")
    Snacks.set("")
    Lunch.set("")
    Burger.set("")
    Pizza.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Dessert.set("")


# ---------------SKAIČIUOTUVO MYGTUKAI------------------

btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="powder blue",
              command=lambda: btnclick(7))

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="powder blue",
              command=lambda: btnclick(8))

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="powder blue",
              command=lambda: btnclick(9))

Addition = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="powder blue",
                  command=lambda: btnclick("+"))

btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="powder blue",
              command=lambda: btnclick(4))

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="powder blue",
              command=lambda: btnclick(5))

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="powder blue",
              command=lambda: btnclick(6))

Substraction = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-", bg="powder blue",
                      command=lambda: btnclick("-"))

btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="powder blue",
              command=lambda: btnclick(1))

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="powder blue",
              command=lambda: btnclick(2))

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="powder blue",
              command=lambda: btnclick(3))

multiply = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="powder blue",
                  command=lambda: btnclick("*"))

btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="powder blue",
              command=lambda: btnclick(0))

btnc = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="c", bg="powder blue",
              command=clrdisplay)

btnequal = Button(f2, padx=16, pady=16, bd=4, width=16, fg="black", font=('ariel', 20, 'bold'), text="=",
                  bg="powder blue", command=eqals)

Decimal = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="powder blue",
                 command=lambda: btnclick("."))

Division = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="powder blue",
                  command=lambda: btnclick("/"))

#black fromatter 120

status = Label(f2, font=('aria', 15, 'bold'), width=22, text="By Dovydas Urbanavičius", bd=2, relief=SUNKEN)

# ---------------SKAIČIUOTUVAS LYGIAVIMAS------------------

btn0.grid(row=5, column=0)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

status.grid(row=7, columnspan=3)
Division.grid(row=5, column=3)
Decimal.grid(row=5, column=2)
btnequal.grid(columnspan=4)
btnc.grid(row=5, column=1)
multiply.grid(row=4, column=3)
Addition.grid(row=2, column=3)
Substraction.grid(row=3, column=3)

# ------------------------Administravimo sistema---------------------------------------

rand = StringVar()
Snacks = StringVar()
Lunch = StringVar()
Burger = StringVar()
Pizza = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Dessert = StringVar()

# ------------------------Prekių įvedimas---------------------------------------

lblreference = Label(f1, font=('aria', 16, 'bold'), text="Užsakymo Nr.", fg="steel blue", bd=10, anchor='w')
txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                     justify='right')

lblSnacks = Label(f1, font=('aria', 16, 'bold'), text="Užkandžiai", fg="steel blue", bd=10, anchor='w')
txtSnacks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Snacks, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')

lblLunch = Label(f1, font=('aria', 16, 'bold'), text="Pietūs", fg="steel blue", bd=10, anchor='w')
txtLunch = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Lunch, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')

lblBurger = Label(f1, font=('aria', 16, 'bold'), text="Burgeris", fg="steel blue", bd=10, anchor='w')
txtBurger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')

lblPizza = Label(f1, font=('aria', 16, 'bold'), text="Pica", fg="steel blue", bd=10, anchor='w')
txtPizza = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Pizza, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')

lblDessert = Label(f1, font=('aria', 16, 'bold'), text="Desertas", fg="steel blue", bd=10, anchor='w')
txtDessert = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Dessert, bd=6, insertwidth=4,
                   bg="powder blue", justify='right')

lblreference.grid(row=0, column=0)
lblSnacks.grid(row=1, column=0)
lblLunch.grid(row=2, column=0)
lblBurger.grid(row=3, column=0)
lblPizza.grid(row=4, column=0)
lblDessert.grid(row=5, column=0)

txtreference.grid(row=0, column=1)
txtSnacks.grid(row=1, column=1)
txtLunch.grid(row=2, column=1)
txtBurger.grid(row=3, column=1)
txtPizza.grid(row=4, column=1)
txtDessert.grid(row=5, column=1)

# --------------------------------------------------------------------------------------

lblDrinks = Label(f1, font=('aria', 16, 'bold'), text="Gėrimai", fg="steel blue", bd=10, anchor='w')
txtDrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue",
                  justify='right')

lblcost = Label(f1, font=('aria', 16, 'bold'), text="Kaina", fg="steel blue", bd=10, anchor='w')
txtcost = Entry(f1, font=('ariel', 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="powder blue",
                justify='right')

lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Aptarnavimo mokestis", fg="steel blue", bd=10,
                          anchor='w')
txtService_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                          bg="powder blue", justify='right')

lblTax = Label(f1, font=('aria', 16, 'bold'), text="Mokesčiai", fg="steel blue", bd=10, anchor='w')
txtTax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue", justify='right')

lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Tarpinė suma", fg="steel blue", bd=10, anchor='w')
txtSubtotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="powder blue",
                    justify='right')

lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Iš viso", fg="steel blue", bd=10, anchor='w')
txtTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="powder blue",
                 justify='right')

lblDrinks.grid(row=0, column=2)
lblcost.grid(row=1, column=2)
lblService_Charge.grid(row=2, column=2)
lblTax.grid(row=3, column=2)
lblSubtotal.grid(row=4, column=2)
lblTotal.grid(row=5, column=2)

txtDrinks.grid(row=0, column=3)
txtcost.grid(row=1, column=3)
txtService_Charge.grid(row=2, column=3)
txtTax.grid(row=3, column=3)
txtSubtotal.grid(row=4, column=3)
txtTotal.grid(row=5, column=3)

# -----------------------------------------MYGTUKAI------------------------------------------

lblTotal = Label(f1, text="---------------------", fg="grey1")

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                  bg="powder blue", command=ref)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET",
                  bg="powder blue", command=reset)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
                 bg="powder blue", command=qexit)

lblTotal.grid(row=6, columnspan=3)
btnTotal.grid(row=7, column=1)
btnreset.grid(row=7, column=2)
btnexit.grid(row=7, column=3)


def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Kainų sąrašas")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PREKĖS", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="KAINA", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Užkandžiai", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5€", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pietūs", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="8€", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mėsainis", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="9€", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pica", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="12€", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Desertas", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="6€", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Gėrimai", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2€", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="KAINA",
                  bg="powder blue", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
