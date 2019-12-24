#Imports
from tkinter import *
from tkinter import messagebox
import datetime
import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="pizzashop")
cursor=con.cursor()

onlyOnce=1

def InsertData(name, mobile):
    global cursor
    global con
    global onlyOnce
    if onlyOnce==1:
        cursor.execute("INSERT INTO orders (user_name,user_mobile) VALUES (%s,%s)", (name, mobile))
    order_no = cursor.lastrowid
    con.commit()
    return order_no



top=""
#sr=1
#totalAmount=0
curValue1=0
curValue2=0
curValue3=0
curValue4=0
curValue5=0
curValue6=0
curValue7=0
curValue8=0
curValue9=0
curValue10=0
curValue11=0

def Item1Count():
    count1=0
    if item1inp.get() == "":
        count1=0
    else:
        count1=int(item1inp.get())
    count1+=1
    pizza1data.set(str(count1))
    totalAmount=int(totalRes.get())+ 170
    totalData.set(str(totalAmount))

def Item2Count():
    count2=0
    if item2inp.get() == "":
        count2=0
    else:
        count2=int(item2inp.get())
    count2+=1
    pizza2data.set(str(count2))
    totalAmount = int(totalRes.get()) + 150
    totalData.set(str(totalAmount))

def Item3Count():
    count3=0
    if item3inp.get() == "":
        count3=0
    else:
        count3=int(item3inp.get())
    count3+=1
    pizza3data.set(str(count3))
    totalAmount = int(totalRes.get()) + 200
    totalData.set(str(totalAmount))

def Item4Count():
    count4=0
    if item4inp.get() == "":
        count4=0
    else:
        count4=int(item4inp.get())
    count4+=1
    pizza4data.set(str(count4))
    totalAmount = int(totalRes.get()) + 240
    totalData.set(str(totalAmount))

def Item5Count():
    count5=0
    if item5inp.get() == "":
        count5=0
    else:
        count5=int(item5inp.get())
    count5+=1
    pizza5data.set(str(count5))
    totalAmount = int(totalRes.get()) + 180
    totalData.set(str(totalAmount))

def Item6Count():
    count6=0
    if item6inp.get() == "":
        count6=0
    else:
        count6=int(item6inp.get())
    count6+=1
    pizza6data.set(str(count6))
    totalAmount = int(totalRes.get()) + 160
    totalData.set(str(totalAmount))

def Item7Count():
    count7=0
    if item7inp.get() == "":
        count7=0
    else:
        count7=int(item7inp.get())
    count7+=1
    pizza7data.set(str(count7))
    totalAmount = int(totalRes.get()) + 120
    totalData.set(str(totalAmount))

def Item8Count():
    count8=0
    if item8inp.get() == "":
        count8=0
    else:
        count8=int(item8inp.get())
    count8+=1
    burger1data.set(str(count8))
    totalAmount = int(totalRes.get()) + 70
    totalData.set(str(totalAmount))

def Item9Count():
    count9=0
    if item9inp.get() == "":
        count9=0
    else:
        count9=int(item9inp.get())
    count9+=1
    burger2data.set(str(count9))
    totalAmount = int(totalRes.get()) + 80
    totalData.set(str(totalAmount))

def Item10Count():
    count10=0
    if item10inp.get() == "":
        count10=0
    else:
        count10=int(item10inp.get())
    count10+=1
    cake1data.set(str(count10))
    totalAmount = int(totalRes.get()) + 60
    totalData.set(str(totalAmount))

def Item11Count():
    count11=0
    if item11inp.get() == "":
        count11=0
    else:
        count11=int(item11inp.get())
    count11+=1
    cake2data.set(str(count11))
    totalAmount = int(totalRes.get()) + 60
    totalData.set(str(totalAmount))

#Update Item 1
def getCurValue1(event):
    global curValue1
    curValue1=(int(item1inp.get()) * 170)

def UpdateItem1(event):
    global curValue1
    amount=int(totalRes.get()) - curValue1
    totalAmount=amount + (int(item1inp.get()) * 170)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 2
