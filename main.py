from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='#9E7CAC')

        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        Subtotal_Input = StringVar()
        Total_Input = StringVar()
        Item_Input = StringVar()
        Qty_Input = StringVar()
        Amount_Input = StringVar()
        choice_Input = StringVar()

        self.Coffee = PhotoImage(file="Pics\Coffee.png")
        self.Hotchoco = PhotoImage(file="Pics\Hotchoco.png")
        self.Lemonade = PhotoImage(file="Pics\Lemonade.png")
        self.Water = PhotoImage(file="Pics\Water.png")
        self.Icedtea = PhotoImage(file="Pics\Icedtea.png")
        self.Coke = PhotoImage(file="Pics\Coke.png")
        self.Milkshake = PhotoImage(file="Pics\Milkshake.png")
        self.Beer = PhotoImage(file="Pics\Beer.png")
        self.Milk = PhotoImage(file="Pics\Milk.png")
        self.Tea = PhotoImage(file="Pics\Tea.png")
        self.Wine = PhotoImage(file="Pics\Wine.png")
        self.Royal = PhotoImage(file="Pics\Royal.png")
        self.Pancake = PhotoImage(file="Pics\Pancake.png")
        self.Burger = PhotoImage(file="Pics\Burger.png")
        self.Fries = PhotoImage(file="Pics\Fries.png")
        self.Chicken = PhotoImage(file="Pics\Chicken.png")
        self.Pizza = PhotoImage(file="Pics\Pizza.png")
        self.Egg = PhotoImage(file="Pics\Egg.png")
        self.Donut = PhotoImage(file="Pics\Donut.png")
        self.Vegsalad = PhotoImage(file="Pics\Vegsalad.png")
        self.Cake = PhotoImage(file="Pics\Cake.png")
        self.Bread = PhotoImage(file="Pics\Bread.png")
        self.Carbonara = PhotoImage(file="Pics\Cabonara.png")
        self.Buttered = PhotoImage(file="Pics\Buttered.png")
        self.Beefsteak = PhotoImage(file="Pics\Beefsteak.png")
        self.Sushi = PhotoImage(file="Pics\Sushi.png")
        self.Ramen = PhotoImage(file="Pics\Ramen.png")
        self.Lasagna = PhotoImage(file="Pics\Lasagna.png")
        self.Spaghetti = PhotoImage(file="Pics\Spaghetti.png")
        self.Siomai = PhotoImage(file="Pics\Siomai.png")
        self.Pancit = PhotoImage(file="Pics\Pancit.png")
        self.Cookies = PhotoImage(file="Pics\Cookies.png")

        def delete():
            selected_items = self.POS_records.selection()
            if selected_items:
                for item in selected_items:
                    item_values = self.POS_records.item(item, "values")
                    price = float(item_values[2][1:])
                    self.POS_records.delete(item)
                ItemCost = 0
                Tax = 3
                for child in self.POS_records.get_children():
                    item_values = self.POS_records.item(child, "values")
                    price = float(item_values[2][1:])
                    ItemCost += price
                Subtotal_Input.set("₱" + str(ItemCost))
                Tax_Input.set("₱" + str((ItemCost * Tax) / 100))
                Total_Input.set("₱" + str(ItemCost + (ItemCost * Tax) / 100))

        def Change():
            ItemCost = 0
            Tax = 3
            cash_input = Cash_Input.get()
            if cash_input == '':
                tkinter.messagebox.showinfo("Point of Sale", "Please enter a cash amount!")
                return

            CashInput = float(cash_input)
            for child in self.POS_records.get_children():
                item_values = self.POS_records.item(child, "values")
                price = float(item_values[2][1:])
                ItemCost += price
            total = ItemCost + (ItemCost * Tax) / 100
            change = CashInput - total
            Change_Input.set("₱" + "{:.2f}".format(change) if change >= 0 else "")
            Total_Input.set("₱" + "{:.2f}".format(total))
            if Cash_Input.get() == "0":
                Change_Input.set("")
            Method()

        def Method():
            if choice_Input.get() in ['CASH', 'VISA CARD', 'MASTER CARD', 'GCASH', 'MAYA']:
                self.txtCost.focus()
                Cash_Input.set("")
            else:
                Cash_Input.set("0")
                Change_Input.set("")

        def Exit():
            Exit = tkinter.messagebox.askyesno("Point of Sale", "Do you want to quit?")
            if Exit > 0:
                root.destroy()
                return

        def Reset():
            self.POS_records.delete(*self.POS_records.get_children())
            Subtotal_Input.set("")
            Tax_Input.set("")
            Total_Input.set("")
            Cash_Input.set("0")
            Change_Input.set("")
            choice_Input.set("")
            self.txtCost.focus()

        MainFrame = Frame(self.root, bg='#9E7CAC')
        MainFrame.grid(padx=8, pady=5)
        ButtonFrame = Frame(MainFrame, bg='#9E7CAC', bd=5, width=1348, height=160, padx=4, pady=4, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bg='#9E7CAC', bd=5, width=980, height=300, padx=4, pady=4, relief=RIDGE)
        DataFrame.pack(side=LEFT)
        DataFrameLEFTCOVER = LabelFrame(DataFrame, bg='#9E7CAC', bd=5, width=980, height=300, padx=4, pady=4, font=('arial', 12, 'bold'), text="Drinks", relief=RIDGE)
        DataFrameLEFTCOVER.pack(side=LEFT)
        ChangeButtonFrame = Frame(DataFrameLEFTCOVER, bd=5, width=300, height=460, padx=4, pady=4, relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT, padx=4)
        ReceiptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, pady=5, padx=1, relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT, padx=4)
        FoodItemFrame = LabelFrame(DataFrame, bd=5, width=450, height=300, padx=5, pady=2, relief=RIDGE, bg='#9E7CAC', font=('arial', 12, 'bold'), text="Food",)
        FoodItemFrame.pack(side=RIGHT)
        CalFrame = Frame(ButtonFrame, bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=0, padx=5)
        ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column=1, padx=5)
        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0, column=2, padx=5)

        self.lblSubTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=5)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txtSubTotal = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Subtotal_Input, bd=2, width=24)
        self.txtSubTotal.grid(row=0, column=1, sticky=W, padx=5)
        self.lblTax = Label(CalFrame, font=('arial', 14, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)
        self.txtTax = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Tax_Input, bd=2, width=24)
        self.txtTax.grid(row=1, column=1, sticky=W, padx=5)
        self.lblTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Total_Input, bd=2, width=24)
        self.txtTotal.grid(row=2, column=1, sticky=W, padx=5)

        self.lblMoP = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Method of Payment", bd=5)
        self.lblMoP.grid(row=0, column=0, sticky=W, padx=5)
        self.cboMoP = ttk.Combobox(ChangeFrame, font=('arial', 14, 'bold'), width=34, state='readonly', textvariable=choice_Input, justify=RIGHT)
        self.cboMoP['values'] = ('','CASH','VISA CARD','MASTER CARD','GCASH','MAYA')
        self.cboMoP.current(0)
        self.cboMoP.grid(row=0, column=1)
        self.lblCost = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Cash", bd=5)
        self.lblCost.grid(row=1, column=0, sticky=W, padx=5)
        self.txtCost = Entry(ChangeFrame, font=('arial', 14, 'bold'), textvariable=Cash_Input, bd=2, width=35, justify=RIGHT)
        self.txtCost.grid(row=1, column=1, sticky=W, padx=5)
        self.txtCost.insert(0,"0")
        self.lblChange = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2, column=0, sticky=W, padx=5)
        self.txtChange = Entry(ChangeFrame, font=('arial', 14, 'bold'), textvariable=Change_Input, bd=2, width=35, justify=RIGHT)
        self.txtChange.grid(row=2, column=1, sticky=W, padx=5)

        self.btnPay = Button(RemoveFrame, padx=2, font=('arial', 14, 'bold'), text="Pay", width=9, height=1, bd=2, command=Change)
        self.btnPay.grid(row=0, column=0, pady=2, padx=7)
        self.btnExit = Button(RemoveFrame, padx=2, font=('arial', 14, 'bold'), text="Exit", width=9, height=1, bd=2, command=Exit)
        self.btnExit.grid(row=0, column=1, pady=2, padx=7)
        self.btnReset = Button(RemoveFrame, padx=2, font=('arial', 14, 'bold'), text="Reset", width=9, height=1, bd=2, command=Reset)
        self.btnReset.grid(row=1, column=0, pady=2, padx=7)
        self.btnRemoveItem = Button(RemoveFrame, padx=2, font=('arial', 14, 'bold'), text="Void Item", width=9, height=1, bd=2, command=delete)
        self.btnRemoveItem.grid(row=1, column=1, pady=2, padx=7)

        def Coffee():
            ItemCost = 59
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Coffee", "1", "₱59"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 59))
            Tax_Input.set("₱" + str(((ItemCost - 59) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 59 + ((ItemCost - 59) * Tax) / 100))

        def Hotchoco():
            ItemCost = 39
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Hotchoco", "1", "₱39"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 39))
            Tax_Input.set("₱" + str(((ItemCost - 39) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 39 + ((ItemCost - 39) * Tax) / 100))

        def Lemonade():
            ItemCost = 14
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Lemonade", "1", "₱14"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 14))
            Tax_Input.set("₱" + str(((ItemCost - 14) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 14 + ((ItemCost - 14) * Tax) / 100))

        def Water():
            ItemCost = 9
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Water", "1", "₱9"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 9))
            Tax_Input.set("₱" + str(((ItemCost - 9) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 9 + ((ItemCost - 9) * Tax) / 100))

        def Icedtea():
            ItemCost = 14
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Iced Tea", "1", "₱14"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 14))
            Tax_Input.set("₱" + str(((ItemCost - 14) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 14 + ((ItemCost - 14) * Tax) / 100))

        def Coke():
            ItemCost = 19
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Coke", "1", "₱19"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 19))
            Tax_Input.set("₱" + str(((ItemCost - 19) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 19 + ((ItemCost - 19) * Tax) / 100))

        def Milkshake():
            ItemCost = 99
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Milk Shake", "1", "₱99"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 99))
            Tax_Input.set("₱" + str(((ItemCost - 99) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 99 + ((ItemCost - 99) * Tax) / 100))

        def Beer():
            ItemCost = 129
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Beer", "1", "₱129"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 129))
            Tax_Input.set("₱" + str(((ItemCost - 129) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 129 + ((ItemCost - 129) * Tax) / 100))

        def Milk():
            ItemCost = 29
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Milk", "1", "₱29"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 29))
            Tax_Input.set("₱" + str(((ItemCost - 29) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 29 + ((ItemCost - 29) * Tax) / 100))

        def Tea():
                ItemCost = 39
                Tax = 1
                self.POS_records.insert("", tk.END, values=("Tea", "1", "₱39"))
                for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child, "values")[2][1:])
                Subtotal_Input.set("₱" + str(ItemCost - 39))
                Tax_Input.set("₱" + str(((ItemCost - 39) * Tax) / 100))
                Total_Input.set("₱" + str(ItemCost - 39 + ((ItemCost - 39) * Tax) / 100))

        def Wine():
            ItemCost = 129
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Wine", "1", "₱129"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 129))
            Tax_Input.set("₱" + str(((ItemCost - 129) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 129 + ((ItemCost - 129) * Tax) / 100))

        def Royal():
            ItemCost = 19
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Royal", "1", "₱39"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 19))
            Tax_Input.set("₱" + str(((ItemCost - 19) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 19 + ((ItemCost - 319) * Tax) / 100))

        def Pancake():
            ItemCost = 29
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Pancake", "1", "₱29"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 29))
            Tax_Input.set("₱" + str(((ItemCost - 29) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 29 + ((ItemCost - 29) * Tax) / 100))

        def Burger():
            ItemCost = 259
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Burger", "1", "₱259"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 29))
            Tax_Input.set("₱" + str(((ItemCost - 259) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 259 + ((ItemCost - 259) * Tax) / 100))

        def Fries():
            ItemCost = 29
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Fries", "1", "₱29"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 29))
            Tax_Input.set("₱" + str(((ItemCost - 29) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 29 + ((ItemCost - 29) * Tax) / 100))

        def Chicken():
            ItemCost = 129
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Chicken", "1", "₱129"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 129))
            Tax_Input.set("₱" + str(((ItemCost - 129) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 129 + ((ItemCost - 129) * Tax) / 100))

        def Pizza():
            ItemCost = 399
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Pizza", "1", "₱399"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 399))
            Tax_Input.set("₱" + str(((ItemCost - 399) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 399 + ((ItemCost - 399) * Tax) / 100))

        def Egg():
            ItemCost = 119
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Sunny-Side Up", "1", "₱119"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 119))
            Tax_Input.set("₱" + str(((ItemCost - 119) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 119 + ((ItemCost - 119) * Tax) / 100))

        def Donut():
            ItemCost = 29
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Doughnut", "1", "₱29"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 29))
            Tax_Input.set("₱" + str(((ItemCost - 29) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 29 + ((ItemCost - 29) * Tax) / 100))

        def Vegsalad():
            ItemCost = 49
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Vegetable Salad", "1", "₱49"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 49))
            Tax_Input.set("₱" + str(((ItemCost - 49) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 49 + ((ItemCost - 49) * Tax) / 100))

        def Cake():
            ItemCost = 59
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Cake", "1", "₱59"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 59))
            Tax_Input.set("₱" + str(((ItemCost - 59) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 59 + ((ItemCost - 59) * Tax) / 100))

        def Bread():
            ItemCost = 19
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Bread", "1", "₱19"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 19))
            Tax_Input.set("₱" + str(((ItemCost - 19) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 19 + ((ItemCost - 19) * Tax) / 100))

        def Carbonara():
            ItemCost = 199
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Carbonara", "1", "₱199"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 199))
            Tax_Input.set("₱" + str(((ItemCost - 199) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 199 + ((ItemCost - 199) * Tax) / 100))

        def Buttered():
            ItemCost = 229
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Buttered Shrimp", "1", "₱229"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 229))
            Tax_Input.set("₱" + str(((ItemCost - 229) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 229 + ((ItemCost - 229) * Tax) / 100))

        def Beefsteak():
            ItemCost = 199
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Beef Steak", "1", "₱199"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 199))
            Tax_Input.set("₱" + str(((ItemCost - 199) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 199 + ((ItemCost - 199) * Tax) / 100))

        def Sushi():
            ItemCost = 239
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Sushi", "1", "₱239"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 239))
            Tax_Input.set("₱" + str(((ItemCost - 239) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 239 + ((ItemCost - 239) * Tax) / 100))

        def Ramen():
            ItemCost = 79
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Ramen", "1", "₱79"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 79))
            Tax_Input.set("₱" + str(((ItemCost - 79) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 79 + ((ItemCost - 79) * Tax) / 100))

        def Lasagna():
            ItemCost = 199
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Lasagna", "1", "₱199"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 199))
            Tax_Input.set("₱" + str(((ItemCost - 199) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 199 + ((ItemCost - 199) * Tax) / 100))

        def Spaghetti():
            ItemCost = 139
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Spaghetti", "1", "₱139"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 139))
            Tax_Input.set("₱" + str(((ItemCost - 139) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 139 + ((ItemCost - 139) * Tax) / 100))

        def Siomai():
            ItemCost = 49
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Siomai", "1", "₱49"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 49))
            Tax_Input.set("₱" + str(((ItemCost - 49) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 49 + ((ItemCost - 49) * Tax) / 100))

        def Pancit():
            ItemCost = 199
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Pancit", "1", "₱199"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 199))
            Tax_Input.set("₱" + str(((ItemCost - 199) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 199 + ((ItemCost - 199) * Tax) / 100))

        def Cookies():
            ItemCost = 49
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Cookies", "1", "₱49"))
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, "values")[2][1:])
            Subtotal_Input.set("₱" + str(ItemCost - 49))
            Tax_Input.set("₱" + str(((ItemCost - 49) * Tax) / 100))
            Total_Input.set("₱" + str(ItemCost - 49 + ((ItemCost - 49) * Tax) / 100))

        scroll_x = Scrollbar(ReceiptFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(ReceiptFrame, orient=VERTICAL)

        self.POS_records=ttk.Treeview(ReceiptFrame, height=20, columns=("Item","Qty","Amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.POS_records.heading("Item", text="Item")
        self.POS_records.heading("Qty", text="Qty")
        self.POS_records.heading("Amount", text="Amount")
        self.POS_records['show'] = 'headings'
        self.POS_records.column("Item", width=85)
        self.POS_records.column("Qty", width=100)
        self.POS_records.column("Amount", width=100)
        self.POS_records.pack(fill=BOTH, expand=1)
        self.POS_records.bind("<ButtonRelease-1>")

        self.btnCoffee = Button(ChangeButtonFrame, padx=2, image=self.Coffee, width=104, height=104, bd=2, command=Coffee)
        self.btnCoffee.grid(row=0, column=0, pady=2, padx=4)
        self.btnHotchoco = Button(ChangeButtonFrame, padx=2, image=self.Hotchoco, width=104, height=104, bd=2, command=Hotchoco)
        self.btnHotchoco.grid(row=0, column=1, pady=2, padx=4)
        self.btnLemonade = Button(ChangeButtonFrame, padx=2, image=self.Lemonade, width=104, height=104, bd=2, command=Lemonade)
        self.btnLemonade.grid(row=0, column=2, pady=2, padx=4)

        self.btnWater = Button(ChangeButtonFrame, padx=2, image=self.Water, width=104, height=104, bd=2, command=Water)
        self.btnWater.grid(row=1, column=0, pady=2, padx=4)
        self.btnIcedtea = Button(ChangeButtonFrame, padx=2, image=self.Icedtea, width=104, height=104, bd=2, command=Icedtea)
        self.btnIcedtea.grid(row=1, column=1, pady=2, padx=4)
        self.btnCoke = Button(ChangeButtonFrame, padx=2, image=self.Coke, width=104, height=104, bd=2, command=Coke)
        self.btnCoke.grid(row=1, column=2, pady=2, padx=4)

        self.btnMilkshake = Button(ChangeButtonFrame, padx=2, image=self.Milkshake, width=104, height=104, bd=2, command=Milkshake)
        self.btnMilkshake.grid(row=2, column=0, pady=2, padx=4)
        self.btnBeer = Button(ChangeButtonFrame, padx=2, image=self.Beer, width=104, height=104, bd=2, command=Beer)
        self.btnBeer.grid(row=2, column=1, pady=2, padx=4)
        self.btnMilk = Button(ChangeButtonFrame, padx=2, image=self.Milk, width=104, height=104, bd=2, command=Milk)
        self.btnMilk.grid(row=2, column=2, pady=2, padx=4)

        self.btnTea = Button(ChangeButtonFrame, padx=2, image=self.Tea, width=104, height=104, bd=2, command=Tea)
        self.btnTea.grid(row=3, column=0, pady=2, padx=4)
        self.btnWine = Button(ChangeButtonFrame, padx=2, image=self.Wine, width=104, height=104, bd=2, command=Wine)
        self.btnWine.grid(row=3, column=1, pady=2, padx=4)
        self.btnRoyal = Button(ChangeButtonFrame, padx=2, image=self.Royal, width=104, height=104, bd=2, command=Royal)
        self.btnRoyal.grid(row=3, column=2, pady=2, padx=4)

        self.btnPancake = Button(FoodItemFrame, padx=2, image=self.Pancake, width=104, height=104, bd=2, command=Pancake)
        self.btnPancake.grid(row=0, column=0, pady=2, padx=4)
        self.btnBurger = Button(FoodItemFrame, padx=2, image=self.Burger, width=104, height=104, bd=2, command=Burger)
        self.btnBurger.grid(row=0, column=1, pady=2, padx=4)
        self.btnFries = Button(FoodItemFrame, padx=2, image=self.Fries, width=104, height=104, bd=2, command=Fries)
        self.btnFries.grid(row=0, column=2, pady=2, padx=4)
        self.btnChicken = Button(FoodItemFrame, padx=2, image=self.Chicken, width=104, height=104, bd=2, command=Chicken)
        self.btnChicken.grid(row=0, column=3, pady=2, padx=4)
        self.btnPizza = Button(FoodItemFrame, padx=2, image=self.Pizza, width=104, height=104, bd=2, command=Pizza)
        self.btnPizza.grid(row=0, column=4, pady=2, padx=4)

        self.btnEgg = Button(FoodItemFrame, padx=2, image=self.Egg, width=104, height=104, bd=2, command=Egg)
        self.btnEgg.grid(row=1, column=0, pady=2, padx=4)
        self.btnDonut = Button(FoodItemFrame, padx=2, image=self.Donut, width=104, height=104, bd=2, command=Donut)
        self.btnDonut.grid(row=1, column=1, pady=2, padx=4)
        self.btnVegsalad = Button(FoodItemFrame, padx=2, image=self.Vegsalad, width=104, height=104, bd=2, command=Vegsalad)
        self.btnVegsalad.grid(row=1, column=2, pady=2, padx=4)
        self.btnCake = Button(FoodItemFrame, padx=2, image=self.Cake, width=104, height=104, bd=2, command=Cake)
        self.btnCake.grid(row=1, column=3, pady=2, padx=4)
        self.btnBread = Button(FoodItemFrame, padx=2, image=self.Bread, width=104, height=104, bd=2, command=Bread)
        self.btnBread.grid(row=1, column=4, pady=2, padx=4)

        self.btnCarbonara = Button(FoodItemFrame, padx=2, image=self.Carbonara, width=104, height=104, bd=2, command=Carbonara)
        self.btnCarbonara.grid(row=2, column=0, pady=2, padx=4)
        self.btnButtered = Button(FoodItemFrame, padx=2, image=self.Buttered, width=104, height=104, bd=2, command=Buttered)
        self.btnButtered.grid(row=2, column=1, pady=2, padx=4)
        self.btnBeefsteak = Button(FoodItemFrame, padx=2, image=self.Beefsteak, width=104, height=104, bd=2, command=Beefsteak)
        self.btnBeefsteak.grid(row=2, column=2, pady=2, padx=4)
        self.btnSushi = Button(FoodItemFrame, padx=2, image=self.Sushi, width=104, height=104, bd=2, command=Sushi)
        self.btnSushi.grid(row=2, column=3, pady=2, padx=4)
        self.btnRamen = Button(FoodItemFrame, padx=2, image=self.Ramen, width=104, height=104, bd=2, command=Ramen)
        self.btnRamen.grid(row=2, column=4, pady=2, padx=4)

        self.btnLasagna = Button(FoodItemFrame, padx=2, image=self.Lasagna, width=104, height=104, bd=2, command=Lasagna)
        self.btnLasagna.grid(row=3, column=0, pady=2, padx=4)
        self.btnSpaghetti = Button(FoodItemFrame, padx=2, image=self.Spaghetti, width=104, height=104, bd=2, command=Spaghetti)
        self.btnSpaghetti.grid(row=3, column=1, pady=2, padx=4)
        self.btnSiomai = Button(FoodItemFrame, padx=2, image=self.Siomai, width=104, height=104, bd=2, command=Siomai)
        self.btnSiomai.grid(row=3, column=2, pady=2, padx=4)
        self.btnPancit = Button(FoodItemFrame, padx=2, image=self.Pancit, width=104, height=104, bd=2, command=Pancit)
        self.btnPancit.grid(row=3, column=3, pady=2, padx=4)
        self.btnCookies = Button(FoodItemFrame, padx=2, image=self.Cookies, width=104, height=104, bd=2, command=Cookies)
        self.btnCookies.grid(row=3, column=4, pady=2, padx=4)

if __name__=='__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()