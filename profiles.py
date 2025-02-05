from tkinter import *
from tkinter import ttk,messagebox

from dbconnect import get_db_connect


def add_prof():
    cp1=c1.get()
    cp2=c2.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("INSERT INTO techsec.users(username,password)VALUES(%s,%s)",(cp1,cp2))
        db.commit()
        messagebox.showinfo("Сообщение","Добавление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при добавлении")
        print(e)
        db.rollback()
        db.close()
        
        
def upd_prof():
    cp1=c1.get()
    cp2=c2.get()
    cp3=c3.get()
    cp4=c4.get()
    cp5=c5.get()
    cp6=c6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("UPDATE techsec.users SET username=%s , password=%s, organ_id=%s, employee_id=%s,permission=%s  WHERE id=%s;",(cp1,cp2,cp3,cp4,cp5,cp6))
        db.commit()
        messagebox.showinfo("Сообщение","Обновление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при обновлении")
        print(e)
        db.rollback()
        db.close()
        
        
def del_prof():
    cp6=c6.get()
    db=get_db_connect()    
    curs=db.cursor()
    try:
        curs.execute("DELETE FROM techsec.users WHERE id=%s;",(cp6))
        db.commit()
        messagebox.showinfo("Сообщение","Удаление прошло успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка","Ошибка при удалении")
        print(e)
        db.rollback()
        db.close()
        

def profile():
    global c1,c2,c3,c4,c5,c6
    pro=Tk()
    pro.title("Добавить профиль")
    pro.resizable(False,False)
    Label(pro,text="Логин",font=("Arial",15),bg="green",fg="black").grid(row=1,column=0,sticky="wens",pady=6,padx=13)
    Label(pro,text="Пароль",font=("Arial",15),bg="green",fg="black").grid(row=2,column=0,sticky="wens",pady=6,padx=13)
    Label(pro,text="Организация",font=("Arial",15),bg="green",fg="black").grid(row=3,column=0,sticky="wens",pady=6,padx=13)
    Label(pro,text="Сотрудник",font=("Arial",15),bg="green",fg="black").grid(row=4,column=0,sticky="wens",pady=6,padx=13)
    Label(pro,text="Предоставленные права",font=("Arial",15),bg="green",fg="black").grid(row=5,column=0,sticky="wens",pady=6,padx=13)
    
    c1=Entry(pro)
    c1.grid(row=1,column=1,pady=6)
    c2=Entry(pro)
    c2.grid(row=2,column=1,pady=6)
    c3=ttk.Combobox(pro)
    c3.grid(row=3,column=1,pady=6)
    c4=ttk.Combobox(pro)
    c4.grid(row=4,column=1,pady=6)
    c5=Entry(pro)
    c5.grid(row=5,column=1,pady=6)
    
    Label(pro,text="ID:",bg="green",font=("Arial",15)).grid(row=9,column=0,sticky="wens",pady=6,padx=20)
    c6=Entry(pro)
    c6.grid(row=9,column=1,pady=6,padx=10)
    Button(pro,text="Найти",bg="green",font=("Arial",15)).grid(row=10,column=0,columnspan=2,sticky="wens",pady=6,padx=10)
    
    Button(pro,text="Создать",font=("Arial",15),bg="green").grid(row=7,column=0,sticky="wens",pady=6,padx=10)
    Button(pro,text="Изменить",bg="green",font=("Arial",15)).grid(row=7,column=1,sticky="wens",pady=6,padx=10)
    Button(pro,text="Удалить",bg="green",font=("Arial",15)).grid(row=8,column=0,sticky="wens",pady=6,padx=10)
    Button(pro,text="Вернуться",font=("Arial",15),bg="green",command=pro.withdraw).grid(row=8,column=1,sticky="wens",pady=6,padx=10)
    pro.mainloop()