def getCurValue2(event):
    global curValue2
    curValue2=(int(item2inp.get()) * 150)

def UpdateItem2(event):
    global curValue2
    amount=int(totalRes.get()) - curValue2
    totalAmount=amount + (int(item2inp.get()) * 150)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 3
def getCurValue3(event):
    global curValue3
    curValue3=(int(item3inp.get()) * 200)

def UpdateItem3(event):
    global curValue3
    amount=int(totalRes.get()) - curValue3
    totalAmount=amount + (int(item3inp.get()) * 200)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 4
def getCurValue4(event):
    global curValue4
    curValue4=(int(item4inp.get()) * 240)

def UpdateItem4(event):
    global curValue4
    amount=int(totalRes.get()) - curValue4
    totalAmount=amount + (int(item4inp.get()) * 240)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 5
def getCurValue5(event):
    global curValue5
    curValue5=(int(item5inp.get()) * 180)

def UpdateItem5(event):
    global curValue5
    amount=int(totalRes.get()) - curValue5
    totalAmount=amount + (int(item5inp.get()) * 180)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 6
def getCurValue6(event):
    global curValue6
    curValue6=(int(item6inp.get()) * 160)

def UpdateItem6(event):
    global curValue6
    amount=int(totalRes.get()) - curValue6
    totalAmount=amount + (int(item6inp.get()) * 160)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 7
def getCurValue7(event):
    global curValue7
    curValue7=(int(item7inp.get()) * 120)

def UpdateItem7(event):
    global curValue7
    amount=int(totalRes.get()) - curValue7
    totalAmount=amount + (int(item7inp.get()) * 120)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 8
def getCurValue8(event):
    global curValue8
    curValue8=(int(item8inp.get()) * 70)

def UpdateItem8(event):
    global curValue8
    amount=int(totalRes.get()) - curValue8
    totalAmount=amount + (int(item8inp.get()) * 70)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 9
def getCurValue9(event):
    global curValue9
    curValue9=(int(item9inp.get()) * 80)

def UpdateItem9(event):
    global curValue9
    amount=int(totalRes.get()) - curValue9
    totalAmount=amount + (int(item9inp.get()) * 80)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 10
def getCurValue10(event):
    global curValue10
    curValue10=(int(item10inp.get()) * 60)

def UpdateItem10(event):
    global curValue10
    amount=int(totalRes.get()) - curValue10
    totalAmount=amount + (int(item10inp.get()) * 60)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

#Update Item 11
def getCurValue11(event):
    global curValue11
    curValue11=(int(item11inp.get()) * 60)

def UpdateItem11(event):
    global curValue11
    amount=int(totalRes.get()) - curValue11
    totalAmount=amount + (int(item11inp.get()) * 60)
    totalData.set(str(int(totalAmount)))
    totalRes.update()

