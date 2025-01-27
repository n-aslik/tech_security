from tkinter import *
from tkinter import ttk,messagebox

def register():
    reg=Tk()
    reg.title("Вход")
    reg.mainloop()

def instruction():
    ins=Tk()
    ins.title("Пройти инструкта")
    ins.mainloop()
    
    
# win=Tk()
# win.title("Карточка сотрудника")

# navbar=Menu()

# header=Menu(tearoff=0)
# header.add_command()
# header.add_command()
# header.add_command()
# search=Menu(tearoff=0)
# search.add_command()
# logout=Menu(tearoff=0)
# logout.add_command()
# navbar.add_cascade(label="Главная",menu=header)
# navbar.add_cascade(label="Поиск",menu=search)
# navbar.add_cascade(label="Выйти",menu=logout) 
  
# win.option_add("*tearoff",False) 
# icon=PhotoImage(file="katodmin.png")
# win.iconphoto(True,icon)
# win.config(menu=navbar)
# win.mainloop()


root=Tk()
root.title("Главная")
root.geometry("450x400")
root.config(bg="white")
root.resizable(False,False)
icon=PhotoImage(file="katodmid.png",palette="white")
Label(root,image=icon).grid(row=0,column=0,sticky="news")
Label(root,text="КАТОД",font=("Arial",15),bg="white",width=16).grid(row=1,column=1,sticky="news")
Button(root,text="Вход",font=("Arial",10),bg="green",width=16,height=2,compound=register).grid(row=2,column=1,sticky="news",pady=6)
Button(root,text="Пройти инструктаж",font=("Arial",10),bg="green",width=16,height=2,command=instruction).grid(row=3,column=1,sticky="news",pady=6)
root.mainloop()