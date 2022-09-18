from cgitb import text
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("600x600")
root.title("E_Levy Calc")
root.resizable(False,False)
root.configure(bg='Blue')

Label(root,text="E-Levy Calculator",bg='Blue',fg='White',font='Arial 20 bold').place(x=200,y=20)

frame1= Frame(root,bg='white',height=300,width=450)
frame1.place(x=80,y=100)

def on_enter(e):
    entry1.delete(0,'end')

def on_leave(e):
    name = entry1.get()
    if name == "":
        entry1.insert(0,'Amount to be Sent')

entry1 = Entry(frame1,width=30,fg='black',bg='white',font=('Microsoft YaHei UI light',11),border=2,highlightthickness=0)
entry1.place(x=100,y=60)
entry1.insert(0,"Amount to be Sent: ")
entry1.bind('<FocusIn>',on_enter)
entry1.bind('<FocusOut>',on_leave)

def calculate():
    try:
        amount = int(entry1.get())
        if amount >= 100:
            taxes = (1.5/100)*amount
            messagebox.showinfo(title="Taxes",message=f"GHc{taxes+amount} is your payment")
        else:
            messagebox.showinfo(title="No Taxes",message="Your dont pay E-levy on ammounts less than or equal GHc100 ")
    except ValueError:
        try:
            amount = float(entry1.get())
            if amount > 100:
                taxes = (1.5/100)*amount
                messagebox.showinfo(title="Taxes",message=f"GHc{taxes+amount} is your payment")
            else:
                messagebox.showinfo(title="No Taxes",message="Your dont pay E-levy on ammounts less than GHc100 ")
        except ValueError:
            messagebox.showerror("title",message="Input Error")


    
    




Button(frame1,text="Calculate",bg='blue',fg='White',relief=GROOVE,command=calculate).place(x=190,y=100)






root.mainloop()