def GenerateBill():

    def OrderMore():
        global onlyOnce
        onlyOnce+=1
        customerNameInp.config(state=DISABLED)
        customerMobileInp.config(state=DISABLED)
        top.withdraw()

    def checkMobile(number):
        if number.isdigit():
            if len(number) == 10:
                if number[0] == "9" or number[0] == "8" or number[0] == "7":
                    return True
                else:
                    messagebox.showinfo("Mobile Validation", "Number Starts with Either 9 | 8 | 7")
                    return False
            else:
                messagebox.showinfo("Mobile Validation", "Mobile Number Should be 10 Digits")
                return False
        else:
            messagebox.showinfo("Mobile Validation", "Only Digits are Allowed")
            return False


    def OrderPlaced():
        top.focus_set()
        messagebox.showinfo("Order Place","Order Placed \n Thank You "+customerNameInp.get())

    def OrderCancel():
        global cursor
        global con
        order_no = cursor.lastrowid
        cursor.execute("DELETE FROM orders WHERE order_id=%s", (order_no,))
        con.commit()
        root.destroy()

    def getItem():
        sr=1
        if item1inp.get() == "":
            mainData.insert(END,"")
        elif int(item1inp.get()) >= 1:
            price = (int(item1inp.get()) * 170)
            mainData.insert(END,("  "+(str(sr) + "\t Chicken Golden Delight \t\t   170 \t\t" + str(item1inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item2inp.get() == "":
            mainData.insert(END,"")
        elif int(item2inp.get()) >= 1:
            price = (int(item2inp.get()) * 150)
            mainData.insert(END,("  "+(str(sr) + "\t Veg Digital Veggie \t\t\t 150 \t" + str(item2inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item3inp.get() == "":
            mainData.insert(END,"")
        elif int(item3inp.get()) >= 1:
            price = (int(item3inp.get()) * 200)
            mainData.insert(END,("  "+(str(sr) + "\t Chicken Dominator \t\t\t 200 \t" + str(item3inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item4inp.get() == "":
            mainData.insert(END,"")
        elif int(item4inp.get()) >= 1:
            price = (int(item4inp.get()) * 240)
            mainData.insert(END,("  "+(str(sr) + "\t Veg Farm House \t\t\t 240 \t" + str(item4inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item5inp.get() == "":
            mainData.insert(END,"")
        elif int(item5inp.get()) >= 1:
            price = (int(item5inp.get()) * 180)
            mainData.insert(END,("  "+(str(sr) + "\t Veg Golden Delight \t\t\t 180 \t" + str(item5inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item6inp.get() == "":
            mainData.insert(END,"")
        elif int(item6inp.get()) >= 1:
            price = (int(item6inp.get()) * 160)
            mainData.insert(END,("  "+(str(sr) + "\t Veg Extravaganza \t\t\t 160 \t" + str(item6inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item7inp.get() == "":
            mainData.insert(END,"")
        elif int(item7inp.get()) >= 1:
            price = (int(item7inp.get()) * 120)
            mainData.insert(END,("  "+(str(sr) + "\t Veg Special Pizza \t\t\t 120 \t" + str(item7inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item8inp.get() == "":
            mainData.insert(END,"")
        elif int(item8inp.get()) >= 1:
            price = (int(item8inp.get()) * 70)
            mainData.insert(END,("  "+(str(sr) + "\t Veg Burger \t\t\t 70 \t" + str(item8inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item9inp.get() == "":
            mainData.insert(END,"")
        elif int(item9inp.get()) >= 1:
            price = (int(item9inp.get()) * 80)
            mainData.insert(END,("  "+(str(sr) + "\t Chicken Burger \t\t\t 80 \t" + str(item9inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item10inp.get() == "":
            mainData.insert(END,"")
        elif int(item10inp.get()) >= 1:
            price = (int(item10inp.get()) * 60)
            mainData.insert(END,("  "+(str(sr) + "\t Choclate Cake Muffin \t\t\t 60 \t" + str(item10inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")

        if item11inp.get() == "":
            mainData.insert(END,"")
        elif int(item11inp.get()) >= 1:
            price = (int(item11inp.get()) * 60)
            mainData.insert(END,("  "+(str(sr) + "\t Vanilla Cake Muffin \t\t\t 60 \t" + str(item11inp.get()) + "\t" + str(price)+"\n")))
            sr += 1
        else:
            mainData.insert(END,"")


    if customerNameInp.get() == "":
        messagebox.showinfo("Bill", "Please enter customer name")
        customerNameInp.focus_set()
    elif customerMobileInp.get() == "":
        messagebox.showinfo("Bill","Please enter mobile number")
        customerMobileInp.focus_set()
    elif checkMobile(customerMobileInp.get()) == False:
        customerMobileInp.focus_set()
    elif int(totalRes.get()) == 0:
        messagebox.showinfo("Bill", "Please select some item...")
    else:
        orderNumber = InsertData(customerNameInp.get(), customerMobileInp.get())

        custName = StringVar()
        order = StringVar()
        cmobile = StringVar()

        order.set("Order No. : " + str(orderNumber))
        custName.set("Customer Name : "+customerNameInp.get())
        cmobile.set("Mobile : "+customerMobileInp.get())

        top=Toplevel()
        top.resizable(0,0)
        top.focus_set()
        top.wm_iconbitmap('pizza.ico')
        w = 500
        h = 650
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        top.configure(background="white")

        head=Label(top, text="Delicious Pizza Shop", font=("Lucida Handwriting", 30, "bold italic"), bg="white",
                        width=20, fg="#4472C4")
        head.pack(fill=X,pady=30)
        billName=Label(top,text="Customer Bill",bg="white",justify="center",font=("Arial",15,"bold italic")).place(x=170,y=90)


        customerName=Label(top,textvariable=custName,bg="white",justify="center",font=("Arial",12,"bold italic"))
        customerName.place(x=140,y=120)


        orderNumber = Label(top, textvariable=order, bg="white", justify="center",font=("Arial", 12, "bold italic"))
        orderNumber.place(x=5, y=150)


        CusMob = Label(top, textvariable=cmobile, bg="white", justify="center", font=("Arial", 12, "bold italic"))
        CusMob.place(x=335, y=150)

        date=Label(top,text="Date : ",font=("Arial",12,"bold"),bg="white").place(x=5,y=180)
        curDateTime=datetime.datetime.now()
        todayDate=StringVar()
        todayDate.set(str(curDateTime.strftime("%d/%m/%Y")))
        displayDate=Label(top,textvariable=todayDate,font=("Arial",12,"bold"),bg="white").place(x=60,y=180)
        time = Label(top, text="Time : ", font=("Arial", 12, "bold"), bg="white").place(x=350, y=180)
        todayTime = StringVar()
        todayTime.set(str(curDateTime.strftime("%I:%M %p")))
        displayDate = Label(top, textvariable=todayTime, font=("Arial", 12, "bold"), bg="white").place(x=400, y=180)

        title=Label(top,text="SR. No. \t Item Name \t Unit Price \t Qty \t Price",bg="gray",fg="white",font=("Arial",13,"bold")).place(x=7,y=220)

        mainData = Text(top, width=700, height=200, font=("Arial", 13, "bold"))
        mainData.place(x=0, y=250)
        getItem()
        mainData.insert(END,"\n\n")
        mainData.insert(END, "\t\t\t Total \t\t\t"+totalRes.get())

        mainData.tag_add("here", "end-1c linestart", END)
        mainData.tag_config("here", background="red", foreground="white", font=("Arial", 18, "bold"))

        doneBill = Button(top, text="Place Order!", fg="white", bg="green", font=("Arial", 18, "bold italic"),command=OrderPlaced).place(x=30, y=550)

        addMore = Button(top, text="Add More", fg="white", bg="blue", font=("Arial", 18, "bold italic"),
                          command=OrderMore).place(x=200, y=550)

        cancelOrder = Button(top, text="Cancel", fg="white", bg="red", font=("Arial", 18, "bold italic"),
                         command=OrderCancel).place(x=340, y=550)

        lblThanks=Label(top,text="Thank You! Visit Again", font=("Monotype Corsiva", 18, "bold italic"),bg="white").place(x=130,y=600)





time1=""


root=Tk()
root.resizable(0,0)
w=1350
h=768
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.wm_iconbitmap('pizza.ico')
root.title("Delicious Pizza Shop")

canvas=Canvas(root,width=1350,height=768)
canvas.pack(fill="both")
background=PhotoImage(file='images\\back.png')
canvas.create_image(680,385,image=background)

heading=Label(root,text="Delicious Pizza Shop",font=("Lucida Handwriting",30,"bold italic"),bg="white",width=20,fg="#4472C4")
heading.place(x=400,y=30)
clock=Label(root,font=("Arial",14,"italic"),bg="white",fg="#45223b")
clock.place(x=410,y=90)

customerNameLabel=Label(root,text="Customer Name : ",font=("Arial",15,"bold italic"),bg="white").place(x=400,y=160)
customerNameInp=Entry(root,font=("Arial",15,"italic"),justify="center")
customerNameInp.place(x=600,y=160)

customerMobileLabel=Label(root,text="Mobile : ",font=("Arial",15," bold italic"),bg="white").place(x=400,y=200)
customerMobileInp=Entry(root,font=("Arial",15,"italic"),justify="center")
customerMobileInp.place(x=600,y=200)


pizza1=PhotoImage(file="images\\pizza1.png")
item1=Button(root,image=pizza1,width=150,height=150,command=Item1Count).place(x=60,y=90)
pizza1data=StringVar()
item1inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza1data,justify="center",bg="#e4e1f2")
item1inp.place(x=150,y=270)
item1inp.bind("<FocusIn>",getCurValue1)
item1inp.bind("<Return>",UpdateItem1)
item1lbl=Label(root,text="Chicken Golden Delight",font=("Arial",11,"italic"),bg="white").place(x=60,y=250)
item1price=Label(root,text="₹170 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=100,y=270)

pizza2=PhotoImage(file="images\\pizza2.png")
item2=Button(root,image=pizza2,width=150,height=150,command=Item2Count).place(x=60,y=300)
pizza2data=StringVar()
item2inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza2data,justify="center",bg="#e4e1f2")
item2inp.place(x=150,y=480)
item2inp.bind("<FocusIn>",getCurValue2)
item2inp.bind("<Return>",UpdateItem2)
item2lbl=Label(root,text="Veg Digital Veggie",font=("Arial",11,"italic"),bg="white").place(x=60,y=455)
item2price=Label(root,text="₹150 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=100,y=480)

pizza3=PhotoImage(file="images\\pizza3.png")
item3=Button(root,image=pizza3,width=150,height=150,command=Item3Count).place(x=60,y=510)
pizza3data=StringVar()
item3inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza3data,justify="center",bg="#e4e1f2")
item3inp.place(x=150,y=690)
item3inp.bind("<FocusIn>",getCurValue3)
item3inp.bind("<Return>",UpdateItem3)
item3lbl=Label(root,text="Chicken Dominator",font=("Arial",11,"italic"),bg="white").place(x=60,y=665)
item3price=Label(root,text="₹200 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=100,y=690)

pizza4=PhotoImage(file="images\\pizza4.png")
item4=Button(root,image=pizza4,width=150,height=150,command=Item4Count).place(x=320,y=300)
pizza4data=StringVar()
item4inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza4data,justify="center",bg="#e4e1f2")
item4inp.place(x=410,y=480)
item4inp.bind("<FocusIn>",getCurValue4)
item4inp.bind("<Return>",UpdateItem4)
item4lbl=Label(root,text="Veg Farm House",font=("Arial",11,"italic"),bg="white").place(x=320,y=455)
item4price=Label(root,text="₹240 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=360,y=480)

pizza5=PhotoImage(file="images\\pizza5.png")
item5=Button(root,image=pizza5,width=150,height=150,command=Item5Count).place(x=320,y=510)
pizza5data=StringVar()
item5inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza5data,justify="center",bg="#e4e1f2")
item5inp.place(x=410,y=690)
item5inp.bind("<FocusIn>",getCurValue5)
item5inp.bind("<Return>",UpdateItem5)
item5lbl=Label(root,text="Veg Golden Delight",font=("Arial",11,"italic"),bg="white").place(x=320,y=665)
item5price=Label(root,text="₹180 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=360,y=690)

pizza6=PhotoImage(file="images\\pizza6.png")
item6=Button(root,image=pizza6,width=150,height=150,command=Item6Count).place(x=570,y=300)
pizza6data=StringVar()
item6inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza6data,justify="center",bg="#e4e1f2")
item6inp.place(x=660,y=480)
item6inp.bind("<FocusIn>",getCurValue6)
item6inp.bind("<Return>",UpdateItem6)
item6lbl=Label(root,text="Veg Extravaganza",font=("Arial",11,"italic"),bg="white").place(x=570,y=455)
item6price=Label(root,text="₹160 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=610,y=480)

pizza7=PhotoImage(file="images\\pizza7.png")
item7=Button(root,image=pizza7,width=150,height=150,command=Item7Count).place(x=570,y=510)
pizza7data=StringVar()
item7inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=pizza7data,justify="center",bg="#e4e1f2")
item7inp.place(x=660,y=690)
item7inp.bind("<FocusIn>",getCurValue7)
item7inp.bind("<Return>",UpdateItem7)
item7lbl=Label(root,text="Veg Special Pizza",font=("Arial",11,"italic"),bg="white").place(x=570,y=665)
item7price=Label(root,text="₹120 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=610,y=690)

burger1=PhotoImage(file="images\\burger1.png")
item8=Button(root,image=burger1,width=150,height=150,command=Item8Count).place(x=820,y=300)
burger1data=StringVar()
item8inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=burger1data,justify="center",bg="#e4e1f2")
item8inp.place(x=910,y=480)
item8inp.bind("<FocusIn>",getCurValue8)
item8inp.bind("<Return>",UpdateItem8)
item8lbl=Label(root,text="Veg Burger",font=("Arial",11,"italic"),bg="white").place(x=820,y=455)
item8price=Label(root,text="₹70 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=860,y=480)

burger2=PhotoImage(file="images\\burger2.png")
item9=Button(root,image=burger2,width=150,height=150,command=Item9Count).place(x=820,y=510)
burger2data=StringVar()
item9inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=burger2data,justify="center",bg="#e4e1f2")
item9inp.place(x=910,y=690)
item9inp.bind("<FocusIn>",getCurValue9)
item9inp.bind("<Return>",UpdateItem9)
item9lbl=Label(root,text="Chicken Burger",font=("Arial",11,"italic"),bg="white").place(x=820,y=665)
item9price=Label(root,text="₹80 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=860,y=690)

cake1=PhotoImage(file="images\\cake1.png")
item10=Button(root,image=cake1,width=150,height=150,command=Item10Count).place(x=1070,y=90)
cake1data=StringVar()
item10inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=cake1data,justify="center",bg="#e4e1f2")
item10inp.place(x=1160,y=270)
item10inp.bind("<FocusIn>",getCurValue10)
item10inp.bind("<Return>",UpdateItem10)
item10lbl=Label(root,text="Choclate Cake Muffin",font=("Arial",11,"italic"),bg="white").place(x=1070,y=245)
item10price=Label(root,text="₹60 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=1110,y=270)

cake2=PhotoImage(file="images\\cake2.png")
item11=Button(root,image=cake2,width=150,height=150,command=Item11Count).place(x=1070,y=300)
cake2data=StringVar()
item11inp=Entry(root,width=4,font=("Arial",15,"italic"),textvariable=cake2data,justify="center",bg="#e4e1f2")
item11inp.place(x=1160,y=480)
item11inp.bind("<FocusIn>",getCurValue11)
item11inp.bind("<Return>",UpdateItem11)
item11lbl=Label(root,text="Vanilla Cake Muffin",font=("Arial",11,"italic"),bg="white").place(x=1070,y=455)
item11price=Label(root,text="₹60 ",font=("Arial",14,"italic"),bg="white",fg="blue").place(x=1110,y=480)


totalLabel=Label(root,text="",justify=LEFT,font=("Arial",17," bold"),bg="red",fg="white")
total=Label(root,text=" Total Amount : ",font=("Arial",17,"italic bold"),bg="red",fg="white").place(x=1000,y=540)
totalLabel.place(x=1000,y=530)
totalLabel.config(padx=160,pady=10)
totalData=StringVar()
totalRes=Entry(root,font=("Arial",18," bold"),width=9,textvariable=totalData)
totalRes.insert(0,"0")
totalRes.place(x=1180,y=540)

order=Button(root,text="Order Now!",fg="white",bg="green",font=("Arial",18,"bold italic"),command=GenerateBill).place(x=1080,y=620)

#Functions
def TimeDate():
    global time1
    time2=datetime.datetime.now()
    if time2 != time1:
        time1 = time2
        clock.config(text="Current Date and Time : "+time2.strftime("%A %d %B, %Y %I:%M:%S %p"),font=("Arial",15,"bold"))
    clock.after(200,TimeDate)

TimeDate()

root.mainloop()
