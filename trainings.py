from tkinter import *
from tkinter import ttk,messagebox
import os
from dbconnect import get_db_connect


def add_train():
    tr1=t1.get()
    tr2=t2.get()
    tr3=t3.get()
    tr4=t4.get()
    tr5=t5.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.training(title,number,hyper_link,hire_date,expire_date)VALUES(%s,%s,%s,%s,%s)",(tr1,tr2,tr3,tr4,tr5))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_train():
    tr1=t1.get()
    tr2=t2.get()
    tr3=t3.get()
    tr4=t4.get()
    tr5=t5.get()
    tr6=t6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.training SET title=%s ,number=%s, hyper_link=%s, hire_date=%s, expire_date=%s WHERE id=%s ;",(tr1,tr2,tr3,tr4,tr5,tr6))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_train():
    tr6=t6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.training WHERE id=%s;",(tr6))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def open_train(event):
    tr3=t3.get()
    os.startfile(tr3,"rb")
    
def training():
    global t1,t2,t3,t4,t5,t6
    train=Tk()
    train.title("Добавить обучения")
    train.resizable(False,False)
    Label(train,text="Название",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(train,text="Номер",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(train,text="Гиперссылка",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(train,text="Дата получения",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(train,text="Срок действия",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    
    t1=Entry(train)
    t1.grid(row=1,column=1,pady=6)
    t2=Entry(train)
    t2.grid(row=2,column=1,pady=6)
    t3=Entry(train)
    t3.grid(row=3,column=1,pady=6)
    t4=Entry(train)
    t4.grid(row=4,column=1,pady=6)
    t5=Entry(train)
    t5.grid(row=5,column=1,pady=6)
    
    Label(train,text="ID:",bg="green",font=("Arial",15)).grid(row=9,column=0,sticky="wens",pady=6,padx=20)
    t6=Entry(train)
    t6.grid(row=9,column=1,pady=6,padx=10)
    Button(train,text="Найти",bg="green",font=("Arial",15)).grid(row=10,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(train,text="Открыть",font=("Arial",15),bg="green",width=16).grid(row=3,column=2,sticky="wens",pady=6,padx=10)
    Button(train,text="Создать",font=("Arial",15),bg="green",width=16).grid(row=7,column=0,sticky="wens",pady=6,padx=10)
    Button(train,text="Изменить",bg="green",font=("Arial",15)).grid(row=7,column=1,sticky="wens",pady=6,padx=10)
    Button(train,text="Удалить",bg="green",font=("Arial",15)).grid(row=8,column=0,sticky="wens",pady=6,padx=10)
    Button(train,text="Вернуться",font=("Arial",15),bg="green",width=16,command=train.withdraw).grid(row=8,column=1,sticky="wens",pady=6,padx=10)
    train.mainloop()


    
    